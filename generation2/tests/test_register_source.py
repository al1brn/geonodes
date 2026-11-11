"""Run without Blender: python3 -B generation2/tests/test_register_source.py."""
import ast
from pathlib import Path
import runpy
import textwrap
from types import SimpleNamespace as NS
import unittest

ROOT = Path(__file__).resolve().parents[1]
NodeCall = runpy.run_path(str(ROOT / 'node_call.py'))['NodeCall']
tree = ast.parse((ROOT / 'node_implementation.py').read_text())
owner = next(node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == 'NodeImplementation')
methods = [node for node in owner.body if isinstance(node, ast.FunctionDef)
           and node.name in ('register_source', '_register_source')]
cls = ast.ClassDef(name='Registry', bases=[], keywords=[], body=methods, decorator_list=[])
namespace = dict(NodeCall=NodeCall, ast=ast, textwrap=textwrap,
                 core_module=NS(constants=NS(DOMAIN_CLASSES={'Point', 'Edge'})),
                 utils=NS(get_node_names=lambda tree_type: {'TestNode': 'Test'}))
exec(compile(ast.fix_missing_locations(ast.Module(body=[cls], type_ignores=[])), '<registry>', 'exec'), namespace)
Registry = namespace['Registry']


class RegisterSourceTest(unittest.TestCase):
    def setUp(self):
        Registry.files, Registry.cross_refs = {}, {}
        self.node = NS(name='Test', btree=NS(bl_idname='GeometryNodeTree'),
                       bnode=NS(name='Test', bl_idname='TestNode'))

    def test_destinations_choose_their_files(self):
        for destination, filename, factory in (
            ('Float', 'float.py', NodeCall.method),
            ('Point', 'dom_point.py', NodeCall.method),
            ('nd', 'static_nd.py', NodeCall.class_method),
            ('gnmath', 'gnmath.py', NodeCall.function),
        ):
            with self.subTest(destination=destination):
                options = {'self_socket': 'Value'} if destination in ('Float', 'Point') else {}
                call = factory('example', class_name=destination, **options)
                source = 'def example():\n    return None\n'
                Registry.register_source(self.node, call, source)
                self.assertEqual(Registry.files['GeometryNodeTree'][filename], [source])
                self.assertEqual(Registry.cross_refs['GeometryNodeTree']['TestNode'][destination][0]['returns'], 'OUT')

    def test_output_and_setter_metadata(self):
        getter = NodeCall.getter('value', class_name='Point', self_socket='Value', return_socket='Result')
        setter = NodeCall.setter('value', class_name='Point', self_socket='Value')
        Registry.register_source(self.node, getter, '@property\ndef value(self):\n    return None\n')
        Registry.register_source(self.node, setter, '@value.setter\ndef value(self, value):\n    pass\n')
        refs = Registry.cross_refs['GeometryNodeTree']['TestNode']['Point']
        self.assertEqual([ref['returns'] for ref in refs], ['Result', None])
        self.assertTrue(refs[0]['is_get'])
        self.assertTrue(refs[1]['is_set'])

    def test_validation_and_reference_only_registration(self):
        source = 'def example():\n    pass\n'
        with self.assertRaisesRegex(ValueError, 'class_name'):
            Registry.register_source(self.node, NodeCall.function('example'), source)
        call = NodeCall.function('example', class_name='gnmath')
        Registry.register_source(self.node, call, source, write_source=False)
        self.assertEqual(Registry.files['GeometryNodeTree'], {})
        with self.assertRaisesRegex(ValueError, 'Duplicate implementation'):
            Registry.register_source(self.node, call, source)
        Registry.register_source(None, call, source, tree_type='ShaderNodeTree')
        self.assertIn('gnmath.py', Registry.files['ShaderNodeTree'])


if __name__ == '__main__':
    unittest.main()
