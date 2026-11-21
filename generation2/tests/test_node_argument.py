"""Run with Blender --background --python generation2/tests/test_node_argument.py."""
from pathlib import Path
import sys
import textwrap
from types import SimpleNamespace as NS
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from geonodes.generation2.sourcewriter import SourceWriter
from geonodes.generation2.node_argument import NodeArguments
from geonodes.generation2.node_info import NodeInfo
from geonodes.generation2.node_param import NodeParam
from geonodes.generation2.node_implementation import NodeImplementation
from geonodes.generation2.node_call import NodeCall
from geonodes.generation2.typealiases import TypeAliases
from geonodes.generation2.tree import Tree


class NodeArgumentsTest(unittest.TestCase):
    def test_non_enum_parameters_precede_enums_without_changing_node_call_order(self):
        args = NodeArguments()
        args.set_socket_keyword('input_socket')
        specs = [('mode', 'A', 'ENUM', ('A', 'B')),
                 ('flags', {'A'}, 'ENUM_FLAG', ('A', 'B')),
                 ('name', '', 'VALUE', None),
                 ('count', 1, 'VALUE', None)]
        for name, value, kind, enums in specs:
            args.add_parameter(NodeParam(None, name, value, kind, enums=enums))
        header_names = [part.split(':')[0].split('=')[0].strip() for part in args.get_header()]
        self.assertEqual(header_names, ['input_socket', 'name', 'count', 'mode', 'flags'])
        self.assertEqual(args.get_node_call(), ['mode=mode', 'flags=flags', 'name=name', 'count=count'])

    def test_attribute_name_is_first_positional_parameter(self):
        with Tree('ShaderNodeTree') as tree:
            info = NodeInfo(tree.btree, tree.create_node('Attribute'))
            order = info.config_order
            fn, calls, source = self.generate(info, method_type='FUNCTION')
            fn('Color')
            self.assertEqual(calls[-1][1]['attribute_name'], 'Color')
            self.assertEqual(calls[-1][1]['attribute_type'], 'GEOMETRY')
            self.assertEqual(info.config_order, order)
            self.assertLess(source.index('attribute_name:'), source.index('attribute_type:'))
            self.assertLess(source.index('attribute_type=attribute_type'),
                            source.index('attribute_name=attribute_name'))

    def test_fixed_values_and_quoted_node_name(self):
        args = NodeArguments()
        args.add_fixed_parameter(NS(name='operation'), 'ADD')
        args.add_fixed_socket(NS(identifier='Text', socket_name='Text', group_name=None), "a'b")
        calls = []
        writer = SourceWriter()
        writer.write(args.get_code_source("Node's name"))
        exec(writer.source, {'Node': lambda *a, **kw: calls.append((a, kw))})
        self.assertEqual(calls, [(("Node's name",), dict(operation='ADD', named_sockets={'ID_Text': "a'b"}))])

    def test_enum_typing_and_dynamic_named_inputs(self):
        args = NodeArguments()
        aliases = TypeAliases()
        args.add_parameter(NS(name='mode', value='A', param_type='ENUM',
                              enums=['A', 'B'], typing=['A', 'B']), aliases)
        args.add_socket(NS(is_virtual=True, name='NAMED'))
        args.make_arg_names_unique()
        writer = SourceWriter()
        writer.write(args.get_mockup(as_method=False))
        env = {'Node': lambda *a, **kw: kw}
        exec(aliases.source + writer.source, env)
        env['method'](named_sockets={'A': 1}, B=2)
        self.assertEqual(len(aliases), 1)
        self.assertIn('mode: T_MODE_1', writer.source)

    def generate(self, info, **options):
        source = NodeImplementation(info, type_aliases=TypeAliases())._gen_source_code(
            NodeCall(method_name='build', **options))
        calls = []
        def node(*a, **kw):
            calls.append((a, kw))
            return NS(_out='result', _second_out=lambda obj: 'second')
        env = {'Node': node, 'SocketType': NS(get_data_type_for_node=lambda *a: 'FLOAT')}
        exec('from __future__ import annotations\n' +
             ('class Example:\n' + source if options.get('method_type') != 'FUNCTION' else source), env)
        return (env['build'] if options.get('method_type') == 'FUNCTION' else env['Example'].build), calls, source

    def test_math_function_and_method(self):
        for tree_type in ('GeometryNodeTree', 'ShaderNodeTree'):
            with Tree(tree_type) as tree:
                info = NodeInfo(tree.btree, tree.create_node('Math'))
                fn, calls, source = self.generate(info, method_type='FUNCTION', parameters={'operation': 'ADD'})
                self.assertEqual(fn(value=2, value_1=3), 'result')
                self.assertEqual(calls[-1][1]['operation'], 'ADD')
                self.assertEqual(list(calls[-1][1]['named_sockets'].values()), [2, 3])
                fn, calls, source = self.generate(info, method_type='METHOD', self_socket='Value', parameters={'operation': 'ADD'})
                marker = object()
                self.assertEqual(fn(marker, value=4), 'result')
                self.assertEqual(list(calls[-1][1]['named_sockets'].values()), [marker, 4])
                compile(textwrap.dedent(source), '<method>', 'exec')

    def test_auto_type_and_fixed_type(self):
        with Tree() as tree:
            info = NodeInfo(tree.btree, tree.create_node('Map Range'))
            fn, calls, _ = self.generate(info, method_type='METHOD', self_socket='Value', auto_data_type='Value')
            fn(object())
            self.assertEqual(calls[-1][1]['data_type'], 'FLOAT')
            fn, calls, _ = self.generate(info, method_type='METHOD', self_socket='Value', auto_data_type='missing', parameters={'data_type': 'FLOAT'})
            fn(object())
            self.assertEqual(calls[-1][1]['data_type'], 'FLOAT')

    def test_multi_input_and_selection(self):
        with Tree() as tree:
            info = NodeInfo(tree.btree, tree.create_node('Join Geometry'))
            fn, calls, _ = self.generate(info, method_type='METHOD', self_socket='Geometry')
            marker = object()
            fn(marker, 1, 2)
            self.assertEqual(calls[-1][1]['named_sockets']['ID_Geometry'], [marker, 1, 2])
            info = NodeInfo(tree.btree, tree.create_node('Set Position'))
            fn, calls, _ = self.generate(info, method_type='METHOD', self_socket='Geometry', geo_selection=True)
            fn(NS(get_selection=lambda: True))
            self.assertIs(calls[-1][1]['named_sockets']['ID_Selection'], True)


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
