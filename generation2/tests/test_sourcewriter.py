"""Run without Blender: python3 -B generation2/tests/test_sourcewriter.py."""
import ast
import itertools
from pathlib import Path
import runpy
import unittest

SourceWriter = runpy.run_path(
    str(Path(__file__).resolve().parents[1] / 'sourcewriter.py')
)['SourceWriter']

TypeAliases = runpy.run_path(
    str(Path(__file__).resolve().parents[1] / 'typealiases.py')
)['TypeAliases']

class SourceWriterTest(unittest.TestCase):
    def test_type_aliases_in_argument_annotations(self):
        aliases = TypeAliases()
        for registry in (None, aliases):
            writer = SourceWriter('build', type_aliases=registry)
            writer.positional_argument('value', ['FLOAT', 'VECTOR'])
            writer.positional_argument('*values', ('VECTOR', 'FLOAT'))
            writer.keyword_argument('mode', "'FLOAT'", ['FLOAT', 'VECTOR'])
            writer.write_header()
            writer.write_doc_string()
            writer.write('return value', indent=1)
            self.assertTrue(writer.check_syntax())
            namespace = {}
            exec(aliases.source if registry is not None else 'from typing import Literal', namespace)
            exec(writer.source, namespace)
            self.assertEqual(namespace['build']('FLOAT'), 'FLOAT')
            if registry is not None:
                self.assertEqual(len(aliases), 1)
                self.assertTrue(all(arg.typing == 'T_VALUE_1' for arg in writer.arguments))
            else:
                self.assertEqual(writer.arguments[0].typing, "Literal['FLOAT', 'VECTOR']")
            self.assertIn("value : {'FLOAT', 'VECTOR'}", namespace['build'].__doc__)

    def test_optional_split_markers_preserve_valid_code(self):
        tokens = runpy.run_path(str(Path(__file__).resolve().parents[1] / 'sourcewriter.py'))
        for token in (tokens['R0'], tokens['R1'], tokens['R2']):
            for limit in (30, 1000):
                with self.subTest(token=token, limit=limit):
                    writer = SourceWriter('build')
                    writer.max_len = limit
                    writer.write(f"def build({token}first_argument=1,{token}second_argument=2):")
                    writer.write('return first_argument + second_argument', indent=1)
                    namespace = {}
                    exec(writer.source, namespace)
                    self.assertEqual(namespace['build'](), 3)
                    self.assertNotIn(token, writer.source)
                    self.assertNotIn('%', writer.source)

    def test_split_length_includes_indentation(self):
        writer = SourceWriter('build')
        writer.max_len = 22
        writer.write('call(§%first,§%second)', indent=1)
        self.assertEqual(writer.source, '    call(\n        first,\n        second)\n')

    def test_plain_newlines_and_multiple_lines(self):
        writer = SourceWriter('build')
        writer.write('first\nsecond', new_line=False)
        self.assertEqual(writer.source, 'first\nsecond')
        writer = SourceWriter('build')
        writer.write('first', 'second')
        self.assertEqual(writer.source, 'first\nsecond\n')

    def test_splittable_sequence_preserves_values(self):
        for values in (["'first'", "'second'", "'third'"],
                       ("'first'", "'second'", "'third'")):
            for limit in (20, 1000):
                writer = SourceWriter('build')
                writer.max_len = limit
                writer.write('value = ' + writer.splittable(values))
                namespace = {}
                exec(writer.source, namespace)
                expected = ['first', 'second', 'third']
                self.assertEqual(namespace['value'], expected if isinstance(values, list) else tuple(expected))


    def test_empty_literal_annotations_are_rejected(self):
        for registry in (None, TypeAliases()):
            for typing in ([], ()):
                writer = SourceWriter('build', type_aliases=registry)
                with self.assertRaises(ValueError):
                    writer.positional_argument('value', typing)
                self.assertEqual(writer.arguments, [])

    def test_explicit_alias_and_plain_annotations_in_documentation(self):
        aliases = TypeAliases()
        alias = aliases.literal(['FLOAT'], prefix='T_VALUE')
        writer = SourceWriter('build', type_aliases=aliases)
        writer.positional_argument('value', alias)
        writer.positional_argument('socket', 'Socket')
        writer.positional_argument('other')
        self.assertEqual(writer.arguments[0].typing, alias)
        self.assertEqual(writer.arguments[0].doc_typing, "{'FLOAT'}")
        self.assertEqual(writer.arguments[1].typing, 'Socket')
        self.assertEqual(writer.arguments[1].doc_typing, 'Socket')
        self.assertIsNone(writer.arguments[2].typing)
        self.assertIsNone(writer.arguments[2].doc_typing)
        for registry in (None, aliases):
            writer = SourceWriter('build', type_aliases=registry)
            writer.positional_argument('value', ['FLOAT'])
            self.assertEqual(writer.arguments[0].doc_typing, "{'FLOAT'}")

    def test_node_calls_preserve_values_in_short_and_multiline_forms(self):
        for limit, args, sockets, parameters in itertools.product(
            (20, 1000), (None, [], ['*values']),
            (None, [], ["'value': value", "'other': 2"]),
            (None, [], ["mode='TEST'", 'enabled=True']),
        ):
            with self.subTest(limit=limit, args=args, sockets=sockets, parameters=parameters):
                writer = SourceWriter('build')
                writer.max_len = limit
                writer.write_header()
                writer.write_node_call("Node's name", args, sockets, parameters)
                writer.write('return node', indent=1)
                self.assertTrue(writer.check_syntax())
                namespace = dict(Node=lambda *a, **kw: (a, kw), values=[3, 4], value=7)
                exec(writer.source, namespace)
                actual_args, actual_kwargs = namespace['build']()
                self.assertEqual(actual_args, ("Node's name", *([3, 4] if args else [])))
                self.assertEqual(actual_kwargs['named_sockets'],
                                 None if sockets is None else ({'value': 7, 'other': 2} if sockets else {}))
                self.assertEqual({k: v for k, v in actual_kwargs.items() if k != 'named_sockets'},
                                 {'mode': 'TEST', 'enabled': True} if parameters else {})

    def test_docstrings_preserve_multiline_text_with_and_without_arguments(self):
        for with_args in (False, True):
            writer = SourceWriter('build')
            writer.add_doc('Summary\nFirst line\nSecond line')
            writer.returns = 'int\n    Result description'
            if with_args:
                writer.positional_argument('value', 'int', 'First comment\nSecond comment')
            writer.write_header()
            writer.write_doc_string()
            namespace = {}
            exec(writer.source, namespace)
            doc = namespace['build'].__doc__
            self.assertIn('First line\n    Second line', doc)
            self.assertNotIn(',\n', doc)

    def test_all_function_kinds_and_wrapped_headers(self):
        for kind in ('FUNCTION', 'STATIC_METHOD', 'METHOD', 'SETTER', 'GETTER',
                     'CLASS_METHOD', 'CLASS_PROPERTY'):
            for limit in (20, 1000):
                with self.subTest(kind=kind, limit=limit):
                    writer = SourceWriter('value', kind)
                    writer.max_len = limit
                    if kind not in ('GETTER', 'CLASS_PROPERTY'):
                        writer.positional_argument('argument_with_a_long_name')
                    writer.write_header()
                    writer.write_doc_string()
                    writer.write('return None', indent=1)
                    self.assertTrue(writer.check_syntax())
                    source = writer.source if kind == 'FUNCTION' else 'class Example:\n' + writer.source
                    tree = ast.parse(source)
                    function = tree.body[0] if kind == 'FUNCTION' else tree.body[0].body[0]
                    expected = {'STATIC_METHOD': 'staticmethod', 'SETTER': 'value.setter',
                                'GETTER': 'property', 'CLASS_METHOD': 'classmethod',
                                'CLASS_PROPERTY': 'utils.classproperty'}.get(kind)
                    self.assertEqual([ast.unparse(d) for d in function.decorator_list],
                                     [expected] if expected else [])


    def test_check_syntax_rejects_invalid_code_without_executing_it(self):
        for kind in ('FUNCTION', 'METHOD'):
            with self.subTest(kind=kind):
                writer = SourceWriter('broken', kind)
                writer.write_header()
                writer.write('return (', indent=1)
                with self.assertRaises(SyntaxError):
                    writer.check_syntax()

        writer = SourceWriter('not_executed')
        writer.write_header()
        writer.write("raise RuntimeError('must not execute')", indent=1)
        self.assertTrue(writer.check_syntax())

        # Compilation also rejects constructs accepted by ast.parse.
        writer = SourceWriter('invalid_break')
        writer.write_header()
        writer.write('break', indent=1)
        with self.assertRaises(SyntaxError):
            writer.check_syntax()


if __name__ == '__main__':
    unittest.main()
