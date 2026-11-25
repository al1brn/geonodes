"""Run with Blender --background --python core_5_3/tests/test_node_arrange_hints.py."""
from pathlib import Path
import sys
import unittest

import bpy

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from geonodes.core_5_3 import GeoNodes, nd


class NodeArrangeHintsTest(unittest.TestCase):
    def tearDown(self):
        tree = bpy.data.node_groups.get('Arrange hints test')
        if tree is not None:
            bpy.data.node_groups.remove(tree)

    def test_properties_and_chaining(self):
        with GeoNodes('Arrange hints test'):
            node = nd.comment('A comment')
            self.assertIs(node._custom_property('test_value', 42), node)
            self.assertEqual(node._bnode['test_value'], 42)
            node._custom_property('test_value', 7)
            self.assertEqual(node._bnode['test_value'], 7)
            self.assertIs(node._set_arrange(), node)
            self.assertNotIn('arrange_horizontal', node._bnode)
            self.assertNotIn('arrange_vertical', node._bnode)
            for horizontal in ('outer_left', 'left', 'mid', 'right', 'outer_right'):
                for vertical in ('outer_top', 'top', 'mid', 'bottom', 'outer_bottom'):
                    self.assertIs(node._set_arrange(horizontal, vertical), node)
                    self.assertEqual(node._bnode['arrange_horizontal'], horizontal)
                    self.assertEqual(node._bnode['arrange_vertical'], vertical)
            node._set_arrange(horizontal='left')
            self.assertEqual(node._bnode['arrange_vertical'], 'outer_bottom')
            with self.assertRaises(ValueError):
                node._set_arrange(horizontal='right', vertical='invalid')
            self.assertEqual(node._bnode['arrange_horizontal'], 'left')
            self.assertEqual(node._bnode['arrange_vertical'], 'outer_bottom')


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
