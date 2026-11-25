"""Run with Blender --background --python core_5_2/tests/test_float_operators.py."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from geonodes.core_5_2 import Float, Node, GeoNodes, ShaderNodes


class FloatOperatorsTest(unittest.TestCase):
    def test_arithmetic_and_inplace_modulo(self):
        for factory in (GeoNodes, ShaderNodes):
            with self.subTest(environment=factory.__name__):
                with factory('Float operators test'):
                    value = Float(7)
                    for result, operation in ((value + 2, 'ADD'), (2 - value, 'SUBTRACT'),
                                              (value * 2, 'MULTIPLY'), (2 / value, 'DIVIDE'),
                                              (value ** 2, 'POWER'), (2 ** value, 'POWER'),
                                              (value % 2, 'MODULO'), (2 % value, 'MODULO'),
                                              (abs(value), 'ABSOLUTE'), (round(value), 'ROUND')):
                        self.assertEqual(result._bsocket.node.operation, operation)
                    reflected = (2 % value)._bsocket.node
                    self.assertEqual(reflected.inputs[0].links[0].from_socket.default_value, 2)
                    self.assertEqual(reflected.inputs[1].links[0].from_socket, value._bsocket)
                    original = value
                    previous_socket = value._bsocket
                    value %= 3
                    self.assertIs(value, original)
                    self.assertNotEqual(value._bsocket, previous_socket)
                    self.assertEqual(value._bsocket.node.operation, 'MODULO')
                    self.assertEqual(value._bsocket.node.inputs[0].links[0].from_socket, previous_socket)
                    vector = Node('Combine XYZ', named_sockets={'X': 1, 'Y': 2, 'Z': 3})._out
                    self.assertEqual((value % vector).SOCKET_TYPE, 'VECTOR')
                    self.assertEqual((vector % value).SOCKET_TYPE, 'VECTOR')
                    for invalid in ('__modulo__', '__rmodulo__', '__imodulo__'):
                        self.assertFalse(hasattr(type(value), invalid))


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
