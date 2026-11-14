"""First checks without Blender: python3 -B generation2/tests/test_gen_node_call.py."""
import ast
import inspect
from pathlib import Path
import runpy
from types import MethodType, SimpleNamespace
import unittest
from typing import Literal

ROOT = Path(__file__).resolve().parents[1]
# Load only the generator under test; the full module imports Blender.
tree = ast.parse((ROOT / 'node_implementation.py').read_text())
cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == 'NodeImplementation')
method = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == 'gen_node_call')
method.body = [node for node in method.body if not isinstance(node, ast.ImportFrom)]
param_tree = ast.parse((ROOT / 'node_param.py').read_text())
param_tree.body = [node for node in param_tree.body if not isinstance(node, ast.Import)]
param_namespace = {}
exec(compile(param_tree, '<node_param>', 'exec'), param_namespace)
NodeCall = runpy.run_path(str(ROOT / 'node_call.py'))['NodeCall']
TypeAliases = runpy.run_path(str(ROOT / 'typealiases.py'))['TypeAliases']
attach_arguments = runpy.run_path(str(ROOT / 'tests/argument_fixtures.py'))['attach_arguments']
namespace = dict(
    NodeCall=NodeCall,
    TAB="    ",
    R0=runpy.run_path(str(ROOT / "sourcewriter.py"))["R0"],
    NodeParam=param_namespace['NodeParam'],
    SourceWriter=runpy.run_path(str(ROOT / 'sourcewriter.py'))['SourceWriter'],
    core_module=SimpleNamespace(utils=SimpleNamespace(snake_case=lambda s: s.lower().replace(' ', '_'))),
)
exec(compile(ast.Module(body=[method], type_ignores=[]), '<generator>', 'exec'), namespace)


def socket(name, identifier=None, names=None, multi=False):
    return SimpleNamespace(names=set(names or [name]), identifier=identifier or name,
                           enabled=True, class_name='object', socket_type='BOOLEAN' if name == 'Selection' else 'GEOMETRY' if name == 'Geometry' else 'VALUE',
                           is_multi=multi, socket_name=name, group_name=None)


