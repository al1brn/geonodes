"""Run without Blender: python3 -B generation2/tests/test_node_calls.py."""
import ast
from dataclasses import fields
from types import SimpleNamespace
from pathlib import Path
import runpy
import unittest

module = runpy.run_path(str(Path(__file__).resolve().parents[1] / 'node_call.py'))
NodeCall, NodeCalls = module['NodeCall'], module['NodeCalls']


class NodeCallsTest(unittest.TestCase):
    def setUp(self):
        self.base = NodeCall.method('value', self_socket='Value')

    def test_aligned_columns_and_broadcast(self):
        loop = NodeCalls.attributes(self.base, class_name=['Float', 'Integer'],
                        method_name=['first', 'second'], is_jump=[True])
        variants = list(loop)
        self.assertEqual([(spec.class_name, spec.method_name, spec.is_jump) for spec in variants],
                         [('Float', 'first', True), ('Integer', 'second', True)])
        self.assertEqual(self.base.method_name, 'value')
        self.assertFalse(self.base.is_jump)

    def test_dictionaries_with_different_keys(self):
        overrides = [
            {'class_name': 'Float', 'method_name': 'first', 'parameters': {'data_type': 'FLOAT'}},
            {'class_name': 'String', 'method_type': 'CLASS_METHOD', 'method_name': 'FromValue'},
        ]
        variants = list(NodeCalls.overrides(self.base, overrides=overrides))
        self.assertEqual(variants[0].self_socket, 'Value')
        self.assertIsNone(variants[1].self_socket)
        self.assertEqual(variants[1].method_type, 'CLASS_METHOD')
        self.assertIn('class_name', overrides[0])

    def test_nested_loops_produce_all_combinations(self):
        inner = NodeCalls.attributes(self.base, class_name=['Float', 'Integer'], method_name=['a', 'b'])
        outer = NodeCalls.overrides(inner, overrides=[{'method_name': 'outer'}, {'is_jump': True}])
        self.assertEqual([(spec.class_name, spec.method_name, spec.is_jump) for spec in outer],
                         [('Float', 'outer', False), ('Float', 'a', True),
                          ('Integer', 'outer', False), ('Integer', 'b', True)])
        self.assertEqual([(spec.class_name, spec.method_name) for spec in inner], [('Float', 'a'), ('Integer', 'b')])
        routed = inner.replace(class_name='Socket')
        self.assertEqual([spec.class_name for spec in routed], ['Socket', 'Socket'])

    def test_empty_and_single_loops(self):
        self.assertIs(list(NodeCalls(self.base))[0], self.base)
        inner = NodeCalls.attributes(self.base, class_name=['Float', 'Integer'])
        before = list(inner)
        # A neutral wrapper forwards the objects yielded by its base.
        wrapped = NodeCalls(inner)
        inner.loop = lambda: iter(before)
        after = list(wrapped)
        self.assertTrue(all(a is b for a, b in zip(before, after)))
        self.assertEqual(list(NodeCalls.overrides(self.base, overrides=[])), [])
        self.assertEqual(list(NodeCalls.attributes(self.base, method_name=[])), [])

    def test_invalid_variations_and_keys(self):
        with self.assertRaises(ValueError):
            NodeCalls.attributes(self.base, method_name=['a', 'b'], is_jump=[True, False, True])
        with self.assertRaises(TypeError):
            NodeCalls.overrides(self.base, overrides=[{}], method_name='other')
        with self.assertRaises(TypeError):
            NodeCalls.overrides(self.base, overrides=[{'typo': True}])
        with self.assertRaises(TypeError):
            list(NodeCalls.overrides(self.base, overrides=[{'class_name': ('Float', 'Integer')}]))[0]._check()

    def test_spec_carries_one_destination(self):
        self.assertIn('class_name', {field.name for field in fields(NodeCall)})
        spec = NodeCall.method('test', self_socket='Value', class_name='Float')
        self.assertEqual(list(NodeCalls(spec))[0].class_name, 'Float')
        self.assertEqual(spec.replace(method_name='other').class_name, 'Float')
        with self.assertRaises(TypeError):
            NodeCall.method('test', self_socket='Value', class_name=('Float', 'Integer'))._check()
        with self.assertRaises(TypeError):
            NodeCall.function(('first', 'second'))._check()
        self.assertEqual(str(self.base), '<NodeCall value METHOD>')

    def test_descriptions_propagate_destinations_to_specs(self):
        root = Path(__file__).resolve().parents[1]
        tree = ast.parse((root / 'node_implementation.py').read_text())
        owner = next(node for node in tree.body if isinstance(node, ast.ClassDef)
                     and node.name == 'NodeImplementation')
        method = next(node for node in owner.body if isinstance(node, ast.FunctionDef)
                      and node.name == 'get_node_implementation')
        config = runpy.run_path(str(root / 'config.py'))
        namespace = dict(NodeCall=NodeCall, NodeCalls=NodeCalls,
            config=SimpleNamespace(**config),
            core_module=SimpleNamespace(utils=SimpleNamespace(
                snake_case=lambda name: name.lower().replace(' ', '_'),
                CamelCase=lambda name: name.replace(' ', ''))))
        exec(compile(ast.Module(body=[method], type_ignores=[]), '<descriptions>', 'exec'), namespace)
        first = SimpleNamespace(enabled=True, socket_type='GEOMETRY',
                                socket_name='Curve', class_name='Curve', is_attribute=False)
        node = SimpleNamespace(name='Offset Point in Curve', bl_idname='Test',
            inputs={'Curve': first}, outputs={}, color_tag='INPUT', is_shader=False,
            has_domain_parameter=False, has_data_type_parameter=False,
            data_type_drives_inputs=False, data_type_drives_outputs=False,
            data_type_drives_first_input=False, has_items=False, data_type_input=lambda: None)
        loop = namespace['get_node_implementation'](SimpleNamespace(node=node))
        self.assertIsInstance(loop, NodeCalls)
        self.assertEqual([(spec.class_name, spec.method_name, spec.self_socket) for spec in loop],
                         [('Curve', 'offset_point', 'Curve'), ('Spline', 'offset_point', 'Curve')])

    def test_intermediate_calls_are_not_validated(self):
        base = NodeCall.method('sample')
        inner = NodeCalls.attributes(base, class_name=['Float', 'Vector'])
        outer = NodeCalls.attributes(inner, self_socket='Value')
        self.assertTrue(all(call._check() is call for call in outer))
        self.assertIsNone(base.self_socket)
        with self.assertRaisesRegex(ValueError, 'self_socket'):
            base._check()


if __name__ == '__main__':
    unittest.main()
