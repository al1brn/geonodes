"""Run in Blender: blender --background --python generation2/tests/test_driven_sockets.py."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from geonodes.generation2.node_info import NodeInfo
from geonodes.generation2.node_socket import NodeSocket
from geonodes.generation2.tree import Tree


class DrivenSocketsTest(unittest.TestCase):
    def test_map_range_stores_independent_snapshots(self):
        with Tree('GeometryNodeTree') as tree:
            node = NodeInfo(tree.btree, tree.create_node('Map Range'))
            scalar = node.data_type_driven_sockets['FLOAT']['inputs']
            vector = node.data_type_driven_sockets['FLOAT_VECTOR']['inputs']
            self.assertTrue(all(isinstance(socket, NodeSocket) for socket in scalar + vector))
            self.assertEqual((scalar[0].identifier, scalar[0].socket_name, scalar[0].socket_type),
                             ('Value', 'Value', 'VALUE'))
            self.assertEqual((vector[0].identifier, vector[0].socket_name, vector[0].socket_type),
                             ('Vector', 'Vector', 'VECTOR'))
            node.set_params(data_type='FLOAT_VECTOR')
            self.assertEqual(node.data_type_input, 'Vector')
            self.assertTrue(node.data_type_drives_first_input)
            node.get_possible_sockets(data_type='FLOAT_VECTOR')
            self.assertEqual(node.bnode.data_type, 'FLOAT')
            self.assertEqual(vector[0].socket_name, 'Vector')
            self.assertEqual(vector[0].socket_type, 'VECTOR')
            self.assertEqual(node.data_type_input, 'Value')

    def test_empty_input_lists_and_no_type_parameter(self):
        with Tree('GeometryNodeTree') as tree:
            node = NodeInfo(tree.btree, tree.create_node('Random Value'))
            for value, sockets in node.data_type_driven_sockets.items():
                self.assertNotIn('ID', [socket.identifier for socket in sockets['inputs']])
                self.assertNotIn('Seed', [socket.identifier for socket in sockets['inputs']])
                node.set_params(data_type=value)
                if not sockets['inputs']:
                    self.assertIsNone(node.data_type_input)
                    self.assertFalse(node.data_type_drives_first_input)
            node = NodeInfo(tree.btree, tree.create_node('Math'))
            self.assertEqual(node.data_type_driven_sockets, {})
            self.assertIsNone(node.data_type_input)
            self.assertFalse(node.data_type_drives_first_input)


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
