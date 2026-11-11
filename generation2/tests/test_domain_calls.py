"""Run without Blender: python3 -B generation2/tests/test_domain_calls.py."""
import ast
from pathlib import Path
import runpy
from types import SimpleNamespace as NS
import unittest

ROOT = Path(__file__).resolve().parents[1]
module = runpy.run_path(str(ROOT / 'node_call.py'))
NodeCall, NodeCalls = module['NodeCall'], module['NodeCalls']
tree = ast.parse((ROOT / 'node_implementation.py').read_text())
owner = next(node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == 'NodeImplementation')
method = next(node for node in owner.body if isinstance(node, ast.FunctionDef) and node.name == 'get_domain_loop_calls')
namespace = dict(NodeCall=NodeCall, NodeCalls=NodeCalls,
                 NodeParam=NS(Parameter=lambda node, name: node.domain_parameter))
exec(compile(ast.Module(body=[method], type_ignores=[]), '<domain calls>', 'exec'), namespace)


class DomainCallsTest(unittest.TestCase):
    def generate(self, call, domains=('POINT', 'EDGE')):
        implementation = NS(node=NS(name='Test', bnode=NS(domain_parameter=NS(enums=domains))))
        return namespace['get_domain_loop_calls'](implementation, call)

    def test_general_call_and_fixed_domains(self):
        call = NodeCall.method('sample', class_name='Geometry', self_socket='Geometry',
                               parameters={'data_type': 'FLOAT'}, domain_loop=True, is_jump=True)
        variants = list(self.generate(call))
        self.assertEqual([variant.class_name for variant in variants], ['Geometry', 'Point', 'Edge'])
        self.assertEqual([variant.parameters for variant in variants], [
            {'data_type': 'FLOAT'}, {'data_type': 'FLOAT', 'domain': 'POINT'},
            {'data_type': 'FLOAT', 'domain': 'EDGE'}])
        for variant in variants:
            self.assertEqual(variant.self_socket, 'Geometry')
            self.assertTrue(variant.is_jump)
            self.assertFalse(variant.domain_loop)
        self.assertTrue(call.domain_loop)
        self.assertEqual(call.parameters, {'data_type': 'FLOAT'})
        variants[1].parameters['data_type'] = 'INT'
        self.assertEqual(variants[2].parameters['data_type'], 'FLOAT')

    def test_class_method_without_general_destination(self):
        call = NodeCall.class_method('Sample', domain_loop=True)
        variants = list(self.generate(call, ('CURVE', 'SPLINE', 'CORNER', 'INSTANCE', 'LAYER', 'AUTO')))
        self.assertEqual([variant.class_name for variant in variants],
                         ['Spline', 'Spline', 'Corner', 'Instance', 'Layer', 'Geometry'])
        self.assertTrue(all(variant.method_type == 'CLASS_METHOD' and variant.self_socket is None
                            for variant in variants))

    def test_no_domain_choices(self):
        self.assertEqual(list(self.generate(NodeCall.class_method('Sample'), ())), [])
        with self.assertRaisesRegex(ValueError, 'domain enum'):
            self.generate(NodeCall.class_method('Sample'), None)


if __name__ == '__main__':
    unittest.main()
