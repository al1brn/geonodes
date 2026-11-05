"""Python implementations of an introspected node."""

import ast
import keyword
import inspect
import textwrap
from pathlib import Path

import bpy

from .. import core_module
from . import config, utils, source_code
from .output import ENVIRONMENTS, render_modules
from .argument import Argument
from .node_info import NodeInfo
from .node_param import NodeParam


class NodeImplementation:
    """Describe a node implementation and generate its Python source code."""

    files = {}
    cross_refs = {}
    tree_type = 'GeometryNodeTree'

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
    def register_source(cls, node, filename, destination, source, returns='OUT', *, write_source=True, rules=[]):
        """Register source and its cross reference, rejecting duplicate names."""

        try:
            function = ast.parse(textwrap.dedent(source)).body[0]
        except Exception as e:
            print(f"Compilation error in '{node.name}'")
            if len(rules):
                print("\n".join(rules))
            print()
            raise e

        name = function.name
        reference = {
            'func_name': name,
            'node_name': node.bnode.name,
            'tree_type': node.btree.bl_idname,
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
        tree_type = node.btree.bl_idname
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
                        cls.register_source(node, None, destination, inspect.getsource(function),
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
        try:
            for selected_type in selected:
                cls.tree_type = selected_type
                cls.files[selected_type] = {}
                cls.cross_refs[selected_type] = {}

                cls.gen_static_code()
                cls.gen_gnmath()
                cls.gen_nodes()
                cls.gen_properties()
        finally:
            cls.tree_type = previous_type
        if write:
            cls.write_files(use_core_new=use_core_new)
        environments = ', '.join(ENVIRONMENTS[selected_type] for selected_type in selected)
        action = 'Generation completed' if write else 'Source collection completed (no files written)'
        print(f'\n{action}: {environments}.')

    # ====================================================================================================
    # Generate math module
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Main : call the various sources of math functions
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def gen_gnmath(cls):
        """Collect all math families and Color Mix operations."""
        cls.gen_math_functions()
        if cls.tree_type == 'GeometryNodeTree':
            cls.gen_integer_math_functions()
            cls.gen_boolean_math_functions()
        cls.gen_vector_math_functions()
        if cls.tree_type == 'GeometryNodeTree':
            cls.gen_bit_math_functions()
        cls.gen_mix_color_functions()
        cls.gen_compare_functions()

    # ----------------------------------------------------------------------------------------------------
    # Check operations
    # ----------------------------------------------------------------------------------------------------

    @staticmethod
    def _check_operations(node, operations, param_name='operation'):
        """Refuse to generate when an enum operation is not accounted for."""
        available = set(NodeParam.Parameter(node.bnode, param_name).enums)
        handled = set(operations)
        missing = available - handled
        obsolete = handled - available
        if missing or obsolete:
            details = []
            if missing:
                details.append(f'unhandled operations: {sorted(missing)}')
            if obsolete:
                details.append(f'operations unavailable in Blender: {sorted(obsolete)}')
            raise ValueError(f"{node.bnode.name}.{param_name}: " + '; '.join(details))

    # ----------------------------------------------------------------------------------------------------
    # Math Node
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def gen_math_functions(cls):
        """Collect Math functions, Float methods and scalar Float operators.

        Names and operator mappings are explicit here, independently of the
        legacy generation dictionaries. The public Float subclass retains its
        hand-written operators, including vector dispatch and comparisons.
        No generated files are written by this method.
        """
        operations = (
            ('ADD', 'add'), ('SUBTRACT', 'subtract'), ('MULTIPLY', 'multiply'),
            ('DIVIDE', 'divide'), ('MULTIPLY_ADD', 'multiply_add'),
            ('POWER', 'power'), ('LOGARITHM', 'log'), ('SQRT', 'sqrt'),
            ('INVERSE_SQRT', 'inverse_sqrt'), ('ABSOLUTE', 'abs'), ('EXPONENT', 'exp'),
            ('MINIMUM', 'min'), ('MAXIMUM', 'max'), ('LESS_THAN', 'less_than'),
            ('GREATER_THAN', 'greater_than'), ('SIGN', 'sign'), ('COMPARE', 'compare'),
            ('SMOOTH_MIN', 'smooth_min'), ('SMOOTH_MAX', 'smooth_max'),
            ('ROUND', 'round'), ('FLOOR', 'floor'), ('CEIL', 'ceil'), ('TRUNC', 'trunc'),
            ('FRACT', 'fract'), ('MODULO', 'modulo'), ('FLOORED_MODULO', 'floored_modulo'),
            ('WRAP', 'wrap'), ('SNAP', 'snap'), ('PINGPONG', 'pingpong'),
            ('SINE', 'sin'), ('COSINE', 'cos'), ('TANGENT', 'tan'),
            ('ARCSINE', 'asin'), ('ARCCOSINE', 'acos'), ('ARCTANGENT', 'arctangent'),
            ('ARCTAN2', 'atan2'), ('SINH', 'sinh'), ('COSH', 'cosh'), ('TANH', 'tanh'),
            ('RADIANS', 'radians'), ('DEGREES', 'degrees'),
        )
        binary_operators = (
            ('add', 'add', True, None),
            ('sub', 'subtract', False, None),
            ('mul', 'multiply', True, None),
            ('truediv', 'divide', False, None),
            ('mod', 'modulo', False, None),
            ('pow', 'power', False, None),
        )
        unary_operators = (
            ('__neg__', 'self.multiply(-1)'), ('__abs__', 'self.abs()'),
            ('__round__', 'self.round()'), ('__trunc__', 'self.trunc()'),
            ('__floor__', 'self.floor()'), ('__ceil__', 'self.ceil()'),
        )
        tree = bpy.data.node_groups.new(name='Math functions', type=cls.tree_type)
        try:
            node = NodeInfo(tree, tree.nodes.new(type='ShaderNodeMath'))
            cls._check_operations(node, (op[0] for op in operations))
            base = cls(node)
            for operation, name in operations:
                if cls.tree_type == 'GeometryNodeTree' and operation in ('LESS_THAN', 'GREATER_THAN', 'COMPARE'):
                    name = 'm' + name
                implementation = base.copy()
                implementation['operation'] = operation
                cls.register_source(node, 'gnmath.py', 'gnmath',
                                    '\n'.join(implementation._gen_source(name, method_type='FUNCTION', return_kind='OUT')))
                cls.register_source(node, 'float.py', 'Float',
                                    '\n'.join(implementation._gen_source(name, method_type='METHOD', return_kind='OUT')))

            for operator, method, commutative, code_class in binary_operators:
                call = f'self.{method}(other)'
                reverse = call if commutative else f'type(self)(other).{method}(self)'
                for name, expression in (
                    (f'__{operator}__', call),
                    (f'__r{operator}__', reverse),
                    (f'__i{operator}__', f'self._jump({call})'),
                ):
                    copy_code = getattr(code_class, name, None)
                    source = (base.gen_source(kind='METHOD', copy_code=copy_code) if copy_code is not None else
                              f'    def {name}(self, other):\n        return {expression}\n')
                    cls.register_source(node, 'float.py', 'Float', source)

            for name, expression in unary_operators:
                source = f'    def {name}(self):\n        return {expression}\n'
                cls.register_source(node, 'float.py', 'Float', source)
        finally:
            bpy.data.node_groups.remove(tree)

    # ----------------------------------------------------------------------------------------------------
    # Integer Math Node
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def gen_integer_math_functions(cls):
        """Collect Integer Math functions, Integer methods and integer operators.

        Global function names retain the existing gnmath convention. Dunder
        methods delegate to ordinary methods without docstrings. Division uses
        divide_floor for //; true division and mixed-type dispatch remain in
        the hand-written Integer subclass.
        """
        operations = (
            ('ADD', 'add', 'iadd'), ('SUBTRACT', 'subtract', 'isubtract'),
            ('MULTIPLY', 'multiply', 'imultiply'), ('DIVIDE', 'divide', 'idivide'),
            ('MULTIPLY_ADD', 'multiply_add', 'imultiply_add'),
            ('ABSOLUTE', 'abs', 'iabs'), ('NEGATE', 'negate', 'negate'),
            ('POWER', 'power', 'ipower'), ('MINIMUM', 'min', 'imin'),
            ('MAXIMUM', 'max', 'imax'), ('SIGN', 'sign', 'isign'),
            ('DIVIDE_ROUND', 'divide_round', 'divide_round'),
            ('DIVIDE_FLOOR', 'divide_floor', 'divide_floor'),
            ('DIVIDE_CEIL', 'divide_ceil', 'divide_ceil'),
            ('FLOORED_MODULO', 'floored_modulo', 'ifloored_modulo'),
            ('MODULO', 'modulo', 'imodulo'), ('GCD', 'gcd', 'gcd'), ('LCM', 'lcm', 'lcm'),
        )
        binary_operators = (
            ('add', 'add', True, None),
            ('sub', 'subtract', False, None),
            ('mul', 'multiply', True, None),
            ('floordiv', 'divide_floor', False, None),
            ('mod', 'modulo', False, None),
            ('pow', 'power', False, None),
        )
        tree = bpy.data.node_groups.new(name='Integer Math functions', type=cls.tree_type)
        try:
            node = NodeInfo(tree, tree.nodes.new(type='FunctionNodeIntegerMath'))
            cls._check_operations(node, (op[0] for op in operations))
            base = cls(node)
            for operation, method_name, function_name in operations:
                implementation = base.copy()
                implementation['operation'] = operation
                cls.register_source(node, 'gnmath.py', 'gnmath',
                                    '\n'.join(implementation._gen_source(function_name, method_type='FUNCTION', return_kind='OUT')))
                cls.register_source(node, 'integer.py', 'Integer',
                                    '\n'.join(implementation._gen_source(method_name, method_type='METHOD', return_kind='OUT')))

            for operator, method, commutative, code_class in binary_operators:
                call = f'self.{method}(other)'
                reverse = call if commutative else f'type(self)(other).{method}(self)'
                for name, expression in (
                    (f'__{operator}__', call),
                    (f'__r{operator}__', reverse),
                    (f'__i{operator}__', f'self._jump({call})'),
                ):
                    copy_code = getattr(code_class, name, None)
                    source = (base.gen_source(kind='METHOD', copy_code=copy_code) if copy_code is not None else
                              f'    def {name}(self, other):\n        return {expression}\n')
                    cls.register_source(node, 'integer.py', 'Integer', source)

            for name, method in (('__neg__', 'negate'), ('__abs__', 'abs')):
                source = f'    def {name}(self):\n        return self.{method}()\n'
                cls.register_source(node, 'integer.py', 'Integer', source)
        finally:
            bpy.data.node_groups.remove(tree)

    # ----------------------------------------------------------------------------------------------------
    # Boolean Math Node
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def gen_boolean_math_functions(cls):
        """Collect Boolean Math functions, Boolean methods and operators.

        Keep the existing names, arithmetic aliases and rejection of Python
        truth testing. Operators delegate to ordinary methods, without docs.
        """
        operations = (
            ('AND', 'band'), ('OR', 'bor'), ('NOT', 'bnot'), ('NAND', 'not_and'),
            ('NOR', 'nor'), ('XNOR', 'xnor'), ('XOR', 'xor'),
            ('IMPLY', 'imply'), ('NIMPLY', 'nimply'),
        )
        binary_operators = (
            ('and', 'band', True), ('or', 'bor', True), ('xor', 'xor', True),
            ('add', 'bor', True), ('mul', 'band', True), ('sub', 'nimply', False),
        )
        tree = bpy.data.node_groups.new(name='Boolean Math functions', type=cls.tree_type)
        try:
            node = NodeInfo(tree, tree.nodes.new(type='FunctionNodeBooleanMath'))
            cls._check_operations(node, (op[0] for op in operations))
            base = cls(node)
            for operation, name in operations:
                implementation = base.copy()
                implementation['operation'] = operation
                cls.register_source(node, 'gnmath.py', 'gnmath',
                                    '\n'.join(implementation._gen_source(name, method_type='FUNCTION', return_kind='OUT')))
                cls.register_source(node, 'boolean.py', 'Boolean',
                                    '\n'.join(implementation._gen_source(name, method_type='METHOD', return_kind='OUT')))

            for operator, method, commutative in binary_operators:
                call = f'self.{method}(other)'
                reverse = call if commutative else f'type(self)(other).{method}(self)'
                for name, expression in (
                    (f'__{operator}__', call),
                    (f'__r{operator}__', reverse),
                    (f'__i{operator}__', f'self._jump({call})'),
                ):
                    source = f'    def {name}(self, other):\n        return {expression}\n'
                    cls.register_source(node, 'boolean.py', 'Boolean', source)
            for name in ('__neg__', '__invert__'):
                source = f'    def {name}(self):\n        return self.bnot()\n'
                cls.register_source(node, 'boolean.py', 'Boolean', source)
            message = "Boolean Socket is not a python bool. Use 'switch' method or operators & | "
            source = f'    def __bool__(self):\n        raise NodeError({message!r})\n'
            cls.register_source(node, 'boolean.py', 'Boolean', source, returns=None)
        finally:
            bpy.data.node_groups.remove(tree)

    # ----------------------------------------------------------------------------------------------------
    # Vector Math Node
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def gen_vector_math_functions(cls):
        """Collect Vector Math functions, Vector methods and operators.

        Scalar outputs are selected by _gen_source for each operation.
        Multiplication/division by scalars use scale; @ is the dot product.
        """
        operations = (
            ('ADD', 'add', 'vadd'), ('SUBTRACT', 'subtract', 'vsubtract'),
            ('MULTIPLY', 'multiply', 'vmultiply'), ('DIVIDE', 'divide', 'vdivide'),
            ('MULTIPLY_ADD', 'multiply_add', 'vmultiply_add'),
            ('CROSS_PRODUCT', 'cross', 'cross'), ('PROJECT', 'project', 'project'),
            ('REFLECT', 'reflect', 'reflect'), ('REFRACT', 'refract', 'refract'),
            ('FACEFORWARD', 'faceforward', 'faceforward'), ('DOT_PRODUCT', 'dot', 'dot'),
            ('DISTANCE', 'distance', 'distance'), ('LENGTH', 'length', 'length'),
            ('SCALE', 'scale', 'scale'), ('NORMALIZE', 'normalize', 'normalize'),
            ('ABSOLUTE', 'abs', 'vabs'), ('POWER', 'power', 'vpower'),
            ('SIGN', 'sign', 'vsign'), ('MINIMUM', 'min', 'vmin'),
            ('MAXIMUM', 'max', 'vmax'), ('ROUND', 'round', 'vround'),
            ('FLOOR', 'floor', 'vfloor'), ('CEIL', 'ceil', 'vceil'),
            ('FRACTION', 'fraction', 'vfraction'), ('MODULO', 'modulo', 'vmodulo'),
            ('WRAP', 'wrap', 'vwrap'), ('SNAP', 'snap', 'vsnap'),
            ('SINE', 'sin', 'vsin'), ('COSINE', 'cos', 'vcos'), ('TANGENT', 'tan', 'vtan'),
        )
        binary_operators = (
            ('add', 'self.add(other)', 'self.add(other)', None),
            ('sub', 'self.subtract(other)', 'type(self)(other).subtract(self)', None),
            ('mul', 'self.scale(other) if utils.is_value_like(other) else self.multiply(other)', 'self.scale(other) if utils.is_value_like(other) else self.multiply(other)', None),
            ('truediv', 'self.scale(1 / other) if utils.is_value_like(other) else self.divide(other)', 'type(self)(other).divide(self)', None),
            ('mod', 'self.modulo(other)', 'type(self)(other).modulo(self)', None),
            ('pow', 'self.power(other)', 'type(self)(other).power(self)', None),
        )
        unary_operators = (
            ('__neg__', 'self.scale(-1)'), ('__abs__', 'self.abs()'),
            ('__floor__', 'self.floor()'), ('__ceil__', 'self.ceil()'),
        )
        tree = bpy.data.node_groups.new(name='Vector Math functions', type=cls.tree_type)
        try:
            node = NodeInfo(tree, tree.nodes.new(type='ShaderNodeVectorMath'))
            cls._check_operations(node, (op[0] for op in operations))
            base = cls(node)
            for operation, method_name, function_name in operations:
                implementation = base.copy()
                implementation['operation'] = operation
                cls.register_source(node, 'gnmath.py', 'gnmath',
                                    '\n'.join(implementation._gen_source(function_name, method_type='FUNCTION', return_kind='OUT')))
                cls.register_source(node, 'vector.py', 'Vector',
                                    '\n'.join(implementation._gen_source(method_name, method_type='METHOD', return_kind='OUT')))

            for operator, call, reverse, code_class in binary_operators:
                for name, expression in (
                    (f'__{operator}__', call),
                    (f'__r{operator}__', reverse),
                    (f'__i{operator}__', f'self._jump({call})'),
                ):
                    copy_code = getattr(code_class, name, None)
                    source = (base.gen_source(kind='METHOD', copy_code=copy_code) if copy_code is not None else
                              f'    def {name}(self, other):\n        return {expression}\n')
                    cls.register_source(node, 'vector.py', 'Vector', source)
            for name, expression in unary_operators:
                source = f'    def {name}(self):\n        return {expression}\n'
                cls.register_source(node, 'vector.py', 'Vector', source)
            source = '    def __matmul__(self, other):\n        return self.dot(other)\n'
            cls.register_source(node, 'vector.py', 'Vector', source)
        finally:
            bpy.data.node_groups.remove(tree)

    # ----------------------------------------------------------------------------------------------------
    # Bit Math Node
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def gen_bit_math_functions(cls):
        """Collect Bit Math functions, Integer methods and bitwise operators.

        Names retain the bw_ prefix. A negative shift implements right shift.
        Dunder methods delegate to the ordinary methods without docstrings.
        """
        operations = (
            ('AND', 'bw_and'), ('OR', 'bw_or'), ('XOR', 'bw_xor'),
            ('NOT', 'bw_not'), ('SHIFT', 'bw_shift'), ('ROTATE', 'bw_rotate'),
        )
        tree = bpy.data.node_groups.new(name='Bit Math functions', type=cls.tree_type)
        try:
            node = NodeInfo(tree, tree.nodes.new(type='FunctionNodeBitMath'))
            cls._check_operations(node, (op[0] for op in operations))
            base = cls(node)
            for operation, name in operations:
                implementation = base.copy()
                implementation['operation'] = operation
                cls.register_source(node, 'gnmath.py', 'gnmath',
                                    '\n'.join(implementation._gen_source(name, method_type='FUNCTION', return_kind='OUT')))
                cls.register_source(node, 'integer.py', 'Integer',
                                    '\n'.join(implementation._gen_source(name, method_type='METHOD', return_kind='OUT')))

            for operator, method in (('and', 'bw_and'), ('or', 'bw_or'), ('xor', 'bw_xor')):
                call = f'self.{method}(other)'
                for name, expression in (
                    (f'__{operator}__', call),
                    (f'__r{operator}__', call),
                    (f'__i{operator}__', f'self._jump({call})'),
                ):
                    source = f'    def {name}(self, other):\n        return {expression}\n'
                    cls.register_source(node, 'integer.py', 'Integer', source)

            for operator, shift, reverse_shift in (
                ('lshift', 'other', 'self'), ('rshift', '-other', '-self'),
            ):
                call = f'self.bw_shift({shift})'
                for name, expression in (
                    (f'__{operator}__', call),
                    (f'__r{operator}__', f'type(self)(other).bw_shift({reverse_shift})'),
                    (f'__i{operator}__', f'self._jump({call})'),
                ):
                    source = f'    def {name}(self, other):\n        return {expression}\n'
                    cls.register_source(node, 'integer.py', 'Integer', source)
            source = '    def __invert__(self):\n        return self.bw_not()\n'
            cls.register_source(node, 'integer.py', 'Integer', source)
        finally:
            bpy.data.node_groups.remove(tree)

    # ----------------------------------------------------------------------------------------------------
    # Color Mix Node
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def gen_mix_color_functions(cls):
        """Collect Color Mix operations as global functions and Color methods.

        Fix RGBA and the blend mode; expose factor after a/b and keep the
        clamp options free. No dunder methods are generated.
        """
        operations = (
            'MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE',
            'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE',
            'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE',
        )
        tree = bpy.data.node_groups.new(name='Color Mix functions', type=cls.tree_type)
        try:
            node = NodeInfo(tree, tree.nodes.new(type='ShaderNodeMix'))
            node.set_params(data_type='RGBA', factor_mode='UNIFORM')
            cls._check_operations(node, operations, param_name='blend_type')
            base = cls(node)
            base['data_type'] = 'RGBA'
            base['factor_mode'] = 'UNIFORM'
            for operation in operations:
                implementation = base.copy()
                implementation['blend_type'] = operation
                name = 'mix_' + operation.lower()
                cls.register_source(node, 'gnmath.py', 'gnmath',
                                    implementation.gen_source(kind='FUNCTION', name=name,
                                                              return_socket='OUT', last_sockets=('Factor',)))
                cls.register_source(node, 'color.py', 'Color',
                                    implementation.gen_source(kind='METHOD', name=name, self_socket='a',
                                                              return_socket='OUT', last_sockets=('Factor',)))
        finally:
            bpy.data.node_groups.remove(tree)

    # ----------------------------------------------------------------------------------------------------
    # Compare Node
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def gen_compare_functions(cls):
        """Collect comparisons for this environment's available node types.

        Geometry comparisons use Compare; scalar shader comparisons use Math.
        Vector comparisons in Geometry Nodes use ELEMENT mode.
        """
        if cls.tree_type == 'ShaderNodeTree':
            cls._gen_shader_compare_functions()
            return
        numeric = ('LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL')
        equality = ('EQUAL', 'NOT_EQUAL')
        types = (
            ('FLOAT', 'Float', '', numeric), ('INT', 'Integer', 'i', numeric),
            ('VECTOR', 'Vector', 'v', numeric), ('RGBA', 'Color', 'c', (*equality, 'BRIGHTER', 'DARKER')),
            ('STRING', 'String', 's', equality), ('OBJECT', 'Object', 'object_', equality),
            ('IMAGE', 'Image', 'image_', equality), ('COLLECTION', 'Collection', 'collection_', equality),
            ('MATERIAL', 'Material', 'material_', equality), ('FONT', 'Font', 'font_', equality),
            ('SOUND', 'Sound', 'sound_', equality),
        )
        dunders = {'LESS_THAN': '__lt__', 'LESS_EQUAL': '__le__', 'GREATER_THAN': '__gt__',
                   'GREATER_EQUAL': '__ge__', 'EQUAL': '__eq__', 'NOT_EQUAL': '__ne__'}

        def argument(name, class_name, socket_name):
            return Argument(arg_type='SOCKET', arg_name=name, typing=class_name,
                            arg_value='None', node_value=name,
                            comment=f"{name} : {class_name}, optional\n    socket '{socket_name}'")

        tree = bpy.data.node_groups.new(name='Compare functions', type=cls.tree_type)
        try:
            node = NodeInfo(tree, tree.nodes.new(type='FunctionNodeCompare'))
            cls._check_operations(node, (row[0] for row in types), param_name='data_type')

            # Compound Shader comparisons reuse the Math functions in gnmath.
            math_node = NodeInfo(tree, tree.nodes.new(type='ShaderNodeMath'))
            for name, expression, has_epsilon in (
                ('mless_equal', 'subtract(1, mgreater_than(a, b))', False),
                ('mgreater_equal', 'subtract(1, mless_than(a, b))', False),
                ('mnot_equal', 'subtract(1, mcompare(a, b, epsilon=epsilon))', True),
            ):
                implementation = cls(math_node)
                implementation['operation'] = 'SUBTRACT'
                implementation['use_clamp'] = False
                arguments = [argument('a', 'Float', 'Value'), argument('b', 'Float', 'Value')]
                if has_epsilon:
                    arguments.append(argument('epsilon', 'Float', 'Epsilon'))
                header = ', '.join(f'{a.arg_name}: {a.typing} = None' for a in arguments)
                source = f'def {name}({header}):\n'
                source += implementation.gen_docstring(arguments, returns='Float', return_socket='OUT', indent=4)
                source += f'    return {expression}\n'
                cls.register_source(math_node, 'gnmath.py', 'gnmath', source)

            for data_type, class_name, prefix, operations in types:
                node.set_params(data_type=data_type, mode='ELEMENT', operation=operations[0])
                cls._check_operations(node, operations)
                base = cls(node)
                base['data_type'] = data_type
                base['mode'] = 'ELEMENT'
                for operation in operations:
                    implementation = base.copy()
                    implementation['operation'] = operation
                    method_name = operation.lower()
                    function_name = prefix + method_name
                    source = implementation.gen_source(kind='FUNCTION', name=function_name, return_socket='OUT')
                    cls.register_source(node, 'gnmath.py', 'gnmath', source)

                    has_epsilon = data_type in {'FLOAT', 'VECTOR', 'RGBA'} and operation in equality
                    arguments = [argument('b', class_name, 'B')]
                    if has_epsilon:
                        arguments.append(argument('epsilon', 'Float', 'Epsilon'))
                    header = ', '.join(f'{a.arg_name}: {a.typing} = None' for a in arguments)
                    source = f'    def {method_name}(self, {header}):\n'
                    source += implementation.gen_docstring(arguments, is_jump=False, self_socket='A',
                                                           returns='Boolean', return_socket='OUT')
                    source += '        from . import gnmath\n'
                    extra = ', epsilon=epsilon' if has_epsilon else ''
                    source += f'        return gnmath.{function_name}(self, b{extra})\n'
                    filename = class_name.lower() + '.py'
                    cls.register_source(node, filename, class_name, source)
                    if operation in dunders:
                        source = f'    def {dunders[operation]}(self, other):\n        return self.{method_name}(other)\n'
                        cls.register_source(node, filename, class_name, source)
        finally:
            bpy.data.node_groups.remove(tree)

    # ----------------------------------------------------------------------------------------------------
    # Shader specific comparizons
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def _gen_shader_compare_functions(cls):
        """Complete shader comparisons from the ordinary Math functions."""
        comparisons = (
            ('less_than', 'less_than', '__lt__', False),
            ('less_equal', 'less_equal', '__le__', False),
            ('greater_than', 'greater_than', '__gt__', False),
            ('greater_equal', 'greater_equal', '__ge__', False),
            ('equal', 'compare', '__eq__', True),
            ('not_equal', 'not_equal', '__ne__', True),
        )
        tree = bpy.data.node_groups.new(name='Shader comparisons', type='ShaderNodeTree')
        try:
            node = NodeInfo(tree, tree.nodes.new(type='ShaderNodeMath'))
            for name, expression, epsilon in (
                ('less_equal', 'subtract(1, greater_than(a, b))', False),
                ('greater_equal', 'subtract(1, less_than(a, b))', False),
                ('not_equal', 'subtract(1, compare(a, b, epsilon=epsilon))', True),
                ('equal', 'compare(a, b, epsilon=epsilon)', True),
            ):
                header = 'a=None, b=None' + (', epsilon=None' if epsilon else '')
                cls.register_source(node, 'gnmath.py', 'gnmath',
                                    f'def {name}({header}):\n    return {expression}\n')
            for class_name in ('Float', 'Integer'):
                # Direct Float methods already come from gen_math_functions.
                methods = comparisons if class_name == 'Integer' else tuple(
                    row for row in comparisons if row[0] not in ('less_than', 'greater_than'))
                for name, function, _, epsilon in methods:
                    extra = ', epsilon=None' if epsilon else ''
                    forward = ', epsilon=epsilon' if epsilon else ''
                    source = (f'    def {name}(self, b=None{extra}):\n'
                              f'        from . import gnmath\n'
                              f'        return gnmath.{function}(self, b{forward})\n')
                    cls.register_source(node, class_name.lower() + '.py', class_name, source)
                for name, _, dunder, _ in comparisons:
                    cls.register_source(node, class_name.lower() + '.py', class_name,
                                        f'    def {dunder}(self, other):\n        return self.{name}(other)\n')
        finally:
            bpy.data.node_groups.remove(tree)

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
                print("DEBUG", cls.tree_type, name, identifier)
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
                    cls.register_source(getter_node, filename, destination, source, returns=getter.get('output', 'OUT') if getter else None)
                    cls.register_source(setter_node, filename, destination, setter, returns=None)
        finally:
            bpy.data.node_groups.remove(tree)

    @classmethod
    def gen_source_code(cls):
        """Collect explicitly assigned methods from source_code containers.

        Each entry associates a Blender node, a destination class and a source
        class. Copy its methods through gen_source, keeping collision checks.
        """
        additions = ()
        if not additions:
            return
        tree = bpy.data.node_groups.new(name='Specific implementations', type=cls.tree_type)
        try:
            available = utils.get_node_names(cls.tree_type)
            for node_id, class_name, code_class in additions:
                if node_id not in available:
                    continue
                try:
                    node = NodeInfo(tree, tree.nodes.new(type=node_id))
                    implementation = cls(node)
                    for method in vars(code_class).values():
                        if not inspect.isfunction(method):
                            continue
                        source = implementation.gen_source(kind='METHOD', copy_code=method)
                        cls.register_source(node, class_name.lower() + '.py', class_name, source)
                finally:
                    tree.nodes.clear()
        finally:
            bpy.data.node_groups.remove(tree)

    @classmethod
    def gen_static_code(cls):
        """Collect nd accessors and cross references for the current environment."""
        def generate(node):
            name = core_module.utils.snake_case(node.bnode.name)
            source = '\n'.join(cls(node)._gen_source(
                name, method_type='CLASS_PROPERTY' if node.is_class_property else 'CLASS_METHOD',
                return_kind='OUT' if node.is_class_property else 'NODE'))
            cls.register_source(node, 'static_nd.py', 'nd', source,
                                returns='OUT' if node.is_class_property else 'NODE')

        NodeInfo.loop_on_nodes(generate, tree_type=cls.tree_type)

    @classmethod
    def gen_nodes(cls):
        """Generate the supplied descriptions, expanding domain and type loops."""
        domains = {'POINT': 'Point', 'EDGE': 'Edge', 'FACE': 'Face', 'CORNER': 'Corner',
                   'CURVE': 'Spline', 'SPLINE': 'Spline', 'INSTANCE': 'Instance', 'LAYER': 'Layer',
                   'AUTO': 'Geometry'}

        # ---------------------------------------------------------------------------
        # Generate from a single spec dict
        # ---------------------------------------------------------------------------

        def generate_from_spec(node, spec):
            implementation = cls(node)
            if not spec.get('implement', True):
                return

            def emit(class_name, **parameters):

                if class_name is None:
                    return
                variant = implementation.copy()
                variant.parameters.update(spec.get('parameters', {}))
                for parameter, value in parameters.items():
                    variant[parameter] = value

                # classes can be a single class or a tuple of classes
                classes = class_name if isinstance(class_name, tuple) else (class_name,)

                # same for method names
                names = spec['method_name']
                names = names if isinstance(names, tuple) else (names,) * len(classes)
                methods = spec.get('is_class_method', False)
                methods = methods if isinstance(methods, tuple) else (methods,) * len(classes)

                if len(names) != len(classes) or len(methods) != len(classes):
                    raise ValueError(f"Inconsistent implementation description for {node.name!r}: {spec!r}")

                for destination, name, class_method in zip(classes, names, methods, strict=True):

                    # Core implementation

                    source = '\n'.join(variant._gen_source(
                        name, 
                        method_type='CLASS_METHOD' if class_method else 'METHOD',
                        self_socket=spec.get('self_socket'), 
                        is_jump=spec.get('jump', False),
                        auto_data_type=spec.get('data_type_input') if spec.get('auto_data_type') else None,
                        return_kind=spec.get('return_kind', 'OUT')))

                    prefix = 'dom_' if destination in core_module.constants.DOMAIN_CLASSES else ''
                    cls.register_source(
                        node, 
                        prefix + destination.lower() + '.py', 
                        destination,
                        source, 
                        returns=spec.get('return_kind', 'OUT'),
                        rules=spec['rules'])

                    # __getitem__ / __setitem__

                    as_item = config.ITEM_IMPLEMENTATION.get(node.name, None)
                    if (as_item is not None) and (not class_method):

                        return_kind = spec.get('return_kind', 'OUT')
                        return_kind = as_item.get('OUT', return_kind)

                        source = '\n'.join(variant._gen_source(
                            '__getitem__' if as_item['kind']=='get' else '__setitem__', 
                            method_type='METHOD',
                            self_socket=spec.get('self_socket'), 
                            is_jump=spec.get('jump', False),
                            auto_data_type=spec.get('data_type_input') if spec.get('auto_data_type') else None,
                            return_kind=return_kind))

                        cls.register_source(node, prefix + destination.lower() + '.py', destination,
                                            source, returns=return_kind)

            if spec.get('domain_loop'):
                class_name = spec.get('class_name')
                if class_name is not None:
                    emit(class_name)
                for domain in NodeParam.Parameter(node.bnode, 'domain').enums:
                    emit(domains[domain], domain=domain)
            elif not spec.get('data_type_loop'):
                emit(spec.get('class_name'))

            if spec.get('data_type_loop'):
                parameter = node.data_type_parameter
                for value in parameter.enums:
                    socket_type = core_module.constants.DATA_TYPE_HOMONYMS.get(value, value)
                    emit(core_module.constants.CLASS_NAMES[socket_type], **{parameter.name: value})    

        # ---------------------------------------------------------------------------
        # Spec coming from get_node_implementation can be multiple
        # ---------------------------------------------------------------------------

        def generate(node):
            implementation = cls(node)
            specs = implementation.get_node_implementation()
            if not isinstance(specs, (tuple, list)):
                specs = (specs,)
            for spec in specs:
                generate_from_spec(node, spec)

        # ---------------------------------------------------------------------------
        # Main is a loop on nodes
        # ---------------------------------------------------------------------------

        NodeInfo.loop_on_nodes(generate, tree_type=cls.tree_type)

    def __init__(self, node):
        self.node = node
        self.parameters = dict.fromkeys(node.snapshot_params())

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
        return result

    # ====================================================================================================
    # Get the standard node implementation
    # ====================================================================================================

    def get_node_implementation(self):
        """Describe the node implementation, including requested parameter loops."""
        node = self.node
        inputs = [socket for socket in node.inputs.values() if socket.enabled and socket.socket_type != 'CUSTOM']
        outputs = [socket for socket in node.outputs.values() if socket.enabled and socket.socket_type != 'CUSTOM']
        first_input = inputs[0] if inputs else None
        first_output = outputs[0] if outputs else None

        # ---------------------------------------------------------------------------
        # Hacks
        # ---------------------------------------------------------------------------

        # Node: Value to String
        # Hacks because despite its name, Value is driven by data_type parameter
        # Auto algo implements only on Float with a data_type loop which is bad

        if node.name == 'Value to String':
            category = "Hack"
            rules = ["'Value to String' hack"]
            return ({
                'category': category,
                'class_name': 'Float',
                'method_name' : 'to_string',
                'data_type': 'FLOAT',
                'rules': rules,
                }, {
                'category': category,
                'class_name': 'Integer',
                'method_name' : 'to_string',
                'data_type': 'INT',
                'rules': rules,
                }, {
                'category': category,
                'class_name': 'String',
                'method_name' : 'FromValue',
                'auto_data_type': 'Value',
                'rules': rules,
                },
            )
    
        # ---------------------------------------------------------------------------
        # Static only : no implementation
        # ---------------------------------------------------------------------------

        if node.bl_idname in config.STATIC_IMPLEMENTATION_ONLY:
            return {
                'category': "Static Only",
                'implement': False,
                'rules': ["Static only node"],
            }
        rules = [f"{node.has_domain_parameter=}",
                 f"{node.has_data_type_parameter=}",
                 f"{node.data_type_drives_inputs=}",
                 f"{node.data_type_drives_outputs=}",
                 f"{node.data_type_drives_first_input=}",
                 f"{node.has_items=}",
                 ]

        # ---------------------------------------------------------------------------
        # Texture nodes
        # ---------------------------------------------------------------------------

        if node.color_tag == 'TEXTURE':

            tokens = [token for token in node.name.split() if token != 'Texture']
            method_name = core_module.utils.CamelCase(' '.join(tokens))
            rules += ["Texture Node"]

            repl = config.SPECIAL_NODES.get(node.name, {})

            return {
                'category': "Texture",
                'class_name': repl.get('class_name', "Texture"),
                'method_name': repl.get('method_name', method_name),
                'is_class_method': repl.get('is_class_method', True),
                'rules': rules,
            }

        rules += ["Not a texture node"]

        # ---------------------------------------------------------------------------
        # data_type input
        # used for data_type_loop
        # ---------------------------------------------------------------------------

        if node.has_data_type_parameter:
            data_type_inputs = node.data_type_socket_changes['inputs']
            data_type_input = (node.max_inputs[data_type_inputs[0]]['name']
                                if data_type_inputs else None)
        else:
            data_type_input = None

        # ---------------------------------------------------------------------------
        # Input nodes
        # ---------------------------------------------------------------------------
        
        if node.color_tag == 'INPUT':
        
            class_name = None
        
            method_name = core_module.utils.snake_case(node.name)
            is_class_method = False

            category = "Input Node"
            rules += ["Input Node"]
        
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
                    
            repl = config.SPECIAL_NODES.get(node.name, {})
                        
            return {
                'category' : category,
                'class_name': repl.get('class_name', class_name),
                'method_name': repl.get('method_name', method_name),
                'is_class_method': repl.get('is_class_method', is_class_method),
                'rules': rules,
                }
            
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
                
                
            repl = config.SPECIAL_NODES.get(node.name, {})
        
            return {
                'category': category,
                'class_name': repl.get('class_name', class_name),
                'method_name': repl.get('method_name', method_name),
                'jump': repl.get('jump', jump),
                'data_type_input': repl.get('data_type_input', data_type_input),
                'auto_data_type': repl.get('auto_data_type', data_type_input is not None),
                'data_type_loop': repl.get('data_type_loop', data_type_loop),
                'domain_loop': repl.get('domain_loop', domain_loop),
                'rules': rules,
            }
        
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
        
            repl = config.SPECIAL_NODES.get(node.name, {})
        
            return {
                'category': category,
                'class_name': repl.get('class_name', class_name),
                'method_name': repl.get('method_name', method_name),
                'is_class_method': repl.get('is_class_method', True),
                'rules': rules,
            }
        rules += ["First output socket is not Geometry"]

        # ---------------------------------------------------------------------------
        # Grid node
        # ---------------------------------------------------------------------------

        if node.color_tag == 'GEOMETRY' and (node.is_grid_input or node.is_grid_output):

            category = 'Grid'
            rules += [f"Grid node {node.is_grid_input=}, {node.is_grid_output=}"]

            data_type_loop = False
            auto_data_type = False
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

            repl = config.SPECIAL_NODES.get(node.name, {})
            return {
                'category': category,
                'class_name': repl.get('class_name', class_name),
                'method_name': repl.get('method_name', method_name),
                'is_class_method': repl.get('is_class_method', is_class_method),
                'auto_data_type': repl.get('auto_data_type', auto_data_type),
                'data_type_input': repl.get('data_type_input', data_type_input),
                'data_type_loop': repl.get('data_type_loop', data_type_loop),
                'jump': repl.get('jump', jump),
                'rules': rules,
            }
        
        rules += ["Node is not grid"]

        # ---------------------------------------------------------------------------
        # First socket is driven by data_type
        # ---------------------------------------------------------------------------

        if node.data_type_drives_first_input:
            repl = config.SPECIAL_NODES.get(node.name, {})
            method_name = core_module.utils.snake_case(node.name)
            return {
                'category': 'Data type driven',
                'class_name': repl.get('class_name', None),
                'method_name': repl.get('method_name', method_name),
                'is_class_method': repl.get('is_class_method', True),
                'data_type_loop': repl.get('data_type_loop', True),
                'rules': rules + ["'data_type' parameter drives first input"],
            }

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
                    return {
                        'category': 'Manual', 'implement': False, 'rules': rules,
                    }
                class_name = first_output.class_name
                is_class_method = True
                method_name = core_module.utils.CamelCase(node.name)
            else:
                class_name = first_input.class_name
                method_name = core_module.utils.snake_case(node.name)

        repl = config.SPECIAL_NODES.get(node.name, {})

        return {
            'category': category,
            'class_name': repl.get('class_name', class_name),
            'method_name': repl.get('method_name', method_name),
            'is_class_method': repl.get('is_class_method', is_class_method),
            'data_type_input': repl.get('data_type_input', data_type_input),
            'auto_data_type': repl.get('auto_data_type', data_type_input is not None),
            'rules': rules,
        }

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

    def loop_on_parameter(self, param_name, func_name, *, kind='STATIC_METHOD',
                          self_socket=None, return_socket=None, is_jump=False,
                          last_sockets=(), **parameters):
        """Yield implementation source for each enum value in this configuration.

        func_name receives the enum identifier and returns the Python method name.
        Each implementation has its own copy of the parameter configuration.
        """
        base = self.copy()
        for name, value in parameters.items():
            base[name] = value
        base[param_name] = None
        fixed = base._fixed_parameters()
        initial = self.node.snapshot_params()
        try:
            self.node.set_params(**fixed)
            param = NodeParam.Parameter(self.node.bnode, param_name)
            if param is None or param.param_type != 'ENUM':
                raise ValueError(f"Parameter {param_name!r} must be an enum")
            values = param.enums
        finally:
            self.node.set_params(**{name: snapshot['value'] for name, snapshot in initial.items()})
        for value in values:
            implementation = base.copy()
            implementation[param_name] = value
            yield implementation.gen_source(kind=kind, name=func_name(value),
                                            self_socket=self_socket, return_socket=return_socket,
                                            is_jump=is_jump, last_sockets=last_sockets)

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
            param = NodeParam(self.node.bnode, param_name, snapshot['value'], snapshot['type'])
            prop = self.node.bnode.bl_rna.properties[param_name]
            param.enums = (tuple(item.identifier for item in prop.enum_items)
                           if snapshot['type'] in {'ENUM', 'ENUM_FLAG'} else None)
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

    # ====================================================================================================
    # Standard source generator
    # ====================================================================================================

    def _gen_source(
            self,
            method_name,
            *,
            method_type="METHOD",       # METHOD, FUNCTION, CLASS_METHOD, CLASS_PROPERTY, SETTER, GETTER
            self_socket=None,           # Name of the self socket
            is_jump=False,
            use_geo_selection=True,     # if selection exists, use geometry selection rather than argument
            return_kind='OUT',          # "NODE", class_name
            return_socket=None,         # explicit output identifier or name
            auto_data_type=None,        # socket name for auto data_type
        ):

        # ---------------------------------------------------------------------------
        # Preparation
        # ---------------------------------------------------------------------------

        margin = "" if method_type == 'FUNCTION' else "    "
        if method_type not in ('METHOD', 'SETTER', 'GETTER', 'CLASS_METHOD', 'CLASS_PROPERTY', 'FUNCTION'):
            raise ValueError(f"Unknown implementation kind: {method_type!r}")

        is_instance = method_type in ('METHOD', 'SETTER', 'GETTER')

        # Instance only flags
        if not is_instance:
            assert not is_jump, f"is_jump can't be True in '{self.name}' for {method_type=}"
            assert self_socket is None, f"No self_socket for {method_type=}"

        # ---------------------------------------------------------------------------
        # Parameters
        # ---------------------------------------------------------------------------

        # None in the implementation configuration means a free parameter.
        param_args = []
        # Parameters the value of which is defined in the current NodeImplementation config
        fixed_params = {}
        # Free parameters will be included in the arguments
        free_params = []

        parameters = self.node.snapshot_params()
        for param_name, value in self.parameters.items():
            snapshot = parameters[param_name]
            param = NodeParam(self.node.bnode, param_name, snapshot['value'], snapshot['type'])
            param.enums = snapshot['enums']

            if value is None:
                argument = Argument.from_param(param)
                argument.arg_value = repr(param.value)
                if param.param_type == 'VALUE':
                    argument.typing = type(param.value).__name__
                free_params.append(argument)
            else:
                argument = Argument.from_param(param, value=value)
                fixed_params[param_name] = value

            param_args.append(argument)

        # ---------------------------------------------------------------------------
        # Sockets arguments
        # ---------------------------------------------------------------------------

        configurations = self.node.param_filter(**{
            name: value for name, value in self._fixed_parameters().items()
            if name in self.node.enum_parameters
        })
        if not configurations:
            raise ValueError(f"No socket configuration for {self.node.name!r}: {fixed_params!r}")

        items_name = core_module.constants.ONE_ITEMS_NODES.get(self.node.bl_idname)
        items = getattr(self.node.bnode, items_name) if items_name else None
        anonymous_items = items is not None and 'name' not in {
            param.identifier for param in items.bl_rna.functions['new'].parameters if not param.is_output}
        items_start = len(self.node.bnode.inputs) - len(items) - 1 if anonymous_items else None
        dynamic = False
        selected_sockets = []
        for socket in self.node.max_inputs:
            active = tuple(key for key in configurations if key not in socket['enabled'])
            if active:
                socket_types = socket['socket_type']
                if any((socket_types[key] if isinstance(socket_types, dict) else socket_types) == 'CUSTOM'
                       for key in active):
                    dynamic = not anonymous_items
                    continue
                if anonymous_items:
                    indices = socket['index']
                    if all((indices[key] if isinstance(indices, dict) else indices) >= items_start
                           for key in active):
                        continue
                selected = socket.copy()
                selected['configurations'] = active
                selected_sockets.append(selected)

        selected_sockets.sort(key=lambda socket: (
            socket['name'] in ('Factor', 'Fac'),
            min(socket['index'][key] if isinstance(socket['index'], dict) else socket['index']
                for key in socket['configurations'])))

        # ---------------------------------------------------------------------------
        # Multi_input socket
        # ---------------------------------------------------------------------------

        has_multi_input_socket = False
        multi_input_index = -1
        for i_sock, sock in enumerate(selected_sockets):
            identifier = sock['identifier']
            if isinstance(identifier, dict):
                identifier = next(identifier[configuration] for configuration in configurations
                                    if configuration not in sock['enabled']
                                    and identifier[configuration] is not None)
            node_socket = self.node.inputs[identifier]
            if node_socket.is_multi_input:
                has_multi_input_socket = True
                multi_input_index = i_sock
                selected_sockets[i_sock]['is_multi'] = True
                break

        if has_multi_input_socket:
            identifiers = set(selected_sockets[multi_input_index]['physical_identifiers'])
            for sock in selected_sockets:
                if identifiers.intersection(sock['physical_identifiers']):
                    sock['is_multi'] = True

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
                selected_sockets[self_socket_index]['ignore'] = True
            else:
                names = []
                for i_sock, sock in enumerate(selected_sockets):
                    names.append(sock['name'])
                    if sock['name'] == self_socket:
                        sock['ignore'] = True
                        self_socket_index = i_sock
                        break

                if self_socket_index < 0:
                    raise AttributeError(f"{self_socket=} not found in {names}")

        if has_self_socket:
            receiver = selected_sockets[self_socket_index]
            identifier = receiver['identifier']
            if isinstance(identifier, dict):
                identifier = next(identifier[key] for key in receiver['configurations']
                                  if identifier[key] is not None)
            identifiers = {identifier}
            for sock in selected_sockets:
                if identifiers.intersection(sock['physical_identifiers']):
                    sock['is_self'] = True
                    sock['ignore'] = True

        # ---------------------------------------------------------------------------
        # Selection socket
        # ---------------------------------------------------------------------------

        if is_instance and use_geo_selection and len(selected_sockets) >= 2:
            if selected_sockets[1]['name'] == 'Selection':
                selected_sockets[1]['is_selection'] = True
                selected_sockets[1]['ignore'] = True
            else:
                use_geo_selection = False

        # ---------------------------------------------------------------------------
        # Build argument list
        # ---------------------------------------------------------------------------

        for sock in selected_sockets:
            classes = set()
            for configuration in configurations:
                if configuration in sock['enabled']:
                    continue
                exists = sock['exists']
                if not (exists[configuration] if isinstance(exists, dict) else exists):
                    continue
                socket_type = sock['socket_type']
                socket_type = socket_type[configuration] if isinstance(socket_type, dict) else socket_type
                name = sock['name']
                name = name[configuration] if isinstance(name, dict) else name
                classes.add(self.node.socket_class_name(socket_type, name))
            sock['typing'] = next(iter(classes)) if len(classes) == 1 else 'Socket'

        arguments = []
        for sock in selected_sockets:
            if sock.get('is_self', False):
                arguments.append({
                    'kind': 'SOCKET',
                    'is_self': True,
                    'socket_name': sock['name'],
                    'arg_name': (core_module.utils.snake_case(sock['name'])
                                 if not arguments else None),
                    'socket_index': selected_sockets.index(sock),
                })

        if has_multi_input_socket:
            name = selected_sockets[multi_input_index]['name']
            arguments.append({
                'kind': 'SOCKET',
                'is_multi': True,
                'socket_name': name,
                'arg_name': core_module.utils.snake_case(name),
                'typing': selected_sockets[multi_input_index]['typing'],
                'socket_index': multi_input_index,
            })

        for socket_index, sock in enumerate(selected_sockets):
            if sock.get('ignore', False) or sock.get('is_multi', False):
                continue
            name = sock['name']
            arguments.append({
                'kind': 'SOCKET',
                'socket_name': name,
                'arg_name': core_module.utils.snake_case(name),
                'typing': sock['typing'],
                'socket_index': socket_index,
            })

        used_argument_names = set()

        for param in free_params:
            name = param.arg_name
            arg_name = core_module.utils.snake_case(name)
            arguments.append({
                'kind': 'PARAMETER',
                'param_name': name,
                'arg_name': arg_name,
                'typing': param.typing,
                'arg_value': param.arg_value,
            })
            used_argument_names.add(arg_name)

        # ---------------------------------------------------------------------------
        # Unique argument names
        # ---------------------------------------------------------------------------

        for arg in arguments:
            if arg['kind'] == 'PARAMETER':
                break

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
                free_params = [arg for arg in free_params if arg.arg_name != computed_data_type]

        # ---------------------------------------------------------------------------
        # Sockets passed to the node (separate from method arguments)
        # ---------------------------------------------------------------------------

        node_sockets = []
        for index, sock in enumerate(selected_sockets):
            is_self = sock.get('is_self', False)
            if sock.get('is_selection', False):
                value = 'selection'
            elif sock.get('is_multi', False):
                argument = next(arg for arg in arguments
                                if arg.get('is_multi', False))
                name = argument['arg_name']
                value = f'[self, *{name}]' if is_self else f'list({name})'
            elif is_self:
                value = 'self'
            else:
                argument = next(arg for arg in arguments
                                if arg['kind'] == 'SOCKET'
                                and arg.get('socket_index') == index)
                value = argument['arg_name']
            node_sockets.append({
                'socket_name': sock['name'],
                'arg_value': value,
                'configurations': sock['configurations'],
                'is_multi': sock.get('is_multi', False),
            })

        # ---------------------------------------------------------------------------
        # Source code generation
        # ---------------------------------------------------------------------------

        yield f"{margin}# Node {self.node.name}"

        if method_type == 'CLASS_METHOD':
            yield "    @classmethod"
        elif method_type == 'CLASS_PROPERTY':
            yield "    @utils.classproperty"
        elif method_type == 'GETTER':
            yield "    @property"
        elif method_type == 'SETTER':
            yield f"    @{method_name}.setter"

        # -------------------------
        # Signature
        # -------------------------

        s = f"{margin}def {method_name}("
        sep = ", "

        if method_type in ('CLASS_METHOD', 'CLASS_PROPERTY'):
            s += 'cls'
        elif method_type != 'FUNCTION':
            s += 'self'
        else:
            sep = ""

        if anonymous_items:
            s += sep + '*values: Socket'
            sep = ', '
        if dynamic:
            s += sep + 'named_sockets=None'
            sep = ', '

        for arg in arguments:
            if arg.get('is_self', False):
                continue
            if arg.get('is_multi'):
                s += sep + f"*{arg['arg_name']}: {arg['typing']}"
            elif arg['kind'] == 'PARAMETER':
                annotation = f": {arg['typing']}" if arg['typing'] else ''
                s += sep + f"{arg['arg_name']}{annotation} = {arg['arg_value']}"
            else:
                s += sep + f"{arg['arg_name']}: {arg['typing']} = None"

            sep = ", "

        if anonymous_items and self.node.bl_idname == 'GeometryNodeIndexSwitch':
            s += sep + 'default_index: int = 0'
        if dynamic:
            s += sep + '**sockets'
        s += "):"
        yield s

        # -------------------------
        # Docstring
        # -------------------------

        doc_args = []
        for arg in arguments:
            if arg.get('is_self', False):
                continue
            if arg['kind'] == 'PARAMETER':
                doc_args.append(next(param for param in free_params
                                     if param.arg_name == arg['param_name']))
            else:
                doc_args.append(Argument(
                    arg_type='SOCKET', arg_name=arg['arg_name'],
                    comment=(f"{arg['arg_name']} : {arg['typing']}, optional\n"
                             f"    socket '{arg['socket_name']}'\n"),
                ))

        derived_parameters = None
        if computed_data_type is not None:
            derived_parameters = {
                computed_data_type: f"Inferred from socket '{auto_data_type}' ({data_type_value})."
            }
        docstring = self.gen_docstring(
            doc_args, is_jump=is_jump if is_instance else None,
            self_socket=selected_sockets[self_socket_index]['name'] if has_self_socket else None,
            returns={'OUT': 'Socket', 'NODE': 'Node', 'cls': 'cls'}.get(return_kind, return_kind),
            return_socket='OUT' if return_kind != 'NODE' else None,
            derived_parameters=derived_parameters, indent=0,
        )
        for line in docstring.splitlines():
            yield f"{margin}    {line}"

        # -------------------------
        # Auto data_type
        # -------------------------

        margin += "    "
        if computed_data_type is not None:
            yield (f"{margin}{computed_data_type} = SocketType.get_data_type_for_node("
                   f"{data_type_value}, {self.node.bl_idname!r}, {computed_data_type!r})")

        # -------------------------
        # Selection socket
        # -------------------------

        if any(sock.get('is_selection', False) for sock in selected_sockets):
            yield f"{margin}selection = self.get_selection()"

        # -------------------------
        # Node creation
        # -------------------------

        parameter_values = {arg.arg_name: arg.node_value for arg in param_args}
        fixed_values = self._fixed_parameters()
        parameter_values.update({name: repr(value) for name, value in fixed_values.items()})
        if computed_data_type is not None:
            parameter_values[computed_data_type] = computed_data_type

        # Prepare the actual socket names and values for each retained configuration.
        named_values = {}
        positional_values = {}
        for configuration in configurations:
            active = [(sock, value) for sock, value in zip(selected_sockets, node_sockets)
                      if configuration in value['configurations']]
            active.sort(key=lambda pair: pair[0]['index'][configuration]
                        if isinstance(pair[0]['index'], dict) else pair[0]['index'])
            used_names = set(self.parameters)
            named = []
            positional = []
            for sock, value in active:
                base = sock['name']
                name = base
                suffix = 0
                while core_module.utils.snake_case(name) in used_names:
                    suffix += 1
                    name = f'{base}_{suffix}'
                used_names.add(core_module.utils.snake_case(name))
                if value['is_multi']:
                    positional.append(f"*{value['arg_value']}")
                else:
                    named.append(f"{name!r}: {value['arg_value']}")
            named_values[configuration] = '{' + ', '.join(named) + '}'
            positional_values[configuration] = '[' + ', '.join(positional) + ']'

        variable_sockets = (len(set(named_values.values())) > 1
                            or len(set(positional_values.values())) > 1)
        if variable_sockets:
            configuration_values = []
            for name in self.node.driving_parameters:
                expression = parameter_values[name]
                prop = self.node.bnode.bl_rna.properties[name]
                if prop.type == 'ENUM' and name not in fixed_values:
                    names = {item.identifier.lower(): item.identifier for item in prop.enum_items}
                    names.update({item.name.lower(): item.identifier for item in prop.enum_items})
                    if prop.is_enum_flag:
                        expression = f"frozenset({names!r}.get(_value.lower(), _value) for _value in {expression})"
                    else:
                        expression = f"{names!r}.get({expression}.lower(), {expression})"
                elif prop.type == 'ENUM' and prop.is_enum_flag:
                    expression = repr(frozenset(fixed_values[name]))
                configuration_values.append(expression)
            yield f"{margin}_configuration = (" + ', '.join(configuration_values) + ',)'
            named_table = ', '.join(f'{key!r}: {value}' for key, value in named_values.items())
            positional_table = ', '.join(f'{key!r}: {value}' for key, value in positional_values.items())
            yield f"{margin}_node_sockets = {{{named_table}}}[_configuration]"
            yield f"{margin}_node_args = {{{positional_table}}}[_configuration]"
            node_args = [repr(self.node.name), '*_node_args', 'named_sockets=_node_sockets']
        else:
            node_args = [repr(self.node.name)]
            positional = next(iter(positional_values.values()))
            if positional != '[]':
                node_args.append('*' + positional)
            node_args.append('named_sockets=' + next(iter(named_values.values())))

        if anonymous_items:
            node_args.insert(1, '*values')
        if dynamic:
            socket_expression = node_args.pop()
            yield f"{margin}_named_sockets = {socket_expression.removeprefix('named_sockets=')}"
            yield f"{margin}_named_sockets.update({{name: value for name, value in (named_sockets or {{}}).items() if value is not None}})"
            node_args.append('named_sockets=_named_sockets')

        parameter_order = self.node.enum_params_order + tuple(
            name for name in parameter_values if name not in self.node.enum_params_order
        )
        node_args.extend(f"{name}={parameter_values[name]}" for name in parameter_order)
        if dynamic:
            node_args.append('**sockets')
        yield f"{margin}node = Node({', '.join(node_args)})"
        if anonymous_items and self.node.bl_idname == 'GeometryNodeIndexSwitch':
            yield f"{margin}_selector = node._bnode.inputs['Index']"
            yield f"{margin}_selector.default_value = default_index"
            yield f"{margin}_interface = node._get_interface_socket(_selector)"
            yield f"{margin}if _interface is not None:"
            yield f"{margin}    _interface.default_value = default_index"

        # -------------------------
        # Return
        # -------------------------

        if method_type != 'SETTER':
            if return_socket is not None:
                yield f"{margin}return node[{return_socket!r}]"

            elif return_kind == 'OUT':
                if is_jump:
                    yield f"{margin}self._jump(node._out)"
                    yield f"{margin}return node._second_out(self)"
                else:
                    yield f"{margin}return node._out"

            elif return_kind == 'cls':
                yield f"{margin}return cls(node._out)"

            elif return_kind == 'NODE':
                yield f"{margin}return node"

            else:
                yield f"{margin}return {return_kind}(node._out)"

        



        






        


        












        
