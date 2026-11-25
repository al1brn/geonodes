"""Run with Blender --background --python generation/tests/test_additional_type_loops.py."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from geonodes.generation import config, gen_config
from geonodes.generation.tree_class import TreeClass


class AdditionalTypeLoopsTest(unittest.TestCase):
    def test_repeated_generation_preserves_config_and_resolves_receivers(self):
        expected = deepcopy(config.ADDITIONAL_IMPLEMENTATIONS)
        gen_config.build()
        for _ in range(2):
            for tree_type in ('GeometryNodeTree', 'ShaderNodeTree'):
                tree = TreeClass(tree_type)
                tree.gen_additional()
                for class_name, identifier in (('float', 'Value'), ('vector', 'Vector')):
                    sources = tree.files[tree_type][class_name + '.py']
                    source = next(s for s in sources if 'def interpolate(' in s)
                    self.assertIn(f"'ID_{identifier}': self", source)
                    compile('from __future__ import annotations\nclass Methods:\n' + source,
                            '<interpolate>', 'exec')
                self.assertEqual(config.ADDITIONAL_IMPLEMENTATIONS, expected)


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
