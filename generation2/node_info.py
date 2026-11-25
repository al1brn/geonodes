import bpy
from ast import literal_eval

from ..kernel import snake_case, get_socket_type, get_class_name

from . import config, utils
from .node_param import NodeParam
from .node_socket import NodeSocket
from .node_argument import NodeArguments
from .node_dims import NODE_DIMS

# ====================================================================================================
# Node items
# ====================================================================================================

class NodeItems:
    
    def __init__(self, node_info, bnode, name):
        """ Node items wrapper
        
        Dynamic sockets are create in items collection
        - case 1 (Bake, Capture Attribute): sockets are defined by name and type, no data_type parameter
          capture_attribute(named_items={'First': value1}, second=value2)
        - case 2 (Menu Switch) : sockets are defined by name only, data_type defines type
          menu_switch({'First': value1}, second=value2, data_type='FLOAT')
        - case 3 (Index Switch, Combine List) : no named needed, data_type defines type
          index_switch(value1, value2, index=..., data_type='FLOAT')
          
        """

        self.node_info = node_info
        self.name = name
        self.items = getattr(bnode, name)
        
        # signature analyzis will create a least one item
        items_count = len(self.items)
        in_count = len(node_info.bnode.inputs)
        out_count = len(node_info.bnode.outputs)
        
        # signature of 'new'
        self.analyze_signature()
        assert len(self.items) > items_count, "Algo error"
        
        # Do we have new sockets ?
        self.create_inputs = len(node_info.bnode.inputs) > in_count
        self.create_outputs = len(node_info.bnode.outputs) > out_count
        
        # Let's clear the collection
        self.items.clear()
        
        # Virtual sockets now that items is cleared
        self.virtual_input_socket = None
        for i_sock, sock in enumerate(node_info.bnode.inputs):
            if sock.type == 'CUSTOM':
                self.virtual_input_socket = NodeSocket.from_socket(sock, i_sock)
                break

        self.virtual_output_socket = None
        for i_sock, sock in enumerate(node_info.bnode.outputs):
            if sock.type == 'CUSTOM':
                self.virtual_output_socket = NodeSocket.from_socket(sock, i_sock)
                break

        # Do data_type drives the items type
        self.anonymous_items = False
        self.single_type = False
        
        if self.create_inputs:
            assert self.virtual_input_socket is not None, f"Algo error: {node_info.name}"
            self.anonymous_items = self.signature == 'EMPTY'
            self.single_type = self.signature in ('EMPTY', 'NAME')
            
    # ---------------------------------------------------------------------------
    # Analyze the signature of 'new' method
    # ---------------------------------------------------------------------------
    
    def analyze_signature(self):
        """ Get the signature between name, socket_type, none or both

        CAUTION: create at least one item
        """
        
        self.signature = None
        self.socket_types = None
        
        try:
            self.items.new()
            self.signature = 'EMPTY'
            return

        except TypeError as e:
            if str(e).endswith('required parameter "socket_type" not specified'):
                pass
            elif str(e).endswith('required parameter "name" not specified'):
                self.items.new(name="Fake")
                self.signature = "NAME"
                return
            else:
                raise
                
        try:
            self.items.new(socket_type='ERR')
        except Exception as e:
            token = "not found in "
            p = str(e).find(token)
            assert p>=0, f"Algo error: {str(e)}"
            self.socket_types = literal_eval(str(e)[p + len(token):])
            
            
        try:
            self.items.new(socket_type=self.socket_types[0])
            self.signature = "TYPE"
            return
        
        except TypeError as e:
            if not str(e).endswith('required parameter "name" not specified'):
                raise
            
        self.items.new(name="Fake", socket_type=self.socket_types[0])
        self.signature = "NAME_TYPE"

# ====================================================================================================
# Class NodeInfo
# ====================================================================================================

