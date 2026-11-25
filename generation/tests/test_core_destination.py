"""Version guards; runnable with plain Python, without Blender."""
import runpy
from types import ModuleType
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


class CoreDestinationTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.core = self.root / 'core_5_2'
        self.core.mkdir()
        (self.root / 'core_5_3').mkdir()
        (self.core / 'constants.py').write_text('from .config_current import *\n')
        self.config = self.core / 'config_current.py'
        self.config.write_text('blender_version = (5, 2, 0)\n')
        self.bpy = SimpleNamespace(app=SimpleNamespace(version=(5, 2, 0)))
        package_folder = Path(__file__).resolve().parents[2]
        versions = ModuleType('geonodes._versions')
        versions.__dict__.update(runpy.run_path(str(package_folder / '_versions.py')))
        with patch.dict(sys.modules, {'bpy': self.bpy, 'geonodes._versions': versions}):
            self.functions = runpy.run_path(
                str(package_folder / 'generation' / '__init__.py'),
                run_name='geonodes.generation.__init__',
            )

    def test_current_version_controls_destination(self):
        self.assertEqual(self.functions['target_core'](self.root), self.core)
        self.bpy.app.version = (5, 3, 0)
        self.assertEqual(self.functions['target_core'](self.root), self.root / 'core_5_3')

    def test_other_versions_cannot_be_overwritten(self):
        before = self.config.read_bytes()
        self.bpy.app.version = (5, 3, 0)
        with self.assertRaisesRegex(RuntimeError, 'must generate into core_5_3'):
            self.functions['target_core'](self.core)
        self.assertEqual(self.config.read_bytes(), before)

    def test_patch_releases_target_same_folder(self):
        self.bpy.app.version = (5, 2, 1)
        self.assertEqual(self.functions['target_core'](self.root), self.core)

    def test_seeded_config_can_be_rebuilt_for_new_version(self):
        # A copied handwritten API can still contain the previous version's config.
        self.config.write_text('blender_version = (5, 1, 0)\n')
        self.assertEqual(self.functions['target_core'](self.root), self.core)

    def test_missing_destination_is_rejected(self):
        self.bpy.app.version = (5, 4, 0)
        with self.assertRaisesRegex(FileNotFoundError, 'core_5_4'):
            self.functions['target_core'](self.root)


if __name__ == '__main__':
    unittest.main()
