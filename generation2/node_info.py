"""Node introspection.

TEMPORARY HACK: ShaderNodeOutputLineStyle (Line Style Output) IS NOT PROCESSED.
Its target enum becomes invalid during parameter exploration and floods the
console with RNA warnings. NodeInfo.loop_on_nodes skips it before creating
the wrapper. This exclusion applies to all NodeInfo-based exploration.
Revisit this exclusion after investigating the Blender RNA behavior.
"""

import bpy

from ..kernel import snake_case, get_socket_type, get_class_name

from . import config, utils
from .node_param import NodeParam
from .node_socket import NodeSocket
from .node_argument import NodeArgument
from .node_dims import NODE_DIMS

class NodeInfo:
    STD_ATTRS = None
    def __init__(self, btree, bnode):
        self.btree = btree
        self.bnode = bnode

        self._inputs = None
        self._outputs = None

        self.has_structure_type = False

        self.get_std_attrs()

        # -------------------------
        # dynamic sockets
        # -------------------------

        self.items = {}
        for attr_name in dir(self.bnode):
            if attr_name[-6:] == '_items':

                meth = getattr(self.bnode, attr_name).new
                sig_type = 'EMPTY'

                try:
                    meth()
                    sig_type = 'EMPTY'

                except TypeError as e:
                    if str(e).endswith('required parameter "socket_type" not specified'):
                        sig_type = 'TYPE'
                    elif str(e).endswith('required parameter "name" not specified'):
                        sig_type = 'NAME'
                    else:
                        raise e

                if sig_type == 'TYPE':
                    try:
                        meth(socket_type='ERR')
                    except Exception as e:
                        token = "not found in "
                        p = str(e).find(token)
                        assert p>=0, f"Algo error: {str(e)}"
                        types = eval(str(e)[p + len(token):]) 

                    try:
                        meth(name="Fake", socket_type=[types[0]])
                        assert False, "Till 5.3: not an existing case"
                        sig_type = 'NAME_TYPE'
                    except:
                        pass

                elif sig_type == 'NAME':
                    meth(name="Fake")

                self.items[attr_name]= sig_type

        self.has_items = len(self.items) > 0


        # Clear items to avoid fake inputs
        try:
            getattr(self.bnode, self.items_name).clear()
        except:
            pass

        # -------------------------
        # Default config
        # -------------------------

        self.analyze_config()

        self.default_params = self.snapshot_params()

    # ====================================================================================================
    # Wrapping
    # ====================================================================================================

    # ---------------------------------------------------------------------------
    # Tree
    # ---------------------------------------------------------------------------

    @property
    def tree_type(self):
        return self.btree.bl_idname

    @property
    def is_shader(self):
        return self.btree.bl_idname == 'ShaderNodeTree'

    @property
    def is_geonodes(self):
        return self.btree.bl_idname == 'GeometryNodeTree'

    # ---------------------------------------------------------------------------
    # Node
    # ---------------------------------------------------------------------------

    @property
    def name(self):
        """Return the Blender node's name."""
        return self.bnode.name

    @property
    def bl_idname(self):
        """Return the Blender node's bl_idname."""
        return self.bnode.bl_idname

    @property
    def color_tag(self):
        """Return the Blender node's color category."""
        return self.bnode.color_tag

    # ---------------------------------------------------------------------------
    # Parameters
    # ---------------------------------------------------------------------------

    @property
    def has_parameters(self):
        """Whether the node exposes any parameters."""
        return bool(self.snapshot_params())

    # ---------------------------------------------------------------------------
    # Sockets
    # ---------------------------------------------------------------------------
    
    @property
    def has_input_sockets(self):
        """Whether the node has input sockets, including virtual sockets."""
        return bool(self.inputs)

    @property
    def has_output_sockets(self):
        """Whether the node has output sockets, including virtual sockets."""
        return bool(self.outputs)

    @property
    def is_class_property(self):
        """Whether the node is a parameterless input with a single output."""
        if self.has_input_sockets or self.has_parameters or len(self.outputs) != 1:
            return False
        return next(iter(self.outputs.values())).socket_type != 'CUSTOM'

    @property
    def has_multi_input(self):
        """Whether any input socket accepts multiple links."""
        return any(socket.is_multi_input for socket in self.inputs.values())

    @property
    def multi_input_socket(self):
        """Return the first multi-input NodeSocket, or None."""
        return next((socket for socket in self.inputs.values() if socket.is_multi_input), None)

    @property
    def has_dynamic_inputs(self):
        """Whether any explored input socket is virtual."""
        return any(socket.socket_type == 'CUSTOM' for socket in self.inputs.values())

    @property
    def has_dynamic_outputs(self):
        """Whether any explored output socket is virtual."""
        return any(socket.socket_type == 'CUSTOM' for socket in self.outputs.values())

    @property
    def is_grid_input(self):
        if not self.has_input_sockets:
            return False
        return self.get_input_socket(0).is_grid

    @property
    def is_grid_output(self):
        if not self.has_output_sockets:
            return False
        return self.get_output_socket(0).is_grid

    @property
    def has_domain_parameter(self):
        """Whether the node exposes a domain parameter."""
        return 'domain' in self.snapshot_params()

    @property
    def has_selection(self):
        """Whether Selection follows a Geometry input in the current configuration.

        This is the condition used by the former NodeInfo.get_arguments to
        replace the Selection argument with self.get_selection() in methods.
        """
        previous = None
        for socket in self.bnode.inputs:
            if not socket.enabled or socket.type == 'CUSTOM':
                continue
            if (socket.label or socket.name) == 'Selection' and previous == 'GEOMETRY':
                return True
            previous = socket.type
        return False

    # ====================================================================================================
    # Parameters
    # ====================================================================================================

    def reset_params(self):
        for param_name in self.config_order:
            setattr(self.bnode, param_name, self.config[param_name]['default'])


    def set_params(self, **params):
        """Set the supplied parameters, leaving other parameters unchanged."""
        for param_name in self.config_order:
            if param_name in params:
                setattr(self.bnode, param_name, params[param_name])

    def snapshot_params(self):
        """Return parameter values and enum choices in the node's current state."""
        params = {}
        standard = self.get_std_attrs()
        for prop in self.bnode.bl_rna.properties:
            name = prop.identifier
            if name in standard or prop.is_readonly or name.endswith('_items'):
                continue
            if name.startswith('__'):
                continue

            param = NodeParam.Parameter(self.bnode, name)
            if param is not None:
                params[name] = {
                    'type': param.param_type,
                    'value': param.value,
                    'enums': param.enums,
                }

        # structure_type params is not directly exposed
        # it can be set with (socket_type, shape) to set socket_type
        if 'structure_type' in params:
            self.has_structure_type = True
            params.pop('structure_type')

        return params

    # ----------------------------------------------------------------------------------------------------
    # Loop on configurations
    # ----------------------------------------------------------------------------------------------------

    def loop_on_configurations(self, func, **parameters):

        def set_parameters(**params):

            remaining = list(self.config_order)
            for param_name in self.config_order:
                if param_name in params:
                    setattr(self.bnode, param_name, params[param_name])
                    remaining.remove(param_name)

            if len(remaining):
                snapshot = self.snapshot_params()
                next_param = remaining[0]

                for param_value in snapshot[next_param]['enums']:
                    new_params = {**params, next_param: param_value}
                    set_parameters(**new_params)

            else:
                func(self, **params)

        try:
            set_parameters(**parameters)
        finally:
            self.reset_params()

    # ====================================================================================================
    # Sockets
    # ====================================================================================================

    @property
    def inputs(self):
        if self._inputs is None:
            self._inputs = {socket.identifier: socket for socket in
                            self.get_possible_sockets(group=False)}
        return self._inputs

    @property
    def outputs(self):
        if self._outputs is None:
            self._outputs = {socket.identifier: socket for socket in
                             self.get_possible_sockets(inout='OUTPUT', group=False)}
        return self._outputs

    def get_sockets(self, inout):
        if inout=='INPUT':
            return self.inputs.values()
        else:
            return self.outputs.values()

    def get_input_socket(self, name_or_index):
        if isinstance(name_or_index, int):
            return list(self.inputs.values())[name_or_index]
        else:
            return self.inputs[name_or_index]

    def get_output_socket(self, name_or_index):
        if isinstance(name_or_index, int):
            return list(self.outputs.values())[name_or_index]
        else:
            return self.outputs[name_or_index]

    def all_sockets(self):
        """Capture every input/output socket, including disabled sockets."""
        return {
            'inputs': {
                socket.identifier: NodeSocket(socket, index)
                for index, socket in enumerate(self.bnode.inputs) if socket.type != 'CUSTOM'
            },
            'outputs': {
                socket.identifier: NodeSocket(socket, index)
                for index, socket in enumerate(self.bnode.outputs) if socket.type != 'CUSTOM'
            },
        }

    def snapshot_sockets(self):
        """Return only enabled sockets, indexed by identifier."""
        return {
            direction: {identifier: socket for identifier, socket in sockets.items()
                        if socket.enabled}
            for direction, sockets in self.all_sockets().items()
        }

    # ----------------------------------------------------------------------------------------------------
    # Initialize parameters description
    # ----------------------------------------------------------------------------------------------------

    def analyze_config(self):
        """ Identifies the enum parameters and their order

        The value of a parameter can change the possible values of another one.
        In that case, the first parameter drivers the other one and must be set
        before when enumerating the configurations.

        The methode initialize:
        - config_order (tuple): the order to use to enumerate the parameters
        - config (dict): param_name -> {'default': str, 'enums': tuple} 
        """

        # ---------------------------------------------------------------------------
        # Relationship between two parameters
        # ---------------------------------------------------------------------------

        def relationship(param1, param2):
            """ Does a relationship exist bewteen two parameters

            0: No relationship
            1: param1 drives param2
            2: param2 drives param1
            """
            params = self.snapshot_params()
            vals1 = params[param1]['enums']
            vals2 = params[param2]['enums']

            for val1 in vals1:
                try:
                    setattr(self.bnode, param1, val1)
                except Exception as e:
                    raise e

                new_params = self.snapshot_params()
                new_vals2 = new_params[param2]['enums']

                if set(new_vals2) != set(vals2):
                    return 1

            setattr(self.bnode, param1, params[param1]['value'])
            setattr(self.bnode, param2, params[param2]['value'])

            for val2 in vals2:
                try:
                    setattr(self.bnode, param2, val2)
                except Exception as e:
                    raise e

                new_params = self.snapshot_params()
                new_vals1 = new_params[param1]['enums']

                if set(new_vals1) != set(vals1):
                    return 2

            return 0

        # ---------------------------------------------------------------------------
        # Main
        # ---------------------------------------------------------------------------

        params = self.snapshot_params()
        enum_params = [param_name for param_name, param in params.items() 
                       if (param['type'] == 'ENUM') and len(param['enums'])]

        if len(enum_params) == 0:
            self.config_order = ()

        elif len(enum_params) == 1:
            self.config_order = tuple(enum_params)

        elif len(enum_params) == 2:
            order = relationship(enum_params[0], enum_params[1])
            if order in (0, 1):
                self.config_order = tuple(enum_params)
            else:
                self.config_order = (enum_params[1], enum_params[0])
        else:
            orders = []
            for p1 in enum_params[:-1]:
                for p2 in enum_params[1:]:
                    order = relationship(p1, p2)
                    if order == 1:
                        orders.append((p1, p2))
                    elif order == 2:
                        orders.append((p2, p1))

            if len(orders) > 1:
                assert False, f"'{self.name}' Not Implemented: {orders}"

            ordered = list(orders[0]) if len(orders) else []
            for param in enum_params:
                if param in ordered:
                    continue
                ordered.append(param)

            self.config_order = tuple(ordered)

        self.config = {}
        for param_name in self.config_order:
            self.config[param_name] = {
                'default': params[param_name]['value'],
                'enums': params[param_name]['enums'],
            }

        self.reset_params()

        # ---------------------------------------------------------------------------
        # data type param
        # ---------------------------------------------------------------------------

        # data_type exists or not
        self.data_type_name = None
        self.data_type_config_index = None
        for i, name in enumerate(self.config_order):
            if name in ('data_type', 'input_type', 'socket_type'):
                self.data_type_name = name
                self.data_type_config_index = i 
                break

        self.data_type_drives_inputs = False
        self.data_type_drives_outputs = False
        self.data_type_driven_sockets = {}

        # If exists, looks for driven sockets
        if self.data_type_name is not None:

            # sockets which are enabled at least once for a given data_type value
            def dt_loop(value):

                enabled_ids = {}
                for inout, direction in (('INPUT', 'inputs'), ('OUTPUT', 'outputs')):
                    enabled_ids[direction] = [socket.identifier for socket in
                        self.get_possible_sockets(inout=inout, group=False,
                                                  **{self.data_type_name: value})]

                return enabled_ids

            # Enabled sockets counters
            counters = {'inputs': {}, 'outputs': {}}

            # Sockets changing types
            types = {'inputs': {}, 'outputs': {}}

            # Data type possible values
            data_type_values = params[self.data_type_name]['enums']

            # Enabled sockets per data_type
            #dt_sockect_ids = {}

            for value in data_type_values:

                # Enabling
                enabled_ids = dt_loop(value)
                #dt_sockect_ids[value] = enabled_ids
                
                for direction in ('inputs', 'outputs'):
                    for sid in enabled_ids[direction]:
                        if sid in counters[direction]:
                            counters[direction][sid] += 1
                        else:
                            counters[direction][sid] = 1

                # Types
                self.set_params(**{self.data_type_name: value})
                for direction in ('inputs', 'outputs'):
                    for sock in self.snapshot_sockets()[direction].values():
                        if sock.enabled:
                            if sock.identifier in types[direction]:
                                types[direction][sock.identifier].add(sock.socket_type)
                            else:
                                types[direction][sock.identifier] = {sock.socket_type}

            driven_ids = {'inputs': [], 'outputs': []}
            for direction in ('inputs', 'outputs'):
                # Include sockets whose type changes with data_type.
                for sid, stypes in types[direction].items():
                    if len(stypes) > 1:
                        driven_ids[direction].append(sid)

                # Include sockets absent from some data_type variants.
                for sid, counter in counters[direction].items():
                    if counter < len(data_type_values):
                        driven_ids[direction].append(sid)

            # Conserver les snapshots des sockets, dans leur ordre physique.
            for value in data_type_values:
                self.data_type_driven_sockets[value] = {}
                self.set_params(**{self.data_type_name: value})
                sockets = self.snapshot_sockets()
                for direction in ('inputs', 'outputs'):
                    self.data_type_driven_sockets[value][direction] = [
                        socket for socket in sockets[direction].values()
                        if socket.socket_type == get_socket_type(value)
                        and socket.identifier in driven_ids[direction]]

            self.data_type_drives_inputs = any(
                sockets['inputs'] for sockets in self.data_type_driven_sockets.values())
            self.data_type_drives_outputs = any(
                sockets['outputs'] for sockets in self.data_type_driven_sockets.values())

        self.reset_params()

    # ----------------------------------------------------------------------------------------------------
    # Get the possible sockets for a configuration
    # ----------------------------------------------------------------------------------------------------

    def get_possible_sockets(self, *, inout="INPUT", group=True, **parameters):

        """Merge sockets across configurations compatible with fixed parameters.

        INPUT remains the default. OUTPUT uses the same exploration. group=False
        preserves physical identifiers for introspection; the default groups
        mutually exclusive homonyms for generated signatures.
        """
        if inout not in ('INPUT', 'OUTPUT'):
            raise ValueError(f'Unknown socket direction: {inout!r}')
        direction = 'inputs' if inout == 'INPUT' else 'outputs'
        sockets_by_id = {}

        def collect(node, **kwargs):
            for socket in node.all_sockets()[direction].values():
                if not socket.enabled:
                    continue
                previous = sockets_by_id.get(socket.identifier)
                if previous is None:
                    sockets_by_id[socket.identifier] = socket
                else:
                    previous.add_possible_socket([socket])

        self.loop_on_configurations(collect, **parameters)
        sockets = sorted(sockets_by_id.values(), key=lambda socket: socket.index)
        if not group:
            return sockets

        # --------------------------------------------------
        # Group sockets by their name
        # --------------------------------------------------

        shared_names = {}
        for sock in sockets:
            if not sock.enabled:
                continue

            if sock.socket_name in shared_names:
                shared_names[sock.socket_name].append(sock)
            else:
                shared_names[sock.socket_name] = [sock]

        # --------------------------------------------------
        # Identifies groups among homonyms
        # --------------------------------------------------

        merged = []
        for socket_name, socks in shared_names.items():

            if len(socks) == 1:
                merged.append(socks[0])
                continue

            # Count the types
            # No variable socket_name
            types = set()
            has_var_names = False
            for sock in socks:
                has_var_names |= len(sock.names) > 1
                types.add(sock.socket_type)

            # Actual group: no var_names and all types are different
            if (len(types) == len(socks)) and (not has_var_names):
                socket = socks[0]
                socket.enabled = True

                socket.group_name = socket_name
                socket.group_sockets = [{
                    'identifier': sock.identifier,
                    'socket_type': sock.socket_type,
                    'class_name': sock.class_name,
                    } for sock in socks]
                socket.socket_type = 'SOCKET'
                socket.class_name = 'Socket'

                merged.append(socket)

            else:
                for sock in socks:
                    merged.append(sock)

        return merged

    def get_node_arguments(self, *, self_socket=None, fixed_sockets=None,
                           last_sockets=(), use_geo_selection=False,
                           auto_data_type=None, **parameters) -> list[NodeArgument]:
        """Prepare independent contextual wrappers, without changing this node.

        All supplied parameters are fixed, including non-enums and None. Only
        enum parameters select socket configurations in get_possible_sockets;
        other fixed values are also applied during exploration. Unspecified
        parameters remain exposed, in config_order followed by snapshot order.
        The receiver is selected before last_sockets reorders whole wrappers.
        Explicitly fixed sockets take precedence over automatic selection.
        """
        initial = self.snapshot_params()
        unknown = parameters.keys() - initial.keys()
        if unknown:
            raise ValueError(f'{self.name}: unknown parameters: {sorted(unknown)}')

        try:
            self.set_params(**parameters)
            for name, value in parameters.items():
                if name not in self.config_order:
                    setattr(self.bnode, name, value)
            snapshots = self.snapshot_params()
            sockets = self.get_possible_sockets(**parameters)
        finally:
            # Restore enum masters first, then the remaining parameter values.
            self.set_params(**{name: info['value'] for name, info in initial.items()})
            for name, info in initial.items():
                if name not in self.config_order and name in parameters:
                    setattr(self.bnode, name, info['value'])

        used_names = {'self', 'cls', 'node', 'named_sockets'}

        def unique_name(name):
            base = snake_case(name) or 'value'
            candidate = base
            index = 0
            while candidate in used_names:
                index += 1
                candidate = f'{base}_{index}'
            used_names.add(candidate)
            return candidate

        # Dynamic items reserve their names before ordinary arguments.
        items_argument = None
        if self.has_items:
            if list(self.items.values())[0] == 'EMPTY': # dict {items name: TYPE | EMPTY} 
                items_argument = NodeArgument(None, unique_name('dyn_sockets'), role='ANONYMOUS_ITEMS')
            else:
                items_argument = NodeArgument(None, unique_name('items'), role='NAMED_ITEMS',
                                              kwargs_name=unique_name('named_items'))

        # Parameters reserve their Python names before the socket arguments.
        param_arguments = []
        param_names = list(self.config_order) + [name for name in snapshots if name not in self.config_order]
        for name in param_names:
            info = snapshots[name]
            default = initial[name]['value'] if name in parameters else info['value']
            parameter = NodeParam(self.bnode, name, default, info['type'], enums=info['enums'])
            context = dict(role='FIXED', value=parameters[name]) if name in parameters else {}
            param_arguments.append(NodeArgument(parameter, unique_name(name), **context))

        def matches(socket, name):
            return (name in socket.names or name == socket.identifier
                    or name == f'ID_{socket.identifier}' or name == socket.group_name)

        receiver = None
        if self_socket is not None:
            receiver = next((socket for socket in sockets if matches(socket, self_socket)), None)
            if receiver is None:
                raise ValueError(f'{self.name}: unknown receiver socket: {self_socket!r}')

        remaining_fixed = dict(fixed_sockets or {})
        arguments = []
        for index, socket in enumerate(sockets):
            names = [socket.socket_name] + sorted(socket.names - {socket.socket_name})
            fixed_names = [name for name in remaining_fixed if matches(socket, name)]
            if len(fixed_names) > 1:
                raise ValueError(f'{self.name}: multiple fixed values for socket {socket.identifier!r}')
            ui_name = self_socket if socket is receiver and self_socket in socket.names else names[0]
            context = {}
            if fixed_names:
                if socket is receiver:
                    raise ValueError(f'{self.name}: receiver socket cannot also be fixed')
                fixed_name = fixed_names[0]
                if fixed_name in socket.names:
                    ui_name = fixed_name
                context = dict(role='FIXED', value=remaining_fixed.pop(fixed_name))
            elif socket is receiver:
                context = dict(role='SELF')
            elif (use_geo_selection and index == 1 and receiver is sockets[0]
                  and sockets[0].socket_type == 'GEOMETRY'
                  and socket.socket_type == 'BOOLEAN' and 'Selection' in socket.names):
                ui_name = 'Selection'
                selection = unique_name('selection')
                context = dict(role='COMPUTED', value=selection,
                               computation=f'{selection} = self.get_selection()')

            name = unique_name(ui_name)
            aliases = ()
            if not context and len(names) > 1 and not socket.is_multi:
                aliases = tuple((ui, name if ui == ui_name else unique_name(ui)) for ui in names)
            arguments.append(NodeArgument(socket, name, aliases=aliases, socket_name=ui_name, **context))

        if remaining_fixed:
            raise ValueError(f'{self.name}: unknown fixed sockets: {sorted(remaining_fixed)}')

        # Resolve inference against final names, including deduplicated aliases.
        if auto_data_type is not None:
            type_parameter = self.data_type_parameter
            if type_parameter is None:
                raise ValueError(f'{self.name}: no type parameter for automatic inference')
            if type_parameter.name not in parameters:
                target = next((arg for arg in arguments
                               if arg.role in ('ARGUMENT', 'SELF') and matches(arg.source, auto_data_type)), None)
                if target is None:
                    raise ValueError(f'{self.name}: unknown type inference socket: {auto_data_type!r}')
                expression = 'self' if target.role == 'SELF' else dict(target.aliases).get(auto_data_type, target.name)
                parameter = next(arg for arg in param_arguments if arg.source.name == type_parameter.name)
                parameter.role = 'COMPUTED'
                parameter.value = parameter.name
                parameter.computation = (
                    f'{parameter.name} = SocketType.get_data_type_for_node('
                    f'{expression}, {self.bl_idname!r}, {type_parameter.name!r})')

        # Ordering affects exposition only; physical order was used above.
        first = [arg for arg in arguments if arg.role == 'SELF']
        rest = [arg for arg in arguments if arg.role != 'SELF']
        last = [arg for arg in rest if any(matches(arg.source, name) for name in last_sockets)]
        return (first + [arg for arg in rest if not any(arg is item for item in last)]
                + last + param_arguments + ([items_argument] if items_argument is not None else []))

    @property
    def data_type_parameter(self):
        """ data_type, socket_type or input_type parameter
        """
        parameters = self.snapshot_params()
        for name in ('data_type', 'input_type', 'socket_type'):
            if name in parameters:
                return NodeParam.Parameter(self.bnode, name)
        return None

    @property
    def has_data_type_parameter(self):
        return self.data_type_name is not None

    def data_type_input(self, data_type=None):
        """Name of the first input driven by the type parameter, or None."""
        if self.data_type_drives_inputs:
            if data_type is None:
                data_type = getattr(self.bnode, self.data_type_name)
            sockets = self.data_type_driven_sockets[data_type]['inputs']
            return sockets[0].socket_name if sockets else None
        return None

    @property
    def data_type_drives_first_input(self):
        if self.data_type_drives_inputs:
            data_type = getattr(self.bnode, self.data_type_name)
            sockets = self.data_type_driven_sockets[data_type]['inputs']
            if sockets:
                for bsock in self.bnode.inputs:
                    if bsock.enabled:
                        return bsock.identifier == sockets[0].identifier
        return False

    # ====================================================================================================
    # Utilities
    # ====================================================================================================

    @classmethod
    def get_std_attrs(cls):
        """Return the standard node attributes, initializing them once."""
        if cls.STD_ATTRS is None:
            cls.STD_ATTRS = set(dir(bpy.types.Node))
            cls.STD_ATTRS.update(bpy.types.Node.bl_rna.properties.keys())
            cls.STD_ATTRS.update((
                'active_item', 'active_index',
                'active_input_index', 'active_output_index',
                'active_generation_index', 'active_main_index',
                'inspection_index', 'ui_shortcut',
                'use_legacy_normal', 'legacy_corner_normals',
            ))
        return cls.STD_ATTRS

    @classmethod
    def socket_class_name(cls, socket_type, name=None):
        """Resolve a class name without using the active runtime environment."""
        if socket_type == 'GEOMETRY':
            try:
                return cls.geometry_class(name)
            except ValueError:
                return 'Geometry'
        if socket_type == 'SHADER' and name == 'Volume':
            return 'VolumeShader'
        
        return get_class_name(socket_type)

    @classmethod
    def geometry_class(cls, name):
        """Resolve a geometry socket name using the legacy explicit mapping."""
        if name in ('Mesh', 'Meshes', 'Mesh 1', 'Mesh 2', 'Bounding Box', 'Convex Hull', 'Dual Mesh'):
            return 'Mesh'
        if name in ('Curve', 'Curves', 'Spline', 'Splines', 'Guide Curves', 'Profile Curve'):
            return 'Curve'
        if name in ('Instance', 'Instances', 'Curve Instances'):
            return 'Instances'
        if name in ('Cloud', 'Points', 'Point Cloud'):
            return 'Cloud'
        if name == 'Volume':
            return 'Volume'
        if name == 'Grease Pencil':
            return 'GreasePencil'
        if name in ('Geometry', 'Geometries', 'Transform', 'Target Geometry', 'Selection',
                    'Inverted', 'Output', '0', '1', 'A', 'B', 'False', 'True', 'Value', 'List',
                    'Component', 'Profile', 'Target', 'Source', 'Item'):
            return 'Geometry'
        raise ValueError(f"Unknown Geometry socket name: {name!r}. Update NodeInfo.geometry_class.")


    @classmethod
    def loop_on_nodes(cls, func, tree_type="GeometryNodeTree"):
        """Apply func(node_info) to every node type supported by the requested tree.

        Nodes are created in a temporary tree named "Loop on Nodes".
        utils.loop_on_nodes collects them in a dictionary, sorts by UI name,
        then runs the processing callbacks.
        The tree is removed when the loop finishes, including on callback errors.
        config.DEPRECATED_NODES are skipped before creating their NodeInfo wrapper.
        """
        def process(bnode):
            if bnode.bl_idname in config.DEPRECATED_NODES:
                return
            # TEMP HACK documented at the top of this module.
            if bnode.bl_idname == 'ShaderNodeOutputLineStyle':
                return
            node = cls(bnode.id_data, bnode)
            func(node)

        utils.loop_on_nodes(process, tree_type=tree_type)

    # ====================================================================================================
    # Build the NODE_INFO entry
    # ====================================================================================================

    @property
    def node_info_entry(self):

        params = {}
        for name, param in self.default_params.items():
            params[name] = {
                'default'   : param['value'],
                'type'      : param['type'],
                'enum'      : param['enums'],
            }

        inputs, outputs, menus = {}, {}, {}
        for inout, target in (('INPUT', inputs), ('OUTPUT', outputs)):
            
            sockets = self.get_possible_sockets(inout=inout)

            for sock in sockets:
                target[sock.socket_name] = {
                    'bl_idname'     : sock.bl_idname,
                    'label'         : sock.label,
                    'name'          : sock.name,
                    'socket_type'   : sock.socket_type,
                    'aliases'       : sock.names,
                }
                if (inout == 'INPUT') and (sock.socket_type == 'MENU'):
                    menus[sock.identifier] = {
                        'default': sock.default_value, 
                        'values': sock.enums
                        }

        dims = NODE_DIMS[self.tree_type].get(self.bl_idname, None)
        if dims is None:
            print(f"CAUTION: node without dimensions in node_dims module: '{self.name}'")

        node_info = {
            'name'          : self.name,
            'params'        : params,
            'items'         : [self.items] if self.has_items else {}, 
            'menu_sockets'  : menus,
            'inputs'        : inputs, 
            'outputs'       : outputs, 
            'has_custom_in' : self.has_dynamic_inputs,
            'has_custom_out': self.has_dynamic_outputs,
            'dims'          : dims,
        }

        return node_info

