"""Run without Blender: python3 generation/tests/test_node_call_duplicates.py."""
from dataclasses import fields
from pathlib import Path
import runpy
import unittest

api = runpy.run_path(str(Path(__file__).resolve().parents[1] / 'node_call.py'))
NodeCall, NodeCalls = api['NodeCall'], api['NodeCalls']


class DuplicateCallsTest(unittest.TestCase):
    def setUp(self):
        self.base = NodeCall.method('value', class_name='Float', self_socket='Value',
                                    parameters={'options': {'A', 'B'}},
                                    fixed_sockets={'Min': [0, 1]})

    def test_equality_ignores_only_metadata(self):
        self.assertEqual(self.base, self.base.replace(category='Other', rules='Other rule'))
        for field in fields(self.base):
            if field.compare:
                with self.subTest(field=field.name):
                    other = self.base.replace()
                    setattr(other, field.name, object())
                    self.assertNotEqual(self.base, other)
        self.assertIs(self.base.__eq__(object()), NotImplemented)
        with self.assertRaises(TypeError):
            hash(self.base)

    def test_constructor_and_assemblies_keep_first(self):
        duplicate = self.base.replace(rules='another route')
        other = self.base.replace(method_name='other')
        calls = NodeCalls(self.base, duplicate, other)
        self.assertEqual(len(calls), 2)
        self.assertIs(calls[0], self.base)
        calls.append(duplicate)
        calls.extend([duplicate, other])
        calls += [duplicate]
        calls.extend(calls)
        self.assertEqual(calls, [self.base, other])
        list.append(calls, duplicate)
        self.assertIs(calls.remove_duplicates(), calls)
        self.assertEqual(calls, [self.base, other])

    def test_replace_and_overrides_collapse_converging_variants(self):
        calls = NodeCalls(self.base, self.base.replace(method_name='other'))
        result = calls.replace(method_name='same')
        self.assertEqual(len(result), 1)
        self.assertEqual(len(calls), 2)
        result = calls.overrides([{'method_name': 'same'}, {'method_name': 'same'}])
        self.assertEqual(len(result), 1)

    def test_conflicting_implementations_remain_distinct(self):
        calls = NodeCalls(self.base, self.base.replace(parameters={'mode': 'OTHER'}),
                          self.base.replace(return_socket='Result'))
        self.assertEqual(len(calls), 3)

    def test_random_constructor_and_method_converge(self):
        constructor = NodeCalls.class_method('RandomValue', category='Constructor')
        method = NodeCalls.method('random_value', self_socket='Min', category='Method')
        override = dict(method_type='CLASS_METHOD', method_name='Random', self_socket=None)
        calls = constructor.overrides(override)
        calls.extend(method.overrides(override))
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0].method_name, 'Random')


if __name__ == '__main__':
    unittest.main()
