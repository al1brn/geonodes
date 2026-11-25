"""Run without Blender: python3 generation/tests/test_compare_versions.py."""
from pathlib import Path
import runpy
import tempfile
import unittest

api = runpy.run_path(str(Path(__file__).resolve().parents[1] / 'compare_versions.py'))


class CompareVersionsTest(unittest.TestCase):
    def test_argument_append_and_insert_for_class_and_static_methods(self):
        before = {'signatures': {
            ('Vector', 'example', False, False, False): '(self, vector=(1, 2, 3), scale=None)',
            ('nd', 'example', False, False, True): '(cls, vector=(1, 2, 3), scale=None)',
        }}
        after = {'signatures': {
            ('Vector', 'example', False, False, False): '(self, vector=(1, 2, 3), scale=None, extra=None)',
            ('nd', 'example', False, False, True): '(cls, vector=(1, 2, 3), extra=None, scale=None)',
        }}
        changes = api['compare_arguments'](before, after)
        self.assertEqual(changes, [
            {'method': 'Vector.example', 'kind': 'appended', 'arguments': ['extra']},
            {'method': 'nd.example', 'kind': 'inserted', 'arguments': ['extra']},
        ])

    def test_argument_removal_reordering_and_default_changes_are_not_additions(self):
        key = ('Float', 'example', False, False, False)
        before = {'signatures': {key: '(self, a=None, b=None)'}}
        for signature in ('(self, b=None)', '(self, b=None, a=None, extra=None)',
                          '(self, a=1, b=2)'):
            with self.subTest(signature=signature):
                self.assertEqual(api['compare_arguments'](
                    before, {'signatures': {key: signature}}
                ), [])

    def test_keyword_only_and_variadic_argument_order(self):
        self.assertEqual(
            api['_argument_names']('(cls, value=None, /, *items, factor=None, **sockets)'),
            ['value', '*items', 'factor', '**sockets'],
        )

    def test_modified_node_has_signatures_from_each_version(self):
        with tempfile.TemporaryDirectory() as directory:
            paths = []
            for label, signature, mode in (
                ('old', '(self, value=None)', 'OLD'),
                ('new', '(self, value=None, extra=None)', 'NEW'),
            ):
                core = Path(directory) / label
                generated = core / 'geonodes/generated'
                generated.mkdir(parents=True)
                path = core / 'config.py'
                names = {'GeometryNodeTree': {'Example': 'A'}}
                info = {'A': {'params': {'mode': mode}}}
                path.write_text(f'NODE_NAMES = {names!r}\nNODE_INFO = {info!r}\n')
                refs = {'A': {'Float': [{'func_name': 'example', 'signature': signature}]}}
                (generated / 'cross_reference.py').write_text(f'CROSS_REF = {refs!r}\n')
                paths.append(path)
            result = api['compare_versions'](*paths)
            entry = result['trees']['GeometryNodeTree']['modified']['A']
            self.assertEqual(entry['old_implementations']['headers'], ['Float.example(self, value=None)'])
            self.assertEqual(entry['new_implementations']['headers'], ['Float.example(self, value=None, extra=None)'])
            report = api['render_report'](result)
            old_section = report.split('##### Old version', 1)[1].split('##### New version', 1)[0]
            new_section = report.split('##### New version', 1)[1].split('##### Changes', 1)[0]
            self.assertIn('Float.example(self, value=None)', old_section)
            self.assertNotIn('extra', old_section)
            self.assertIn('extra=None', new_section)
            self.assertIn('OLD', report)
            self.assertIn('NEW', report)
            self.assertIn('Float.example` — arguments appended: `extra`', report)

    def test_added_node_headers_and_static_only_from_cross_references(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            old, new = root / 'old.py', root / 'new.py'
            old.write_text("NODE_NAMES = {'GeometryNodeTree': {}}\nNODE_INFO = {}\n")
            names = {'GeometryNodeTree': {'Construct': 'A', 'Input': 'B', 'Unknown': 'C'}}
            new.write_text(f'NODE_NAMES = {names!r}\nNODE_INFO = {{}}\n')
            generated = root / 'geonodes/generated'
            generated.mkdir(parents=True)
            references = {
                'A': {
                    'nd': [{'func_name': 'construct', 'signature': '(cls)'}],
                    'Vector': [{'func_name': 'Construct', 'signature': '(cls, value=None)',
                                'is_classmethod': True}],
                    'Float': [{'func_name': 'construct', 'signature': '(self, value=None)'}],
                },
                'B': {'nd': [{'func_name': 'input', 'signature': '(cls)'}]},
            }
            # The reader must parse data without executing the file.
            (generated / 'cross_reference.py').write_text(
                "raise RuntimeError('must not execute')\n" + f'CROSS_REF = {references!r}\n'
            )
            result = api['compare_versions'](old, new)
            entries = result['trees']['GeometryNodeTree']['added_implementations']
            self.assertIn('@classmethod Vector.Construct(cls, value=None)', entries['A']['headers'])
            self.assertIn('Float.construct(self, value=None)', entries['A']['headers'])
            self.assertFalse(entries['A']['static_only'])
            self.assertTrue(entries['B']['static_only'])
            self.assertFalse(entries['C']['static_only'])
            report = api['render_report'](result)
            self.assertIn('Static only', report)
            self.assertIn('Vector.Construct', report)
            self.assertNotIn('nd.construct', report)
            self.assertIn('Implémentations non renseignées', report)

    def test_missing_cross_reference_does_not_claim_static_only(self):
        with tempfile.TemporaryDirectory() as directory:
            entries = api['implementation_headers'](directory, 'ShaderNodeTree', ['A'])
            self.assertEqual(entries['A'], {'headers': [], 'static_only': False, 'signatures': {}})

    def test_cross_references_are_selected_per_environment(self):
        with tempfile.TemporaryDirectory() as directory:
            for environment, class_name in (('geonodes', 'Float'), ('shadernodes', 'Shader')):
                folder = Path(directory) / environment / 'generated'
                folder.mkdir(parents=True)
                refs = {'A': {class_name: [{'func_name': 'method', 'signature': '(self)'}]}}
                (folder / 'cross_reference.py').write_text(f'CROSS_REF = {refs!r}\n')
            geo = api['implementation_headers'](directory, 'GeometryNodeTree', ['A'])
            shader = api['implementation_headers'](directory, 'ShaderNodeTree', ['A'])
            self.assertEqual(geo['A']['headers'], ['Float.method(self)'])
            self.assertEqual(shader['A']['headers'], ['Shader.method(self)'])

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