class NodeInfo:
    STD_ATTRS = None
    def __init__(self, btree, bnode):
        self.btree = btree
        self.bnode = bnode

        self._inputs = None
        self._outputs = None

        self.has_structure_type = False

        self.get_std_attrs()

        # Analyze config
        self.analyze_config()

        # Default params
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
    def virtual_socket(self):
        if self.creation_items is not None:
            return self.creation_items.virtual_input_socket

    @property
    def has_dynamic_inputs(self):
        return any(socket.socket_type == 'CUSTOM' for socket in self.inputs.values())

    @property
    def has_dynamic_outputs(self):
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

    @property
    def has_selection_out(self):
        if len(self.bnode.outputs) < 2:
            return False
        if self.bnode.outputs[0].type != 'GEOMETRY':
            return False
        if self.bnode.outputs[1].type != 'BOOLEAN':
            return False
        return True

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

    @property
    def last_sockets(self):
        last = []
        for sock in self.bnode.inputs:
            if sock.enabled and (sock.type == 'MENU'
                                 or (sock.name == 'Factor' and sock.type == 'VALUE')):
                last.append(sock.name)
        return last

    @property
    def has_geometry_in(self):
        first = next((s for s in self.inputs.values()
                      if s.enabled and not s.is_virtual), None)
        return first is not None and first.socket_type == 'GEOMETRY'
    
    @property
    def has_geometry_out(self):
        first = next((s for s in self.outputs.values()
                      if s.enabled and not s.is_virtual), None)
        return first is not None and first.socket_type == 'GEOMETRY'

    @property
    def auto_jump(self):
        if not (self.has_geometry_in and self.has_geometry_out):
            return False
        in_class = next(s.class_name for s in self.inputs.values()
                        if s.enabled and not s.is_virtual)
        out_class = next(s.class_name for s in self.outputs.values()
                         if s.enabled and not s.is_virtual)
        return in_class == out_class

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

        if False:
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
        sockets = {
            'inputs': {
                socket.identifier: NodeSocket.from_socket(socket, index)
                for index, socket in enumerate(self.bnode.inputs)
            },
            'outputs': {
                socket.identifier: NodeSocket.from_socket(socket, index)
                for index, socket in enumerate(self.bnode.outputs)
            },
        }
        if self.virtual_socket is not None:
            for nsock in sockets['inputs'].values():
                if nsock.socket_type == 'CUSTOM':
                    nsock.name = self.virtual_socket.name
            
        return sockets

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

        # ::::: Items

        # This first analyze will clear dynamic sockets if any

        self.items = []
        for attr_name in dir(self.bnode):
            if attr_name[-6:] == '_items':
                self.items.append(NodeItems(self, self.bnode, attr_name))

        # Get the items which create input sockets
        self.creation_items = None
        for items in self.items:
            if items.create_inputs:
                self.creation_items = items
                break

        # ::::: Parameters

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

        # ::::: data type param

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
            for value in data_type_values:

                # Enabling
                enabled_ids = dt_loop(value)
                
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

            # Dynamic sockets whose type is driven by data_type
            virtual_socket = {'inputs': None, 'outputs': None}
            if self.creation_items is not None:
                if self.creation_items.single_type:
                    if self.creation_items.anonymous_items:
                        self.creation_items.virtual_input_socket.name = 'ANONYMOUS'
                    virtual_socket['inputs'] = self.creation_items.virtual_input_socket
                if self.creation_items.create_outputs:
                    virtual_socket['outputs'] = self.creation_items.virtual_output_socket


            # Keep sockets snapshots in their primitive order
            for value in data_type_values:
                self.data_type_driven_sockets[value] = {}
                self.set_params(**{self.data_type_name: value})
                sockets = self.snapshot_sockets()
                for direction in ('inputs', 'outputs'):
                    self.data_type_driven_sockets[value][direction] = [
                        socket for socket in sockets[direction].values()
                        if socket.socket_type == get_socket_type(value)
                        and socket.identifier in driven_ids[direction]]

                    # Append virtual socket
                    if virtual_socket[direction] is not None:
                        self.data_type_driven_sockets[value][direction].append(virtual_socket[direction])

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

            # Count the types and sub types
            # No variable socket_name
            types = set()
            sub_types = set()
            has_var_names = False
            for sock in socks:
                has_var_names |= len(sock.names) > 1
                types.add(sock.socket_type)
                if sock.subtype_label is not None:
                    sub_types.add(sock.subtype_label)

            # Actual group: no var_names and (all types are different or all sub_types are different)
            diff_types = len(types) == len(socks)
            diff_sub_types = len(sub_types) == len(socks)
            if (diff_types or diff_sub_types) and (not has_var_names):
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

    # ====================================================================================================
    # Build the node arguments for the passes configuration
    # ====================================================================================================

    def get_node_arguments(
            self, *, 
            self_socket     = None, 
            fixed_sockets   = None,
            last_sockets    = None,
            geo_selection   = False,
            auto_data_type  = None,
            type_aliases    = None,
            **parameters) -> NodeArguments:

        if fixed_sockets is None:
            fixed_sockets = {}

        data_type_compution_is_expected = False            

        # ---------------------------------------------------------------------------
        # Node configuration
        # ---------------------------------------------------------------------------

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

        # ---------------------------------------------------------------------------
        # Error
        # ---------------------------------------------------------------------------

        arguments = NodeArguments()

        def raise_error(msg):
            arguments.make_arg_names_unique(reserved={'self', 'cls', 'node', 'computed_type', 'named_sockets', 'sockets', 'items', 'all_sockets'})

            print('-'*60)
            print(arguments.get_mockup(as_method=True, doc=False))
            print('-'*60)

            raise RuntimeError(f"'{self.name}' : {msg}")

        # ---------------------------------------------------------------------------
        # Add the parameter arguments
        # ---------------------------------------------------------------------------

        param_names = list(self.config_order) + [name for name in snapshots if name not in self.config_order]
        for name in param_names:

            info = snapshots[name]
            default = initial[name]['value'] if name in parameters else info['value']
            node_param = NodeParam(self.bnode, name, default, info['type'], enums=info['enums'])

            if name in parameters:
                arguments.add_fixed_parameter(node_param, parameters[name])
            elif auto_data_type is not None and name == self.data_type_name:
                # data_type will be computed later
                arguments.add_computed_parameter(node_param, '', value_name='computed_type')
                data_type_compution_is_expected = True
            else:
                arguments.add_parameter(node_param, type_aliases)

        # ---------------------------------------------------------------------------
        # Loop on sockets
        # ---------------------------------------------------------------------------

        receiver_socket = next((socket for socket in sockets
                                if socket.socket_name == self_socket), None)
        geo_selection = (geo_selection and self.has_selection and bool(sockets)
                         and self_socket == sockets[0].socket_name
                         and sockets[0].socket_type == 'GEOMETRY')
        last_sockets = set(self.last_sockets if last_sockets is None else last_sockets)

        keyword_only_is_set = False
        for first in (True, False):
            for index, socket in enumerate(sockets):

                if first == (socket.socket_name in last_sockets):
                    if first and not keyword_only_is_set:
                        if config.USE_KEYWORD_ONLY:
                            arguments.set_keyword_only()
                        keyword_only_is_set = True
                    continue

                # Fixed socket
                if socket.socket_name in fixed_sockets:
                    arguments.add_fixed_socket(socket, fixed_sockets[socket.socket_name])
                    continue

                # Selection socket
                if index == 1 and geo_selection:
                    arguments.add_computed_socket(socket, "selection", "selection = self.get_selection()")
                    continue

                # General case
                arg_name = arguments.add_socket(socket, is_self=socket is receiver_socket)

                # Auto data_type
                if data_type_compution_is_expected and auto_data_type == socket.socket_name:
                    if arg_name is None:
                        raise_error(f"Impossible to use auto_data_type with socket {auto_data_type}. No arg_name is available.")

                    computation = f"computed_type = SocketType.get_data_type_for_node({arg_name}, {self.bl_idname!r}, {self.data_type_name!r})"
                    arguments.computations.append(computation)
                    data_type_compution_is_expected = False


        # ---------------------------------------------------------------------------
        # Finalize
        # ---------------------------------------------------------------------------

        arguments.make_arg_names_unique(reserved={'self', 'cls', 'node', 'computed_type', 'named_sockets', 'sockets', 'items', 'all_sockets'})

        if data_type_compution_is_expected:
            raise_error(f"Impossible to find the socket to compute data_type with {auto_data_type=}.")


        return arguments

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
        if socket_type == 'SHADER':
            return cls.shader_class(name)
        
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
    def shader_class(cls, name):
        if name in ("Volume",):
            return "VolumeShader"
        else:
            return "Shader"


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
            'items'         : [it.name for it in self.items], 
            'menu_sockets'  : menus,
            'inputs'        : inputs, 
            'outputs'       : outputs, 
            'has_custom_in' : self.has_dynamic_inputs,
            'has_custom_out': self.has_dynamic_outputs,
            'dims'          : dims,
        }

        return node_info

