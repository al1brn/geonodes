"""Python implementations of an introspected node."""

import ast
import keyword
import inspect
import textwrap
from pathlib import Path
from typing import get_args
from dataclasses import replace

import bpy

from .. import core_module
from . import gen_config
from . import config, utils
from .node_call import NodeCall, NodeCalls
from .sourcewriter import SourceWriter, FUNC_TYPE
from .typealiases import TypeAliases
from .tree import Tree
from .output import ENVIRONMENTS, render_modules
from .argument import Argument
from .node_info import NodeInfo
from .node_param import NodeParam

SocketType = core_module.common.sockettype.SocketType

TAB = "    "

# ====================================================================================================
# Node Implementation
# ====================================================================================================

class NodeImplementation:
    """Describe a node implementation and generate its Python source code."""

    files = {}
    cross_refs = {}
    tree_type = 'GeometryNodeTree'
    type_aliases = None

    # ====================================================================================================
    # Node Implementation instance wraps a node_info 
    # ====================================================================================================

    def __init__(self, node):
        self.node = node
        self.type_aliases = type(self).type_aliases
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
        result = type(self)(self.node)
        result.parameters = self.parameters.copy()
        result.type_aliases = self.type_aliases
        return result

    def set_parameters(self, **parameters):
        for name, value in parameters.items():
            self[name] = value

    def clear_parameters(self):
        for name in self.parameters:
            self.parameters[name] = None


    @property
    def fixed_enums(self):
        return {name: value for name, value in self.parameters.items() if (name in self.node.config) and (value is not None)}


    # ====================================================================================================
    # Write Files
    # ====================================================================================================

    @classmethod
    def write_files(cls, use_core_new=True):
        """Write directly to each environment's generated folder in core_new."""
        if not use_core_new:
            raise ValueError('Environment generation targets core_new only; core is unchanged.')
        core_path = Path(__file__).resolve().parent.parent / 'core_new'
        modules = {}
        for tree_type, sources in cls.files.items():
            modules.update(render_modules(core_path, tree_type, sources, cls.cross_refs.get(tree_type, {})))
        # render_modules validates every selected module before any write.
        for path, source in modules.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(source, encoding='utf-8')
            print(f'Generated: {path}')

    # ====================================================================================================
    # Register source
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Register source code dynamically generated
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def register_source(cls, node, node_call: NodeCall, source, *, tree_type=None, write_source=True):
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
            prefix = 'dom_' if destination in core_module.constants.DOMAIN_CLASSES else ''
            filename = prefix + destination.lower() + '.py'
        returns = (None if node_call.method_type == 'SETTER' else
                   node_call.return_socket if node_call.return_socket is not None else
                   node_call.return_kind)
        cls._register_source(node, filename, destination, source, returns=returns,
                             tree_type=tree_type, write_source=write_source, rules=node_call.rules)

    @classmethod
    def _register_source(cls, node, filename, destination, source, returns='OUT', *, tree_type=None, write_source=True, rules=[]):
        """Register source and its cross reference, rejecting duplicate names."""

        if tree_type is None:
            tree_type = node.btree.bl_idname

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


            print(f"Compilation error in '{node.name}'")
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
        files = cls.files.setdefault(tree_type, {})
        cross_refs = cls.cross_refs.setdefault(tree_type, {})

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

    # ----------------------------------------------------------------------------------------------------
    # Takes hand written source code references
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def gen_handwritten_references(cls):
        """Register actual handwritten signatures without copying their code."""
        tree = bpy.data.node_groups.new('Handwritten references', cls.tree_type)
        available = utils.get_node_names(cls.tree_type)
        try:
            for identifier, destinations in config.HANDWRITTEN_IMPLEMENTATIONS.items():
                if identifier not in available:
                    continue
                node = NodeInfo(tree, tree.nodes.new(identifier))
                for destination, names in destinations.items():
                    owner = getattr(core_module, destination)
                    for name in names:
                        function = inspect.getattr_static(owner, name)
                        if isinstance(function, (classmethod, staticmethod)):
                            function = function.__func__
                        cls._register_source(node, None, destination, inspect.getsource(function),
                                            write_source=False)
        finally:
            bpy.data.node_groups.remove(tree)    

    # ====================================================================================================
    # Main method : generate full API
    # ====================================================================================================

    @classmethod
    def generate(cls, *, tree_type=None, use_core_new=True, write=True):
        """Generate both environments, or just the supplied Blender tree type.

        Collections and naming collisions are scoped by tree_type. No files
        are written until all selected generation steps succeed.
        """
        selected = tuple(ENVIRONMENTS) if tree_type is None else (tree_type,)
        for selected_type in selected:
            if selected_type not in ENVIRONMENTS:
                raise ValueError(f'Unsupported tree type: {selected_type!r}')
        cls.files.clear()
        cls.cross_refs.clear()
        previous_type = cls.tree_type
        previous_aliases = cls.type_aliases
        try:
            for selected_type in selected:
                cls.tree_type = selected_type
                cls.files[selected_type] = {}
                cls.cross_refs[selected_type] = {}
                cls.type_aliases = TypeAliases()

                cls.gen_static_code()
                cls.gen_math()
                cls.gen_compare()
                cls.gen_mix()
                cls.gen_nodes()
                #cls.gen_properties()
                #cls.gen_typed_constructors()
                #cls.gen_additional()
                cls.files[selected_type]['type_aliases.py'] = [cls.type_aliases.source]

        finally:
            cls.tree_type = previous_type
            cls.type_aliases = previous_aliases
        if write:
            cls.write_files(use_core_new=use_core_new)
        environments = ', '.join(ENVIRONMENTS[selected_type] for selected_type in selected)
        action = 'Generation completed' if write else 'Source collection completed (no files written)'
        print(f'\n{action}: {environments}.')

    # ====================================================================================================
    # Generate nd module
    # ====================================================================================================

    @classmethod
    def gen_static_code(cls):
        """Collect nd accessors and cross references for the current environment."""
        def generate(node):
            name = core_module.utils.snake_case(node.bnode.name)
            constructor = NodeCall.class_property if node.is_class_property else NodeCall.class_method
            node_call = constructor(name, class_name='nd', return_kind='OUT')
            source = cls(node).gen_node_call(node_call)
            cls.register_source(node, node_call, source)

        NodeInfo.loop_on_nodes(generate, tree_type=cls.tree_type)

    # ====================================================================================================
    # Operations
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Math
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def gen_math(cls):

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
        for name, specs in MATH[cls.tree_type].items():
            node_specs.setdefault(name, []).extend(specs)

        with Tree(cls.tree_type) as tree:
            for node_name, specs in node_specs.items():
                if node_name not in tree.nodes:
                    continue

                node = tree.create_node(node_name)
                class_name = CLASS_NAMES[node_name]

                node_info = NodeInfo(tree.btree, node)
                impl_base = cls(node_info)

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
                    cls.register_source(node_info, function_spec,
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
                    cls.register_source(node_info, method_spec,
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

                            cls.register_source(node_info,
                                                method_spec.replace(method_name=f'__{op_name}__'), source)

                        elif op_code is not None:
                            source = f"{TAB}def __{op_name}__(self, other):\n"
                            source += f"{TAB*2}return {op_code}\n"

                            cls.register_source(node_info,
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

                                cls.register_source(node_info,
                                                    method_spec.replace(method_name=f'__{prefix}{op_name}__'), source)

    # ----------------------------------------------------------------------------------------------------
    # Compare
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def gen_compare(cls):

        operators = {'LESS_THAN': 'lt', 'GREATER_THAN': 'gt', 'LESS_EQUAL': 'le', 'GREATER_EQUAL': 'ge',
                     'EQUAL': 'eq', 'NOT_EQUAL': 'ne', 'BRIGHTER': 'gt', 'DARKER': 'lt'}

        if cls.tree_type != 'GeometryNodeTree':
            return

        with Tree(cls.tree_type) as tree:

            node_info = NodeInfo(tree.btree, tree.create_node('Compare'))

            for data_type in node_info.config['data_type']['enums']:

                class_name = core_module.utils.SocketType.from_type(data_type).class_name

                node_info.set_params(data_type=data_type)
                params = node_info.snapshot_params()

                operations = params['operation']['enums']
                for operation in operations:
                    method_name = core_module.utils.snake_case(operation)
                    implementation = NodeImplementation(node_info)
                    implementation["data_type"] = data_type
                    implementation["operation"] = operation

                    ispec = NodeCall.method(
                        class_name = class_name,
                        method_name = method_name,
                        self_socket = "A",
                    )

                    cls.register_source(node_info, ispec, implementation.gen_node_call(ispec))

                    op_name = operators[operation]
                    source = f"{TAB}def __{op_name}__(self, other):\n"
                    source += f"{TAB*2}return self.{method_name}(other)\n"

                    cls.register_source(node_info, ispec.replace(method_name=f'__{op_name}__'), source)

    # ----------------------------------------------------------------------------------------------------
    # Compare
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def gen_mix(cls):

        with Tree(cls.tree_type) as tree:

            node_info = NodeInfo(tree.btree, tree.create_node('Mix'))

            for data_type in node_info.config['data_type']['enums']:
                class_name = core_module.utils.SocketType.from_type(data_type).class_name

                implementation = NodeImplementation(node_info)
                implementation["data_type"] = data_type

                ispec = NodeCall.class_method(
                    class_name = class_name,
                    method_name = "Mix",
                    last_sockets=('Factor',),
                )
                cls.register_source(node_info, ispec, implementation.gen_node_call(ispec))


                ispec = NodeCall.method(
                    class_name = class_name,
                    method_name = "mix",
                    self_socket="A",
                    last_sockets=('Factor',),
                )
                cls.register_source(node_info, ispec, implementation.gen_node_call(ispec))

    # ====================================================================================================
    # Properties
    # ====================================================================================================

    @classmethod
    def gen_properties(cls):
        """Assemble declared instance getters and setters, retaining both references."""
        tree = bpy.data.node_groups.new('Property generation', cls.tree_type)
        nodes = {}

        def get_node(name):
            if name not in nodes:
                identifiers = utils.get_node_names(cls.tree_type)
                identifier = next((key for key, value in identifiers.items() if value == name), name)
                nodes[name] = NodeInfo(tree, tree.nodes.new(type=identifier))
            return nodes[name]

        def generate_part(spec, kind, name):
            node = get_node(spec['node'])
            implementation = cls(node)
            value = None
            if kind == 'SETTER':
                value = ('parameter', spec['parameter']) if 'parameter' in spec else ('socket', spec['socket'])
            for parameter, snapshot in node.snapshot_params().items():
                if value != ('parameter', parameter):
                    implementation[parameter] = spec.get('parameters', {}).get(parameter, snapshot['value'])
            receiver = next((socket.name for socket in node.bnode.inputs
                             if socket.enabled and socket.type == 'GEOMETRY'), None)
            source = implementation.gen_source(
                kind=kind, name=name, self_socket=receiver,
                return_socket=spec.get('output', 'OUT'), is_jump=kind == 'SETTER',
                property_value=value, fixed_sockets=spec.get('sockets', {}))
            return node, source

        try:
            for destination, properties in config.PROPERTIES[cls.tree_type].items():
                filename = ('dom_' if destination in core_module.constants.DOMAIN_CLASSES else '') + destination.lower() + '.py'
                for name, specification in properties.items():
                    getter = specification.get('getter')
                    setter_node, setter = generate_part(specification['setter'], 'SETTER', name)
                    if getter is None:
                        getter_node = setter_node
                        source = (f'    @property\n    def {name}(self):\n'
                                  f'        """Write-only property; setter node: {setter_node.bnode.name}."""\n'
                                  f'        raise NodeError({f"Property {destination}.{name} is write only."!r})\n')
                    else:
                        getter_node, source = generate_part(getter, 'GETTER', name)
                        # Promote the same node's automatically generated getter
                        # to the explicitly configured read/write property.
                        references = cls.cross_refs.get(cls.tree_type, {}).get(getter_node.bnode.bl_idname, {}).get(destination, [])
                        previous = next((ref for ref in references if ref['func_name'] == name and
                                         (ref['is_get'] or ref['is_classmethod'])), None)
                        if previous is not None:
                            references.remove(previous)
                            sources = cls.files[cls.tree_type][filename]
                            sources[:] = [code for code in sources if ast.parse(textwrap.dedent(code)).body[0].name != name]
                    cls._register_source(getter_node, filename, destination, source, returns=getter.get('output', 'OUT') if getter else None)
                    cls._register_source(setter_node, filename, destination, setter, returns=None)
        finally:
            bpy.data.node_groups.remove(tree)

    # ====================================================================================================
    # All nodes
    # ====================================================================================================

    @classmethod
    def gen_nodes(cls):
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

            #print("DEBUG", type(node_call), repr(node_call))

            if not node_call.implement or node_call.class_name is None:
                return

            node_impl = cls(node)
            node_impl.parameters.update(node_call.parameters)

            source = node_impl.gen_node_call(node_call)

            cls.register_source(node, node_call, source)

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

                cls.register_source(node, ispec, source)

        # ---------------------------------------------------------------------------
        # Spec coming from get_node_implementation can be multiple
        # ---------------------------------------------------------------------------

        def generate(node):
            implementation = cls(node)
            node_calls = implementation.get_node_implementation()

            print(f"DEBUG {node.name}: {type(node_calls)}")

            generate_from_spec(node, node_calls)

        # ---------------------------------------------------------------------------
        # Main is a loop on nodes
        # ---------------------------------------------------------------------------

        NodeInfo.loop_on_nodes(generate, tree_type=cls.tree_type)

    # ====================================================================================================
    # Add constructors with subtypes : Float.Angle, Vector.Velocity,...
    # ====================================================================================================

    @classmethod
    def gen_typed_constructors(cls):

        for tree_type in ('GeometryNodeTree', 'ShaderNodeTree'):

            with Tree(tree_type) as tree:
                valids = []
                for socket_name in tree.valid_input_sockets:
                    if socket_name == 'NodeSocketSound':
                        continue
                    sock = tree.btree.interface.new_socket(socket_type=socket_name, name=socket_name)
                    stype = SocketType(sock)
                    valids.append(stype.type)

            for socket_type in valids:

                if socket_type == 'NodeSocketSound':
                    continue

                d = gen_config.SOCKETS[socket_type]

                if d[tree_type] is None:
                    continue

                if tree_type == 'ShaderNodeTree':
                    print("GENERATING Constructor for", socket_type, d[tree_type])

                # Class subtypes
                subtypes = d.get('subtypes', ['NONE'])
                if not len(subtypes):
                    subtypes = ['NONE']

                for subtype in subtypes:

                    create_socket = subtype == 'NONE'
                    if create_socket:
                        name  = d['class_name']
                        fname = "_create_input_socket"
                    else:
                        name  = "".join([s.title() for s in subtype.split('_')])
                        fname = name

                    props = d['props']
                    class_name = d['class_name']
                    ptype, def_val = gen_config.PYTHON_TYPES.get(class_name, (object, None))
                    if ptype is object:
                        ptype = 'object'

                    # ---------------------------------------------------------------------------
                    # Arguments
                    # ---------------------------------------------------------------------------

                    has_default = 'default' in props

                    args = {}

                    # ----- Value, Name

                    if has_default:
                        if create_socket:
                            args['value'] = (
                                f": {ptype} = {def_val}",
                                (ptype, def_val, "Default value"),
                                'default_value = defval')
                        else:
                            args['value'] = (
                                f": {ptype} = {def_val}",
                                (ptype, def_val, "Default value"),
                                'value')

                    args['name']  = (
                        f": str = '{name}'", 
                        ("str", name, "Input socket name"), 
                        'name')
                    
                    # ----- sort properties
                    
                    sorted_props = []
                    if 'min' in props:
                        sorted_props.extend(['min', 'max'])
                    sorted_props.append('tip')

                    for prop in props:
                        if prop in sorted_props or prop in ['subtype', 'default']:
                            continue
                        sorted_props.append(prop)

                    for prop in sorted_props:
                        prop_val = props[prop]

                        stype = prop_val[1]
                        doctype = stype
                        sdef = f"'{prop_val[2]}'" if stype == 'str' else prop_val[2]
                        scomm = f"Property {prop_val[0]}"
                        if isinstance(stype, tuple):
                            stype = f"Literal{list(stype)}"
                            doctype = 'str'
                            sdef = f"'{prop_val[2]}'"
                            scomm += f" in {prop_val[1]}"

                        if stype == 'Literal[]':
                            stype = 'str'

                        args[prop] = (
                            f": {stype} = {sdef}",
                            (doctype, sdef, scomm),
                            prop,
                        )

                        if prop == "tip":
                            args["panel"] = (': str = ""', ("str", "", "Panel name"), "panel")

                    if len(d['subtypes']):
                        if create_socket:
                            args["subtype"] = (
                                f": str = 'NONE'",
                                ("str", 'NONE', f"Socket sub type in {d['subtypes']}"),
                                "subtype",
                            )
                        else:
                            args["subtype"] = (None, None, f"'{subtype}'")

                    # ---------------------------------------------------------------------------
                    # Header
                    # ---------------------------------------------------------------------------

                    margin = TAB

                    code = f"{margin}@classmethod\n"
                    arguments = ['cls']
                    for arg_name, arg_val in args.items():
                        if arg_val[0] is not None:
                            arguments.append(f"{arg_name}{arg_val[0]}")

                    code += format_header(fname, *arguments, margin=margin) + "\n"
                    margin += TAB

                    # ---------------------------------------------------------------------------
                    # Doc
                    # ---------------------------------------------------------------------------

                    code += f'{margin}""" > {name} Input\n\n'
                    code += f"{margin}New <#{class_name}> input with subtype '{subtype}'.\n\n"

                    code += f"{margin}Parameters\n"
                    code += f"{margin}----------\n"
                    for arg_name, arg_val in args.items():
                        if arg_val[0] is not None:
                            code += f"{margin}{arg_name} : {arg_val[1][0]}, default=`{arg_val[1][1]}`\n{margin}    {arg_val[1][2]}\n\n"
                    code += "\n"

                    code += f"{margin}Returns\n"
                    code += f"{margin}-------\n"
                    code += f"{margin}{class_name}\n"
                    code += f'{margin}"""\n'

                    # ---------------------------------------------------------------------------
                    # Code
                    # ---------------------------------------------------------------------------

                    if create_socket:

                        code += f"{margin}from ..treeclass import Tree\n\n"

                        if has_default:
                            code += f"{margin}defval = utils.python_value_for_socket(value, cls.SOCKET_TYPE)\n\n"

                        bl_idname = d['ShaderNodeTree'] if d['GeometryNodeTree'] is None else d['GeometryNodeTree'] 

                        scall = f"return Tree.current_tree().create_input_socket('{bl_idname}', "

                    else:
                        scall = "return cls("


                    sep = ""
                    for arg_name, arg_val in args.items():
                        if arg_val[2] is None:
                            continue
                        elif '=' in arg_val[2]:
                            scall += f"{sep}{arg_val[2]}"
                        else:
                            scall += f"{sep}{arg_name}={arg_val[2]}"
                        sep = ", "

                    scall += ")"
                    tab =""
                    for line in textwrap.wrap(scall, width=100):
                        code += margin + tab + line + "\n"
                        tab = TAB

                    cls._register_source(
                        None, 
                        d['class_name'].lower() + '.py', 
                        d['class_name'], 
                        code,
                        tree_type = tree_type,
                        rules=[])

                    """
                    if class_name in gen['source'] and name in gen['source'][class_name]:
                        print(gen['source'][class_name][name])
                        raise RuntimeError(f"The subtype constructor {name} already exists in class {class_name}.")
                    
                    if class_name != 'Input':
                        if class_name in gen['source']:
                            gen['source'][class_name][name] = code
                        else:
                            print(f"CAUTION (generate): class name '{class_name}' not in gen['source']. Impossible to create source code for '{name}'")
                    """

    # ====================================================================================================
    # Get the standard node implementation
    # ====================================================================================================

    def get_domain_calls(self, node_call: NodeCall) -> NodeCalls:
        """Construire les variantes d'un appel pour les domaines du nœud.

        Parameters
        ----------
        node_call : NodeCall
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

        overrides = []
        if node_call.class_name is not None:
            overrides.append({})

        for domain in parameter.enums:
            overrides.append({
                'class_name': domains[domain],
                'parameters': {**node_call.parameters, 'domain': domain},
            })
        return NodeCalls.overrides(node_call, overrides)

    def get_data_type_calls(self, node_call: NodeCall) -> NodeCalls:

        parameter = self.node.data_type_parameter
        if parameter is None:
            raise ValueError(f"{self.node.name}: no data_type parameter")

        overrides = []
        for data_type in parameter.enums:
            overrides.append({
                'class_name': SocketType.from_type(data_type).class_name,
                'auto_data_type': None,
                'parameters': {**node_call.parameters, parameter.name: data_type},
            })
            if self.node.data_type_drives_inputs and node_call.has_self:
                overrides[-1]['self_socket'] = self.node.data_type_input(data_type)

        return NodeCalls.overrides(node_call, overrides)

    # ====================================================================================================
    # Build default node implementation
    # ====================================================================================================

    def get_node_implementation(self):
        """Describe the node implementation, including requested parameter loops."""

        node = self.node
        inputs = [socket for socket in node.inputs.values() if socket.enabled and socket.socket_type != 'CUSTOM']
        outputs = [socket for socket in node.outputs.values() if socket.enabled and socket.socket_type != 'CUSTOM']
        first_input = inputs[0] if inputs else None
        first_output = outputs[0] if outputs else None

        name_tokens = [token.strip() for token in node.name.split(" ")]
        method_name = core_module.utils.snake_case(' '.join(name_tokens))        
        MethodName = core_module.utils.CamelCase(' '.join(name_tokens))        

        # ---------------------------------------------------------------------------
        # Hacks
        # ---------------------------------------------------------------------------

        # Node: Value to String
        # Hacks because despite its name, Value is driven by data_type parameter
        # Auto algo implements only on Float with a data_type loop which is bad

        if node.name == 'Value to String':
            category = "Hack"
            rules = ["'Value to String' hack"]

            return NodeCalls(
                NodeCalls.attributes(NodeCall.method(
                    category = category,
                    method_name = "to_string",
                    self_socket = "Value",
                    parameters = {'data_type': "FLOAT"},
                    rules = rules
                ), class_name="Float"),
                NodeCalls.attributes(NodeCall.method(
                    category = category,
                    method_name = "to_string",
                    self_socket = "Value",
                    parameters = {'data_type': "INT"},
                    rules = rules
                ), class_name="Integer"),
                NodeCalls.attributes(NodeCall.class_method(
                    category = category,
                    method_name = "FromValue",
                    auto_data_type = "Value",
                    rules = rules
                ), class_name="String"),
            )

        # ---------------------------------------------------------------------------
        # Static only : no implementation
        # ---------------------------------------------------------------------------

        if node.bl_idname in config.STATIC_IMPLEMENTATION_ONLY:
            return NodeCall(
                method_type = 'FUNCTION',
                category = "Static Only",
                method_name = "no_name",
                implement = False,
                rules = ["Static only node"],
            )
        
        rules = [f"{node.has_domain_parameter=}",
                 f"{node.has_data_type_parameter=}",
                 f"{node.data_type_drives_inputs=}",
                 f"{node.data_type_drives_outputs=}",
                 f"{node.data_type_drives_first_input=}",
                 f"{node.has_items=}",
                 ]
        over_spec = config.SPECIAL_NODES.get(node.name, {})

        # ---------------------------------------------------------------------------
        # Texture nodes
        # ---------------------------------------------------------------------------

        if node.color_tag == 'TEXTURE':

            tokens = [token for token in node.name.split() if token != 'Texture']
            method_name = core_module.utils.CamelCase(' '.join(tokens))
            rules += ["Texture Node"]

            return NodeCalls.attributes(NodeCall.class_method(
                category = "Texture",
                method_name = method_name,
                rules = rules,
            ), class_name="Texture").replace(**over_spec)


        rules += ["Not a texture node"]

        # ---------------------------------------------------------------------------
        # Shader BSDF
        # ---------------------------------------------------------------------------

        if node.is_shader:
            if name_tokens[-1] == 'BSDF':
                method_name = core_module.utils.CamelCase(' '.join(name_tokens[:-1]))

                return NodeCalls.attributes(NodeCall.class_method(
                    category = "Shader",
                    method_name = method_name,
                    rules = rules + [f"Ends with BSDF -> Shader constructor"],
                ), class_name="Shader").replace(**over_spec)

        # ---------------------------------------------------------------------------
        # data_type drives both input and output sockets
        # ---------------------------------------------------------------------------

        if node.has_data_type_parameter:
            in_count = len(node.data_type_socket_changes['inputs'])
            out_count = len(node.data_type_socket_changes['outputs'])
            if in_count > 0 and out_count > 0:
                rules += ["Data type drives input and output sockets"]

                node_call = NodeCall.method(
                    category = 'Method',
                    method_name = method_name,
                    rules = rules,
                ).replace(**over_spec)
                return self.get_data_type_calls(node_call)

        # ---------------------------------------------------------------------------
        # data_type input
        # used for data_type_loop
        # ---------------------------------------------------------------------------

        data_type_input = node.data_type_input()

        # ---------------------------------------------------------------------------
        # Input nodes
        # ---------------------------------------------------------------------------
        
        if node.color_tag == 'INPUT':
        
            class_name = None
        
            method_name = core_module.utils.snake_case(node.name)
            is_class_method = False

            category = "Input Node"
            rules += ["Input Node"]

            # Info node
            if (len(name_tokens) > 1) and (name_tokens[-1] == 'Info') and first_input is not None:
                rules += ["Info node"]
                class_name = first_input.class_name
                if class_name == name_tokens[0] and len(name_tokens) == 2:
                    method_name = 'info'
                else:
                    method_name = core_module.utils.snake_case(node.name)


            else:
                rules += ["Not Info node"]

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
                
                # if first input is not an attr, this is instance method
                if not in_is_attr:
                    class_name = in_class_name
                    rules += ["Non attribute input"]
                
                # if first output is not an attr, this is class constructor
                elif not out_is_attr:
                    class_name = out_class_name
                    is_class_method = True
                    rules += ["Non Attribute output"]
                
                else:
                    rules += ["Attribute Output"]
                    is_class_method = True
                
                    tokens = [token.strip() for token in node.name.split(" ")]
                
                    if len(tokens) > 2 and tokens[-2] == "of":
                        target = tokens[-1]
                        for dom in config.DOMAINS:
                            if target in [dom, dom + 's']:
                                class_name = config.DOMAIN_NAME.get(dom, dom)
                                method_name = core_module.utils.snake_case(' '.join(tokens[:-2])) 
                                rules += [f"'Domain 1 of Domain 0' name -> {class_name=}, {method_name=}"]
                                break
                        
                    elif len(tokens) > 2 and tokens[0] == "Is":
                        target = tokens[1]
                        for dom in config.DOMAINS:
                            if target in [dom, dom + 's']:
                                class_name = config.DOMAIN_NAME.get(dom, dom)
                                method_name = core_module.utils.snake_case(' '.join(tokens[2:]))
                                rules += [f"'Domain is xxx' name -> {class_name=}, {method_name=}"]
                                break
                            
                    else:
                        target = tokens[0]
                        for dom in ["Grease"] + config.DOMAINS:
                            if target in [dom, dom + 's']:
                                if dom == 'Grease':
                                    class_name = "GreasePencil"
                                    method_name = core_module.utils.snake_case(' '.join(tokens[2:]))
                                else:
                                    class_name = config.DOMAIN_NAME.get(dom, dom)
                                    method_name = core_module.utils.snake_case(' '.join(tokens[1:]))
                                break

            if is_class_method:
                return NodeCalls.attributes(NodeCall.class_method(
                    category = category,
                    method_name = method_name,
                    rules = rules,
                ), class_name=class_name).replace(**over_spec)
            else:
                return NodeCalls.attributes(NodeCall.method(
                    category = category,
                    method_name = method_name,
                    self_socket = first_input.socket_name,
                    rules = rules,
                ), class_name=class_name).replace(**over_spec)
                    
        rules += ["Not an input node"]
                
        # ---------------------------------------------------------------------------
        # Nodes with input geometry
        # ---------------------------------------------------------------------------
    
        if bool(inputs) and first_input.socket_type == 'GEOMETRY':
        
            category = 'Input Geometry'
            rules += ["First input socket is Geometry"]

            geo_socket = first_input
            in_class = geo_socket.class_name
        
            jump = False
            method_name = None

            auto_data_type = data_type_input is not None
            if auto_data_type:
                rules += [f"Data type inferred from input '{data_type_input}'"]
            data_type_loop = False
            domain_loop = False
            jump = False
        
            # ----- Class name / domain
        
            class_name = geo_socket.class_name
            if node.has_domain_parameter:
                domain_loop = True
                rules += [f"Has 'domain' parameter, {domain_loop=}"]
        
            # ----- Output geometry
            
            has_geo_out = bool(outputs)
            if has_geo_out:
                out_socket = first_output
                has_geo_out = out_socket.socket_type == 'GEOMETRY'
                out_class = out_socket.class_name
            
                same_class = out_class == in_class
            else:
                same_class = False

            if has_geo_out:
                jump = same_class
                rules += [f"Out class {'==' if jump else '!='} in class -> jump = {jump}"]
            
            # ----- Conversion "xxx to yyy"
            
            tokens = [token.strip() for token in node.name.split(" ")]
            if "to" in tokens:
            
                is_convert = True
            
                ito = tokens.index("to")
                aft = tokens[ito:]
            
                in_class = 'Domain' if node.has_domain_parameter else geo_socket.class_name 
            
                method_name = core_module.utils.snake_case(' '.join(aft))
                jump = False
            
                rules += [f"Conversion 'class to class', {method_name=}, {jump=}"] 
            
            # ----- Method name
        
            if method_name is None:
                tokens = [token.strip() for token in node.name.split(" ")]
                if geo_socket.class_name in tokens:
                    tokens.remove(geo_socket.class_name)
                    method_name = core_module.utils.snake_case(' '.join(tokens))
                    rules += [f"Remove '{geo_socket.class_name}' from node name -> {method_name=}"]
                elif geo_socket.class_name + 's' in tokens:
                    tokens.remove(geo_socket.class_name + 's')
                    method_name = core_module.utils.snake_case(' '.join(tokens))
                    rules += [f"Remove '{geo_socket.class_name}s' from node name -> {method_name=}"]
                
                else:
                    method_name = core_module.utils.snake_case(node.name)

            if True:
                node_calls = NodeCall.method(
                    category = category,
                    method_name = method_name,
                    class_name = class_name,
                    self_socket = geo_socket.socket_name,
                    is_jump = jump,
                    auto_data_type = data_type_input,
                    rules = rules,
                ).replace(**over_spec)

                if data_type_loop:
                    node_calls = self.get_data_type_calls(node_calls)
                if domain_loop:
                    node_calls = self.get_domain_calls(node_calls)

                return node_calls

            else:

                return NodeCalls.attributes(NodeCall.method(
                    category = category,
                    method_name = method_name,
                    self_socket=geo_socket.socket_name,
                    is_jump = jump,
                    auto_data_type = data_type_input,
                    data_type_loop = data_type_loop,
                    domain_loop = domain_loop,
                    rules = rules,
                ), class_name=class_name).replace(**over_spec)
        
        rules += ["First input socket is not geometry"]
    
        # ---------------------------------------------------------------------------
        # Nodes with output geometry
        # ---------------------------------------------------------------------------
    
        if bool(outputs) and first_output.socket_type == 'GEOMETRY':
        
            category = 'Output Geometry'
            rules += ["First output socket is Geometry"]
        
            out_socket = first_output

            class_name = out_socket.class_name
        
            tokens = [token.strip() for token in node.name.split(" ")]
            if class_name in tokens:
                tokens.remove(class_name)
            method_name = core_module.utils.CamelCase(' '.join(tokens))

            return NodeCalls.attributes(NodeCall.class_method(
                category = category,
                method_name = method_name,
                rules = rules,
            ), class_name=class_name).replace(**over_spec)

        rules += ["First output socket is not Geometry"]

        # ---------------------------------------------------------------------------
        # Grid node
        # ---------------------------------------------------------------------------

        if node.color_tag == 'GEOMETRY' and (node.is_grid_input or node.is_grid_output):

            category = 'Grid'
            rules += [f"Grid node {node.is_grid_input=}, {node.is_grid_output=}"]

            data_type_loop = False
            jump = False

            if node.is_grid_input:
                class_name = first_input.class_name
                is_class_method = False
                method_name = core_module.utils.snake_case(node.name)
            else:
                class_name = first_output.class_name
                is_class_method = True

                tokens = [token.strip() for token in node.name.split(" ")]
                if class_name in tokens:
                    tokens.remove(class_name)
                method_name = core_module.utils.CamelCase(' '.join(tokens))

            if node.has_data_type_parameter:
                data_type_loop = True
                class_name = None
                jump = node.is_grid_input and node.is_grid_output
                rules += [f"Node has data_type parameter"]

            if True:
                if is_class_method:
                    node_calls = NodeCall.class_method(
                        category = category,
                        method_name = method_name,
                        rules = rules,
                    ).replace(**over_spec)
                else:
                    node_calls = NodeCall.method(
                        category = category,
                        method_name = method_name,
                        self_socket = first_input.socket_name,
                        is_jump = jump,
                        rules = rules,
                    ).replace(**over_spec)
                if data_type_loop:
                    node_calls = self.get_data_type_calls(node_calls)

                return node_calls
                
            else:
                if is_class_method:
                    return NodeCalls.attributes(NodeCall.class_method(
                        category = category,
                        method_name = method_name,
                        data_type_loop = data_type_loop,
                        rules = rules,
                    ), class_name=class_name).replace(**over_spec)
                else:
                    return NodeCalls.attributes(NodeCall.method(
                        category = category,
                        method_name = method_name,
                        self_socket = first_input.socket_name,
                        data_type_loop = data_type_loop,
                        is_jump = jump,
                        rules = rules,
                    ), class_name=class_name).replace(**over_spec)

        rules += ["Node is not grid"]

        # ---------------------------------------------------------------------------
        # First socket is driven by data_type
        # ---------------------------------------------------------------------------

        if node.data_type_drives_first_input:
            method_name = core_module.utils.CamelCase(node.name)
            if True:
                node_call = NodeCall.class_method(
                    category = 'Data type driven',
                    method_name = method_name,
                    rules = rules + ["'data_type' parameter drives first input"],
                ).replace(**over_spec)
                return self.get_data_type_calls(node_call)
            else:
                return NodeCalls.attributes(NodeCall.class_method(
                    category = 'Data type driven',
                    method_name = method_name,
                    data_type_loop = True,
                    rules = rules + ["'data_type' parameter drives first input"],
                ), class_name=None).replace(**over_spec)

        rules += ["No 'data_type' driving first input"]
        tokens = [token.strip() for token in node.name.split(" ")]

        # ---------------------------------------------------------------------------
        # Combine / Separate / Conversions
        # ---------------------------------------------------------------------------

        category = "Other"
        class_name = None
        method_name = None

        is_class_method = False

        if tokens[0] == "Combine":
            rules += ["Starts with 'Combine'"]
            class_name = first_output.class_name

            if tokens[1] in core_module.constants.CLASS_NAMES.values():
                method_name = "Combine"
            else:
                method_name = core_module.utils.CamelCase(' '.join(tokens))
            is_class_method = True

            rules += ["Combine node"]

        elif tokens[0] == 'Separate':
            rules += ["Starts with 'Separate'"]

            class_name = first_input.class_name
            if class_name in tokens:
                tokens.remove(class_name)
            method_name = core_module.utils.snake_case(' '.join(tokens))

            rules += ["Separate node"]

        elif "to" in tokens:
            rules += ["'to' in node name"]
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
                method_name = core_module.utils.snake_case(f"to {saft}")

                rules += ["Class to something name"]

            if out_class is not None:
                m_name = core_module.utils.CamelCase("From " + ' '.join(tokens[:ito]))
                if class_name is None:
                    class_name = out_class
                    method_name = m_name
                    is_class_method = True

                    rules += [f"Something to Class -> {class_name}.{method_name} constructor"]

                else:
                    class_name = (class_name, out_class)
                    method_name = (method_name, m_name)
                    is_class_method = (False, True)

                    rules += [f"Class to Class -> two implementations : {class_name} {method_name}"]

        # ---------------------------------------------------------------------------
        # All the other nodes
        # ---------------------------------------------------------------------------

        if class_name is None:
            rules += ["No more rule..."]
            if first_input is None:
                if first_output is None:
                    return NodeCall(
                        method_type = 'FUNCTION',
                        category = 'Manual',
                        method_name = 'no_name',
                        implement = False,
                        rules = rules,
                    ).replace(**over_spec)
                class_name = first_output.class_name
                is_class_method = True
                method_name = core_module.utils.CamelCase(node.name)
            else:
                class_name = first_input.class_name
                method_name = core_module.utils.snake_case(node.name)

        # Conversion nodes can expose an instance method and a constructor.
        if isinstance(is_class_method, tuple):
            specs = []
            for target, name, class_method in zip(class_name, method_name, is_class_method, strict=True):
                if class_method:
                    spec = NodeCall.class_method(
                        category = category,
                        method_name = name,
                        class_name = target,
                        auto_data_type = data_type_input,
                        rules = rules,
                    )
                else:
                    spec = NodeCall.method(
                        category = category,
                        method_name = name,
                        class_name = target,
                        self_socket = first_input.socket_name,
                        auto_data_type = data_type_input,
                        rules = rules,
                    )
                specs.append(spec.replace(**over_spec))
            return NodeCalls(*specs)

        if is_class_method:
            return NodeCalls.attributes(NodeCall.class_method(
                category = category,
                method_name = method_name,
                auto_data_type = data_type_input,
                rules = rules,
            ), class_name=class_name).replace(**over_spec)

        return NodeCalls.attributes(NodeCall.method(
            category = category,
            method_name = method_name,
            self_socket = first_input.socket_name,
            auto_data_type = data_type_input,
            rules = rules,
        ), class_name=class_name).replace(**over_spec)

    # ====================================================================================================
    # Additional implementations
    # ====================================================================================================

    @classmethod
    def gen_from_spec(cls, node_name, spec):

        with Tree(cls.tree_type) as tree:

            node_info = NodeInfo(tree.btree, tree.create_node(node_name))
            implementation = cls(node_info)

            for name, value in spec.get('parameters', {}).items():
                implementation[name] = value

            source = implementation._gen_source(
                method_name = spec['method_name'],
                method_type = spec.get('kind', 'METHOD'),
                self_socket = spec.get('self_socket', None),
                is_jump = spec.get('is_jump', False),
                return_kind = spec.get('returns', 'OUT'),
                auto_data_type = spec.get('auto_data_type', None),
                fixed_sockets = spec.get('fixed_sockets', None),
            )

            class_name = spec['class_name']
            cls._register_source(
                node_info,
                class_name.lower() + '.py', 
                class_name,
                source,
                rules=["Additional implementation"],
            )

    @classmethod
    def gen_additional(cls):

        for additions in (config.ADDITIONAL_IMPLEMENTATIONS['common'], config.ADDITIONAL_IMPLEMENTATIONS[cls.tree_type]):
            for node_name, addition in additions.items():

                if isinstance(addition, dict):
                    addition = [addition,]

                for spec in addition:

                    # --------------------------------------------------
                    # class name is LOOP param_name
                    # --------------------------------------------------

                    tag = "LOOP "
                    class_name = spec['class_name']
                    if class_name.startswith(tag):
                        driving_param = class_name[len(tag):]

                        with Tree(cls.tree_type) as tree:
                            
                            node_info = NodeInfo(tree.btree, tree.create_node(node_name))
                            node_params = node_info.snapshot_params()

                            try:
                                values = node_params[driving_param]['enums']
                            except Exception as e:
                                from pprint import pprint
                                print(f"node '{node_name}' parameters")
                                pprint(node_params)
                                raise AttributeError(f"Addtional '{node_name}': impossible to loop on parameter '{driving_param}' with class_name '{class_name}'.\n{str(e)}")

                        for value in values:
                            stype = SocketType.from_type(value).type
                            class_name = gen_config.SOCKETS[stype]['class_name']

                            class_spec = spec.copy()
                            class_spec['class_name'] = class_name
                            params = class_spec.get('parameters', {})
                            params[driving_param] = value
                            class_spec['parameters'] = params

                            cls.gen_from_spec(node_name, class_spec)

                        continue

                    # --------------------------------------------------
                    # Single implementation
                    # --------------------------------------------------

                    cls.gen_from_spec(node_name, spec)


    # ====================================================================================================
    # Generate source code
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Doc string
    # ----------------------------------------------------------------------------------------------------

    def gen_docstring(self, arguments, *, is_jump=None, self_socket=None,
                      returns='Node', return_socket=None, derived_parameters=None,
                      indent=8):
        """Return the common docstring source for an implementation.

        arguments contains Argument descriptors. is_jump is None outside
        instance methods. Socket names and the return type are supplied by
        the generator; derived_parameters maps parameter names to descriptions
        of their deduction. indent is the indentation of the docstring.
        """
        doc_node = 'ShaderNode' if self.node.btree.bl_idname == 'ShaderNodeTree' else 'Node'
        lines = [f"> Node <&{doc_node} {self.node.bnode.name}>", '']
        if is_jump is not None:
            lines.extend([f"Jump method: {is_jump}.", ''])
        if self_socket is not None:
            lines.extend([f"self: socket '{self_socket}'.", ''])

        fixed = [(name, value) for name, value in self.parameters.items() if value is not None]
        if fixed:
            lines.extend(['**Fixed values**', '', '| Parameter | Value |', '| --- | --- |'])
            lines.extend(f"| `{name}` | `{value!r}` |" for name, value in fixed)
            lines.append('')
        if derived_parameters:
            lines.extend(['**Derived parameters**', ''])
            lines.extend(f"- `{name}`: {description}" for name, description in derived_parameters.items())
            lines.append('')

        exposed = [argument for argument in arguments if argument.is_argument and
                   (not argument.is_self or argument.multiple == 'ARGS')]
        if exposed:
            lines.extend(['Parameters', '----------'])
            for argument in exposed:
                lines.extend(argument.comment.splitlines())
                lines.append('')
        lines.extend(['Returns', '-------', 'None' if returns is None else returns])
        if return_socket is not None:
            lines.append(f"    socket '{return_socket}'")

        padding = ' ' * indent
        text = '\n'.join(lines).replace('\\', '\\\\').replace('"""', '\\"\\"\\"')
        return padding + '""" ' + ('\n' + padding).join(text.split('\n')) + '\n' + padding + '"""\n'

    # ----------------------------------------------------------------------------------------------------
    # Fixed parameters
    # ----------------------------------------------------------------------------------------------------

    def _fixed_parameters(self):
        """Resolve fixed enum identifiers and UI labels using RNA."""
        values = {}
        for name, value in self.parameters.items():
            if value is None:
                continue
            prop = self.node.bnode.bl_rna.properties[name]
            if prop.type == 'ENUM':
                names = {item.identifier.lower(): item.identifier for item in prop.enum_items}
                names.update({item.name.lower(): item.identifier for item in prop.enum_items})
                value = ({names[v.lower()] for v in value} if prop.is_enum_flag else
                         names[value.lower()])
            values[name] = value
        return values

    # ----------------------------------------------------------------------------------------------------
    # Source Code
    # ----------------------------------------------------------------------------------------------------

    def gen_source(self, kind='STATIC_METHOD', name=None, self_socket=None,
                   return_socket=None, is_jump=False, last_sockets=(), copy_code=None,
                   data_type_socket=None, property_value=None, fixed_sockets=None):
        """Return source for a static method, function, method, setter or getter.

        copy_code copies a supplied Python method verbatim, bypassing inference.
        data_type_socket infers an unfixed data_type/input_type from that input
        for METHOD only, removing the parameter from the public signature.
        Unfixed parameters remain free. Every possible enabled UI name becomes
        an argument. A local configuration table filters aliases when needed.
        return_socket=None returns the Node; 'OUT' selects its main output.
        'NODE' explicitly forces the Node, disabling the automatic class property
        for single-output static input nodes.
        GETTER without self_socket creates a class property. Property setters
        return None. Instance implementations can bind self
        to an input socket and jump to the selected output.
        last_sockets moves the specified sockets after other socket arguments,
        before node parameters, in the supplied order. Names can be canonical
        argument keys, physical identifiers or UI names.
        fixed_sockets selects property generation: unselected sockets retain
        node defaults. property_value is ('socket' | 'parameter', name) and
        selects the single assignment argument of a setter.
        """
        if copy_code is not None:
            source = textwrap.dedent(inspect.getsource(copy_code))
            return source if kind == 'FUNCTION' else textwrap.indent(source, '    ')

        if kind not in {'STATIC_METHOD', 'FUNCTION', 'METHOD', 'SETTER', 'GETTER'}:
            raise ValueError(f"Unknown implementation kind: {kind!r}")
        auto_property = kind == 'STATIC_METHOD' and self.node.is_class_property and return_socket != 'NODE'
        class_property = auto_property or (kind == 'GETTER' and self_socket is None and fixed_sockets is None)
        if auto_property:
            return_socket = 'OUT'
        elif return_socket == 'NODE':
            return_socket = None
        instance = kind in {'METHOD', 'SETTER', 'GETTER'} and not class_property
        if self_socket is not None and not instance:
            raise ValueError('self_socket requires an instance implementation')
        if is_jump and (not instance or return_socket is None):
            raise ValueError('A jump requires an instance implementation and an output socket')
        node_name = self.node.bnode.name
        name = core_module.utils.snake_case(node_name) if name is None else name
        if not name.isidentifier() or keyword.iskeyword(name):
            raise ValueError(f"Invalid Python method name: {name!r}")

        parameters = self.node.snapshot_params()
        fixed = self._fixed_parameters()
        items_name = core_module.constants.ONE_ITEMS_NODES.get(self.node.bnode.bl_idname)
        items = getattr(self.node.bnode, items_name) if items_name else None
        anonymous_items = items is not None and 'name' not in {
            param.identifier for param in items.bl_rna.functions['new'].parameters if not param.is_output}
        items_start = len(self.node.bnode.inputs) - len(items) - 1 if anonymous_items else None
        configurations = self.node.param_filter(**{
            name: value for name, value in fixed.items() if name in self.node.enum_parameters
        })
        # Collect all argument names seen in the reduced configurations.
        # Socket-name uniqueness follows Node.Sockets: parameters have priority.
        candidates = {}
        enabled_arguments = {}
        aliases = {}
        dynamic = False
        for config in configurations:
            used = {core_module.utils.snake_case(p) for p in parameters}
            enabled_arguments[config] = []
            for descriptor in self.node.max_inputs:
                if config in descriptor['enabled']:
                    continue
                exists = descriptor['exists']
                if not (exists[config] if isinstance(exists, dict) else exists):
                    continue
                socket_type = descriptor['socket_type']
                socket_type = socket_type[config] if isinstance(socket_type, dict) else socket_type
                if socket_type == 'CUSTOM':
                    dynamic = not anonymous_items
                    continue
                index = descriptor['index'][config] if isinstance(descriptor['index'], dict) else descriptor['index']
                if anonymous_items and index >= items_start:
                    continue
                ui_name = descriptor['name']
                ui_name = ui_name[config] if isinstance(ui_name, dict) else ui_name
                base = core_module.utils.snake_case(ui_name)
                socket_name = base
                index = 0
                while socket_name in used:
                    index += 1
                    socket_name = f'{base}_{index}'
                used.add(socket_name)

                identifiers = descriptor['identifier']
                identifier = identifiers[config] if isinstance(identifiers, dict) else identifiers
                enabled_arguments[config].append(socket_name)
                aliases.setdefault(identifier, set()).add(socket_name)
                reference = self.node.inputs[identifier]
                candidate = candidates.setdefault(socket_name, {
                    'ui_name': ui_name, 'reference': reference, 'types': [],
                    'index': descriptor['index'][config] if isinstance(descriptor['index'], dict) else descriptor['index'],
                })
                if candidate['reference'].is_multi_input != reference.is_multi_input:
                    raise ValueError(f"Inconsistent multi-input socket {socket_name!r} in {node_name!r}")
                if socket_type not in candidate['types']:
                    candidate['types'].append(socket_type)

        used = set(parameters) | {
            'cls', 'self', 'named_sockets', 'sockets', '_node', '_values', '_name', '_socket', '_value',
            '_named_sockets', '_configuration',
        }
        socket_args = []
        for socket_name, candidate in candidates.items():
            arg_name = socket_name
            index = 0
            while arg_name in used:
                index += 1
                arg_name = f'{socket_name}_{index}'
            used.add(arg_name)
            ui_name = candidate['ui_name']
            classes = tuple(dict.fromkeys(
                self.node.socket_class_name(t, ui_name)
                for t in candidate['types']
            ))
            argument = Argument.from_socket(candidate['reference'], arg_name=arg_name,
                                            class_name=' | '.join(classes))
            if candidate['types'] != ['MENU']:
                argument.typing = ' | '.join(classes)
                argument.comment = (f"{arg_name} : {argument.typing}, optional\n"
                                    f"    socket '{ui_name}'\n")
            socket_args.append((argument, socket_name))

        socket_args.sort(key=lambda item: (
            instance and candidates[item[1]]['ui_name'] in ('Factor', 'Fac'),
            candidates[item[1]]['index']))

        if self_socket is not None:
            # One physical socket can have several names across configurations.
            # Bind all its aliases, not just the first candidate's identifier.
            receiver_names = aliases.get(self_socket)
            matches = [(a, n) for a, n in socket_args if n in receiver_names] if receiver_names else []
            if not matches:
                matches = [(a, n) for a, n in socket_args if n == self_socket]
            if not matches:
                matches = [(a, n) for a, n in socket_args
                           if candidates[n]['ui_name'] == self_socket]
            if not matches or (receiver_names is None and len(matches) != 1):
                ui_name = utils.get_node_names(self.node.btree.bl_idname).get(self.node.bnode.bl_idname, node_name)
                available = [(n, a.identifier, candidates[n]['ui_name']) for a, n in socket_args]
                raise ValueError(
                    f"Ambiguous or unknown self socket: {self_socket!r}\n"
                    f"  Node: {self.node.bnode.bl_idname} ({ui_name})\n"
                    f"  Implementation: {name}; fixed parameters: {fixed!r}\n"
                    f"  Available (argument, identifier, UI name): {available!r}")
            for argument, _ in matches:
                argument.is_self = True
                argument.is_argument = argument.multiple == 'ARGS' and kind == 'METHOD' and fixed_sockets is None
                argument.node_value = (f'[self, *{argument.arg_name}]' if argument.is_argument else
                                       '[self]' if argument.multiple == 'ARGS' else 'self')

        if instance and self.node.has_selection:
            for argument, socket_name in socket_args:
                if not argument.is_self and candidates[socket_name]['ui_name'] == 'Selection':
                    argument.is_argument = False
                    argument.node_value = 'self.get_selection()'

        param_args = []
        for param_name, snapshot in parameters.items():
            prop = self.node.bnode.bl_rna.properties[param_name]
            enums = (tuple(item.identifier for item in prop.enum_items)
                     if snapshot['type'] in {'ENUM', 'ENUM_FLAG'} else None)
            param = NodeParam(self.node.bnode, param_name, snapshot['value'], snapshot['type'], enums=enums)
            argument = (Argument.from_param(param, value=fixed[param_name]) if param_name in fixed else
                        Argument.from_param(param))
            # repr preserves quotes and newlines in string defaults.
            argument.arg_value = repr(param.value)
            param_args.append(argument)

        inferred_parameter = None
        inferred_argument = None
        if fixed_sockets is not None:
            for argument, socket_name in socket_args:
                if argument.is_self or not argument.is_argument:
                    continue
                ui_name = candidates[socket_name]['ui_name']
                selected = property_value is not None and property_value[0] == 'socket' and property_value[1] in (socket_name, ui_name)
                if not selected:
                    argument.is_argument = False
                    argument.node_value = repr(fixed_sockets.get(socket_name, fixed_sockets.get(ui_name)))
            if kind == 'SETTER' and property_value is None:
                raise ValueError('A property setter must select its value socket or parameter')
        if kind == 'METHOD' and data_type_socket is not None:
            parameter = self.node.data_type_parameter
            if parameter is not None and parameter.name not in fixed:
                inferred_parameter = parameter.name
                inferred_argument = next((argument for argument, socket_name in socket_args
                                          if socket_name == data_type_socket), None)
                if inferred_argument is None:
                    raise ValueError(f'Unknown type-inference input {data_type_socket!r} for {node_name}')
                for argument in param_args:
                    if argument.arg_name == inferred_parameter:
                        argument.is_argument = False
                        argument.node_value = inferred_parameter

        # Renamed variants of one physical multi-input share one *argument.
        receiver_names = {name for argument, name in socket_args if argument.is_self}
        groups = {}
        for argument, socket_name in socket_args:
            if argument.multiple != 'ARGS' or not argument.is_argument:
                continue
            primary = groups.setdefault(argument.identifier, argument)
            if argument is not primary:
                argument.is_argument = False
            include_self = argument.is_self or (instance and bool(receiver_names) and any(
                socket_name in names and not receiver_names.intersection(names)
                for names in enabled_arguments.values()))
            argument.node_value = (f'[self, *{primary.arg_name}]' if include_self else
                                   f'list({primary.arg_name})')

        exposed_sockets = [(a, name) for a, name in socket_args if a.is_argument]

        def socket_order(item):
            argument, socket_name = item
            names = (socket_name, argument.identifier, candidates[socket_name]['ui_name'])
            return next((index for index, name in enumerate(last_sockets) if name in names), -1)

        if last_sockets:
            exposed_sockets.sort(key=socket_order)
        arguments = [a for a, _ in exposed_sockets] + [a for a in param_args if a.is_argument]
        if anonymous_items:
            arguments.insert(0, Argument(arg_type='SOCKET', arg_name='values', multiple='ARGS',
                                         comment='values : Socket | value\n    Values for the anonymous items.'))
            if self.node.bnode.bl_idname == 'GeometryNodeIndexSwitch':
                arguments.append(Argument(arg_type='UI', arg_name='default_index', arg_value='0', typing='int',
                                          comment='default_index : int, optional\n    Default selector value in the modifier interface.'))
        if kind in {'GETTER', 'SETTER'}:
            expected = 0 if kind == 'GETTER' else 1
            if dynamic or len(arguments) != expected:
                raise ValueError(f'{kind} requires exactly {expected} exposed arguments; fix the other parameters')
        variadic = [a for a in arguments if a.multiple == 'ARGS']
        if len(variadic) > 1 or kind == 'SETTER':
            for argument in variadic:
                argument.multiple = 'NO'
                argument.typing = f"list[{argument.typing}]"
                argument.node_value = argument.arg_name
                argument.comment = (f"{argument.arg_name} : {argument.typing}, optional\n"
                                    f"    Values for the multi-input socket.\n")
            variadic = []

        header = ['cls'] if kind == 'STATIC_METHOD' or class_property else ['self'] if instance else []
        if dynamic:
            header.append('named_sockets=None')
        for argument in variadic + [a for a in arguments if a not in variadic]:
            annotation = f": {argument.typing}" if argument.typing else ''
            header.append(f"*{argument.arg_name}{annotation}" if argument.multiple == 'ARGS' else
                          f"{argument.arg_name}{annotation}" if kind == 'SETTER' else
                          f"{argument.arg_name}{annotation} = {argument.arg_value}")
        if dynamic:
            header.append('**sockets')

        source = {'STATIC_METHOD': '    @classmethod\n', 'GETTER': '    @property\n',
                  'SETTER': f'    @{name}.setter\n'}.get(kind, '')
        if class_property:
            source = '    @utils.classproperty\n'
        source += f"    def {name}(" + ',\n                    '.join(header) + '):\n'
        return_type = 'Node'
        if kind == 'SETTER':
            return_type = None
        elif return_socket is not None:
            types = []
            for config in configurations:
                available = [s for s in self.node.outputs.values()
                             if s.dependencies[config]['enabled'] and s.dependencies[config]['exists']]
                if return_socket == 'OUT':
                    available = available[:1]
                else:
                    available = [s for s in available if return_socket in (
                        s.identifier, s.dependencies[config]['name'],
                        core_module.utils.snake_case(s.dependencies[config]['name']))]
                if len(available) != 1:
                    raise ValueError(f"Ambiguous or unavailable output socket: {return_socket!r}")
                socket = available[0]
                socket_type = socket.dependencies[config]['socket_type']
                class_name = self.node.socket_class_name(socket_type, socket.dependencies[config]['name'])
                if class_name not in types:
                    types.append(class_name)
            return_type = ' | '.join(types)
        source += self.gen_docstring(arguments, is_jump=is_jump if instance else None,
                                     self_socket=self_socket, returns=return_type,
                                     return_socket=return_socket if kind != 'SETTER' else None,
                                     derived_parameters=({inferred_parameter: f'Inferred from {inferred_argument.arg_name}.'}
                                                         if inferred_parameter else None))
        if inferred_parameter:
            source += (f'        {inferred_parameter} = SocketType.get_data_type_for_node('
                       f'{inferred_argument.node_value}, {self.node.bnode.bl_idname!r}, {inferred_parameter!r})\n')

        # Follow the declared enum order, then keep the remaining arguments.
        pending = {a.arg_name: a for a in param_args}
        ordered = [pending.pop(name) for name in self.node.enum_params_order if name in pending]
        ordered.extend(pending.values())
        params = ', '.join(f"{a.arg_name}={a.node_value}" for a in ordered)
        positional_sockets = [(argument, socket_name) for argument, socket_name in socket_args
                              if variadic and argument.multiple == 'ARGS']
        values = ', '.join(f"{socket_name!r}: {argument.node_value}"
                           for argument, socket_name in socket_args
                           if (argument, socket_name) not in positional_sockets)
        source += f"        _named_sockets = {{{values}}}\n"
        source += ('        _named_sockets = {_name: _value for _name, _value in _named_sockets.items()\n'
                   '                          if _value is not None}\n')
        if any(len(names) > 1 for names in aliases.values()):
            # Only aliases need a configuration-dependent selection.
            source += f"        _values = {enabled_arguments!r}\n"
            configuration = []
            for param_name in self.node.driving_parameters:
                prop = self.node.bnode.bl_rna.properties[param_name]
                if prop.type == 'ENUM':
                    names = {item.identifier.lower(): item.identifier for item in prop.enum_items}
                    names.update({item.name.lower(): item.identifier for item in prop.enum_items})
                    if prop.is_enum_flag:
                        value = (f"frozenset({names!r}.get(_value.lower(), _value) "
                                 f"for _value in {param_name})")
                    else:
                        value = f"{names!r}.get({param_name}.lower(), {param_name})"
                else:
                    value = param_name
                if param_name in fixed:
                    value = repr(frozenset(fixed[param_name]) if prop.type == 'ENUM' and prop.is_enum_flag
                                 else fixed[param_name])
                configuration.append(value)
            source += "        _configuration = (" + ', '.join(configuration)
            source += (',' if configuration else '') + ')\n'
            source += ('        _named_sockets = {_name: _value for _name, _value in _named_sockets.items()\n'
                       '                          if _name in _values[_configuration]}\n')
        if dynamic:
            source += ('        _named_sockets.update({_name: _value for _name, _value in (named_sockets or {}).items()\n'
                       '                               if _value is not None})\n')
        positional = '*values' if anonymous_items else ''
        if positional_sockets:
            expressions = {config: next(argument.node_value for argument, socket_name in positional_sockets
                                        if socket_name in enabled_arguments[config]) for config in configurations}
            if len(set(expressions.values())) == 1:
                expression = next(iter(expressions.values()))
                positional = ('*' + expression[5:-1] if expression.startswith('list(') else
                              expression[1:-1] if expression.startswith('[self, *') else '*' + expression)
            else:
                table = ', '.join(f'{config!r}: {expression}' for config, expression in expressions.items())
                source += f'        _node_args = {{{table}}}[_configuration]\n'
                positional = '*_node_args'
        source += f"        _node = Node({node_name!r}" + (', ' + positional if positional else '') + ', named_sockets=_named_sockets'
        if params:
            source += f", {params}"
        if dynamic:
            source += ', **sockets'
        source += ')\n'
        if anonymous_items and self.node.bnode.bl_idname == 'GeometryNodeIndexSwitch':
            source += ("        _selector = _node._bnode.inputs['Index']\n"
                       '        _selector.default_value = default_index\n'
                       '        _interface = _node._get_interface_socket(_selector)\n'
                       '        if _interface is not None:\n'
                       '            _interface.default_value = default_index\n')
        result = '_node' if return_socket is None else '_node._out' if return_socket == 'OUT' else f'_node[{return_socket!r}]'
        if anonymous_items and kind == 'STATIC_METHOD' and return_socket == 'OUT':
            result = f'cls({result})'
        if is_jump:
            source += f'        self._jump({result})\n'
            result = 'self._domain_to_geometry'
        if kind != 'SETTER':
            source += f'        return {result}\n'
        return textwrap.dedent(source) if kind == 'FUNCTION' else source

    # ----------------------------------------------------------------------------------------------------
    # Source code generator
    # ----------------------------------------------------------------------------------------------------

    def _gen_source(
            self,
            method_name,
            *,
            method_type="METHOD",       # METHOD, FUNCTION, CLASS_METHOD, CLASS_PROPERTY, SETTER, GETTER
            self_socket=None,           # Name of the self socket
            is_jump=False,              # Jump
            use_geo_selection=True,     # if selection exists, use geometry selection rather than argument
            return_kind='OUT',          # "NODE", class_name
            return_socket=None,         # explicit output identifier or name
            auto_data_type=None,        # socket name for auto data_type
            fixed_sockets=None,         # Predefined sockets
            last_sockets=(),            # Sockets to move to end (factor in Mix for instance)
        ):

        # ---------------------------------------------------------------------------
        # Preparation
        # ---------------------------------------------------------------------------

        if method_type not in get_args(FUNC_TYPE):
            raise ValueError(f"Unknown implementation type: {method_type!r}")

        is_instance = method_type in ('METHOD', 'SETTER', 'GETTER')

        # Instance only flags
        if not is_instance:
            assert not is_jump, f"is_jump can't be True in '{self.name}' for {method_type=}"
            assert self_socket is None, f"No self_socket for {method_type=}"

        # Fixed sockets
        if fixed_sockets is None:
            fixed_sockets = {}

        source = SourceWriter(method_name, method_type, type_aliases=self.type_aliases)

        # ---------------------------------------------------------------------------
        # Parameters
        # ---------------------------------------------------------------------------

        fixed_params = self.fixed_enums
        free_params = []

        for param_name in self.node.config_order:
            if param_name not in fixed_params:
                free_params.append(param_name)

        # ---------------------------------------------------------------------------
        # Sockets arguments
        # ---------------------------------------------------------------------------

        possible_sockets = self.node.get_possible_sockets(**fixed_params)

        # Remove disabled and fixed sockets
        selected_sockets = [sock for sock in possible_sockets
                            if sock.enabled and (sock.name not in fixed_sockets)]

        # Prepare socket default use and correspondance between argument and sockets
        for sock in selected_sockets:
            sock.ignore         = False # Ignore in argument list
            sock.is_self        = False # This socket is used as self argument
            sock.is_selection   = False # This is the selection socket
            sock.arg_names      = []    # Unique argument names pointing to this socket

        # ---------------------------------------------------------------------------
        # Multi_input socket
        # ---------------------------------------------------------------------------

        has_multi_input_socket = False
        for idx, sock in enumerate(selected_sockets):
            if sock.is_multi_input:
                has_multi_input_socket = True
                multi_input_index = idx

        # ---------------------------------------------------------------------------
        # Self socket
        # ---------------------------------------------------------------------------

        has_self_socket = False
        self_socket_index = -1

        if is_instance and len(selected_sockets):
            has_self_socket = True

            if self_socket is None:
                if has_multi_input_socket:
                    self_socket_index = multi_input_index
                else:
                    self_socket_index = 0
                selected_sockets[self_socket_index].is_self = True
                selected_sockets[self_socket_index].ignore = True
            else:
                names = []
                for i_sock, sock in enumerate(selected_sockets):
                    names.append(sock.socket_name)
                    if sock.socket_name == self_socket:
                        sock.is_self = True
                        sock.ignore = True
                        self_socket_index = i_sock
                        break

                if self_socket_index < 0:
                    raise AttributeError(f"{self_socket=} not found in {names}")

        # ---------------------------------------------------------------------------
        # Selection socket
        # ---------------------------------------------------------------------------

        if is_instance and use_geo_selection and len(selected_sockets) >= 2:
            if selected_sockets[1].socket_name == 'Selection':
                selected_sockets[1].is_selection = True
                selected_sockets[1].ignore = True
            else:
                use_geo_selection = False

        # ===========================================================================
        # Build argument list
        # ===========================================================================

        arguments = []

        # --------------------------------------------------
        # self socket
        # --------------------------------------------------

        if has_self_socket:
            sock = selected_sockets[self_socket_index]
            arguments.append({
                'kind': 'SOCKET',
                'is_self': True,
                'socket_name': sock.socket_name,
                'arg_name': (core_module.utils.snake_case(sock.socket_name)
                            if not arguments else None),
                'socket_index': self_socket_index,
                'identifier': sock.identifier,
            })

        # --------------------------------------------------
        # Multi input socket
        # --------------------------------------------------

        if has_multi_input_socket:
            sock = selected_sockets[multi_input_index]
            arguments.append({
                'kind': 'SOCKET',
                'is_multi': True,
                'socket_name': sock.socket_name,
                'arg_name': core_module.utils.snake_case(sock.socket_name),
                'typing': sock.class_name,
                'socket_index': multi_input_index,
                'identifier': sock.identifier,
            })

        # --------------------------------------------------
        # Anonymous items
        # --------------------------------------------------

        if self.node.has_items and (not self.node.items_with_name) and (not has_multi_input_socket):
            arguments.append({
                'kind': 'ITEMS',
                'is_multi': True,
                'arg_name': 'items',
                'typing': None,
            })

        # --------------------------------------------------
        # Other sockets
        # --------------------------------------------------

        optional_ids = []
        last_args = []
        for i_sock, sock in enumerate(selected_sockets):
            if sock.ignore or sock.is_multi:
                continue

            # Have sockets changing their name
            if len(sock.names) > 1:
                optional_ids.append(sock.identifier)

            # One argument per possible name
            for sock_name in sock.names:
                a = last_args if sock_name in last_sockets else arguments
                a.append({
                    'kind': 'SOCKET',
                    'socket_name': sock_name,
                    'arg_name': core_module.utils.snake_case(sock_name),
                    'typing': sock.class_name,
                    'socket_index': i_sock,
                    'identifier': sock.identifier,
                })
        arguments.extend(last_args)

        # --------------------------------------------------
        # Named items
        # --------------------------------------------------

        if self.node.has_items and self.node.items_with_name:
            arguments.append({
                'kind': 'ITEMS',
                'is_multi': False,
                'arg_name': 'items',
                'typing': None,
            })

        # --------------------------------------------------
        # Parameters
        # --------------------------------------------------

        used_argument_names = set()
        for name in free_params:
            param = self.node.default_params[name]
            arg_name = core_module.utils.snake_case(name)
            typing = None
            if param['type'] == 'ENUM' and param['enums']:
                typing = list(param['enums'])
            elif type(param['value']) in (bool, int, float, str):
                typing = type(param['value']).__name__
            arguments.append({
                'kind': 'PARAMETER',
                'param_name': name,
                'arg_name': arg_name,
                'typing': typing,
                'arg_value': f"{param['value']!r}",
            })
            used_argument_names.add(arg_name)

        # --------------------------------------------------
        # Make sure argument names are unique
        # --------------------------------------------------

        for arg in arguments:
            if arg['kind'] == 'PARAMETER':
                break

            if arg.get('is_self', False):
                continue

            arg_name = arg.get('arg_name', None)
            if arg_name is None:
                continue

            base = arg_name
            suffix = 0
            while arg_name in used_argument_names:
                suffix += 1
                arg_name = f'{base}_{suffix}'
                
            arg['arg_name'] = arg_name
            used_argument_names.add(arg_name)

        # --------------------------------------------------
        # Group unique argument names by id
        # --------------------------------------------------

        synonyms = {}
        for sid in optional_ids:
            synonyms[sid] = [arg['arg_name'] for arg in arguments if arg['kind']=='SOCKET' and arg['identifier']==sid]

        # ---------------------------------------------------------------------------
        # Automatic data type
        # ---------------------------------------------------------------------------

        computed_data_type = None
        if auto_data_type is not None:
            if method_type != 'METHOD':
                raise ValueError('auto_data_type requires an instance method')
            
            type_param = self.node.data_type_parameter
            if type_param is None:
                raise ValueError(f"No data_type or input_type parameter in {self.node.name!r}")
            
            if type_param.name not in fixed_params:
                source_argument = next((arg for arg in arguments
                                        if arg['kind'] == 'SOCKET'
                                        and arg['socket_name'] == auto_data_type), None)
                if source_argument is None:
                    raise ValueError(f"'{self.node.name}': Unknown auto_data_type socket: {auto_data_type!r}")

                data_type_value = 'self' if source_argument.get('is_self') else source_argument['arg_name']
                computed_data_type = type_param.name
                arguments = [arg for arg in arguments
                             if arg.get('param_name') != computed_data_type]

        # ---------------------------------------------------------------------------
        # Node creation arguments
        # ---------------------------------------------------------------------------

        node_args = []
        node_sockets = []
        node_params = []

        if self.node.has_items and (not self.node.items_with_name):
            node_args.append("*items")

        for i_sock, sock in enumerate(selected_sockets):

            # Node(self, *args) or Node(*args)
            if sock.is_multi:
                #assert node_args is None, f"{self.node.name}: Strange case !!!!"
                argument = next(arg for arg in arguments if arg.get('is_multi', False))
                arg_name = argument['arg_name']
                if sock.is_self:
                    node_args.append("self")
                node_args.append(f"*{arg_name}")

            # named_sockets = {'Socket': self}
            elif sock.is_self:
                node_sockets.append(f"'ID_{sock.identifier}': self")

            # named_sockets = {'Selection': selection}
            elif sock.is_selection:
                node_sockets.append(f"'{sock.socket_name}': selection")

            # named_sockets = {'Socket': argument}
            elif len(sock.names) == 1:
                argument = next(arg for arg in arguments
                                if arg['kind'] == 'SOCKET'
                                and arg.get('socket_index') == i_sock)
                if sock.group_name is None:
                    node_sockets.append(f"'ID_{sock.identifier}': {argument['arg_name']}")
                else:
                    node_sockets.append(f"'{sock.group_name}': {argument['arg_name']}")

            # named_sockets = {'ID_Identifier': synonyms['Identifier']}
            else:
                assert len(sock.names) > 1, "Algo error"
                node_sockets.append(f"'ID_{sock.identifier}': synonyms['{sock.identifier}']")

        # Fixed sockets
        for k, v in fixed_sockets.items():
            node_sockets.append(f"'{k}': {v!r}")

        # Parameters
        for arg in arguments:
            if arg['kind'] != 'PARAMETER':
                continue
            node_params.append(f"{arg['arg_name']} = {arg['arg_name']}")

        for p_name, p_value in fixed_params.items():
            node_params.append(f"{p_name} = {p_value!r}")

        if computed_data_type is not None:
            node_params.append(
                f"{computed_data_type} = {computed_data_type}"
            )            

        # ===========================================================================        
        # Source code generation
        # ===========================================================================        

        # ---------------------------------------------------------------------------
        # Functon arguments
        # ---------------------------------------------------------------------------

        for arg in arguments:
            if arg.get('is_self', False):
                continue

            if arg.get('is_multi'):
                if arg['kind'] == 'SOCKET':
                    source.positional_argument(
                        f"*{arg['arg_name']}",
                        typing = arg['typing'],
                        comment = None,
                        )

                elif arg['kind'] == 'ITEMS':
                    source.positional_argument("*items")

                else:
                    assert False, "Unknown case"

            elif arg['kind'] == 'ITEMS':
                assert not arg['is_multi'], "Algo error"
                source.keyword_argument(
                        "items",
                        "{}",
                        typing=None, 
                        comment="Dynamic items")

            elif arg['kind'] == 'PARAMETER':
                source.keyword_argument(
                        arg['arg_name'],
                        arg['arg_value'],
                        typing=arg['typing'], 
                        comment="Node parameter")

            else:
                source.keyword_argument(
                        arg['arg_name'],
                        "None",
                        typing=arg['typing'], 
                        comment="Node Socket")

        if self.node.has_items and self.node.items_with_name:
            source.kwargs_argument("named_items")

        # ---------------------------------------------------------------------------
        # Doc string
        # ---------------------------------------------------------------------------

        source.add_doc(
        f"""Node <&{self.node.name}>

        Jump method: {is_jump}

        """)
        source.returns = "OUT"

        # ---------------------------------------------------------------------------
        # Write source
        # ---------------------------------------------------------------------------

        source.write(f"# Node {self.node.name}")
        source.write_header()
        source.write_doc_string()

        # ---------------------------------------------------------------------------
        # Node call
        # ---------------------------------------------------------------------------

        # Auto data_type
        if computed_data_type is not None:
            source.write(f"{computed_data_type} = SocketType.get_data_type_for_node("
                   f"{data_type_value}, {self.node.bl_idname!r}, {computed_data_type!r})",
                   indent=1)

        # Selection socket
        if any(sock.is_selection for sock in selected_sockets):
            source.write(f"selection = self.get_selection()", indent=1)

        # Filter synonyms
        if len(synonyms):
            source.write("synonyms = {}", indent=1)
            
            for sid, arg_names in synonyms.items():
                source.write()
                source.write(f"synonyms['{sid}'] = None", indent=1)
                for arg_name in arg_names:
                    source.write(
                        f"if {arg_name} is not None: synonyms['{sid}'] = {arg_name}",
                        indent=1)
            source.write()

        # items
        if self.node.has_items and self.node.items_with_name:
            node_sockets.append("**items")
            node_params.append("**named_items")

        # Node creation
        source.write_node_call(
            self.node.name, 
            args            = node_args, 
            named_sockets   = node_sockets, 
            parameters      = node_params, 
            )

        # ---------------------------------------------------------------------------
        # Return
        # ---------------------------------------------------------------------------

        if method_type != 'SETTER':
            if return_socket is not None:
                source.write(f"return node[{return_socket!r}]", indent=1)

            elif return_kind == 'OUT':
                if is_jump:
                    source.write(f"self._jump(node._out)", indent=1)
                    source.write(f"return node._second_out(self)", indent=1)
                else:
                    source.write(f"return node._out", indent=1)

            elif return_kind == 'cls':
                source.write(f"return cls(node._out)", indent=1)

            elif return_kind == 'NODE':
                source.write(f"return node", indent=1)

            else:
                source.write(f"return {return_kind}(node._out)", indent=1)

        return source.source

    # ====================================================================================================
    # Source code generator
    # ====================================================================================================

    def gen_node_call(self, node_call: NodeCall):
        """Generate one function from a resolved implementation description."""
        node_call._check()

        from .sourcewriter import R0
        
        # ---------------------------------------------------------------------------
        # Node analysis
        # - what are the free +/ fixed parameters
        # - what are the sockets to feed
        # ---------------------------------------------------------------------------

        # Parameters
        fixed_params = {name: value for name, value in (self.parameters | node_call.parameters).items()
                        if value is not None}
        free_params = []                # list of free param to inclu

        for param_name in self.node.config_order:
            if param_name not in fixed_params:
                free_params.append(param_name)

        # Sockets
        possible_sockets = self.node.get_possible_sockets(**fixed_params)

        # Remove disabled sockets
        free_sockets = [sock for sock in possible_sockets if sock.enabled]

        # ---------------------------------------------------------------------------
        # Correspondance between signature arguments and node initialisation
        #
        # node = Node('Node Name', *args, named_sockets={'Socket Name': None}, **parameters)
        #
        # for each socket/parameter:
        # - source: fixed / argument / computed
        # - argument name if argument
        # - value if fixed
        # - comment for doc string
        # ---------------------------------------------------------------------------

        # --------------------------------------------------
        # Feed inputs with sockets
        # --------------------------------------------------

        inputs = []
        inputs_last = []
        sock_err_names = [] # For error message

        remaining_fixed_sockets = dict(node_call.fixed_sockets or {})

        for i_sock, sock in enumerate(free_sockets):
            
            sock_err_names.extend(list(sock.names))

            synonym_id = sock.identifier if len(sock.names) > 1 else None

            sock_inputs = []
            sock_inputs_last = []
            sock_names = sock.names
            # Impossible to handle two names for multi sockets
            # see 'Mesh Boolean'
            if sock.is_multi:
                sock_names = (sock.socket_name,)

            for name in sock_names:
                spec = {
                    'type'      : 'SOCKET',
                    'name'      : name,
                    'source'    : 'ARGUMENT',

                    'socket'    : sock,
                    'synonym_id': synonym_id,
                    'arg_name'  : core_module.utils.snake_case(name),
                    'typing'    : sock.class_name or 'Socket',
                    'doc'       : (f"Socket '{name}'" if synonym_id is None else
                                   f"Socket '{name}', identifier '{sock.identifier}'"),
                }

                # Selection socket
                if (node_call.has_self and node_call.use_geo_selection and i_sock == 1
                        and name == 'Selection' and sock.socket_type == 'BOOLEAN'):
                    spec['source']  = 'COMPUTED'
                    spec['computation'] = "selection = self.get_selection()"
                    spec['value']   = "selection"
                    spec['doc']     = "Selection from Geometry[selection]"

                # Fixed socket
                if name in remaining_fixed_sockets:
                    spec['source']      = 'FIXED'
                    spec['value']       = remaining_fixed_sockets[name]
                    spec['synonym_id']  = None
                    spec['doc']         = f"Socket '{name}' set to {remaining_fixed_sockets[name]}"

                    remaining_fixed_sockets.pop(name)
                    sock_inputs = [spec]
                    sock_inputs_last = []
                    break

                if name in node_call.last_sockets:
                    sock_inputs_last.append(spec)
                else:
                    sock_inputs.append(spec)

            inputs.extend(sock_inputs)
            inputs_last.extend(sock_inputs_last)

        inputs.extend(inputs_last)

        if len(remaining_fixed_sockets):
            raise AttributeError(f"{self.node.name}: unknown socket(s): {remaining_fixed_sockets} in {[spec['name'] for spec in inputs]}")

        # Self socket
        if node_call.has_self:

            self_socket = node_call.self_socket
            if self_socket.startswith('NODE.'):
                self_socket = getattr(self.node, self_socket[5:])

            self_socket_index = -1
            for i_spec, spec in enumerate(inputs):
                if (spec['type'] != 'SOCKET') or (spec['source'] != 'ARGUMENT'):
                    continue

                if self_socket == spec['name']:
                    spec['is_self'] = True
                    if spec['socket'].is_multi:
                        spec['doc']     = f"self on multi socket '{spec['name']}'"
                    else:
                        spec['doc']     = f"self on socket '{spec['name']}'"
                    self_socket_index = i_spec
                    break

            if self_socket_index < 0:
                raise AttributeError(f"{self.node.name}: impossible to find socket input for {self_socket=}, {sock_err_names}")

            if self_socket_index > 0:
                spec = inputs.pop(self_socket_index)
                inputs.insert(0, spec)

        # --------------------------------------------------
        # Feed inputs with parameters
        # --------------------------------------------------

        data_type_name = None
        data_type_param_spec = None
        if node_call.auto_data_type is not None:
            type_param = self.node.data_type_parameter
            if type_param is None:
                raise ValueError(f"No data_type or input_type parameter in {self.node.name!r}")

            # An explicitly fixed type takes precedence over inference.
            if type_param.name not in fixed_params:
                data_type_name = type_param.name
                data_type_socket_spec = next(
                    (spec for spec in inputs
                     if spec['source'] == 'ARGUMENT' and spec['type'] == 'SOCKET'
                     and spec['name'] == node_call.auto_data_type), None)
                if data_type_socket_spec is None:
                    raise AttributeError(
                        f"{self.node.name}: Socket {node_call.auto_data_type!r} not found in "
                        f"{[spec['name'] for spec in inputs]}")

        # Free parameters
        for name in free_params:
            snapshot = self.node.default_params[name]
            param = NodeParam(self.node.bnode, name, snapshot['value'],
                              snapshot['type'], enums=snapshot['enums'])
            arg_name = core_module.utils.snake_case(name)
            doc_typing = param.typing
            if param.enums:
                doc_typing = '{' + ', '.join(repr(value) for value in param.enums) + '}'
                if param.param_type == 'ENUM_FLAG':
                    doc_typing = f"set[{doc_typing}]"
            doc_type = f"{doc_typing or 'object'}, "
            spec = {
                'type'      : 'PARAMETER',
                'name'      : name,
                'source'    : 'ARGUMENT',

                'arg_name'  : arg_name,
                'typing'    : param.typing,
                'value'     : repr(param.value),
                'doc'       : (f"{arg_name} : {doc_type}optional\n"
                               f"    Node parameter '{name}' (default: {param.value!r})"),
            }
            if name == data_type_name:
                spec['source'] = 'COMPUTED'
                spec['value'] = 'data_type'
                data_type_param_spec = spec

            inputs.append(spec)

        # Fixed parameters
        for name, value in fixed_params.items():
            sval = f"{value!r}"
            inputs.append({
                'type'      : 'PARAMETER',
                'name'      : name,
                'source'    : 'FIXED',

                'value'     : sval,
                'doc'       : f"parameter '{name}' = {sval}",
            })

        # -------------------------
        # Make argument names unique
        # -------------------------

        existing_names = {spec['arg_name'] for spec in inputs
                          if spec['type'] == 'PARAMETER' and spec['source'] == 'ARGUMENT'}
        synonyms = {}
        for spec in inputs:
            if (spec['type'] != 'SOCKET') or (spec['source'] != 'ARGUMENT'):
                continue

            arg_name = spec['arg_name']
            if arg_name in existing_names:
                num = 1
                while f"{arg_name}_{num}" in existing_names:
                    num += 1

                arg_name = f"{arg_name}_{num}"
                spec['arg_name'] = arg_name

            existing_names.add(spec['arg_name'])

            if spec.get('is_self', False) or spec['socket'].is_multi:
                continue

            sid = spec['synonym_id']
            if sid is None:
                continue

            names = synonyms.setdefault(sid, [])
            names.append(arg_name)

        # -------------------------
        # Auto data type
        # -------------------------

        if data_type_name is not None:
            arg_name = ('self' if data_type_socket_spec.get('is_self', False)
                        else data_type_socket_spec['arg_name'])
            data_type_param_spec['computation'] = (
                f"data_type = SocketType.get_data_type_for_node("
                f"{arg_name}, {self.node.bl_idname!r}, {data_type_name!r})")

        # ---------------------------------------------------------------------------
        # We can now build the 3 sets of arrays:
        # - function arguments
        # - doc string
        # - node call
        # ---------------------------------------------------------------------------

        func_args = []
        func_params = []

        doc_fixed = []
        doc_args = []

        node_args = []
        named_sockets = []
        node_params = []

        for spec in inputs:

            # --------------------------------------------------
            # Sourcing from arguments
            # --------------------------------------------------

            if spec['source'] == 'ARGUMENT':

                arg_name = spec['arg_name']

                if spec['type'] == 'SOCKET':
                    if spec['socket'].is_multi:
                        func_args.append(f"*{arg_name}: {spec['typing']}")
                        doc_args.append(
                            f"{arg_name} : {spec['typing']}\n"
                            f"    {spec['doc']} (multiple values)")

                    elif spec.get('is_self', False):
                        doc_fixed.append(spec['doc'])

                    else:
                        func_args.append(f"{arg_name}: {spec['typing']}=None")
                        doc_args.append(
                            f"{arg_name} : {spec['typing']}, optional\n"
                            f"    {spec['doc']} (default: None)")

                else:
                    typing = spec['typing']
                    if isinstance(typing, list):
                        typing = (self.type_aliases.literal(typing, prefix=f"T_{arg_name.upper()}")
                                  if self.type_aliases is not None else
                                  "Literal[" + ', '.join(repr(value) for value in typing) + "]")
                    annotation = f": {typing}" if typing else ''
                    func_params.append(f"{arg_name}{annotation}={spec['value']}")
                    doc_args.append(spec['doc'])

            # --------------------------------------------------
            # Consuming to build node
            # --------------------------------------------------

            if spec['type'] == 'SOCKET':
                if spec['source'] == 'ARGUMENT':

                    arg_name = spec['arg_name']
                    sock     = spec['socket']
                    is_self  = spec.get('is_self', False)
                    sock_id  = f"ID_{sock.identifier}"
                    if sock.group_name is not None:
                        sock_id = sock.group_name

                    if sock.is_multi:
                        if is_self:
                            node_args.extend(["self", f"*{arg_name}"])
                        else:
                            node_args.append(f"*{arg_name}")

                    elif is_self:
                        named_sockets.append(f"'{sock_id}': self")

                    elif spec['synonym_id'] is not None:
                        # will be computed dynamically
                        pass

                    else:
                        named_sockets.append(f"'{sock_id}': {spec['arg_name']}")

                elif spec['source'] == 'FIXED':
                    named_sockets.append(f"{spec['name']!r}: {spec['value']!r}")

                elif spec['source'] == 'COMPUTED':
                    named_sockets.append(f"'{spec['name']}': {spec['value']}")

                else:
                    assert False, spec['source']

            else:
                value = spec['arg_name'] if spec['source'] == 'ARGUMENT' else spec['value']
                node_params.append(f"{spec['name']}={value}")


        # ---------------------------------------------------------------------------
        # Node with items
        # ---------------------------------------------------------------------------

        add_named_items = False
        if self.node.has_items:
            if self.node.items_with_name:
                add_named_items = True
                # def f(...items={'name': value, ...}, ... **named_items)
                # Node(..., named_sockets={..., **items}, ... **named_items)
                func_args.append("items={}")
                func_params.append("**named_items")
                node_params.append("**named_items")
                doc_args.append(f"items : dict, optional\n{TAB}dynamic sockets")
                doc_args.append(f"**named_items : Socket\n{TAB}Dynamic sockets supplied by keyword.")
            else:
                # def f(...*dyn_sockets)
                # Node(..., *dyn_sockets, ...)
                func_args.append("*dyn_sockets")
                node_args.append("*dyn_sockets")
                doc_args.append(f"*dyn_sockets : Socket\n{TAB}Values for anonymous dynamic sockets.")

        # ---------------------------------------------------------------------------
        # We can build the source code
        # ---------------------------------------------------------------------------

        source = SourceWriter(node_call.method_name, func_type=node_call.method_type, type_aliases=self.type_aliases)

        source.write(f"#Node {self.node.name}")

        # decorator
        if node_call.decorator is not None:
            source.write(node_call.decorator)

        # Header
        all_args = ([arg for arg in func_args if arg.startswith('*')]
                    + [arg for arg in func_args if not arg.startswith('*')] + func_params)
        if node_call.first_arg is not None:
            all_args.insert(0, node_call.first_arg)

        #source.write(f"def {node_call.method_name}({', '.join(all_args)}):")
        sep = f",{R0}"
        source.write(f"def {node_call.method_name}({R0}{sep.join(all_args)}):")

        # Doc String
        source.write(f'"""Node {self.node.name}.\n', indent=1)
        source.write(f"Jump: {node_call.is_jump}", indent=1)

        if len(doc_fixed):
            source.write()
            source.write("**Fixed inputs**", indent=1)
            source.write()
            for description in doc_fixed:
                source.write(f"- {description}", indent=1)

        if len(doc_args):
            source.write()
            source.write("Parameters", indent=1)
            source.write("----------", indent=1)
            source.write(*doc_args, indent=1)

        if node_call.method_type != 'SETTER':
            source.write()
            source.write("Returns", indent=1)
            source.write("-------", indent=1)

            if node_call.return_socket is not None:
                source.write("Socket", indent=1)
                source.write(f"    Socket '{node_call.return_socket}'.", indent=1)

            elif node_call.return_kind == 'OUT':
                if node_call.is_jump:
                    source.write("Socket", indent=1)
                    source.write("    Second output socket, or self if there is no second output.", indent=1)
                    source.write("    Updates self from the default output socket.", indent=1)
                else:
                    source.write("Socket", indent=1)
                    source.write("    Default output socket.", indent=1)

            elif node_call.return_kind == 'cls':
                source.write("Self", indent=1)
                source.write("    Default output socket wrapped in the calling class.", indent=1)

            elif node_call.return_kind == 'NODE':
                source.write(f"Node", indent=1)

            else:
                source.write(node_call.return_kind, indent=1)
                source.write(f"    Default output socket wrapped in {node_call.return_kind}.", indent=1)
            
        source.write('"""', indent=1)

        # Pre computations
        for spec in inputs:
            if spec['source'] == 'COMPUTED':
                source.write(spec['computation'], indent=1)

        # Build named sockets before resolving aliases.
        #source.write("named_sockets = {" + ", ".join(named_sockets) + "}", indent=1)
        source.write("named_sockets = " + source.splittable(named_sockets, set), indent=1)
        for sid, synos in synonyms.items():
            source.write(f"named_sockets['ID_{sid}'] = None", indent=1)
            for name in synos:
                source.write(
                    f"if {name} is not None: named_sockets['ID_{sid}'] = {name}",
                    indent=1)

        # Add dynamic sockets
        if add_named_items:
            source.write("named_sockets = {**named_sockets, **items}", indent=1)

        node_args.append("named_sockets=named_sockets")
        node_args.extend(node_params)
        source.write()

        sep = f",{R0}"
        source.write(f"node = Node({R0}" + sep.join([f"{self.node.name!r}"] + node_args) + ")", indent=1)
        #source.write(f"node = Node({self.node.name!r}, {', '.join(node_args)})", indent=1)

        # return

        if node_call.method_type != 'SETTER':
            if node_call.return_socket is not None:
                source.write(f"return node[{node_call.return_socket!r}]", indent=1)

            elif node_call.return_kind == 'OUT':
                if node_call.is_jump:
                    source.write(f"self._jump(node._out)", indent=1)
                    source.write(f"return node._second_out(self)", indent=1)
                else:
                    source.write(f"return node._out", indent=1)

            elif node_call.return_kind == 'cls':
                source.write(f"return cls(node._out)", indent=1)

            elif node_call.return_kind == 'NODE':
                source.write(f"return node", indent=1)

            else:
                source.write(f"return {node_call.return_kind}(node._out)", indent=1)

        return source.source
