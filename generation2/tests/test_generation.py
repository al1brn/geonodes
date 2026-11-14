"""Run without Blender: python3 -B generation2/tests/test_generation.py."""
import ast
from contextlib import ExitStack, redirect_stdout
from io import StringIO
from pathlib import Path
import runpy
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
fixture = runpy.run_path(str(ROOT / 'tests/generation_fixtures.py'))
namespace = fixture['namespace']
TreeClass, generate = namespace['TreeClass'], namespace['generate']
STEPS = ('gen_static_code', 'gen_math', 'gen_compare', 'gen_mix', 'gen_nodes',
         'gen_properties', 'gen_typed_constructors', 'gen_additional')


class GenerationTest(unittest.TestCase):
    def test_config_failure_prevents_collection_and_writing(self):
        with patch.object(namespace['gen_config'], 'build', side_effect=RuntimeError('unknown socket')):
            with patch.object(TreeClass, 'generate') as collect, patch.object(Path, 'write_text') as write:
                with self.assertRaisesRegex(RuntimeError, 'unknown socket'):
                    generate()
                collect.assert_not_called()
                write.assert_not_called()

    def test_single_environment_and_instance_state(self):
        events = []
        with ExitStack() as stack:
            stack.enter_context(patch.object(namespace['gen_config'], 'build', side_effect=lambda: events.append('config')))
            for step in STEPS:
                stack.enter_context(patch.object(TreeClass, step, autospec=True,
                    side_effect=lambda obj, step=step: events.append((step, obj.tree_type))))
            with redirect_stdout(StringIO()):
                first = generate(tree_type='ShaderNodeTree', write=False)
                second = generate(write=False)
        self.assertEqual(events[0], 'config')
        self.assertEqual(events[1:9], [(step, 'ShaderNodeTree') for step in STEPS])
        self.assertEqual(set(first), {'ShaderNodeTree'})
        geometry, shader = second.values()
        self.assertIsNot(geometry.files, shader.files)
        self.assertIsNot(geometry.type_aliases, shader.type_aliases)
        self.assertIsNot(first['ShaderNodeTree'], shader)
        self.assertIs(geometry.implementation(Mock(snapshot_params=lambda: {})).type_aliases, geometry.type_aliases)
        self.assertFalse(hasattr(namespace['NodeImplementation'], 'generate'))
        self.assertFalse(hasattr(namespace['NodeImplementation'], 'files'))

    def test_all_environments_validate_before_any_write(self):
        geometry = TreeClass('GeometryNodeTree')
        shader = TreeClass('ShaderNodeTree')
        with patch.object(geometry, 'render_modules', return_value={Path('/tmp/never_written.py'): 'pass'}):
            with patch.object(shader, 'render_modules', side_effect=ValueError('invalid shader')):
                with patch.object(Path, 'write_text') as write:
                    with self.assertRaisesRegex(ValueError, 'invalid shader'):
                        namespace['write_files']({'GeometryNodeTree': geometry, 'ShaderNodeTree': shader})
                    write.assert_not_called()

    def test_unknown_socket_class_reports_mapping(self):
        tree = ast.parse((ROOT / 'gen_config.py').read_text())
        method = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'check_socket_classes')
        with TemporaryDirectory() as folder:
            env = {'ast': ast, 'target_core': lambda **kw: Path(folder), 'config': namespace['config']}
            exec(compile(ast.Module(body=[method], type_ignores=[]), '<check classes>', 'exec'), env)
            sockets = {'NEW_TYPE': {'class_name': 'NewType', 'GeometryNodeTree': 'NodeSocketNew', 'ShaderNodeTree': None}}
            with self.assertRaisesRegex(RuntimeError, 'NEW_TYPE -> NewType'):
                env['check_socket_classes'](sockets)


if __name__ == '__main__':
    unittest.main()
