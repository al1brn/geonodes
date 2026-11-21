"""Describe and render a single node implementation."""

from dataclasses import replace as dataclass_replace

from ..kernel import snake_case, CamelCase, get_class_name, CLASS_NAMES

from ..kernel import GEOMETRY_CLASSES 
from .config import ADD_LOOP, LOOP_ONLY, NO_STATIC_CODE
from .config import STATIC_IMPLEMENTATION_ONLY, DEFAULT_IMPLEMENTATION, DOMAINS, DOMAIN_NAME
from .config import STATIC_IMPLEMENTATIONS
from .utils import replace_token

from .node_call import NodeCall, NodeCalls
from .node_param import NodeParam
from .sourcewriter import SourceWriter
from .node_info import NodeInfo

TAB = "    "

class NodeImplementation:
    """Describe a node implementation independently of generation state."""

    def __init__(self, node: NodeInfo, *, type_aliases=None):
        self.node = node
        self.type_aliases = type_aliases
        self.parameters = dict.fromkeys(self.node.snapshot_params())


    def __getitem__(self, name):
        return self.parameters[name]


    def __setitem__(self, name, value):
        if name not in self.parameters:
            raise KeyError(name)
        self.parameters[name] = value


    def __len__(self):
        return len(self.parameters)


    def copy(self):
        """Copy the parameter configuration, keeping the same NodeInfo."""
        result = type(self)(self.node, type_aliases=self.type_aliases)
        result.parameters = self.parameters.copy()
        result.type_aliases = self.type_aliases
        return result


    def set_parameters(self, **parameters):
        for name, value in parameters.items():
            self[name] = value


    def clear_parameters(self):
        for name in self.parameters:
            self.parameters[name] = None

    # ====================================================================================================
    # Create NodeCalls from loop on a parameter
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Loop on domain
    # ----------------------------------------------------------------------------------------------------

    def get_domain_calls(self, node_calls: NodeCalls) -> NodeCalls:
        """Construire les variantes d'un appel pour les domaines du nœud.

        Parameters
        ----------
        node_calls : NodeCalls
            Appel de départ. Sa variante générale est conservée si class_name
            est renseigné. Chaque variante de domaine conserve ses attributs
            et ses paramètres fixés, en remplaçant domain et la classe cible.

        Returns
        -------
        NodeCalls
            Appel général éventuel, puis un appel par domaine autorisé.
        """
        domains = {'POINT': 'Point', 'EDGE': 'Edge', 'FACE': 'Face', 'CORNER': 'Corner',
                   'CURVE': 'Spline', 'SPLINE': 'Spline', 'INSTANCE': 'Instance', 'LAYER': 'Layer',
                   'AUTO': 'Geometry'}
        
        parameter = NodeParam.Parameter(self.node.bnode, 'domain')
        if parameter is None or parameter.enums is None:
            raise ValueError(f"{self.node.name}: no domain enum parameter")

        return node_calls.overrides([
            {'class_name': domains[domain], 'parameters': {'domain': domain}}
            for domain in parameter.enums])

    # ----------------------------------------------------------------------------------------------------
    # Loop on data type
    # ----------------------------------------------------------------------------------------------------

    def get_data_type_calls(self, node_calls: NodeCalls) -> NodeCalls:

        parameter = self.node.data_type_parameter
        if parameter is None:
            raise ValueError(f"{self.node.name}: no data_type parameter")

        result = NodeCalls()

        for node_call in node_calls:
            overrides = []
            for data_type in parameter.enums:
                override = {
                    'class_name': get_class_name(data_type),
                    'auto_data_type': None,
                    'parameters': {parameter.name: data_type},
                }

                if (self.node.data_type_drives_inputs and node_call.has_self
                        and node_call.self_socket is None):
                    override['self_socket'] = self.node.data_type_input(data_type)

                overrides.append(override)

            result.extend(NodeCalls(node_call).overrides(overrides))

        return result

    # ----------------------------------------------------------------------------------------------------
    # Loop on a parameter
    # ----------------------------------------------------------------------------------------------------

    def expand_spec(self, spec: dict) -> list[dict]:
        """Expand one description's columns and parameter loops in lockstep."""
        general = object()
        columns = dict(spec)
        parameters = columns.pop('parameters', {})
        loops = {}
        if isinstance(parameters, dict):
            parameters = dict(parameters)
            for name, value in parameters.items():
                if not isinstance(value, str) or value not in (ADD_LOOP, LOOP_ONLY):
                    continue
                parameter = NodeParam.Parameter(self.node.bnode, name)
                if parameter is None or not parameter.enums:
                    raise ValueError(f"{self.node.name}: no enum parameter named {name!r}")
                loops[name] = parameter
                parameters[name] = ([general] if value == ADD_LOOP else []) + list(parameter.enums)
            # Parameter columns participate in the same alignment as all other fields.
            for name, value in parameters.items():
                columns[f'parameters.{name}'] = value
        else:
            columns['parameters'] = parameters

        result = []
        for row in NodeCalls.expand_dict(**columns):
            params = row.pop('parameters', {}).copy()
            for name in parameters if isinstance(parameters, dict) else ():
                value = row.pop(f'parameters.{name}')
                if value is not general:
                    params[name] = value
            for name, parameter in loops.items():
                value = params.get(name, general)
                suffix = '' if value is general else parameter.enum_names[value]
                for field in ('class_name', 'method_name'):
                    if field in row:
                        row[field] = replace_token(row[field], suffix)
                if value is general:
                    continue
                if name == self.node.data_type_name:
                    if row.get('class_name') is None:
                        row['class_name'] = get_class_name(value)
                    row['auto_data_type'] = None
                    if row.get('self_socket') is None and self.node.data_type_drives_inputs:
                        row['self_socket'] = self.node.data_type_input(value)
                elif name == 'domain' and row.get('class_name') is None:
                    # Reuse the standard domain mapping, without changing the node.
                    call = NodeCall.class_method('_domain')
                    variants = self.get_domain_calls(NodeCalls(call))
                    row['class_name'] = next(c.class_name for c in variants
                                             if c.parameters['domain'] == value)
            if params or 'parameters' in spec:
                row['parameters'] = params
            result.append(row)
        return result

    def get_loop_parameter_calls(self, node_calls: NodeCalls, parameter_name: str, include_base=False) -> NodeCalls:
        """ Loop on a node parameter

        Example: 'Curve Sample' loop on mode in ('FACTOR', 'LENGTH')
        method_name = sample_MODE
        token = MODE
        """

        if self.node.has_domain_parameter and parameter_name=='domain':
            return self.get_domain_calls(node_calls=node_calls)

        if self.node.has_data_type_parameter and parameter_name==self.node.data_type_name:
            return self.get_data_type_calls(node_calls)

        parameter = NodeParam.Parameter(self.node.bnode, parameter_name)
        if parameter is None or parameter.enums is None:
            raise ValueError(f"{self.node.name}: no enum parameter named {parameter_name}")

        token = parameter_name.upper()
        enum_names = parameter.enum_names

        result = NodeCalls()
        for node_call in node_calls:
            if include_base:
                ncs = NodeCalls(node_call).overrides({
                    'class_name': replace_token(node_call.class_name, ""),
                    'method_name': replace_token(node_call.method_name, ""),
                    })
                ncs.extend(result)
                result = ncs

            result.extend(NodeCalls(node_call).overrides([{
                    'class_name': replace_token(node_call.class_name, enum_names[value]),
                    'method_name': replace_token(node_call.method_name, enum_names[value]),
                    'parameters': {parameter.name: value},
                } for value in parameter.enums
            ]))

        # Debug option
        if False and self.node.name in ('Sample Curve',):
            for nc in result:
                print('-'*30)
                print(repr(nc))

        return result

    # ====================================================================================================
    # Build default node implementation
    # ====================================================================================================

    def get_default_node_calls(self) -> NodeCalls:
        """Describe the node implementation, including requested parameter loops."""

        if self.node.bl_idname in NO_STATIC_CODE:
            return NodeCalls()

        node = self.node
        inputs = [socket for socket in node.inputs.values() if socket.enabled and socket.socket_type != 'CUSTOM']
        outputs = [socket for socket in node.outputs.values() if socket.enabled and socket.socket_type != 'CUSTOM']
        first_input = inputs[0] if inputs else None
        first_output = outputs[0] if outputs else None
        data_type_input = node.data_type_input()

        name_tokens = [token.strip() for token in node.name.split(" ")]
        method_name = snake_case(' '.join(name_tokens))

        over_spec = STATIC_IMPLEMENTATIONS.get(node.name, {}).copy()
        over_spec.update(DEFAULT_IMPLEMENTATION.get(node.name, {}))
        over_spec = self.expand_spec(over_spec)

        # Debug option
        if False and self.node.name in ('Combine List'):
            print(f"DEBUG get_default_node_calls '{self.node.name} ({self.node.bl_idname})")
            print(f"- inputs          :", [socket.name for socket in inputs])
            print(f"- outputs         :", [socket.name for socket in outputs])
            print(f"- first_input     :", None if first_input is None else first_input.name)
            print(f"- first_output    :", None if first_output is None else first_output.name)
            print(f"- data_type_input :", data_type_input)
            print()

        # ---------------------------------------------------------------------------
        # Hacks
        # ---------------------------------------------------------------------------

        # Node: Value to String
        # Hacks because despite its name, Value is driven by data_type parameter
        # Auto algo implements only on Float with a data_type loop which is bad

        if node.name == 'Value to String':
            category = "Conversion"
            rules = "node.name is 'Value to String'"

            return NodeCalls(
                *NodeCalls.method(
                    category=category,
                    method_name="to_string",
                    self_socket="Value",
                    parameters={'data_type': "FLOAT"},
                    rules=rules,
                    class_name="Float",
                ),
                *NodeCalls.method(
                    category=category,
                    method_name="to_string",
                    self_socket="Value",
                    parameters={'data_type': "INT"},
                    rules=rules,
                    class_name="Integer",
                ),
                *NodeCalls.class_method(
                    category=category,
                    method_name="FromValue",
                    auto_data_type="Value",
                    rules=rules,
                    class_name="String",
                ),
            )                

        # ---------------------------------------------------------------------------
        # Static only : no implementation
        # ---------------------------------------------------------------------------

        if node.bl_idname in STATIC_IMPLEMENTATION_ONLY:
            return NodeCalls.function(
                category    = "Static Only",
                method_name = "no_name",
                implement   = False,
                rules       = "Static only node",
            )            
        

        # ---------------------------------------------------------------------------
        # Texture nodes
        # ---------------------------------------------------------------------------

        if node.color_tag == 'TEXTURE':

            tokens = [token for token in node.name.split() if token != 'Texture']
            method_name = CamelCase(' '.join(tokens))

            return NodeCalls.class_method(
                category="Texture",
                class_name="Texture",
                method_name=method_name,
                rules="Node color tag is TEXTURE",
            ).overrides(over_spec)        

        # ---------------------------------------------------------------------------
        # Shader BSDF
        # ---------------------------------------------------------------------------

        if node.is_shader:
            if name_tokens[-1] == 'BSDF':
                method_name = CamelCase(' '.join(name_tokens[:-1]))

                return NodeCalls.class_method(
                    category = "Shader",
                    class_name = "Shader",
                    method_name = method_name,
                    rules = "Ends with BSDF -> Shader constructor",
                ).overrides(over_spec)


        # ---------------------------------------------------------------------------
        # Nodes with input geometry
        # ---------------------------------------------------------------------------
    
        if node.has_geometry_in:

            category = 'Input Geometry'
            rules = "First input socket is Geometry"

            geo_socket = first_input
            method_name = None

            auto_data_type = data_type_input is not None
            if auto_data_type:
                rules += f"\nData type inferred from input '{data_type_input}'"
            data_type_loop = False
            domain_loop = False
            jump = node.auto_jump
        
            # ----- Class name / domain
        
            class_name = geo_socket.class_name
            if node.has_domain_parameter:
                domain_loop = True
                rules += f"\nHas 'domain' parameter, {domain_loop=}"
        
            # ----- Output geometry
            
            if node.has_geometry_out:
                rules += f"\nOut class {'==' if jump else '!='} in class -> jump = {jump}"
            
            # ----- Conversion "xxx to yyy"
            
            tokens = [token.strip() for token in node.name.split(" ")]
            if "to" in tokens:
            
                is_convert = True
            
                ito = tokens.index("to")
                aft = tokens[ito:]
            
                in_class = 'Domain' if node.has_domain_parameter else geo_socket.class_name 
            
                method_name = snake_case(' '.join(aft))
                jump = False
            
                rules += f"\nConversion 'class to class', {method_name=}, {jump=}"
            
            # ----- Method name
        
            if method_name is None:
                tokens = [token.strip() for token in node.name.split(" ")]
                if geo_socket.class_name in tokens:
                    tokens.remove(geo_socket.class_name)
                    method_name = snake_case(' '.join(tokens))
                    rules += f"\nRemove '{geo_socket.class_name}' from node name -> {method_name=}"
                elif geo_socket.class_name + 's' in tokens:
                    tokens.remove(geo_socket.class_name + 's')
                    method_name = snake_case(' '.join(tokens))
                    rules += f"\nRemove '{geo_socket.class_name}s' from node name -> {method_name=}"
                
                else:
                    method_name = snake_case(node.name)

            node_calls = NodeCalls.method(
                category = category,
                method_name = method_name,
                class_name = class_name,
                self_socket = geo_socket.socket_name,
                is_jump = jump,
                auto_data_type = data_type_input,
                rules = rules,
            ).overrides(over_spec)

            if data_type_loop:
                node_calls = self.get_data_type_calls(node_calls)
            if domain_loop:
                node_calls = self.get_domain_calls(node_calls)

            return node_calls

        # ---------------------------------------------------------------------------
        # Nodes with output geometry
        # ---------------------------------------------------------------------------
    
        if node.has_geometry_out:
        
            category = 'Output Geometry'
            rules = "First output socket is Geometry"
        
            out_socket = first_output

            class_name = out_socket.class_name
        
            tokens = [token.strip() for token in node.name.split(" ")]
            if class_name in tokens:
                tokens.remove(class_name)
            method_name = CamelCase(' '.join(tokens))

            return NodeCalls.class_method(
                category = category,
                class_name = class_name,
                method_name = method_name,
                rules = rules,
            ).overrides(over_spec)

        # ---------------------------------------------------------------------------
        # data_type drives both input and output sockets
        # ---------------------------------------------------------------------------

        # data_type_drives_first_input will be treater later
        if node.has_data_type_parameter and not node.data_type_drives_first_input:
            if (node.data_type_drives_inputs and node.data_type_drives_outputs
                    and all(sockets['inputs'] for sockets in node.data_type_driven_sockets.values())):

                node_call = NodeCalls.method(
                    category = 'Method',
                    method_name = method_name,
                    rules = "Data type drives input and output sockets",
                ).overrides(over_spec)
                return self.get_data_type_calls(node_call)

        # ---------------------------------------------------------------------------
        # Input nodes
        # ---------------------------------------------------------------------------
        
        if node.color_tag == 'INPUT':
        
            class_name = None
        
            method_name = snake_case(node.name)
            is_class_method = False

            category = "Input Node"
            rules = "Node is an Input Node"

            # Info node
            if (len(name_tokens) > 1) and (name_tokens[-1] == 'Info') and first_input is not None:
                rules += "\nNode is xxx Info"
                class_name = first_input.class_name
                if class_name == name_tokens[0] and len(name_tokens) == 2:
                    method_name = 'info'
                else:
                    method_name = snake_case(node.name)

            else:
                # First input socket can be None, attr or socket
                if bool(inputs):
                    socket = first_input
                    in_is_attr = socket.is_attribute
                    in_class_name = None if in_is_attr else socket.class_name
                else:
                    in_is_attr = True
                
                # Same for output socket
                if bool(outputs):
                    socket = first_output
                    out_is_attr = socket.is_attribute
                    out_class_name = None if out_is_attr else socket.class_name
                else:
                    out_is_attr = True

                rules += f" {in_is_attr=}, {out_is_attr=}"
                
                # if first input is not an attr, this is instance method
                if not in_is_attr:
                    class_name = in_class_name
                
                # if first output is not an attr, this is class constructor
                elif not out_is_attr:
                    class_name = out_class_name
                    is_class_method = True
                
                else:
                    is_class_method = True
                
                    tokens = [token.strip() for token in node.name.split(" ")]
                
                    if len(tokens) > 2 and tokens[-2] == "of":
                        target = tokens[-1]
                        for dom in DOMAINS:
                            if target in [dom, dom + 's']:
                                class_name = DOMAIN_NAME.get(dom, dom)
                                if class_name in GEOMETRY_CLASSES:
                                    method_name = snake_case(' '.join(tokens))
                                else:
                                    method_name = snake_case(' '.join(tokens[:-2])) 
                                rules += f"\n'Domain 1 of Domain 0' name -> {class_name=}, {method_name=}"
                                break
                        
                    elif len(tokens) > 2 and tokens[0] == "Is":
                        target = tokens[1]
                        for dom in DOMAINS:
                            if target in [dom, dom + 's']:
                                class_name = DOMAIN_NAME.get(dom, dom)
                                # Domain of Class would collide with domain name
                                # for instance : 'Points of Curve' -> points which collides width Curbe.points domain
                                method_name = snake_case(' '.join(tokens[2:]))
                                rules += f"\n'Domain is xxx' name -> {class_name=}, {method_name=}"
                                break
                            
                    else:
                        target = tokens[0]
                        for dom in ["Grease"] + DOMAINS:
                            if target in [dom, dom + 's']:
                                if dom == 'Grease':
                                    class_name = "GreasePencil"
                                    method_name = snake_case(' '.join(tokens[2:]))
                                else:
                                    class_name = DOMAIN_NAME.get(dom, dom)
                                    method_name = snake_case(' '.join(tokens[1:]))
                                break

            if False:
                print(f"DEBUG '{self.node.name}' ({self.node.bl_idname}): {is_class_method=} {class_name=}, {over_spec=}")

            if is_class_method:
                method_name = CamelCase(node.name)
                return NodeCalls.class_method(
                    category = category,
                    class_name = class_name,
                    method_name = method_name,
                    rules = rules,
                ).overrides(over_spec)
            else:
                return NodeCalls.method(
                    category = category,
                    class_name = class_name,
                    method_name = method_name,
                    self_socket = first_input.socket_name,
                    rules = rules,
                ).overrides(over_spec)
                    
        # ---------------------------------------------------------------------------
        # Grid node
        # ---------------------------------------------------------------------------

        if node.color_tag == 'GEOMETRY' and (node.is_grid_input or node.is_grid_output):

            category = 'Grid'
            rules = f"Grid node {node.is_grid_input=}, {node.is_grid_output=}"

            data_type_loop = False
            jump = False

            if node.is_grid_input:
                class_name = first_input.class_name
                is_class_method = False
                method_name = snake_case(node.name)
            else:
                class_name = first_output.class_name
                is_class_method = True

                tokens = [token.strip() for token in node.name.split(" ")]
                if class_name in tokens:
                    tokens.remove(class_name)
                method_name = CamelCase(' '.join(tokens))

            if node.has_data_type_parameter:
                data_type_loop = True
                class_name = None
                jump = node.is_grid_input and node.is_grid_output
                rules += f"\nNode has data_type parameter"

            if is_class_method:
                node_calls = NodeCalls.class_method(
                    category = category,
                    method_name = method_name,
                    rules = rules,
                ).overrides(over_spec)
            else:
                node_calls = NodeCalls.method(
                    category = category,
                    class_name = class_name,
                    method_name = method_name,
                    self_socket = first_input.socket_name,
                    is_jump = jump,
                    rules = rules,
                ).overrides(over_spec)
            if data_type_loop:
                node_calls = self.get_data_type_calls(node_calls)

            return node_calls

        # ---------------------------------------------------------------------------
        # First socket is driven by data_type
        # ---------------------------------------------------------------------------

        if node.data_type_drives_first_input:
            # Two version : constructor and method

            if True:
                ncs = NodeCalls.class_method(
                    category = 'Data type driven',
                    class_name = None,
                    method_name = CamelCase(node.name),
                    rules = "'data_type' parameter drives first input as class method",
                ).overrides(over_spec)
                node_calls = self.get_data_type_calls(ncs)

                ncs = NodeCalls.method(
                    category = 'Data type driven',
                    class_name = None,
                    method_name = snake_case(node.name),
                    self_socket = data_type_input,
                    rules = "'data_type' parameter drives first input as method",
                ).overrides(over_spec)
                node_calls.extend(self.get_data_type_calls(ncs))

                return node_calls

        tokens = [token.strip() for token in node.name.split(" ")]

        # ---------------------------------------------------------------------------
        # Name is "xxx class_name"
        # ---------------------------------------------------------------------------

        if ( (len(name_tokens) == 2) and 
            (name_tokens[-1] in CLASS_NAMES.values()) and
             len(node.bnode.inputs)):
            if CLASS_NAMES[node.bnode.inputs[0].type] == name_tokens[-1]:
                return NodeCalls.method(
                    category = "Transformations",
                    class_name = name_tokens[-1],
                    method_name = snake_case(name_tokens[0]),
                    self_socket = first_input.socket_name,
                    rules = "Name template is 'key_word class_name'",
                ).overrides(over_spec)

        # ---------------------------------------------------------------------------
        # Combine / Separate / Conversions
        # ---------------------------------------------------------------------------

        category = "Other"
        class_name = None
        method_name = None

        is_class_method = False

        if tokens[0] == "Combine":
            rules = "Node name starts with 'Combine'"
            class_name = first_output.class_name

            if tokens[1] in CLASS_NAMES.values():
                method_name = "Combine"
            else:
                method_name = CamelCase(' '.join(tokens))
            is_class_method = True

        elif tokens[0] == 'Separate':
            rules = "Node name starts with 'Separate'"

            class_name = first_input.class_name
            if class_name in tokens:
                tokens.remove(class_name)
            method_name = snake_case(' '.join(tokens))

        elif "to" in tokens:
            rules = "'to' in node name"
            is_class_method = False

            classes = {
                'Vector': 'Vector',
                'Euler': 'Vector',
                'Rotation': 'Rotation',
                'Float': 'Float',
                'Value': 'Float',
                'String': 'String',
                'Integer': 'Integer',
            }

            ito = tokens.index("to")
            sbef = ' '.join(tokens[:ito])
            saft = ' '.join(tokens[ito + 1:])

            in_class = classes.get(sbef)
            out_class = classes.get(saft)

            if in_class is not None:
                class_name = in_class
                method_name = snake_case(f"to {saft}")

                rules += "\nClass to something name"

            if out_class is not None:
                m_name = CamelCase("From " + ' '.join(tokens[:ito]))
                if class_name is None:
                    class_name = out_class
                    method_name = m_name
                    is_class_method = True

                    rules += f"\nSomething to Class -> {class_name}.{method_name} constructor"

                else:
                    class_name = (class_name, out_class)
                    method_name = (method_name, m_name)
                    is_class_method = (False, True)

                    rules += f"\nClass to Class -> two implementations : {class_name} {method_name}"
        else:
            rules = "No rule applied"

        # ---------------------------------------------------------------------------
        # All the other nodes
        # ---------------------------------------------------------------------------


        if class_name is None:
            rules += f"\nclass_name is None"
            if first_input is None:
                rules += " first_input is None"

                if first_output is None:
                    return NodeCalls.function(
                        category = 'Manual',
                        method_name = 'no_name',
                        implement = False,
                        rules = rules + f" {first_output!r}",
                    ).overrides(over_spec)

                
                class_name = first_output.class_name
                is_class_method = True
                method_name = CamelCase(node.name)
            else:
                rules += f"\nfirst_input is not None: {first_input.name}"

                class_name = first_input.class_name
                method_name = snake_case(node.name)

        # Conversion nodes can expose an instance method and a constructor.
        if isinstance(is_class_method, tuple):

            rules += f"\ntuple: {is_class_method=}"

            node_calls = NodeCalls()
            for target, name, class_method in zip(class_name, method_name, is_class_method, strict=True):
                rules += f" -> {is_class_method=}"
                if class_method:
                    spec = NodeCalls.class_method(
                        category = category,
                        method_name = name,
                        class_name = target,
                        auto_data_type = data_type_input,
                        rules = rules,
                    )
                else:
                    spec = NodeCalls.method(
                        category = category,
                        method_name = name,
                        class_name = target,
                        self_socket = first_input.socket_name,
                        auto_data_type = data_type_input,
                        rules = rules,
                    )
                node_calls.extend(spec.overrides(over_spec))
            return node_calls

        rules += f"\n{is_class_method=}"        

        if is_class_method:
            return NodeCalls.class_method(
                category = category,
                class_name = class_name,
                method_name = method_name,
                auto_data_type = data_type_input,
                rules = rules,
            ).overrides(over_spec)

        return NodeCalls.method(
            category = category,
            class_name = class_name,
            method_name = method_name,
            self_socket = first_input.socket_name,
            auto_data_type = data_type_input,
            rules = rules,
        ).overrides(over_spec)

    # ====================================================================================================
    # Generate source code from NodeCall spec
    # ====================================================================================================

    def _gen_source_code(self, node_call: NodeCall):
        """Generate one function from a resolved implementation description."""

        assert isinstance(node_call, NodeCall), "Algor error: use NodeCall not NodeCalls"

        node_call._check()

        if node_call.in_line is not None:
            return node_call.in_line

        # set the parameters
        self.node.reset_params()
        self.set_parameters(**node_call.parameters)

        from .sourcewriter import R0
        
        # Prepare contextual arguments through the shared NodeInfo path.
        fixed_params = {name: value for name, value in self.parameters.items() if value is not None}
        fixed_params.update(node_call.parameters)
        receiver = node_call.self_socket if node_call.has_self else None
        if receiver == 'IGNORE':
            receiver = None
        elif receiver is not None and receiver.startswith('NODE.'):
            receiver = getattr(self.node, receiver[5:])
        inputs = self.node.get_node_arguments(
            self_socket=receiver,
            fixed_sockets=node_call.fixed_sockets,
            last_sockets=node_call.last_sockets,
            geo_selection=node_call.has_self and node_call.geo_selection,
            auto_data_type=node_call.auto_data_type,
            type_aliases=self.type_aliases,
            **fixed_params,
        )

        # ---------------------------------------------------------------------------
        # We can build the source code
        # ---------------------------------------------------------------------------

        source = SourceWriter(indent=0 if node_call.is_function else 1)

        source.write(f"#Node {self.node.name}")

        # decorator
        if node_call.decorator is not None:
            source.write(node_call.decorator)

        # Header
        all_args = inputs.get_header()
        if node_call.first_arg is not None:
            all_args.insert(0, node_call.first_arg)

        sep = f",{R0}"
        source.write(f"def {node_call.method_name}({R0}{sep.join(all_args)}):")

        source.indent += 1

        # Doc String
        source.write(f'"""Node {self.node.name}.\n')
        source.write(f"Jump: {node_call.is_jump}")
        source.write(inputs.get_doc_source())

        if node_call.method_type != 'SETTER':
            source.write()
            source.write("Returns")
            source.write("-------")

            if node_call.return_socket is not None:
                source.write("Socket")
                source.write(f"    Socket '{node_call.return_socket}'.")

            elif node_call.return_kind == 'OUT':
                if node_call.is_jump:
                    if node_call.method_name.startswith('get'):
                        source.write("Socket")
                        source.write("    Second output socket, or self if there is no second output.")
                    else:
                        source.write("Self")
                        source.write("    The updated receiver, or its owning geometry for a domain.")
                    source.write("    Updates self from the default output socket.")
                else:
                    source.write("Socket")
                    source.write("    Default output socket.")

            elif node_call.return_kind == 'SECOND_OUT':
                source.write("Socket")
                fallback_doc = 'self' if node_call.has_self else 'the default output socket'
                source.write(f"    Second available output socket, or {fallback_doc} if there is none.")

            elif node_call.return_kind == 'cls':
                source.write("Self")
                source.write("    Default output socket wrapped in the calling class.")

            elif node_call.return_kind == 'NODE':
                source.write(f"Node")

            else:
                source.write(node_call.return_kind)
                source.write(f"    Default output socket wrapped in {node_call.return_kind}.")
            
        source.write('"""')

        source.write(inputs.get_code_source(self.node.name))

        # return

        if node_call.is_jump:
            source.write("self._jump(node._out)")

        if node_call.method_type != 'SETTER':
            if node_call.return_socket is not None:
                source.write(f"return node[{node_call.return_socket!r}]")

            elif node_call.return_kind == 'OUT':
                if node_call.is_jump:
                    if node_call.method_name.startswith('get'):
                        source.write("return node._second_out(self)")
                    else:
                        source.write("return self.self_return")
                else:
                    source.write(f"return node._out")

            elif node_call.return_kind == 'SECOND_OUT':
                fallback = 'self' if node_call.has_self else 'node._out'
                source.write(f"return node._second_out({fallback})")

            elif node_call.return_kind == 'cls':
                if node_call.is_instance_method:
                    source.write(f"return self.self_class(node._out)")
                else:
                    source.write(f"return cls(node._out)")

            elif node_call.return_kind == 'NODE':
                source.write(f"return node")

            else:
                source.write(f"return {node_call.return_kind}(node._out)")

        return source.source

    # ====================================================================================================
    # Generate source code from NodeCall spec
    # ====================================================================================================

    def gen_source_code(self, node_calls: NodeCall | NodeCalls, register=None):

        if isinstance(node_calls, NodeCall):
            node_calls = NodeCalls(node_calls)

        sources = []

        for node_call in node_calls:

            if not node_call.implement:
                continue

            is_done = False

            # Loop on class_name
            if node_call.class_name == 'Socket':
                assert self.node.has_data_type_parameter, "Algo error"
                calls = self.get_data_type_calls(NodeCalls(node_call))
                self.gen_source_code(calls, register=register)
                is_done = True
                break

            if is_done:
                continue

            # Loop on parameters
            for param_name, param_value in node_call.parameters.items():
                if param_value in (ADD_LOOP, LOOP_ONLY):
                    node_call = dataclass_replace(node_call, parameters={
                        name: value for name, value in node_call.parameters.items()
                        if name != param_name
                    })
                    calls = self.get_loop_parameter_calls(
                        NodeCalls(node_call), 
                        param_name, 
                        include_base = param_value==ADD_LOOP)
                    self.gen_source_code(calls, register=register)
                    is_done = True
                    break

            # A loop was done
            if is_done:
                continue

            if node_call.in_line is None and not self.node.outputs:
                node_call = node_call.replace(return_kind='NODE', return_socket=None)

            source = self._gen_source_code(node_call)

            # Debug option
            if False and self.node.name == 'Combine List':
                print("DEBUG register", self.node.name)
                print(repr(node_call))
                print()
                print(source)
                print()

            if register is not None:
                register(self.node, node_call, source)

            sources.append(source)

        return sources

        

    
