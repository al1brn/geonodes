"""Run with Blender --background --python generation/tests/test_input_node_calls.py."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from geonodes.generation import config
from geonodes.generation.node_implementation import NodeImplementation
from geonodes.generation.node_info import NodeInfo
from geonodes.generation.tree import Tree


class InputNodeCallsTest(unittest.TestCase):
    def calls(self, tree, name):
        return NodeImplementation(NodeInfo(tree.btree, tree.create_node(name))).get_default_node_calls()

    def test_fields_and_topology_have_no_inferred_methods(self):
        with Tree('GeometryNodeTree') as tree:
            for name in ('Position', 'Curve of Point', 'Corners of Edge', 'Face of Corner',
                         'Curve Tangent', 'Instance Rotation', 'Scene Time', 'Normal'):
                with self.subTest(node=name):
                    self.assertFalse(any(call.implement for call in self.calls(tree, name)))

    def test_useful_receivers_and_constructors_are_preserved(self):
        with Tree('GeometryNodeTree') as tree:
            for name, target, method, receiver in (
                ('Object Info', 'Object', 'info', 'Object'),
                ('Image Info', 'Image', 'info', 'Image'),
                ('Collection Children', 'Collection', 'collection_children', 'Collection'),
                ('Collection Info', 'Instances', 'CollectionInfo', None),
                ('Active Camera', 'Object', 'ActiveCamera', None),
                ('Import STL', 'Mesh', 'ImportSTL', None),
                ('Import Text', 'String', 'ImportText', None),
            ):
                with self.subTest(node=name):
                    call, = self.calls(tree, name)
                    self.assertEqual((call.class_name, call.method_name, call.self_socket),
                                     (target, method, receiver))
                    self.assertEqual(call.is_class_method, receiver is None)

    def test_configured_input_can_describe_an_instance_method(self):
        spec = dict(method_type='METHOD', class_name='Integer',
                    method_name='curve_of_point', self_socket='Point Index',
                    return_socket='Index in Curve')
        with Tree('GeometryNodeTree') as tree:
            impl = NodeImplementation(NodeInfo(tree.btree, tree.create_node('Curve of Point')))
            with patch.dict(config.DEFAULT_IMPLEMENTATION, {'Curve of Point': spec}):
                call, = impl.get_default_node_calls()
                self.assertEqual((call.method_type, call.class_name, call.self_socket),
                                 ('METHOD', 'Integer', 'Point Index'))
                source, = impl.gen_source_code(call)
                self.assertIn("'ID_Point Index': self", source)
                self.assertIn("return node['Index in Curve']", source)
                self.assertNotIn('@classmethod', source)

    def test_grid_info_keeps_its_grid_receiver_for_every_type(self):
        with Tree('GeometryNodeTree') as tree:
            impl = NodeImplementation(NodeInfo(tree.btree, tree.create_node('Grid Info')))
            calls = []
            impl.gen_source_code(impl.get_default_node_calls(),
                                 lambda node, call, source: calls.append(call))
            self.assertEqual({call.class_name for call in calls},
                             {'Boolean', 'Integer', 'Float', 'Vector'})
            for call in calls:
                self.assertEqual(call.method_type, 'METHOD')
                self.assertEqual(call.method_name, 'grid_info')
                self.assertTrue(call.self_socket)

    def test_static_overrides_do_not_supply_residual_input_specs(self):
        with Tree('GeometryNodeTree') as tree:
            with patch.dict(config.STATIC_IMPLEMENTATIONS, {
                'Curve of Point': dict(method_type='CLASS_METHOD', class_name='Point',
                                       method_name='Unwanted'),
            }):
                self.assertEqual(self.calls(tree, 'Curve of Point'), [])

    def test_residual_config_must_be_complete(self):
        with Tree('GeometryNodeTree') as tree:
            with patch.dict(config.DEFAULT_IMPLEMENTATION, {
                'Curve of Point': dict(class_name='SplinePoint', method_name='curve_of_point'),
            }):
                with self.assertRaises(TypeError):
                    self.calls(tree, 'Curve of Point')

    def test_existing_explicit_exceptions_expand_without_mutating_config(self):
        expected = deepcopy(config.DEFAULT_IMPLEMENTATION)
        with Tree('GeometryNodeTree') as tree:
            for name in ('Offset Corner in Face', 'Offset Point in Curve', 'Shortest Edge Paths',
                         'NURBS Order', 'NURBS Weight', 'Named Layer Selection',
                         'Mesh Island', 'Import Text', 'Handle Type Selection'):
                with self.subTest(node=name):
                    calls = self.calls(tree, name)
                    self.assertTrue(calls)
                    for call in calls:
                        call._check()
                        self.assertTrue(call.is_class_method)
                    if name == 'Offset Point in Curve':
                        self.assertEqual([c.class_name for c in calls], ['Curve', 'Spline'])
        self.assertEqual(config.DEFAULT_IMPLEMENTATION, expected)


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
