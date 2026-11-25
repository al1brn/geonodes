"""Run with Blender --background --python generation/tests/test_spec_expansion.py."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest
from types import SimpleNamespace
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from geonodes.generation.context import ADD_LOOP, LOOP_ONLY, REPLACE
from geonodes.generation.node_call import NodeCall, NodeCalls
from geonodes.generation.node_implementation import NodeImplementation
from geonodes.generation.node_info import NodeInfo
from geonodes.generation.node_param import NodeParam
from geonodes.generation.tree import Tree


class SpecExpansionTest(unittest.TestCase):
    def test_general_first_and_aligned_domains(self):
        spec = {'class_name': ['Geometry', 'Vertex', 'Edge', 'Face', 'Corner'],
                'parameters': {'mode': ADD_LOOP}}
        before = deepcopy(spec)
        with Tree('GeometryNodeTree') as tree:
            impl = NodeImplementation(NodeInfo(tree.btree, tree.create_node('Mesh to Points')))
            rows = impl.expand_spec(spec)
            self.assertEqual([(r['class_name'], r['parameters']) for r in rows],
                             [('Geometry', {}), ('Vertex', {'mode': 'VERTICES'}),
                              ('Edge', {'mode': 'EDGES'}), ('Face', {'mode': 'FACES'}),
                              ('Corner', {'mode': 'CORNERS'})])
            calls = NodeCalls.method('to_points', self_socket='Mesh').overrides(rows)
            self.assertEqual(len(calls), 5)
            for call in calls:
                source = impl._gen_source_code(call)
                self.assertEqual('mode:' in source, call.class_name == 'Geometry')
                compile('from __future__ import annotations\nclass Methods:\n' + source,
                        '<to_points>', 'exec')
            with self.assertRaisesRegex(ValueError, 'Incompatible list lengths'):
                impl.expand_spec({**spec, 'class_name': ['Vertex', 'Edge']})
        self.assertEqual(spec, before)

    def test_generic_loop_names_and_no_general_for_loop_only(self):
        with Tree('GeometryNodeTree') as tree:
            impl = NodeImplementation(NodeInfo(tree.btree, tree.create_node('Warning')))
            rows = impl.expand_spec({'method_name': REPLACE,
                                     'parameters': {'warning_type': LOOP_ONLY}})
            self.assertEqual([r['method_name'] for r in rows], ['error', 'warning', 'info'])
            self.assertEqual([r['parameters']['warning_type'] for r in rows],
                             ['ERROR', 'WARNING', 'INFO'])

    def test_type_loop_preserves_explicit_receiver(self):
        with Tree('GeometryNodeTree') as tree:
            impl = NodeImplementation(NodeInfo(tree.btree, tree.create_node('Switch')))
            rows = impl.expand_spec({'method_type': 'METHOD', 'self_socket': 'True',
                                     'class_name': None, 'parameters': {'input_type': LOOP_ONLY}})
            self.assertTrue(rows)
            self.assertTrue(all(row['self_socket'] == 'True' for row in rows))
            self.assertTrue(all(row['class_name'] is not None for row in rows))

    def test_two_parameter_loops_are_aligned(self):
        impl = NodeImplementation.__new__(NodeImplementation)
        impl.node = SimpleNamespace(name='Test', bnode=object(), data_type_name=None)
        parameter = SimpleNamespace(enums=['A', 'B'], enum_names={'A': 'A', 'B': 'B'})
        spec = {'class_name': ['First', 'Second', 'Third'],
                'parameters': {'one': ADD_LOOP, 'two': ADD_LOOP, 'fixed': 42}}
        with patch.object(NodeParam, 'Parameter', return_value=parameter):
            rows = impl.expand_spec(spec)
        self.assertEqual([r['parameters'] for r in rows],
                         [{'fixed': 42}, {'one': 'A', 'two': 'A', 'fixed': 42},
                          {'one': 'B', 'two': 'B', 'fixed': 42}])


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
