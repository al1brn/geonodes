"""Run with Blender --background --python generation/tests/test_color_parameters.py."""
from pathlib import Path
from types import SimpleNamespace
import sys
import unittest

import bpy

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from geonodes.generation.node_param import NodeParam
from geonodes.generation.node_call import NodeCall
from geonodes.generation.node_implementation import NodeImplementation
from geonodes.generation.node_info import NodeInfo


class ColorParameterTest(unittest.TestCase):
    def test_rna_colors_preserve_components_and_define_tuple_typing(self):
        for subtype, value in [('COLOR', (0.1, 0.2, 0.3, 1.0)),
                               ('COLOR_GAMMA', (0.1, 0.2, 0.3))]:
            prop = SimpleNamespace(type='FLOAT', is_array=True, subtype=subtype)
            node = SimpleNamespace(value=value, bl_rna=SimpleNamespace(properties={'value': prop}))
            param = NodeParam.Parameter(node, 'value')
            self.assertEqual(param.param_type, 'Color')
            self.assertEqual(param.value, value)
            self.assertEqual(param.typing, 'tuple[' + ', '.join(['float'] * len(value)) + ']')
            self.assertEqual(param.arg_value, repr(value))

    def test_blender_color_is_retained_in_snapshot_and_generated_signature(self):
        tree = bpy.data.node_groups.new('Color Parameter Test', 'GeometryNodeTree')
        try:
            node = tree.nodes.new('FunctionNodeInputColor')
            node.value = (0.25, 0.5, 0.75, 1.0)
            info = NodeInfo(tree, node)
            snapshot = info.snapshot_params()['value']
            self.assertEqual(snapshot['type'], 'Color')
            self.assertEqual(snapshot['value'], (0.25, 0.5, 0.75, 1.0))
            source, = NodeImplementation(info).gen_source_code(
                NodeCall.class_method('color', class_name='nd'))
            self.assertIn('value: tuple[float, float, float, float]', source)
            self.assertIn('value=value', source)
            compile('from __future__ import annotations\nclass Methods:\n' + source, '<color>', 'exec')
        finally:
            bpy.data.node_groups.remove(tree)


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