class GenNodeCallTest(unittest.TestCase):
    def generate(self, sockets, parameters=None, type_parameter=None, snapshots=None, aliases=None, items_named=None, **options):
        parameters = parameters or {}
        node = SimpleNamespace(name="Test's Node", config_order=['mode'],
                               default_params={'mode': {'value': 'DEFAULT'}},
                               get_possible_sockets=lambda **kw: sockets)
        node.has_items = items_named is not None
        node.items_with_name = items_named
        node.bnode = None
        node.bl_idname = 'TestNode'
        node.data_type_parameter = None
        if type_parameter is not None:
            node.data_type_parameter = SimpleNamespace(name=type_parameter)
            node.config_order.append(type_parameter)
            node.default_params[type_parameter] = {'value': 'FLOAT'}
        for snapshot in node.default_params.values():
            snapshot.update(type='VALUE', enums=None)
        if snapshots:
            node.default_params.update(snapshots)
            node.config_order = list(node.default_params)
        attach_arguments(node)
        implementation = SimpleNamespace(node=node, parameters={'mode': None} | parameters,
                                         type_aliases=aliases)
        source = namespace['gen_node_call'](implementation, NodeCall(method_type=options.get('method_type', 'METHOD'),
            method_name='build', **{key: value for key, value in options.items() if key != 'method_type'}))
        calls = []
        def Node(*args, **kwargs):
            calls.append((args, kwargs))
            return SimpleNamespace(_out='result')
        def infer(value, node_id, parameter):
            return (value, node_id, parameter)
        env = dict(Node=Node, Socket=object, Literal=Literal, SocketType=SimpleNamespace(get_data_type_for_node=infer))
        if aliases is not None:
            exec(aliases.source, env)
        if options.get('method_type') == 'FUNCTION':
            exec(source, env)
            fn = env['build']
        else:
            exec('class Example:\n' + source, env)
            fn = env['Example'].build
        return fn, calls, source

    def test_instance_and_free_parameter(self):
        fn, calls, _ = self.generate([socket('Value'), socket('Other')], self_socket='Value')
        receiver = object()
        self.assertEqual(fn(receiver, other=7, mode='CUSTOM'), 'result')
        self.assertEqual(calls, [(("Test's Node",), dict(named_sockets={'ID_Value': receiver, 'ID_Other': 7}, mode='CUSTOM'))])

    def test_fixed_values(self):
        fn, calls, _ = self.generate([socket('Text')], {'mode': 'FIXED'},
                                     method_type='FUNCTION', fixed_sockets={'Text': "a'b"})
        fn()
        self.assertEqual(calls[0][1], dict(named_sockets={'Text': "a'b"}, mode='FIXED'))

    def test_selection_and_opt_out(self):
        receiver = SimpleNamespace(get_selection=lambda: 'selected')
        for enabled in (True, False):
            fn, calls, _ = self.generate([socket('Geometry'), socket('Selection')], use_geo_selection=enabled, self_socket='Geometry')
            fn(receiver, **({} if enabled else {'selection': False}))
            self.assertEqual(calls[0][1]['named_sockets']['Selection' if enabled else 'ID_Selection'], 'selected' if enabled else False)

    def test_aliases_and_explicit_receiver(self):
        fn, calls, _ = self.generate([socket('Geometry'), socket('A', 'physical', ['A', 'B'])], self_socket='Geometry')
        receiver = object()
        fn(receiver, b=0)
        self.assertEqual(calls[0][1]['named_sockets'], {'ID_Geometry': receiver, 'ID_physical': 0})

    def test_multi_input_receiver(self):
        fn, calls, _ = self.generate([socket('Values', multi=True)], self_socket='Values')
        receiver = object()
        fn(receiver, 2, 3)
        self.assertEqual(calls[0][0], ("Test's Node", receiver, 2, 3))

    def test_auto_type_from_receiver(self):
        for parameter in ('data_type', 'input_type'):
            with self.subTest(parameter=parameter):
                fn, calls, _ = self.generate([socket('Value')],
                    type_parameter=parameter, auto_data_type='Value', self_socket='Value')
                receiver = object()
                fn(receiver)
                self.assertNotIn(parameter, inspect.signature(fn).parameters)
                self.assertEqual(calls[0][1][parameter], (receiver, 'TestNode', parameter))

    def test_auto_type_uses_renamed_argument(self):
        fn, calls, _ = self.generate([socket('Geometry'), socket('Mode')],
            type_parameter='data_type', auto_data_type='Mode', self_socket='Geometry')
        fn(object(), mode_1=7)
        self.assertEqual(calls[0][1]['data_type'], (7, 'TestNode', 'data_type'))

    def test_fixed_type_skips_inference_and_socket_lookup(self):
        fn, calls, _ = self.generate([socket('Value')], {'data_type': 'INT'},
            type_parameter='data_type', auto_data_type='Unused', self_socket='Value')
        fn(object())
        self.assertEqual(calls[0][1]['data_type'], 'INT')

    def test_auto_type_without_instance(self):
        for method_type in ('FUNCTION', 'STATIC_METHOD', 'CLASS_METHOD'):
            with self.subTest(method_type=method_type):
                fn, calls, _ = self.generate([socket('Value')],
                    type_parameter='data_type', auto_data_type='Value', method_type=method_type)
                fn(value=7)
                self.assertNotIn('data_type', inspect.signature(fn).parameters)
                self.assertEqual(calls[0][1]['data_type'], (7, 'TestNode', 'data_type'))

    def test_invalid_auto_type_configuration(self):
        with self.assertRaisesRegex(ValueError, 'no type parameter'):
            self.generate([socket('Value')], auto_data_type='Value', self_socket='Value')
        with self.assertRaisesRegex(ValueError, 'Missing'):
            self.generate([socket('Value')], type_parameter='data_type', auto_data_type='Missing', self_socket='Value')

    def test_socket_typing_falls_back_to_socket(self):
        for typing in (None, ''):
            for multi in (False, True):
                with self.subTest(typing=typing, multi=multi):
                    value = socket('Value', multi=multi)
                    value.class_name = typing
                    fn, calls, source = self.generate([value], method_type='FUNCTION')
                    self.assertIs(inspect.signature(fn).parameters['value'].annotation, object)
                    self.assertIn('value: Socket', source)
                    fn(7) if multi else fn(value=7)
                    self.assertEqual(calls[0][0] if multi else calls[0][1]['named_sockets'],
                                     ("Test's Node", 7) if multi else {'ID_Value': 7})


    def test_parameter_typing_and_enum_aliases(self):
        aliases = TypeAliases()
        snapshots = {
            'mode': {'type': 'ENUM', 'value': 'A', 'enums': ('A', 'B')},
            'flags': {'type': 'ENUM_FLAG', 'value': set(), 'enums': ('X', 'Y')},
            'unknown': {'type': 'VALUE', 'value': None, 'enums': None},
        }
        for registry in (None, aliases):
            fn, calls, source = self.generate([socket('Value')],
                snapshots=snapshots, aliases=registry, self_socket='Value')
            doc = inspect.getdoc(fn)
            self.assertIn("mode : {'A', 'B'}, optional\n    Node parameter 'mode' (default: 'A')", doc)
            self.assertIn("flags : set[{'X', 'Y'}], optional", doc)
            self.assertIn("unknown : object, optional", doc)
            signature = inspect.signature(fn)
            self.assertEqual(signature.parameters['mode'].annotation, Literal['A', 'B'])
            self.assertEqual(signature.parameters['flags'].annotation, set[Literal['X', 'Y']])
            self.assertEqual(signature.parameters['unknown'].annotation, inspect.Parameter.empty)
            fn(object(), flags={'Y'})
            self.assertEqual(calls[0][1]['flags'], {'Y'})
            self.assertIn("set[Literal['X', 'Y']]", source)
        self.assertEqual(len(aliases), 1)

    def test_socket_documentation_uses_final_names(self):
        fn, _, _ = self.generate(
            [socket('Geometry'), socket('Mode'), socket('A', 'physical', ['A', 'B'])],
            self_socket='Geometry')
        doc = inspect.getdoc(fn)
        self.assertIn("mode_1 : object, optional\n    Socket 'Mode' (default: None)", doc)
        self.assertIn("b : object, optional\n    Socket 'B', identifier 'physical'", doc)
        fn, _, _ = self.generate([socket('Values', multi=True)], self_socket='Values')
        self.assertIn("values : object\n    Socket 'Values' (multiple values)",
                      inspect.getdoc(fn))


    def test_return_documentation(self):
        cases = [
            ({'return_socket': 'Result'}, "Socket 'Result'"),
            ({'return_kind': 'NODE'}, 'Node'),
            ({'return_kind': 'Float'}, 'Default output socket wrapped in Float.'),
            ({'return_kind': 'cls', 'method_type': 'CLASS_METHOD'},
             'Default output socket wrapped in the calling class.'),
            ({'is_jump': True, 'self_socket': 'Value', 'method_type': 'METHOD'},
             'Second output socket, or self if there is no second output.'),
        ]
        for options, expected in cases:
            with self.subTest(options=options):
                fn, _, _ = self.generate([socket('Value')],
                    **({'method_type': 'FUNCTION'} | options))
                doc = inspect.getdoc(fn)
                self.assertIn(expected, doc)
                returns = doc.split('Returns\n-------\n', 1)[1].splitlines()
                self.assertIn(returns[0], ('Socket', 'Node', 'Float', 'Self'))
                if len(returns) > 1:
                    self.assertTrue(returns[1].startswith('    '))


    def test_grouped_socket_uses_group_name(self):
        for receiver in (False, True):
            with self.subTest(receiver=receiver):
                value = socket('Physical', identifier='physical_id')
                value.group_name = 'Value'
                options = {'self_socket': 'Physical'} if receiver else {'method_type': 'FUNCTION'}
                fn, calls, _ = self.generate([value], **options)
                obj = object()
                fn(obj) if receiver else fn(physical=obj)
                self.assertEqual(calls[0][1]['named_sockets'], {'Value': obj})


    def test_same_named_sockets_use_distinct_identifiers(self):
        fn, calls, _ = self.generate(
            [socket('Value', 'first'), socket('Value', 'second')],
            method_type='FUNCTION')
        fn(value=1, value_1=2)
        self.assertEqual(calls[0][1]['named_sockets'], {'ID_first': 1, 'ID_second': 2})


    def test_boolean_parameter_typing(self):
        for value in (False, True):
            with self.subTest(value=value):
                fn, calls, _ = self.generate([], method_type='FUNCTION', snapshots={
                    'enabled': {'type': 'VALUE', 'value': value, 'enums': None},
                    'count': {'type': 'VALUE', 'value': 1, 'enums': None},
                })
                signature = inspect.signature(fn)
                self.assertIs(signature.parameters['enabled'].annotation, bool)
                self.assertIs(signature.parameters['count'].annotation, int)
                fn()
                self.assertIs(calls[0][1]['enabled'], value)


    def test_spec_fixed_parameters_without_mutation(self):
        # Also exercise the new interface directly with fixed values on the spec.
        seen = []
        node = SimpleNamespace(name='Test', config_order=['mode'], default_params={'mode': {'value': 'A', 'type': 'ENUM', 'enums': ('A', 'B')}}, has_items=False,
                               get_possible_sockets=lambda **kw: seen.append(kw) or [])
        attach_arguments(node)
        impl = SimpleNamespace(node=node, parameters={'mode': None}, type_aliases=None)
        spec = NodeCall.function('build', parameters={'mode': 'B'})
        source = namespace['gen_node_call'](impl, spec)
        env = {'Node': lambda *a, **kw: SimpleNamespace(_out=kw)}
        exec(source, env)
        self.assertEqual(env['build']()['mode'], 'B')
        self.assertEqual(seen, [{'mode': 'B'}])
        self.assertEqual(impl.parameters, {'mode': None})
        self.assertEqual(spec.parameters, {'mode': 'B'})


    def test_static_accessors_use_impl_spec(self):
        registry_tree = ast.parse((ROOT / 'tree_class.py').read_text())
        registry = next(n for n in registry_tree.body if isinstance(n, ast.ClassDef) and n.name == 'TreeClass')
        static_method = next(n for n in registry.body
                             if isinstance(n, ast.FunctionDef) and n.name == 'gen_static_code')
        accessor_class = ast.ClassDef(name='Accessors', bases=[], keywords=[],
                                     body=[static_method], decorator_list=[])
        module = ast.fix_missing_locations(ast.Module(body=[accessor_class], type_ignores=[]))
        nodes = [SimpleNamespace(name='Example', bnode=SimpleNamespace(name='Example'),
                    is_class_property=prop, config_order=[], default_params={}, has_items=False,
                    get_possible_sockets=lambda **kw: []) for prop in (True, False)]
        for node in nodes:
            attach_arguments(node)
        namespace['NodeInfo'] = SimpleNamespace(loop_on_nodes=lambda callback, **kw:
                                               [callback(node) for node in nodes])
        exec(compile(module, '<accessors>', 'exec'), namespace)
        records = []
        class Accessors(namespace['Accessors']):
            tree_type = 'GeometryNodeTree'
            def implementation(self, node):
                obj = SimpleNamespace(node=node, parameters={}, type_aliases=None)
                obj.gen_node_call = MethodType(namespace['gen_node_call'], obj)
                return obj
            @classmethod
            def register_source(cls, node, node_call, source, **metadata):
                records.append((node_call, source))
        try:
            Accessors().gen_static_code()
        finally:
            namespace.pop('NodeInfo')
        self.assertEqual(len(records), 2)
        for (node_call, source), decorator in zip(
                records, ('utils.classproperty', 'classmethod')):
            function = ast.parse('class Example:\n' + source).body[0].body[0]
            self.assertEqual(ast.unparse(function.decorator_list[0]), decorator)
            self.assertEqual((node_call.class_name, node_call.return_kind), ('nd', 'OUT'))
            self.assertIn('return node._out', source)


    def test_numpy_dynamic_items_and_fixed_input_documentation(self):
        for named in (False, True):
            fn, _, _ = self.generate([], method_type='FUNCTION', items_named=named)
            doc = inspect.getdoc(fn)
            self.assertTrue(doc.startswith("Node Test's Node."))
            expected = ('**named_items : Socket\n    Dynamic sockets supplied by keyword.'
                        if named else '*dyn_sockets : Socket\n    Values for anonymous dynamic sockets.')
            self.assertIn(expected, doc)
        fn, _, _ = self.generate([socket('Value')], self_socket='Value')
        self.assertIn("**Fixed inputs**\n\n- self on socket 'Value'", inspect.getdoc(fn))


    def test_generator_checks_the_final_call_before_node_access(self):
        with self.assertRaisesRegex(ValueError, 'self_socket'):
            namespace['gen_node_call'](object(), NodeCall.method('sample'))

    def test_named_items_merge_sockets_and_expand_keywords(self):
        fn, calls, _ = self.generate([], method_type='FUNCTION', items_named=True)
        fn(items={'A': 1}, B=2)
        self.assertEqual(calls[0][1], {'named_sockets': {'A': 1}, 'mode': 'DEFAULT', 'B': 2})

    def test_anonymous_items_expand_positionally(self):
        fn, calls, _ = self.generate([], method_type='FUNCTION', items_named=False)
        fn(1, 2, mode='A')
        self.assertEqual(calls[0], (("Test's Node", 1, 2), {'named_sockets': {}, 'mode': 'A'}))

    def test_explicit_none_on_node_call_is_fixed(self):
        node = attach_arguments(SimpleNamespace(name='Test', config_order=[],
            default_params={'font': {'value': 'default', 'type': 'FONT', 'enums': None}},
            has_items=False, get_possible_sockets=lambda **kw: []))
        impl = SimpleNamespace(node=node, parameters={'font': None}, type_aliases=None)
        source = namespace['gen_node_call'](impl, NodeCall.function('build', parameters={'font': None}))
        env = {'Node': lambda *a, **kw: SimpleNamespace(_out=kw)}
        exec(source, env)
        self.assertNotIn('font', inspect.signature(env['build']).parameters)
        self.assertIsNone(env['build']()['font'])


if __name__ == '__main__':
    unittest.main()
