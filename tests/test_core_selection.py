"""Run with Python directly; no Blender or public API import required."""
import runpy
import tempfile
import unittest
from pathlib import Path

select_core = runpy.run_path(
    str(Path(__file__).resolve().parents[1] / '_versions.py')
)['select_core']


class CoreSelectionTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def api(self, name, version):
        folder = self.root / name
        folder.mkdir()
        (folder / '__init__.py').write_text('raise AssertionError("API imported")\n')
        (folder / 'constants.py').write_text(
            '# from .config_obsolete import *\nfrom .config_current import *\n'
        )
        (folder / 'config_current.py').write_text(
            f'blender_version = {version!r}\nraise AssertionError("Config executed")\n'
        )

    def test_loads_matching_named_core_without_executing_api(self):
        self.api('core_5_3', (5, 3, 0))
        self.assertEqual(select_core(self.root, (5, 3, 0)), 'core_5_3')

    def test_installed_versions_are_independent(self):
        self.api('core_5_2', (5, 2, 0))
        self.api('core_5_3', (5, 3, 0))
        self.assertEqual(select_core(self.root, (5, 2, 0)), 'core_5_2')
        self.assertEqual(select_core(self.root, (5, 3, 0)), 'core_5_3')

    def test_patch_releases_share_the_minor_core(self):
        self.api('core_5_3', (5, 3, 0))
        self.assertEqual(select_core(self.root, (5, 3, 2)), 'core_5_3')

    def test_missing_version_has_no_fallback(self):
        self.api('core_5_3', (5, 3, 0))
        for version in ((5, 2, 0), (5, 4, 0)):
            with self.subTest(version=version):
                with self.assertRaisesRegex(RuntimeError, 'No API installed'):
                    select_core(self.root, version)

    def test_wrong_configuration_is_rejected(self):
        self.api('core_5_3', (5, 2, 0))
        with self.assertRaisesRegex(RuntimeError, 'configuration for Blender'):
            select_core(self.root, (5, 3, 0))

    def test_no_installed_api(self):
        with self.assertRaisesRegex(RuntimeError, 'missing core_5_3'):
            select_core(self.root, (5, 3, 0))


if __name__ == '__main__':
    unittest.main()
