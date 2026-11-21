"""Run without Blender: python3 generation2/tests/test_compare_versions.py."""
from pathlib import Path
import runpy
import tempfile
import unittest

api = runpy.run_path(str(Path(__file__).resolve().parents[1] / 'compare_versions.py'))


class CompareVersionsTest(unittest.TestCase):
    def test_changes_by_identifier_and_environment(self):
        with tempfile.TemporaryDirectory() as directory:
            paths = [Path(directory) / name for name in ('old.py', 'new.py')]
            tables = [
                ({'Geo': {'Before': 'A', 'Removed': 'B', 'Layout': 'D'},
                  'Shader': {'Before': 'A'}},
                 {'A': {'params': {'mode': ['X']}, 'dims': (1, 2)}, 'B': {}, 'D': {'dims': (1, 2)}}),
                ({'Geo': {'After': 'A', 'Added': 'C', 'Layout': 'D'}, 'Shader': {}},
                 {'A': {'params': {'mode': ['X', 'Y']}}, 'C': {}, 'D': {'dims': (9, 9)}}),
            ]
            for path, (names, info) in zip(paths, tables):
                path.write_text(f'NODE_NAMES = {names!r}\nNODE_INFO = {info!r}\n')
            result = api['compare_versions'](*paths)
            geo = result['trees']['Geo']
            self.assertEqual(geo['removed'], {'B': 'Removed'})
            self.assertEqual(geo['added'], {'C': 'Added'})
            self.assertEqual(set(geo['modified']), {'A'})
            self.assertEqual(len(geo['modified']['A']['changes']), 2)
            self.assertEqual(result['trees']['Shader']['removed'], {'A': 'Before'})
            self.assertIn('D', api['compare_versions'](*paths, include_dimensions=True)['trees']['Geo']['modified'])
            self.assertIn('Nœuds modifiés (1)', api['render_report'](result))
            self.assertFalse(api['compare_versions'](paths[0], paths[0])['trees']['Geo']['modified'])

    def test_config_is_not_executed(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'config.py'
            path.write_text("raise RuntimeError('must not run')\nNODE_NAMES = {}\nNODE_INFO = {}\n")
            self.assertEqual(api['read_config'](path)['NODE_INFO'], {})
            path.write_text('NODE_NAMES = {}\n')
            with self.assertRaisesRegex(ValueError, 'NODE_INFO'):
                api['read_config'](path)


if __name__ == '__main__':
    unittest.main()
