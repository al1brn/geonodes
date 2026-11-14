"""Run with Blender --background --python generation2/tests/test_possible_sockets.py."""
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from geonodes.generation2.node_info import NodeInfo
from geonodes.generation2.tree import Tree


class PossibleSocketsTest(unittest.TestCase):
    def test_both_directions_and_fixed_variants(self):
        with Tree('GeometryNodeTree') as tree:
            node = NodeInfo(tree.btree, tree.create_node('Map Range'))
            for data_type, receiver, socket_type in (('FLOAT', 'Value', 'VALUE'),
                                                     ('FLOAT_VECTOR', 'Vector', 'VECTOR')):
                inputs = node.get_possible_sockets(data_type=data_type)
                outputs = node.get_possible_sockets(inout='OUTPUT', data_type=data_type)
                self.assertEqual(inputs[0].socket_name, receiver)
                self.assertEqual(inputs[0].socket_type, socket_type)
                self.assertEqual(outputs[0].socket_type, socket_type)
                self.assertEqual(node.bnode.data_type, 'FLOAT')
            self.assertEqual(set(node.outputs), {'Result', 'Vector'})
            self.assertTrue(node.data_type_drives_inputs)
            self.assertTrue(node.data_type_drives_outputs)
            for obsolete in ('param_dependencies', 'configurations', 'enum_parameters',
                             'driving_parameters', 'max_inputs', 'max_outputs'):
                self.assertFalse(hasattr(node, obsolete))

    def test_union_matches_all_enabled_physical_sockets(self):
        with Tree('GeometryNodeTree') as tree:
            for name in ('Math', 'Map Range', 'Switch', 'Mesh Boolean'):
                node = NodeInfo(tree.btree, tree.create_node(name))
                for inout, direction in (('INPUT', 'inputs'), ('OUTPUT', 'outputs')):
                    expected = {}
                    def capture(info, **kwargs):
                        for identifier, socket in info.all_sockets()[direction].items():
                            if socket.enabled:
                                expected.setdefault(identifier, set()).add(socket.socket_name)
                    node.loop_on_configurations(capture)
                    sockets = node.get_possible_sockets(inout=inout, group=False)
                    self.assertEqual({s.identifier: s.names for s in sockets}, expected)
                    self.assertEqual([s.index for s in sockets], sorted(s.index for s in sockets))

    def test_output_only_type_and_class_properties(self):
        with Tree('GeometryNodeTree') as tree:
            node = NodeInfo(tree.btree, tree.create_node('String to Value'))
            self.assertFalse(node.data_type_drives_first_input)
            self.assertTrue(node.data_type_drives_outputs)
            self.assertTrue(NodeInfo(tree.btree, tree.create_node('Position')).is_class_property)
            self.assertFalse(NodeInfo(tree.btree, tree.create_node('Math')).is_class_property)

    def test_exploration_restores_defaults_after_failure(self):
        with Tree('GeometryNodeTree') as tree:
            node = NodeInfo(tree.btree, tree.create_node('Map Range'))
            with patch.object(node, 'all_sockets', side_effect=RuntimeError('probe')):
                with self.assertRaisesRegex(RuntimeError, 'probe'):
                    node.get_possible_sockets(data_type='FLOAT_VECTOR')
            self.assertEqual(node.bnode.data_type, 'FLOAT')


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
