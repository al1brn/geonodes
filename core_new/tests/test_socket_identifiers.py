"""Run in Blender: blender --background --python core_new/tests/test_socket_identifiers.py."""
import contextlib
import io
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from geonodes import core_module as core
from geonodes.core_new.common.treeinterface import ItemPath
from geonodes.core_new.root.node import Node


class SocketIdentifiersTest(unittest.TestCase):
    def test_full_name_preserves_identifiers_and_regular_paths(self):
        for identifier in ('ID_Value_001', 'ID_Value_002', 'ID_Vector_001'):
            self.assertEqual(ItemPath.get_full_name(identifier), identifier)
            self.assertEqual(ItemPath.get_full_name(identifier, 'Panel'), identifier)
        self.assertIsNone(ItemPath.get_full_name(None, 'Panel'))
        for name, panel in (('Value', ''), ('Value_001', 'Panel'), ('Socket', 'Top > Sub')):
            self.assertEqual(ItemPath.get_full_name(name, panel), (ItemPath(panel) + name).path)

    def test_exact_input_identifiers_in_both_environments(self):
        for factory in (core.GeoNodes, core.ShaderNodes):
            with self.subTest(factory=factory.__name__), contextlib.redirect_stdout(io.StringIO()):
                with factory('Test exact input identifiers'):
                    node = Node('Math', named_sockets={'ID_Value': 2.0, 'ID_Value_001': 3.0},
                                operation='ADD')
                    inputs = {socket.identifier: socket for socket in node._bnode.inputs}
                    self.assertEqual(inputs['Value'].default_value, 2.0)
                    self.assertEqual(inputs['Value_001'].default_value, 3.0)
                    node.set_input_socket('ID_Value_001', 7.0, panel='Ignored for exact identifiers')
                    self.assertEqual(inputs['Value_001'].default_value, 7.0)
                    self.assertEqual(node._inputs.by_name('ID_Value_001'), inputs['Value_001'])
                    # Ordinary unique names keep their previous behavior.
                    node.set_input_socket('Value_1', 9.0)
                    self.assertEqual(inputs['Value_001'].default_value, 9.0)


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
