"""Run without Blender: python3 -B generation2/tests/test_typealiases.py."""

from pathlib import Path
import runpy
from typing import get_args
import unittest

TypeAliases = runpy.run_path(
    str(Path(__file__).resolve().parents[1] / 'typealiases.py')
)['TypeAliases']


class TypeAliasesTest(unittest.TestCase):
    def test_reuses_equivalent_literals_and_numbers_new_ones(self):
        aliases = TypeAliases()
        self.assertEqual(aliases.literal(['FLOAT', 'VECTOR']), 'DATA_TYPE_1')
        self.assertEqual(aliases.literal(['VECTOR', 'FLOAT', 'FLOAT']), 'DATA_TYPE_1')
        self.assertEqual(aliases.literal(['FLOAT', 'VECTOR'], prefix='OTHER'), 'DATA_TYPE_1')
        self.assertEqual(aliases.literal(['FLOAT', 'VECTOR', 'COLOR']), 'DATA_TYPE_2')
        self.assertEqual(aliases.literal(['POINT', 'EDGE'], prefix='DOMAIN'), 'DOMAIN_1')
        self.assertEqual(len(aliases), 3)
        self.assertEqual(len(TypeAliases()), 0)

    def test_generated_module_compiles_and_preserves_values(self):
        aliases = TypeAliases(max_len=40)
        values = ['FLOAT', 'VECTOR', 'COLOR', "quote'", 'new\nline', 'back\\slash']
        name = aliases.literal(iter(values))
        self.assertIn('Literal[\n', aliases.source)
        namespace = {}
        exec(compile(aliases.source, '<aliases>', 'exec'), namespace)
        self.assertEqual(get_args(namespace[name]), tuple(values))
        self.assertTrue(all(len(line) <= 40 for line in aliases.source.splitlines()))
        exec(f"def f(data_type: {name} = 'FLOAT'):\n    return data_type", namespace)
        self.assertEqual(namespace['f'](), 'FLOAT')

    def test_distinguishes_boolean_and_integer_literals(self):
        aliases = TypeAliases()
        self.assertNotEqual(aliases.literal([True]), aliases.literal([1]))

    def test_get_doc_string_expands_aliases_and_preserves_other_annotations(self):
        aliases = TypeAliases()
        name = aliases.literal(['FLOAT', 'VECTOR', 'FLOAT'])
        self.assertEqual(aliases.get_doc_string(name), "{'FLOAT', 'VECTOR'}")
        name = aliases.literal([True, 1, None])
        self.assertEqual(aliases.get_doc_string(name), '{True, 1, None}')
        for key in ('Socket', 'UNKNOWN_1', '', None):
            self.assertEqual(aliases.get_doc_string(key), key)

    def test_empty_registry_and_invalid_values(self):
        aliases = TypeAliases()
        compile(aliases.source, '<empty aliases>', 'exec')
        for values in ([],):
            with self.assertRaises(ValueError):
                aliases.literal(values)
        for values in ('FLOAT', [1.5], [[]]):
            with self.assertRaises(TypeError):
                aliases.literal(values)
        for prefix in ('bad-name', 'class', ''):
            with self.assertRaises(ValueError):
                aliases.literal(['FLOAT'], prefix=prefix)
        self.assertEqual(len(aliases), 0)


if __name__ == '__main__':
    unittest.main()
