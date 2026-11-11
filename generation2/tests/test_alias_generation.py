"""Check alias generation without Blender: python3 -B generation2/tests/test_alias_generation.py."""
import ast
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy
from types import SimpleNamespace as NS
from typing import get_args, get_type_hints
import unittest
from unittest.mock import patch

GENERATION = Path(__file__).resolve().parents[1]
CORE = GENERATION.parent / 'core_new'
writer_module = runpy.run_path(str(GENERATION / 'sourcewriter.py'))
TypeAliases = runpy.run_path(str(GENERATION / 'typealiases.py'))['TypeAliases']
output = runpy.run_path(str(GENERATION / 'output.py'))

# Load the real class without importing bpy or initializing the geonodes package.
implementation_path = GENERATION / 'node_implementation.py'
implementation_class = next(node for node in ast.parse(implementation_path.read_text()).body
                            if isinstance(node, ast.ClassDef) and node.name == 'NodeImplementation')
namespace = dict(
    NodeCalls=runpy.run_path(str(GENERATION / "node_call.py"))["NodeCalls"],
    NodeCall=runpy.run_path(str(GENERATION / "node_call.py"))["NodeCall"],
    __file__=str(implementation_path), TypeAliases=TypeAliases,
    SourceWriter=writer_module['SourceWriter'], FUNC_TYPE=writer_module['FUNC_TYPE'],
    get_args=get_args, ENVIRONMENTS=output['ENVIRONMENTS'],
    render_modules=output['render_modules'], Path=Path,
    core_module=NS(utils=NS(snake_case=lambda name: name.lower())),
)
exec(compile(ast.Module(body=[implementation_class], type_ignores=[]), str(implementation_path), 'exec'), namespace)
Implementation = namespace['NodeImplementation']

STEPS = ('gen_static_code', 'gen_math', 'gen_compare', 'gen_mix', 'gen_nodes',
         'gen_properties', 'gen_typed_constructors', 'gen_additional')


def make_node(values):
    params = {'data_type': {'type': 'ENUM', 'value': values[0], 'enums': values}}
    return NS(name='Example', config_order=['data_type'], config={'data_type': {}},
              default_params=params, snapshot_params=lambda: params,
              get_possible_sockets=lambda **kwargs: [], has_items=False, items_with_name=False)


class AliasGenerationTest(unittest.TestCase):
    def setUp(self):
        self.saved = Implementation.files, Implementation.cross_refs, Implementation.type_aliases
        Implementation.files, Implementation.cross_refs = {}, {}
        self.patches = [patch.object(Implementation, step) for step in STEPS]
        self.steps = [p.start() for p in self.patches]
        self.addCleanup(self.restore)

    def restore(self):
        for p in reversed(self.patches):
            p.stop()
        Implementation.files, Implementation.cross_refs, Implementation.type_aliases = self.saved

    def collect(self):
        values = ['FLOAT', 'VECTOR'] if Implementation.tree_type == 'GeometryNodeTree' else ['COLOR']
        implementation = Implementation(make_node(values))
        copied = implementation.copy()
        self.assertIs(copied.type_aliases, implementation.type_aliases)
        sources = [obj._gen_source(name, method_type='FUNCTION')
                   for obj, name in ((implementation, 'example'), (copied, 'other'))]
        Implementation.files[Implementation.tree_type]['gnmath.py'] = sources
        self.assertEqual(len(Implementation.type_aliases), 1)

    def test_generation_collects_importable_aliases_per_environment_and_resets(self):
        self.steps[0].side_effect = self.collect
        for unused in range(2):
            with redirect_stdout(StringIO()):
                Implementation.generate(write=False)
            for tree_type, sources in Implementation.files.items():
                aliases = {}
                exec(sources['type_aliases.py'][0], aliases)
                exec('\n'.join(sources['gnmath.py']), aliases)
                expected = ('FLOAT', 'VECTOR') if tree_type == 'GeometryNodeTree' else ('COLOR',)
                annotation = get_type_hints(aliases['example'])['data_type']
                self.assertEqual(get_args(annotation), expected)
                self.assertIn('T_DATA_TYPE_1', aliases)
                self.assertNotIn('T_DATA_TYPE_2', aliases)
                modules = output['render_modules'](CORE, tree_type, sources)
                folder = CORE / output['ENVIRONMENTS'][tree_type] / 'generated'
                self.assertEqual(modules[folder / 'type_aliases.py'], sources['type_aliases.py'][0])
                self.assertIn('from .type_aliases import T_DATA_TYPE_1', modules[folder / 'gnmath.py'])
            self.assertIs(Implementation.type_aliases, self.saved[2])

    def test_empty_registry_still_produces_module(self):
        with redirect_stdout(StringIO()):
            Implementation.generate(tree_type='ShaderNodeTree', write=False)
        sources = Implementation.files['ShaderNodeTree']
        modules = output['render_modules'](CORE, 'ShaderNodeTree', sources)
        self.assertIn(CORE / 'shadernodes/generated/type_aliases.py', modules)

    def test_write_files_writes_the_alias_module(self):
        self.steps[0].side_effect = self.collect
        with redirect_stdout(StringIO()):
            Implementation.generate(tree_type='ShaderNodeTree', write=False)
        with patch.object(Path, 'mkdir'), patch.object(Path, 'write_text') as write:
            with redirect_stdout(StringIO()):
                Implementation.write_files()
        self.assertTrue(any('T_DATA_TYPE_1 = Literal' in call.args[0] for call in write.call_args_list))


if __name__ == '__main__':
    unittest.main()
