"""Run without Blender: python3 -B generation2/tests/test_node_argument.py."""
from copy import deepcopy
from pathlib import Path
import runpy
from types import SimpleNamespace as NS
import unittest

ROOT = Path(__file__).resolve().parents[1]
module = runpy.run_path(str(ROOT / 'node_argument.py'))
NodeArgument = module['NodeArgument']
TypeAliases = runpy.run_path(str(ROOT / 'typealiases.py'))['TypeAliases']


def socket(name='Value', **options):
    return NS(**(dict(identifier='Value', socket_name=name, class_name='Float',
                     is_multi=False, group_name=None, names={name}) | options))


def parameter(name='mode', value='A', **options):
    return NS(**(dict(name=name, value=value, typing=['A', 'B'],
                     param_type='ENUM', enums=['A', 'B']) | options))


class NodeArgumentTest(unittest.TestCase):
    def test_free_socket_and_independent_receiver_contexts(self):
        source = socket()
        before = deepcopy(vars(source))
        free = NodeArgument(source, 'value_1')
        receiver = NodeArgument(source, 'value_1', role='SELF')
        self.assertEqual(free.get_header(), ['value_1: Float=None'])
        self.assertEqual(free.get_node_call().named_sockets, {'ID_Value': 'value_1'})
        self.assertIn('default: None', free.get_arg_doc()[0])
        self.assertEqual(receiver.get_header(), [])
        self.assertEqual(receiver.get_arg_doc(), [])
        self.assertEqual(receiver.get_fixed_doc(), ["self on socket 'Value'"])
        self.assertEqual(receiver.get_node_call().named_sockets, {'ID_Value': 'self'})
        self.assertEqual(vars(source), before)

    def test_alias_resolution_accepts_zero_and_uses_last_non_none(self):
        argument = NodeArgument(socket(), 'value', aliases=(('Value', 'value'), ('Base', 'base')))
        self.assertEqual(argument.get_header(), ['value: Float=None', 'base: Float=None'])
        self.assertEqual(len(argument.get_arg_doc()), 2)
        for value, base, expected in ((0, None, 0), (2, 3, 3), (None, None, None)):
            env = {'value': value, 'base': base, 'named_sockets': {}}
            exec('\n'.join(argument.get_code()), env)
            self.assertEqual(env['named_sockets']['ID_Value'], expected)

    def test_multi_input_with_and_without_receiver(self):
        for role, expected in (('ARGUMENT', ['*values']), ('SELF', ['self', '*values'])):
            argument = NodeArgument(socket(is_multi=True), 'values', role=role)
            self.assertEqual(argument.get_header(), ['*values: Float'])
            self.assertEqual(argument.get_node_call().positional, expected)
            self.assertIn('multiple values', argument.get_arg_doc()[0])

    def test_fixed_values_are_serialized_once_including_none(self):
        for value in (None, "a'b", False):
            argument = NodeArgument(socket(), 'value', role='FIXED', value=value)
            self.assertEqual(argument.get_header(), [])
            self.assertEqual(argument.get_arg_doc(), [])
            self.assertEqual(argument.get_node_call().named_sockets, {'Value': repr(value)})
            self.assertTrue(argument.get_fixed_doc())
            self.assertEqual(argument.get_code(), [])
        param = NodeArgument(parameter(), 'mode', role='FIXED', value='B')
        self.assertEqual(param.get_node_call().parameters, {'mode': "'B'"})

    def test_enum_aliases_and_documented_choices(self):
        argument = NodeArgument(parameter(), 'mode_1')
        aliases = TypeAliases()
        self.assertEqual(argument.get_header(aliases), ["mode_1: T_MODE_1_1='A'"])
        self.assertEqual(argument.get_header(), ["mode_1: Literal['A', 'B']='A'"])
        self.assertIn("{'A', 'B'}", argument.get_arg_doc()[0])
        self.assertEqual(argument.get_node_call().parameters, {'mode': 'mode_1'})
        self.assertEqual(len(aliases), 1)

    def test_enum_flags_and_absent_typing(self):
        flags = NodeArgument(parameter(value={'A'}, typing="set[Literal['A', 'B']]", param_type='ENUM_FLAG'), 'mode')
        self.assertEqual(flags.get_header(), ["mode: set[Literal['A', 'B']]={'A'}"])
        self.assertIn("set[{'A', 'B'}]", flags.get_arg_doc()[0])
        untyped = NodeArgument(parameter('seed', 0, typing=None, param_type='INT', enums=None), 'seed')
        self.assertEqual(untyped.get_header(), ['seed=0'])

    def test_computed_selection(self):
        argument = NodeArgument(socket('Selection', identifier='Selection', class_name='Boolean'),
                                'selection', role='COMPUTED', value='selection',
                                computation='selection = self.get_selection()')
        self.assertEqual(argument.get_header(), [])
        self.assertEqual(argument.get_arg_doc(), [])
        self.assertEqual(argument.get_fixed_doc(), [])
        self.assertTrue(argument.get_computed_doc())
        env = {'self': NS(get_selection=lambda: 'selection marker')}
        exec('\n'.join(argument.get_code()), env)
        self.assertEqual(env['selection'], 'selection marker')
        self.assertEqual(argument.get_node_call().named_sockets, {'Selection': 'selection'})

    def test_computed_type_and_grouped_socket(self):
        computation = "data_type = SocketType.get_data_type_for_node(value_1, 'TestNode', 'data_type')"
        argument = NodeArgument(parameter('data_type'), 'data_type', role='COMPUTED',
                                value='data_type', computation=computation)
        self.assertEqual(argument.get_header(), [])
        self.assertEqual(argument.get_code(), [computation])
        self.assertEqual(argument.get_node_call().parameters, {'data_type': 'data_type'})
        grouped = NodeArgument(socket(group_name='Value', class_name='Socket'), 'value')
        self.assertEqual(grouped.get_header(), ['value: Socket=None'])
        self.assertEqual(grouped.get_node_call().named_sockets, {'Value': 'value'})

    def test_invalid_contexts_fail_early(self):
        with self.assertRaisesRegex(ValueError, 'receiver'):
            NodeArgument(parameter(), 'mode', role='SELF')
        with self.assertRaisesRegex(ValueError, 'requires a value'):
            NodeArgument(socket(), 'value', role='FIXED')
        with self.assertRaisesRegex(TypeError, 'expression'):
            NodeArgument(socket(), 'value', role='COMPUTED', value=3)

    def test_named_items_expand_sockets_and_node_keywords(self):
        argument = NodeArgument(None, 'items', role='NAMED_ITEMS')
        self.assertEqual(argument.get_header(), ['items={}', '**named_items'])
        call = argument.get_node_call()
        self.assertEqual(call.named_socket_expansions, ['items'])
        self.assertEqual(call.parameter_expansions, ['named_items'])
        self.assertEqual(call.named_sockets, {})
        self.assertEqual(call.parameters, {})
        self.assertEqual(argument.get_code(), [])
        self.assertEqual(len(argument.get_arg_doc()), 2)
        code = ('def example(items={}, **named_items):\n'
                '    return collect(named_sockets={**items}, **named_items)')
        env = {'collect': lambda **kw: kw}
        exec(code, env)
        self.assertEqual(env['example']({'A': 1}, B=2), {'named_sockets': {'A': 1}, 'B': 2})
        self.assertEqual(argument.get_fixed_doc(), [])
        self.assertEqual(argument.get_computed_doc(), [])

    def test_anonymous_items_are_positional(self):
        argument = NodeArgument(None, 'values', role='ANONYMOUS_ITEMS')
        self.assertEqual(argument.get_header(), ['*values'])
        self.assertEqual(argument.get_node_call().positional, ['*values'])
        self.assertEqual(argument.get_code(), [])
        self.assertIn('*values : Socket', argument.get_arg_doc()[0])
        with self.assertRaisesRegex(ValueError, 'Items roles'):
            NodeArgument(socket(), 'values', role='ANONYMOUS_ITEMS')


if __name__ == '__main__':
    unittest.main()
