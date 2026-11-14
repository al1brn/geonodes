"""Collect generated implementations for one Blender tree environment."""

import ast
import inspect
import textwrap

import bpy

from ..kernel import snake_case, get_socket_type, get_class_name
from . import gen_config
from . import config, utils
from .node_call import NodeCall, NodeCalls
from .sourcewriter import SourceWriter
from .typealiases import TypeAliases
from .tree import Tree
from .output import render_modules
from .node_info import NodeInfo
from .node_implementation import NodeImplementation

TAB = "    "

class TreeClass:
    """Own generation state for exactly one tree type."""

    def __init__(self, tree_type):
        if tree_type not in config.TREE_TYPES:
            raise ValueError(f'Unsupported tree type: {tree_type!r}')
        if not gen_config.SOCKETS:
            gen_config.build()
        self.tree_type = tree_type
        self.files = {tree_type: {}}
        self.cross_refs = {tree_type: {}}
        self.type_aliases = TypeAliases()

    def implementation(self, node):
        return NodeImplementation(node, type_aliases=self.type_aliases)

    def generate(self):
        """Collect this environment; writing is coordinated by generate.py."""
        self.files = {self.tree_type: {}}
        self.cross_refs = {self.tree_type: {}}
        self.type_aliases = TypeAliases()
        self.gen_static_code()
        self.gen_math()
        self.gen_compare()
        self.gen_mix()
        self.gen_nodes()
        self.gen_properties()
        self.gen_typed_constructors()
        self.gen_additional()
        self.files[self.tree_type]['type_aliases.py'] = [self.type_aliases.source]
        return self

    def render_modules(self, core_path):
        """Validate all sources in this environment and return rendered modules."""
        return render_modules(core_path, self.tree_type, self.files[self.tree_type],
                              self.cross_refs[self.tree_type])


    def get_class_properties(self, class_name):
        properties = []
        for key in ('common', self.tree_type):
            for name, props in config.PROPERTIES[key].items():
                if name == class_name:
                    properties.extend(list(props.keys()))
        return properties


    def register_source(self, node, node_call: NodeCall, source, *, tree_type=None, write_source=True):
        """Enregistrer source avec la destination et le retour de node_call.

        node_call.class_name désigne la classe cible, 'nd' ou 'gnmath'.
        Le fichier cible et les règles sont déduits de cette description.
        tree_type est nécessaire si node vaut None.
        write_source=False enregistre seulement la référence documentaire.
        """
        destination = node_call.class_name

        if destination is None:
            raise ValueError(f"Missing class_name for {node_call.method_name!r}")
        
        if destination in ('nd', 'ND'):
            filename, destination = 'static_nd.py', 'nd'

        elif destination == 'gnmath':
            filename = 'gnmath.py'

        else:
            if False and (destination == 'Face'):
                print(f"DEBUG register {destination}.{node_call.method_name} {node_call.method_type}")

            # No class property if property exists
            if node_call.method_type in ('CLASS_PROPERTY', 'CLASS_METHOD') and node_call.method_name in self.get_class_properties(destination):
                print(f"INFO {destination}.{node_call.method_name} static property ignored since instance property exists.")
                return

            prefix = 'dom_' if destination in config.DOMAIN_CLASSES else ''
            filename = prefix + destination.lower() + '.py'
        returns = (None if node_call.method_type == 'SETTER' else
                   node_call.return_socket if node_call.return_socket is not None else
                   node_call.return_kind)
        rules = node_call.rules

        if tree_type is None and node is not None:
            tree_type = node.btree.bl_idname
        if tree_type is None:
            raise ValueError('tree_type is required when registering source without a node.')

        if False:
            print("DEBUG SOURCE", node.name)
            print(source)
            print()

        try:
            function = ast.parse(textwrap.dedent(source)).body[0]
        except Exception as e:

            print('-'*80)
            print(source)
            print('-'*80)

            print(f"Compilation error in '{None if node is None else node.name}'")
            if len(rules):
                print("\n".join(rules))
            print()
            raise e

        name = function.name
        reference = {
            'func_name': name,
            'node_name': None if node is None else node.bnode.name,
            'tree_type': tree_type,
            'is_classmethod': any((isinstance(d, ast.Name) and d.id == 'classmethod') or
                                  (isinstance(d, ast.Attribute) and d.attr == 'classproperty')
                                  for d in function.decorator_list),
            'is_get': any((isinstance(d, ast.Name) and d.id == 'property') or
                          (isinstance(d, ast.Attribute) and d.attr == 'classproperty')
                          for d in function.decorator_list),
            'is_set': any(isinstance(d, ast.Attribute) and d.attr == 'setter'
                          for d in function.decorator_list),
            'returns': returns,
            'signature': f'({ast.unparse(function.args)})',
        }
        files = self.files.setdefault(tree_type, {})
        cross_refs = self.cross_refs.setdefault(tree_type, {})

        for node_id, destinations in cross_refs.items():
            for previous in destinations.get(destination, []):
                if previous['func_name'] != name:
                    continue
                if ((reference['is_set'] and previous['is_get']) or
                        (reference['is_get'] and previous.get('is_set', False))):
                    continue

                def describe(identifier, ref):
                    kind = 'setter' if ref.get('is_set', False) else 'property' if ref['is_get'] else 'classmethod' if ref['is_classmethod'] else 'method'
                    ui_name = utils.get_node_names(ref['tree_type']).get(identifier, ref['node_name'])
                    return (f"{identifier} ({ui_name})\n"
                            f"    {kind}: {destination}.{name}{ref['signature']}\n"
                            f"    return socket: {ref['returns']!r}")

                raise ValueError(
                    f'Duplicate implementation: {destination}.{name}\n'
                    f'  Already registered: {describe(node_id, previous)}\n'
                    f'  Conflicting proposal: {describe(node.bnode.bl_idname, reference)}\n'
                    'Resolve the naming conflict in generation2/config.py.'
                )
            
        if write_source:
            files.setdefault(filename, []).append(source)

        if node is not None:
            cross_refs.setdefault(node.bnode.bl_idname, {}).setdefault(destination, []).append(reference)


    def gen_handwritten_references(self):
        """Register actual handwritten signatures without copying their code."""
        tree = bpy.data.node_groups.new('Handwritten references', self.tree_type)
        available = utils.get_node_names(self.tree_type)
        try:
            for identifier, destinations in config.HANDWRITTEN_IMPLEMENTATIONS.items():
                if identifier not in available:
                    continue
                node = NodeInfo(tree, tree.nodes.new(identifier))
                for destination, names in destinations.items():
                    assert False, "To be updated"
                    owner = getattr(core_module, destination)
                    for name in names:
                        function = inspect.getattr_static(owner, name)
                        constructor = (NodeCall.class_method if isinstance(function, classmethod) else
                                       NodeCall.static_method if isinstance(function, staticmethod) else
                                       NodeCall.method)
                        if isinstance(function, (classmethod, staticmethod)):
                            function = function.__func__
                        source = inspect.getsource(function)
                        node_call = constructor(name, class_name=destination, in_line=source)
                        self.register_source(node, node_call, source, write_source=False)
        finally:
            bpy.data.node_groups.remove(tree)    


    def gen_static_code(self):
        """Collect nd accessors and cross references for the current environment."""
        def generate(node):
            name = snake_case(node.bnode.name)
            constructor = NodeCall.class_property if node.is_class_property else NodeCall.class_method
            node_call = constructor(name, class_name='nd', return_kind='OUT')
            source = self.implementation(node).gen_node_call(node_call)
            self.register_source(node, node_call, source)

        NodeInfo.loop_on_nodes(generate, tree_type=self.tree_type)


    def gen_math(self):

        # 0 : operation name
        # 1 : method name
        # 2 : function name
        # 3 : operator name

        # Operator name can be
        # - a single str -> name of the operator
        # - a couple (operator name, source code)
        # - a list of above

        MATH = {
            # ==================================================
            # Common
            # ==================================================

            'common': {

            # --------------------------------------------------
            # Math Node
            # --------------------------------------------------
                'Math': [

            # Methods with binary operator
            ('ADD', 'add', 'add',                   'add'),
            ('SUBTRACT', 'subtract', 'subtract',    'sub'),
            ('MULTIPLY', 'multiply', 'multiply',    ['mul', ('neg', 'self.multiply(-1)')]),
            ('DIVIDE', 'divide', 'divide',          'truediv'), 
            ('POWER', 'power', 'power',             'pow'), 
            ('MODULO', 'modulo', 'modulo',          'modulo'), 

            # Methods with unary operator
            ('ABSOLUTE', 'abs', 'abs',              'abs'), 
            ('ROUND', 'round', 'round',             'round'), 
            ('TRUNC', 'trunc', 'trunc',             'trunc'), 
            ('FLOOR', 'floor', 'floor',             'floor'), 
            ('CEIL', 'ceil', 'ceil',                'ceil'), 
            
            # Other methods
            ('MULTIPLY_ADD', 'multiply_add'), ('LOGARITHM', 'log'), ('SQRT', 'sqrt'),
            ('INVERSE_SQRT', 'inverse_sqrt'), ('EXPONENT', 'exp'),
            ('MINIMUM', 'min'), ('MAXIMUM', 'max'), 
            ('SIGN', 'sign'), 
            ('SMOOTH_MIN', 'smooth_min'), ('SMOOTH_MAX', 'smooth_max'),
            ('FRACT', 'fract'), ('FLOORED_MODULO', 'floored_modulo'),
            ('WRAP', 'wrap'), ('SNAP', 'snap'), ('PINGPONG', 'pingpong'),
            ('SINE', 'sin'), ('COSINE', 'cos'), ('TANGENT', 'tan'),
            ('ARCSINE', 'asin'), ('ARCCOSINE', 'acos'), ('ARCTANGENT', 'arctangent'),
            ('ARCTAN2', 'atan2'), ('SINH', 'sinh'), ('COSH', 'cosh'), ('TANH', 'tanh'),
            ('RADIANS', 'radians'), ('DEGREES', 'degrees'),
                ], 

            # --------------------------------------------------
            # Vector Math Node
            # --------------------------------------------------

                'Vector Math': [

            # Methods with binary operator
            ('ADD', 'add', 'vadd',                  'add'),
            ('SUBTRACT', 'subtract', 'vsubtract',   'sub'),
            ('MULTIPLY', 'multiply', 'vmultiply',   'mul'),
            ('DIVIDE', 'divide', 'vdivide',         'truediv'), 
            ('POWER', 'power', 'vpower',            'pow'), 
            ('MODULO', 'modulo', 'vmodulo',         'modulo'), 

            # Methods with unary operator
            ('ABSOLUTE', 'abs', 'vabs',             'abs'), 
            ('ROUND', 'round', 'vround',            'round'), 
            ('FLOOR', 'floor', 'vfloor',            'floor'), 
            ('CEIL', 'ceil', 'vceil',               'ceil'), 
            ('SCALE', 'scale', 'scale',              ('neg', 'self.scale(-1)')), 

            # Other methods            
            ('MULTIPLY_ADD', 'multiply_add', 'vmultiply_add'),
            ('CROSS_PRODUCT', 'cross', 'cross'), ('PROJECT', 'project', 'project'),
            ('REFLECT', 'reflect', 'reflect'), ('REFRACT', 'refract', 'refract'),
            ('FACEFORWARD', 'faceforward', 'faceforward'), ('DOT_PRODUCT', 'dot', 'dot'),
            ('DISTANCE', 'distance', 'distance'), ('LENGTH', 'length', 'length'),
            ('NORMALIZE', 'normalize', 'normalize'),
            ('SIGN', 'sign', 'vsign'), ('MINIMUM', 'min', 'vmin'),
            ('MAXIMUM', 'max', 'vmax'), 
            ('FRACTION', 'fraction', 'vfraction'), 
            ('WRAP', 'wrap', 'vwrap'), ('SNAP', 'snap', 'vsnap'),
            ('SINE', 'sin', 'vsin'), ('COSINE', 'cos', 'vcos'), ('TANGENT', 'tan', 'vtan'),
                ],

            # --------------------------------------------------
            # Integer Math Node
            # --------------------------------------------------

                'Integer Math': [

            # Methods with binary operator
            ('ADD', 'add', 'iadd',                   'add'),
            ('SUBTRACT', 'subtract', 'isubtract',    'sub'),
            ('MULTIPLY', 'multiply', 'imultiply',    'mul'),
            ('DIVIDE', 'divide', 'idivide',          'floordiv'), 
            ('POWER', 'power', 'ipower',             'pow'), 
            ('MODULO', 'modulo', 'imodulo',          'modulo'), 

            # Methods with unary operator
            ('ABSOLUTE', 'abs', 'iabs',             'abs'), 
            ('NEGATE', 'negate', 'negate',          'neg'),
            
            # Other methods
            ('MULTIPLY_ADD', 'multiply_add', 'imultiply_add'), ('SIGN', 'sign', 'isign'),
            ('MINIMUM', 'min', 'imin'), ('MAXIMUM', 'max', 'imax'), 
            ('DIVIDE_ROUND', 'divide_round', 'divide_round'),
            ('DIVIDE_FLOOR', 'divide_floor', 'divide_floor'),
            ('DIVIDE_CEIL', 'divide_ceil', 'divide_ceil'),
            ('FLOORED_MODULO', 'floored_modulo', 'ifloored_modulo'),
            ('GCD', 'gcd', 'gcd'), ('LCM', 'lcm', 'lcm'),
                ],

            # --------------------------------------------------
            # Boolean Math Node
            # --------------------------------------------------

                'Boolean Math': [

            # Methods with binary operator
            ('AND', 'band', 'band', ['and', 'mul']),
            ('OR', 'bor', 'bor',   ['or', 'add']),
            ('XOR', 'xor', 'xor',   ['xor', 'sub']),

            # Methods width unary operator
            ('NOT', 'bnot', 'bnot', 'neg'),

            # Other methods
            ('NAND', 'not_and'), ('NOR', 'nor'), ('XNOR', 'xnor'),
            ('IMPLY', 'imply'), ('NIMPLY', 'nimply'),
                ],
            },

            # ==================================================
            # Geometry nodes
            # ==================================================

            'GeometryNodeTree': {
                'Math': [
                    ('LESS_THAN', 'math_less_than'),
                    ('GREATER_THAN', 'math_greater_than'), 
                    ('COMPARE', 'math_compare'),
                ],

            # --------------------------------------------------
            # Bit Math Node
            # --------------------------------------------------

                'Bit Math': [
            # Methods with binary operator
            ('AND', 'bw_and', 'bw_and',         'and'), 
            ('OR', 'bw_or', 'bw_or',            'or'), 
            ('XOR', 'bw_xor', 'bw_xor',         'xor'),
            ('SHIFT', 'bw_shift', 'bw_shift',   ['lshift', ('rshift', 'self.bw_shift(-other)'), ('rrshift', 'type(self)(other).bw_shift(-self)'), ('irshift', 'self._jump(self << -other)')]), 

            # Methods width unary operator
            ('NOT', 'bw_not', 'bw_not',         'invert'), 

            # Other methods
            ('ROTATE', 'bw_rotate'),
                ],
            },

            # ==================================================
            # Shader nodes
            # ==================================================

            'ShaderNodeTree': {
                'Math': [
                    ('LESS_THAN', 'less_than'),
                    ('GREATER_THAN', 'greater_than'), 
                    ('COMPARE', 'compare'),
                ],
            },
        }

        CLASS_NAMES = {
            'Math'          : "Float",
            'Vector Math'   : "Vector",
            'Integer Math'  : "Integer",
            'Boolean Math'  : "Boolean",
            'Bit Math'      : "Integer",
        }

        node_specs = {name: list(specs) for name, specs in MATH['common'].items()}
        for name, specs in MATH[self.tree_type].items():
            node_specs.setdefault(name, []).extend(specs)

        with Tree(self.tree_type) as tree:
            for node_name, specs in node_specs.items():
                if node_name not in tree.nodes:
                    continue

                node = tree.create_node(node_name)
                class_name = CLASS_NAMES[node_name]

                node_info = NodeInfo(tree.btree, node)
                impl_base = self.implementation(node_info)

                for spec in specs:
                    operation = spec[0]
                    method_name = spec[1]
                    func_name = spec[2] if len(spec) > 2 else method_name

                    implementation = impl_base.copy()
                    implementation['operation'] = operation

                    function_spec = NodeCall.function(
                        func_name,
                        class_name='gnmath',
                        parameters={'operation': operation},
                    )
                    self.register_source(node_info, function_spec,
                                        implementation.gen_node_call(function_spec))
                    
                    self_socket = next(socket.socket_name for socket in
                                       node_info.get_possible_sockets(operation=operation)
                                       if socket.enabled and socket.socket_type != 'CUSTOM')
                    method_spec = NodeCall.method(
                        method_name,
                        class_name=class_name,
                        self_socket=self_socket,
                        parameters={'operation': operation},
                    )
                    self.register_source(node_info, method_spec,
                                        implementation.gen_node_call(method_spec))

                    if len(spec) < 4:
                        continue

                    # -------------------------
                    # Operators
                    # -------------------------

                    op_specs = spec[3]
                    if not isinstance(op_specs, list):
                        op_specs = [op_specs]

                    for op_spec in op_specs:
                        op_code = None
                        if isinstance(op_spec, tuple):
                            op_name = op_spec[0]
                            op_code = op_spec[1]
                        else:
                            op_name = op_spec
                            if utils.is_unary_operator(op_name):
                                op_code = f"self.{method_name}()"

                        if utils.is_unary_operator(op_name):
                            source = f"{TAB}def __{op_name}__(self):\n"
                            source += f"{TAB*2}return {op_code}\n"

                            self.register_source(node_info,
                                                method_spec.replace(method_name=f'__{op_name}__'), source)

                        elif op_code is not None:
                            source = f"{TAB}def __{op_name}__(self, other):\n"
                            source += f"{TAB*2}return {op_code}\n"

                            self.register_source(node_info,
                                                method_spec.replace(method_name=f'__{op_name}__'), source)
                        
                        else:
                            for prefix in ["", "r", "i"]:

                                source = f"{TAB}def __{prefix}{op_name}__(self, other):\n"

                                if prefix in ("", "i"):
                                    source += f"{TAB*2}value = self.{method_name}(other)\n"
                                else:
                                    source += f"{TAB*2}value = type(self)(other).{method_name}(self)\n"
                                
                                if prefix == "i":
                                    source += f"{TAB*2}self._jump(value)\n"
                                    source += f"{TAB*2}return self\n"
                                else:
                                    source += f"{TAB*2}return value\n"

                                self.register_source(node_info,
                                                    method_spec.replace(method_name=f'__{prefix}{op_name}__'), source)


    def gen_compare(self):

        operators = {'LESS_THAN': 'lt', 'GREATER_THAN': 'gt', 'LESS_EQUAL': 'le', 'GREATER_EQUAL': 'ge',
                     'EQUAL': 'eq', 'NOT_EQUAL': 'ne', 'BRIGHTER': 'gt', 'DARKER': 'lt'}

        if self.tree_type != 'GeometryNodeTree':
            return

        with Tree(self.tree_type) as tree:

            node_info = NodeInfo(tree.btree, tree.create_node('Compare'))

            for data_type in node_info.config['data_type']['enums']:

                class_name = get_class_name(data_type)

                node_info.set_params(data_type=data_type)
                params = node_info.snapshot_params()

                operations = params['operation']['enums']
                for operation in operations:
                    method_name = snake_case(operation)
                    implementation = self.implementation(node_info)
                    implementation["data_type"] = data_type
                    implementation["operation"] = operation

                    ispec = NodeCall.method(
                        class_name = class_name,
                        method_name = method_name,
                        self_socket = "A",
                    )

                    self.register_source(node_info, ispec, implementation.gen_node_call(ispec))

                    op_name = operators[operation]
                    source = f"{TAB}def __{op_name}__(self, other):\n"
                    source += f"{TAB*2}return self.{method_name}(other)\n"

                    self.register_source(node_info, ispec.replace(method_name=f'__{op_name}__'), source)


    def gen_mix(self):

        with Tree(self.tree_type) as tree:

            node_info = NodeInfo(tree.btree, tree.create_node('Mix'))

            for data_type in node_info.config['data_type']['enums']:
                class_name = get_class_name(data_type)

                implementation = self.implementation(node_info)
                implementation["data_type"] = data_type

                ispec = NodeCall.class_method(
                    class_name = class_name,
                    method_name = "Mix",
                    last_sockets=('Factor',),
                )
                self.register_source(node_info, ispec, implementation.gen_node_call(ispec))


                ispec = NodeCall.method(
                    class_name = class_name,
                    method_name = "mix",
                    self_socket="A",
                    last_sockets=('Factor',),
                )
                self.register_source(node_info, ispec, implementation.gen_node_call(ispec))


    def gen_properties(self):

        for class_name, properties in {**config.PROPERTIES['common'], **config.PROPERTIES[self.tree_type]}.items():
            for prop_name, set_get in properties.items():
                for sg in ('getter', 'setter'):
                    spec = set_get.get(sg)

                    # No spec
                    if spec is None:
                        if sg == 'setter':
                            break
                        # Write only
                        source = SourceWriter(indent=1)
                        source.write(f"@property\ndef {prop_name}(self):")
                        source.write(
                            f'"""Write-only property; {prop_name}."""',
                            f"raise NodeError({f"Property {class_name}.{prop_name} is write only."!r})\n",
                            indent=1)

                        node_call = NodeCall.getter(
                            class_name = class_name,
                            method_name = prop_name,
                            in_line = source.source,
                        )
                        self.register_source(None, node_call, source.source, tree_type=self.tree_type)
                        break


                    # Read the config
                    node_name = spec['node']
                    parameters = spec.get('parameters', {}).copy()
                    fixed_sockets = spec.get('fixed_sockets', {})
                    in_socket = spec.get('socket', {})
                    is_jump = True

                    with Tree(self.tree_type) as tree:

                        node_info = NodeInfo(tree.btree, tree.create_node(node_name))

                        # Self socket is the geometry input
                        # Put un assigned sockets into fixed to exclude them from arguments
                        self_socket = None
                        names_err = []
                        for bsock in node_info.bnode.inputs:
                            sock_name = bsock.label if bool(bsock.label) else bsock.name
                            if (self_socket is None) and bsock.enabled and bsock.type == 'GEOMETRY':
                                self_socket = sock_name
                            else:
                                if sock_name != in_socket:
                                    fixed_sockets[sock_name] = None
                            names_err.append(sock_name)

                        if self_socket is None:
                            if sg == 'setter':
                                raise AttributeError(f"'{node_name}' {class_name}.{prop_name} setter: no valid self socket found in {names_err}")
                            self_socket = 'IGNORE'
                            is_jump = False

                        # Include free parameters into parameter to exclude themt from argumnents
                        for name, param in node_info.default_params.items():
                            if name not in parameters:
                                parameters[name] = param.value

                        # Let's build the calling specs
                        constructor = NodeCall.getter if sg == 'getter' else NodeCall.setter
                        node_call = constructor(
                            class_name = class_name,
                            method_name = prop_name,
                            self_socket = self_socket,
                            is_jump = sg == 'setter',
                            fixed_sockets = fixed_sockets,
                            parameters = parameters,
                        )

                        # We gen the source
                        node_impl = self.implementation(node_info)
                        node_impl.parameters.update(node_call.parameters)
                        source = node_impl.gen_node_call(node_call)

                        self.register_source(node_info, node_call, source)


    def gen_nodes(self):
        """Generate the supplied descriptions, expanding domain and type loops."""

        domains = {'POINT': 'Point', 'EDGE': 'Edge', 'FACE': 'Face', 'CORNER': 'Corner',
                   'CURVE': 'Spline', 'SPLINE': 'Spline', 'INSTANCE': 'Instance', 'LAYER': 'Layer',
                   'AUTO': 'Geometry'}

        # ---------------------------------------------------------------------------
        # Generate from a single spec dict
        # ---------------------------------------------------------------------------

        def generate_from_spec(node, node_call):

            if isinstance(node_call, NodeCalls):
                for nc in node_call:
                    generate_from_spec(node, nc)
                return

            if not node_call.implement or node_call.class_name is None:
                return

            node_impl = self.implementation(node)
            node_impl.parameters.update(node_call.parameters)

            source = node_impl.gen_node_call(node_call)

            self.register_source(node, node_call, source)

            # __getitem__ / __setitem__

            as_item = config.ITEM_IMPLEMENTATION.get(node.name, None)
            if (as_item is not None) and (node_call.method_type=='METHOD'):

                ispec = node_call.replace(
                    method_type = 'METHOD',
                    method_name = '__getitem__' if as_item['kind']=='get' else '__setitem__',
                )
                ret_kind = as_item.get('OUT', ispec.return_kind)
                if ret_kind is not None:
                    ispec.return_kind = ret_kind

                source = node_impl.gen_node_call(ispec)

                self.register_source(node, ispec, source)

        # ---------------------------------------------------------------------------
        # Spec coming from get_node_implementation can be multiple
        # ---------------------------------------------------------------------------

        def generate(node):
            implementation = self.implementation(node)
            node_calls = implementation.get_node_implementation()
            generate_from_spec(node, node_calls)

        # ---------------------------------------------------------------------------
        # Main is a loop on nodes
        # ---------------------------------------------------------------------------

        NodeInfo.loop_on_nodes(generate, tree_type=self.tree_type)


    def gen_typed_constructors(self):
        """Generate input constructors and subtype shortcuts for this environment."""

        # List of typed socket types
        tree_type = self.tree_type
        with Tree(tree_type) as tree:
            valids = []
            for socket_name in tree.valid_input_sockets:
                if socket_name == 'NodeSocketSound':
                    continue
                sock = tree.btree.interface.new_socket(socket_type=socket_name, name=socket_name)
                socket_type = get_socket_type(sock)
                if socket_type not in valids:
                    valids.append(socket_type)

        # Loop on this list
        for socket_type in valids:

            # Remove those out of tree type
            socket_descr = gen_config.SOCKETS[socket_type]
            if socket_descr[tree_type] is None:
                continue

            # Read the class name and props
            class_name = socket_descr['class_name']
            ptype, def_val = config.PYTHON_TYPES.get(class_name, ('object', None))
            props = socket_descr['props']
            if ptype == 'str' and 'default' in props:
                def_val = props['default'][2]

            # Sort the props for a proper order in arguments
            sorted_props = [name for name in ('min', 'max', 'tip') if name in props]
            sorted_props.append('panel')
            sorted_props += [name for name in props
                             if name not in ('min', 'max', 'tip', 'panel', 'default', 'subtype')]
            subtypes = ['NONE'] + [subtype for subtype in socket_descr.get('subtypes', ())
                                   if subtype != 'NONE']

            # One method per subtype
            for subtype in subtypes:

                # ::::: Prepare

                # prop name, exposed ndame and method name
                create_socket = subtype == 'NONE'
                name = class_name if create_socket else ''.join(part.title() for part in subtype.split('_'))
                method_name = '_create_input_socket' if create_socket else name

                # list of arguments
                # name, annotation, default, documentation, forwarded expression
                arguments = []

                # Socket default value
                if 'default' in props:
                    arguments.append(('value', ptype, def_val, 'Default value.',
                                      'default_value=value' if create_socket else 'value=value'))
                arguments.append(('name', 'str', name, 'Input socket name.', 'name=name'))

                # Other arguments
                for arg_name in sorted_props:
                    if arg_name == 'panel':
                        arguments.append(('panel', 'str', '', 'Panel name.', 'panel=panel'))
                        continue
                    prop_name, val_type, value = props[arg_name]
                    annotation = (f"Literal{list(val_type)!r}" if val_type else 'str') if isinstance(val_type, tuple) else val_type
                    arguments.append((arg_name, annotation, value, f'Property {prop_name}.',
                                      f'{arg_name}={arg_name}'))

                # subtype
                if create_socket and 'subtype' in props:
                    arguments.append(('subtype', 'str', 'NONE', 'Socket subtype.', 'subtype=subtype'))

                # ::::: Write the source

                # Header
                source = SourceWriter(indent=1)
                source.write('@classmethod', f'def {method_name}(', '    cls,')
                for arg_name, annotation, value, _, _ in arguments:
                    source.write(f'{arg_name}: {annotation} = {value!r},', indent=1)
                source.write('):')

                # Doc string
                source.write(f'"""Create a {class_name} input with subtype {subtype}.', indent=1)
                source.write()
                source.write('Parameters', '----------', indent=1)
                for arg_name, annotation, value, doc, _ in arguments:
                    source.write(f'{arg_name} : {annotation}, optional', f'    {doc} Default: {value!r}.', indent=1)
                source.write()
                source.write('Returns', '-------', class_name, '    Input socket.', '"""', indent=1)

                # Prepare call
                forwarded = [argument[4] for argument in arguments]
                if create_socket:
                    source.write('from ...root.tree import Tree', indent=1)
                    if 'default' in props:
                        source.write('value = utils.python_value_for_socket(value, cls.SOCKET_TYPE)', indent=1)
                    forwarded.insert(0, repr(socket_descr[tree_type]))
                    call_name = 'Tree.current_tree().create_input_socket'
                else:
                    forwarded.append(f'subtype={subtype!r}')
                    call_name = 'cls'

                # Call
                source.write(f'return {call_name}(', indent=1)
                for argument in forwarded:
                    source.write(argument + ',', indent=2)
                source.write(')', indent=1)

                node_call = NodeCall.class_method(method_name, class_name=class_name,
                                                 return_kind=class_name, in_line=source.source)
                self.register_source(None, node_call, node_call.in_line, tree_type=tree_type)


    def gen_additional(self):
        """Generate additional descriptions through NodeCall and the standard generator."""
        for additions in (config.ADDITIONAL_IMPLEMENTATIONS['common'], config.ADDITIONAL_IMPLEMENTATIONS[self.tree_type]):
            for node_name, addition in additions.items():

                if isinstance(addition, dict):
                    addition = [addition,]

                with Tree(self.tree_type) as tree:
                    node_info = NodeInfo(tree.btree, tree.create_node(node_name))
                    implementation = self.implementation(node_info)

                    for spec in addition:
                        node_call = NodeCall(**{'rules': ['Additional implementation'], **spec})

                        # --------------------------------------------------
                        # class name is LOOP param_name
                        # --------------------------------------------------

                        tag = "LOOP "
                        class_name = node_call.class_name
                        if class_name is not None and class_name.startswith(tag):
                            driving_param = class_name[len(tag):]
                            node_params = node_info.snapshot_params()
                            if driving_param not in node_params or not node_params[driving_param].get('enums'):
                                raise AttributeError(
                                    f"Additional '{node_name}': impossible to loop on parameter "
                                    f"'{driving_param}' with class_name '{class_name}'.")

                            calls = NodeCalls.overrides(node_call, [
                                dict(class_name=get_class_name(value),
                                     parameters={**node_call.parameters, driving_param: value},
                                     self_socket=(node_info.data_type_input(value)
                                                  if node_call.has_self and node_call.self_socket is None
                                                  else node_call.self_socket))
                                for value in node_params[driving_param]['enums']
                            ])
                        else:
                            # --------------------------------------------------
                            # Single implementation
                            # --------------------------------------------------
                            calls = NodeCalls(node_call)

                        for call in calls:
                            if not call.implement:
                                continue
                            source = implementation.gen_node_call(call)
                            self.register_source(node_info, call, source)
