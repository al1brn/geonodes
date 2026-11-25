"""Run directly with Python; verifies isolation without starting Blender."""
import importlib
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from types import ModuleType, SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]


class VersionContextTest(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        generation = self.root / 'generation'
        generation.mkdir()
        (generation / '__init__.py').write_text('')
        shutil.copy2(ROOT / '_versions.py', self.root / '_versions.py')
        shutil.copy2(ROOT / 'generation/context.py', generation / 'context.py')
        self.bpy = SimpleNamespace(app=SimpleNamespace(version=(5, 3, 0)))
        package = ModuleType('_version_context_fixture')
        package.__path__ = [str(self.root)]
        modules = patch.dict(sys.modules, {'_version_context_fixture': package, 'bpy': self.bpy})
        modules.start()
        self.addCleanup(modules.stop)

    def prepare(self, minor):
        core = self.root / f'core_5_{minor}'
        core.mkdir()
        (core / '__init__.py').write_text('raise AssertionError("Core API initialized")\n')
        shutil.copytree(ROOT / 'core_5_3/kernel', core / 'kernel',
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        with (core / 'kernel/constants.py').open('a') as stream:
            stream.write(f'\nCLASS_NAMES["TEST_ORIGIN"] = "kernel_5_{minor}"\n')
        data = self.root / 'generation' / f'api_5_{minor}'
        data.mkdir()
        (data / '__init__.py').write_text('')
        config = (ROOT / 'generation/api_5_3/config.py').read_text()
        (data / 'config.py').write_text(config + f'\nTEST_ORIGIN = "config_5_{minor}"\n')
        (data / 'node_dims.py').write_text(f'NODE_DIMS = {{"origin": {minor}}}\n')

    def load(self):
        return importlib.import_module('_version_context_fixture.generation.context')

    def test_loads_kernel_and_descriptions_without_initializing_api(self):
        self.prepare(3)
        context = self.load()
        self.assertEqual(context.CLASS_NAMES['TEST_ORIGIN'], 'kernel_5_3')
        self.assertEqual(context.config.TEST_ORIGIN, 'config_5_3')
        self.assertEqual(context.node_dims.NODE_DIMS['origin'], 3)
        self.assertNotIn('_version_context_fixture.core_5_3', sys.modules)

    def test_versioned_tables_are_independent(self):
        self.prepare(3)
        self.prepare(4)
        context = self.load()
        previous_kernel, previous_config = context.kernel, context.config
        self.bpy.app.version = (5, 4, 0)
        context = importlib.reload(context)
        self.assertEqual(context.CLASS_NAMES['TEST_ORIGIN'], 'kernel_5_4')
        self.assertEqual(context.config.TEST_ORIGIN, 'config_5_4')
        self.assertEqual(previous_kernel.CLASS_NAMES['TEST_ORIGIN'], 'kernel_5_3')
        self.assertEqual(previous_config.TEST_ORIGIN, 'config_5_3')
        self.assertIsNot(previous_kernel, context.kernel)

    def test_missing_generation_data_is_explicit(self):
        with self.assertRaisesRegex(FileNotFoundError, 'api_5_3'):
            self.load()

    def test_missing_kernel_is_explicit(self):
        self.prepare(3)
        shutil.rmtree(self.root / 'core_5_3/kernel')
        with self.assertRaisesRegex(FileNotFoundError, 'Kernel package not found'):
            self.load()


if __name__ == '__main__':
    unittest.main()
