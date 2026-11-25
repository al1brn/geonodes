"""Run with Blender --background --python generation/tests/test_vector_parameters.py."""
from pathlib import Path
import sys
import unittest

import bpy

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from geonodes import GeoNodes, Mesh, Vector
from geonodes.generation.node_call import NodeCall
from geonodes.generation.node_implementation import NodeImplementation
from geonodes.generation.node_info import NodeInfo
from geonodes.generation.node_param import NodeParam


class VectorParameterTest(unittest.TestCase):
    def test_vector_parameter_survives_introspection_and_generation(self):
        tree = bpy.data.node_groups.new('Vector Parameter Test', 'GeometryNodeTree')
        try:
            node = tree.nodes.new('FunctionNodeInputVector')
            node.vector = (1, 2, 3)
            param = NodeParam.Parameter(node, 'vector')
            self.assertEqual(param.param_type, 'Vector')
            self.assertEqual(param.value, (1, 2, 3))
            self.assertEqual(param.typing, 'tuple[float, float, float]')
            self.assertEqual(param.arg_value, '(1.0, 2.0, 3.0)')
            info = NodeInfo(tree, node)
            self.assertEqual(info.snapshot_params()['vector']['type'], 'Vector')
            source, = NodeImplementation(info).gen_source_code(NodeCall.class_method('vector'))
            self.assertIn('vector: tuple[float, float, float]', source)
            compile('from __future__ import annotations\nclass ND:\n' + source,
                    '<vector>', 'exec')
        finally:
            bpy.data.node_groups.remove(tree)

    def test_constant_vector_and_extrusion_offset(self):
        name = 'Vector Constant and Extrusion Test'
        try:
            with GeoNodes(name):
                vector = Vector((1, 2, 3))
                self.assertEqual(tuple(vector._bsocket.node.vector), (1, 2, 3))
                vector.out('Vector')
                Mesh.Grid().faces.extrude(offset=(0, 0, 0.5)).out()
            tree = bpy.data.node_groups[name]
            self.assertTrue(all(link.is_valid for link in tree.links))
        finally:
            tree = bpy.data.node_groups.get(name)
            if tree is not None:
                bpy.data.node_groups.remove(tree)


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
