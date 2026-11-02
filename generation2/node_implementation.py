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

                # Module gnmath
                cls.gen_gnmath()

                # Geometry domain inputs
                cls.gen_input_nodes()

                # Default node implementations
                cls.gen_default_implementation()

                # Complementary implementations with a fixed domain
                if selected_type == 'GeometryNodeTree':
                    cls.gen_domain_implementations()

                # Specific source-code additions
                cls.gen_source_code()

                # Static node access for this environment
                cls.gen_static_nodes()
        finally:
            cls.tree_type = previous_type
        if write:
            cls.write_files(use_core_new=use_core_new)
        environments = ', '.join(ENVIRONMENTS[selected_type] for selected_type in selected)
        action = 'Generation completed' if write else 'Source collection completed (no files written)'
        print(f'\n{action}: {environments}.')

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

    @classmethod
    def register_source(cls, node, filename, destination, source, returns='OUT'):
        """Register source and its cross reference, rejecting duplicate names."""
        function = ast.parse(textwrap.dedent(source)).body[0]
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

                def describe(identifier, ref):
                    kind = 'property' if ref['is_get'] else 'classmethod' if ref['is_classmethod'] else 'method'
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
        files.setdefault(filename, []).append(source)
        cross_refs.setdefault(node.bnode.bl_idname, {}).setdefault(destination, []).append(reference)

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
            ('MINIMUM', 'min'), ('MAXIMUM', 'max'), ('LESS_THAN', 'mless_than'),
            ('GREATER_THAN', 'mgreater_than'), ('SIGN', 'sign'), ('COMPARE', 'compare'),
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
                implementation = base.copy()
                implementation['operation'] = operation
                cls.register_source(node, 'gnmath.py', 'gnmath',
                                    implementation.gen_source(kind='FUNCTION', name=name, return_socket='OUT'))
                # Float.compare is handwritten in each environment socket class.
                if operation != 'COMPARE':
                    cls.register_source(node, 'float.py', 'Float',
                                        implementation.gen_source(kind='METHOD', name=name,
                                                                  self_socket='Value', return_socket='OUT'))

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
                                    implementation.gen_source(kind='FUNCTION', name=function_name,
                                                              return_socket='OUT'))
                cls.register_source(node, 'integer.py', 'Integer',
                                    implementation.gen_source(kind='METHOD', name=method_name,
                                                              self_socket='Value', return_socket='OUT'))

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
                                    implementation.gen_source(kind='FUNCTION', name=name, return_socket='OUT'))
                cls.register_source(node, 'boolean.py', 'Boolean',
                                    implementation.gen_source(kind='METHOD', name=name,
                                                              self_socket='Boolean', return_socket='OUT'))

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

    @classmethod
    def gen_vector_math_functions(cls):
        """Collect Vector Math functions, Vector methods and operators.

        Scalar outputs are determined by gen_source for each operation.
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
                                    implementation.gen_source(kind='FUNCTION', name=function_name,
                                                              return_socket='OUT'))
                cls.register_source(node, 'vector.py', 'Vector',
                                    implementation.gen_source(kind='METHOD', name=method_name,
                                                              self_socket='Vector', return_socket='OUT'))

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
                                    implementation.gen_source(kind='FUNCTION', name=name, return_socket='OUT'))
                cls.register_source(node, 'integer.py', 'Integer',
                                    implementation.gen_source(kind='METHOD', name=name,
                                                              self_socket='A', return_socket='OUT'))

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
                ('mnot_equal', 'subtract(1, compare(a, b, epsilon=epsilon))', True),
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

    @classmethod
    def _gen_shader_compare_functions(cls):
        """Generate scalar shader comparisons using Math only."""
        comparisons = (
            ('less_than', 'mless_than', '__lt__', False),
            ('less_equal', 'mless_equal', '__le__', False),
            ('greater_than', 'mgreater_than', '__gt__', False),
            ('greater_equal', 'mgreater_equal', '__ge__', False),
            ('equal', 'compare', '__eq__', True),
            ('not_equal', 'mnot_equal', '__ne__', True),
        )
        tree = bpy.data.node_groups.new(name='Shader comparisons', type='ShaderNodeTree')
        try:
            node = NodeInfo(tree, tree.nodes.new(type='ShaderNodeMath'))
            for name, expression, epsilon in (
                ('mless_equal', 'subtract(1, mgreater_than(a, b))', False),
                ('mgreater_equal', 'subtract(1, mless_than(a, b))', False),
                ('mnot_equal', 'subtract(1, compare(a, b, epsilon=epsilon))', True),
            ):
                header = 'a=None, b=None' + (', epsilon=None' if epsilon else '')
                cls.register_source(node, 'gnmath.py', 'gnmath',
                                    f'def {name}({header}):\n    return {expression}\n')
            for name, function, dunder, epsilon in comparisons:
                extra = ', epsilon=None' if epsilon else ''
                forward = ', epsilon=epsilon' if epsilon else ''
                cls.register_source(node, 'gnmath.py', 'gnmath',
                                    f'def {name}(a=None, b=None{extra}):\n    return {function}(a, b{forward})\n')
                for class_name in ('Float', 'Integer'):
                    source = (f'    def {name}(self, b=None{extra}):\n'
                              f'        from . import gnmath\n'
                              f'        return gnmath.{function}(self, b{forward})\n')
                    cls.register_source(node, class_name.lower() + '.py', class_name, source)
                    cls.register_source(node, class_name.lower() + '.py', class_name,
                                        f'    def {dunder}(self, other):\n        return self.{name}(other)\n')
        finally:
            bpy.data.node_groups.remove(tree)

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

    @classmethod
    def gen_input_nodes(cls):
        """Collect INPUT implementations inferred by NodeInfo plus overrides.

        NodeInfo.input_implementation documents the domain/name rules.
        INPUT_IMPLEMENTATIONS overrides individual fields or covers unmatched
        nodes. Each class method returns the Node and keeps its input arguments.
        create_properties (default True) creates snake_case output properties
        only without active inputs or free parameters. property_names renames
        selected Python names; None excludes a property. Other properties keep
        their generated names.

        If an inferred method name equals an automatic property name, keep the
        property: Face Area produces Face.area, not a second area() method.
        Explicit names must be distinct; collisions raise an error. Properties
        are never inferred for nodes needing arguments, such as Corners of Edge.
        No files are written. Only INPUT nodes undergo NodeInfo introspection.
        """
        if cls.tree_type != 'GeometryNodeTree':
            return
        seen = set()

        def generate(bnode):
            identifier = bnode.bl_idname
            if identifier in config.INPUT_IMPLEMENTATIONS:
                seen.add(identifier)
                if bnode.color_tag != 'INPUT':
                    raise ValueError(f'{bnode.name} is not an INPUT node')
            if identifier in config.DEPRECATED_NODES or bnode.color_tag != 'INPUT':
                return
            node = NodeInfo(bnode.id_data, bnode)
            specification = node.input_implementation()
            if specification is not None:
                cls._gen_input_implementation(node, specification)

        utils.loop_on_nodes(generate, tree_type=cls.tree_type)
        missing = config.INPUT_IMPLEMENTATIONS.keys() - seen
        if missing:
            raise ValueError(f'Configured INPUT nodes not found: {sorted(missing)}')

    @classmethod
    def _gen_input_implementation(cls, node, specification):
        """Generate one resolved INPUT proposal; shared by rules and overrides."""
        implementation = cls(node)
        for name, value in specification.get('parameters', {}).items():
            implementation[name] = value
        class_name = specification['class_name']
        prefix = 'dom_' if class_name in core_module.constants.DOMAIN_CLASSES else ''
        filename = prefix + class_name.lower() + '.py'
        properties = {}
        can_create = (specification.get('create_properties', True)
                      and all(value is not None for value in implementation.parameters.values()))
        if can_create:
            fixed = implementation._fixed_parameters()
            configurations = node.param_filter(**{
                name: value for name, value in fixed.items() if name in node.enum_parameters
            })
            has_inputs = any(key not in socket['enabled'] and (
                socket['exists'][key] if isinstance(socket['exists'], dict) else socket['exists'])
                for key in configurations for socket in node.max_inputs)
            if not has_inputs:
                identifiers = set()
                for key in configurations:
                    for identifier, socket in node.outputs.items():
                        state = socket.dependencies[key]
                        if (not state['exists'] or not state['enabled']
                                or state['socket_type'] == 'CUSTOM' or identifier in identifiers):
                            continue
                        base = core_module.utils.snake_case(state['name'])
                        property_name, index = base, 0
                        while property_name in properties:
                            index += 1
                            property_name = f'{base}_{index}'
                        properties[property_name] = identifier
                        identifiers.add(identifier)
                renames = specification.get('property_names', {})
                unknown = renames.keys() - properties.keys()
                if unknown:
                    raise ValueError(f"Unknown properties for {node.bnode.name}: {sorted(unknown)}")
                renamed = {}
                for name, identifier in properties.items():
                    name = renames.get(name, name)
                    if name is None:
                        continue
                    if name in renamed:
                        raise ValueError(f'Duplicate INPUT property: {class_name}.{name}')
                    renamed[name] = identifier
                properties = renamed
        method_name = specification.get('name')
        if method_name in properties:
            explicit = config.INPUT_IMPLEMENTATIONS.get(node.bnode.bl_idname, {})
            if 'name' in explicit:
                raise ValueError(f'INPUT method/property name collision: {class_name}.{method_name}')
            method_name = None
        if method_name is not None:
            source = implementation.gen_source(kind='STATIC_METHOD', name=method_name, return_socket='NODE')
            cls.register_source(node, filename, class_name, source, returns='NODE')
        for property_name, socket_name in properties.items():
            source = implementation.gen_source(kind='GETTER', name=property_name, return_socket=socket_name)
            cls.register_source(node, filename, class_name, source, returns=socket_name)

    @classmethod
    def gen_default_implementation(cls):
        """Collect default proposals, enum variants and explicit additions.

        Visit the selected tree type; shared nodes are generated in each environment.
        NONE proposals stay available through nd. Naming collisions are
        rejected by register_source and must be resolved in config.
        """
        seen = set()

        def generate(node):
            identifier = node.bnode.bl_idname
            if identifier in seen:
                return
            seen.add(identifier)
            cls._gen_default_implementation(node, node.default_implementation())

        NodeInfo.loop_on_nodes(generate, tree_type=cls.tree_type)

    @classmethod
    def _gen_default_implementation(cls, node, proposal, **parameters):
        """Emit a default proposal, shared by ordinary and fixed-domain passes."""
        if 'implementations' in proposal:
            for variant in proposal['implementations']:
                cls._gen_default_implementation(node, variant, **parameters)
        elif proposal['kind'] != 'NONE':
            implementation = cls(node)
            for name, value in {**parameters, **proposal.get('parameters', {})}.items():
                implementation[name] = value
            class_name = proposal['class_name']
            kind = proposal['kind']
            data_type_socket = node.inferred_data_type_socket if kind == 'METHOD' else None
            source = implementation.gen_source(
                kind='STATIC_METHOD' if kind == 'CONSTRUCTOR' else kind,
                name=proposal['name'], self_socket=proposal['self_socket'],
                return_socket=proposal['return_socket'] or 'NODE',
                is_jump=proposal['is_jump'], data_type_socket=data_type_socket)
            prefix = 'dom_' if class_name in core_module.constants.DOMAIN_CLASSES else ''
            cls.register_source(node, prefix + class_name.lower() + '.py', class_name,
                                source, returns=proposal['return_socket'] or 'NODE')

            # Conversion proposals also expose the source-class method
            # shown in NodeInfo's signature preview.
            if proposal['is_convert_to'] and kind == 'CONSTRUCTOR':
                source_class, _ = node.convert_to_classes
                classes = set(core_module.constants.CLASS_NAMES.values()) | set(core_module.constants.GEOMETRY_CLASSES)
                if source_class in classes:
                    for socket in node.inputs.values():
                        if any(state['exists'] and state['enabled'] and
                               (node.geometry_class(state['name']) if state['socket_type'] == 'GEOMETRY'
                                else core_module.constants.CLASS_NAMES.get(state['socket_type'])) == source_class
                               for state in socket.dependencies.values()):
                            method = dict(proposal, kind='METHOD', class_name=source_class,
                                          name=node.default_name(source_class, kind='METHOD'),
                                          self_socket=socket.identifier, is_convert_to=False)
                            cls._gen_default_implementation(node, method, **parameters)
                            break
        for addition in proposal.get('additional_implementations', ()):
            cls._gen_default_implementation(node, addition, **parameters)

    @classmethod
    def gen_domain_implementations(cls):
        """Generate default code for each accepted domain, without data types.

        Fixed-domain variants use the same emitter, documentation and cross
        references as the default implementations. NONE proposals (including
        zones and Viewer) remain excluded.
        """
        def generate(node):
            if not node.has_domain_parameter or node.has_data_type_parameter:
                return
            if node.bnode.bl_idname in config.NO_DEFAULT_IMPLEMENTATION:
                return
            for domain in NodeParam.Parameter(node.bnode, 'domain').enums:
                proposal = node.default_implementation(domain=domain)
                cls._gen_default_implementation(node, proposal, domain=domain)

        NodeInfo.loop_on_nodes(generate, tree_type='GeometryNodeTree')

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
    def gen_static_nodes(cls):
        """Collect nd accessors and cross references for the current environment."""
        def generate(node):
            name = core_module.utils.snake_case(node.bnode.name)
            source = cls(node).gen_source(kind='STATIC_METHOD', name=name)
            cls.register_source(node, 'static_nd.py', 'nd', source,
                                returns='OUT' if node.is_class_property else 'NODE')

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

        exposed = [argument for argument in arguments if argument.is_argument and not argument.is_self]
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
                   data_type_socket=None):
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
        """
        if copy_code is not None:
            source = textwrap.dedent(inspect.getsource(copy_code))
            return source if kind == 'FUNCTION' else textwrap.indent(source, '    ')

        if kind not in {'STATIC_METHOD', 'FUNCTION', 'METHOD', 'SETTER', 'GETTER'}:
            raise ValueError(f"Unknown implementation kind: {kind!r}")
        auto_property = kind == 'STATIC_METHOD' and self.node.is_class_property and return_socket != 'NODE'
        class_property = auto_property or (kind == 'GETTER' and self_socket is None)
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
                    dynamic = True
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

        socket_args.sort(key=lambda item: candidates[item[1]]['index'])

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
                argument.is_argument = False
                argument.node_value = '[self]' if argument.multiple == 'ARGS' else 'self'

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

        exposed_sockets = [(a, name) for a, name in socket_args if a.is_argument]

        def socket_order(item):
            argument, socket_name = item
            names = (socket_name, argument.identifier, candidates[socket_name]['ui_name'])
            return next((index for index, name in enumerate(last_sockets) if name in names), -1)

        if last_sockets:
            exposed_sockets.sort(key=socket_order)
        arguments = [a for a, _ in exposed_sockets] + [a for a in param_args if a.is_argument]
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

        # Set driving parameters before parameters whose enum choices depend on them.
        pending = {a.arg_name: a for a in param_args}
        ordered = []
        while pending:
            ready = [p for p in pending if not (self.node.param_dependencies.get(p, set()) & pending.keys())]
            if not ready:
                raise ValueError(f"Cyclic parameter dependencies in node {node_name!r}")
            for p in ready:
                ordered.append(pending.pop(p))
        params = ', '.join(f"{a.arg_name}={a.node_value}" for a in ordered)
        values = ', '.join(f"{socket_name!r}: {argument.node_value}"
                           for argument, socket_name in socket_args)
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
        source += f"        _node = Node({node_name!r}, named_sockets=_named_sockets"
        if params:
            source += f", {params}"
        if dynamic:
            source += ', **sockets'
        source += ')\n'
        result = '_node' if return_socket is None else '_node._out' if return_socket == 'OUT' else f'_node[{return_socket!r}]'
        if is_jump:
            source += f'        self._jump({result})\n'
            result = 'self._domain_to_geometry'
        if kind != 'SETTER':
            source += f'        return {result}\n'
        return textwrap.dedent(source) if kind == 'FUNCTION' else source
