"""Check alias generation without Blender: python3 -B generation2/tests/test_alias_generation.py."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy
from types import SimpleNamespace as NS
from typing import get_args, get_type_hints
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
fixture = runpy.run_path(str(ROOT / 'tests/generation_fixtures.py'))
namespace, CORE = fixture['namespace'], fixture['CORE']
TreeClass, generate = namespace['TreeClass'], namespace['generate']
attach_arguments = runpy.run_path(str(ROOT / 'tests/argument_fixtures.py'))['attach_arguments']
STEPS = ('gen_static_code', 'gen_math', 'gen_compare', 'gen_mix', 'gen_nodes',
         'gen_properties', 'gen_typed_constructors', 'gen_additional')


def make_node(values):
    params = {'data_type': {'type': 'ENUM', 'value': values[0], 'enums': values}}
    return attach_arguments(NS(name='Example', bl_idname='TestNode', data_type_parameter=None,
        config_order=['data_type'], default_params=params, has_items=False,
        get_possible_sockets=lambda **kw: []))


class AliasGenerationTest(unittest.TestCase):
    def setUp(self):
        self.patches = [patch.object(TreeClass, step, autospec=True) for step in STEPS]
        self.steps = [p.start() for p in self.patches]
        for p in self.patches:
            self.addCleanup(p.stop)

    def collect(self, tree):
        values = ['FLOAT', 'VECTOR'] if tree.tree_type == 'GeometryNodeTree' else ['COLOR']
        implementation = tree.implementation(make_node(values))
        copied = implementation.copy()
        self.assertIs(copied.type_aliases, tree.type_aliases)
        sources = [obj.gen_node_call(namespace['NodeCall'].function(name))
                   for obj, name in ((implementation, 'example'), (copied, 'other'))]
        tree.files[tree.tree_type]['gnmath.py'] = sources
        self.assertEqual(len(tree.type_aliases), 1)

    def test_generation_collects_importable_aliases_per_environment_and_resets(self):
        self.steps[0].side_effect = self.collect
        previous = None
        for unused in range(2):
            with redirect_stdout(StringIO()):
                trees = generate(write=False)
            for tree_type, tree in trees.items():
                sources = tree.files[tree_type]
                aliases = {}
                exec(sources['type_aliases.py'][0], aliases)
                exec('\n'.join(sources['gnmath.py']), aliases)
                expected = ('FLOAT', 'VECTOR') if tree_type == 'GeometryNodeTree' else ('COLOR',)
                self.assertEqual(get_args(get_type_hints(aliases['example'])['data_type']), expected)
                self.assertIn('T_DATA_TYPE_1', aliases)
                self.assertNotIn('T_DATA_TYPE_2', aliases)
                modules = tree.render_modules(CORE)
                folder = CORE / namespace['config'].TREE_MODULES[tree_type] / 'generated'
                self.assertEqual(modules[folder / 'type_aliases.py'], sources['type_aliases.py'][0])
                self.assertIn('from .type_aliases import T_DATA_TYPE_1', modules[folder / 'gnmath.py'])
                if previous is not None:
                    self.assertIsNot(tree.type_aliases, previous[tree_type].type_aliases)
            previous = trees

    def test_empty_registry_still_produces_module(self):
        with redirect_stdout(StringIO()):
            trees = generate(tree_type='ShaderNodeTree', write=False)
        modules = trees['ShaderNodeTree'].render_modules(CORE)
        self.assertIn(CORE / 'shadernodes/generated/type_aliases.py', modules)

    def test_write_files_writes_the_alias_module(self):
        self.steps[0].side_effect = self.collect
        with redirect_stdout(StringIO()):
            trees = generate(tree_type='ShaderNodeTree', write=False)
        with patch.object(Path, 'mkdir'), patch.object(Path, 'write_text') as write:
            with redirect_stdout(StringIO()):
                namespace['write_files'](trees)
        self.assertTrue(any('T_DATA_TYPE_1 = Literal' in call.args[0] for call in write.call_args_list))


if __name__ == '__main__':
    unittest.main()
