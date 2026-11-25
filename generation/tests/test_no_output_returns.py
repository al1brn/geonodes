"""Run with Blender --background --python generation/tests/test_no_output_returns.py."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from geonodes.generation.node_call import NodeCall
from geonodes.generation.node_implementation import NodeImplementation
from geonodes.generation.node_info import NodeInfo
from geonodes.generation.tree import Tree


class NoOutputReturnsTest(unittest.TestCase):
    def test_no_output_overrides_all_socket_returns_without_mutating_spec(self):
        for tree_type in ('GeometryNodeTree', 'ShaderNodeTree'):
            with Tree(tree_type) as tree:
                impl = NodeImplementation(NodeInfo(tree.btree, tree.create_node('Comment')))
                for kind in ('OUT', 'SECOND_OUT', 'cls', 'Float', 'NODE'):
                    with self.subTest(tree_type=tree_type, kind=kind):
                        call = NodeCall.class_method('comment', return_kind=kind,
                                                     return_socket='Missing')
                        recorded = []
                        source, = impl.gen_source_code(call, lambda n, c, s: recorded.append(c))
                        self.assertIn('return node\n', source)
                        self.assertNotIn('return node[', source)
                        self.assertIn('Node\n', source)
                        self.assertEqual(recorded[0].return_kind, 'NODE')
                        self.assertIsNone(recorded[0].return_socket)
                        self.assertEqual(call.return_kind, kind)
                        self.assertEqual(call.return_socket, 'Missing')
                        compile('from __future__ import annotations\nclass ND:\n' + source,
                                '<comment>', 'exec')

    def test_setter_still_has_no_return(self):
        with Tree('GeometryNodeTree') as tree:
            impl = NodeImplementation(NodeInfo(tree.btree, tree.create_node('Warning')))
            call = NodeCall.setter('message', self_socket='Message',
                                   parameters={'warning_type': 'INFO'})
            source, = impl.gen_source_code(call)
            self.assertNotIn('return ', source)
            self.assertNotIn('Returns', source)


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
