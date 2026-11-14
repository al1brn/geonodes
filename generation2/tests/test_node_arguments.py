"""Run with Blender --background --python generation2/tests/test_node_arguments.py."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from geonodes.generation2.node_info import NodeInfo
from geonodes.generation2.node_argument import NodeArgument
from geonodes.generation2.tree import Tree


class NodeArgumentsTest(unittest.TestCase):
    def test_parameters_fixed_variants_and_independent_contexts(self):
        for tree_type in ('GeometryNodeTree', 'ShaderNodeTree'):
            with Tree(tree_type) as tree:
                info = NodeInfo(tree.btree, tree.create_node('Map Range'))
                initial = info.snapshot_params()
                scalar = info.get_node_arguments(self_socket='Value', data_type='FLOAT')
                vector = info.get_node_arguments(self_socket='Vector', data_type='FLOAT_VECTOR')
                self.assertTrue(all(isinstance(arg, NodeArgument) for arg in scalar + vector))
                self.assertEqual((scalar[0].role, scalar[0].socket_name), ('SELF', 'Value'))
                self.assertEqual((vector[0].role, vector[0].socket_name), ('SELF', 'Vector'))
                self.assertEqual(scalar[0].get_typing(), 'Float')
                self.assertEqual(vector[0].get_typing(), 'Vector')
                fixed = next(arg for arg in vector if not arg._is_socket and arg.source.name == 'data_type')
                self.assertEqual(fixed.role, 'FIXED')
                self.assertEqual(fixed.value, 'FLOAT_VECTOR')
                self.assertEqual(fixed.get_header(), [])
                self.assertEqual(info.snapshot_params(), initial)

    def test_selection_receiver_and_fixed_precedence(self):
        with Tree() as tree:
            info = NodeInfo(tree.btree, tree.create_node('Set Position'))
            args = info.get_node_arguments(self_socket='Geometry', use_geo_selection=True,
                                          last_sockets=('Position',))
            selected = next(arg for arg in args if arg.socket_name == 'Selection')
            self.assertEqual(selected.role, 'COMPUTED')
            self.assertIn('self.get_selection()', selected.computation)
            self.assertEqual(selected.get_header(), [])
            self.assertEqual([arg.socket_name for arg in args if arg._is_socket][-1], 'Position')
            fixed = info.get_node_arguments(self_socket='Geometry', use_geo_selection=True,
                                           fixed_sockets={'Selection': None})
            selected = next(arg for arg in fixed if arg.socket_name == 'Selection')
            self.assertEqual(selected.role, 'FIXED')
            self.assertEqual(selected.get_node_call().named_sockets, {'Selection': 'None'})
            other = info.get_node_arguments(self_socket='Position', use_geo_selection=True)
            self.assertEqual(next(arg for arg in other if arg.socket_name == 'Selection').role, 'ARGUMENT')

    def test_aliases_are_deduplicated_and_fixed_alias_keeps_ui_name(self):
        with Tree() as tree:
            info = NodeInfo(tree.btree, tree.create_node('Math'))
            args = info.get_node_arguments(self_socket='Value')
            headers = [header for arg in args for header in arg.get_header()]
            self.assertTrue(any('value_1:' in header for header in headers))
            aliased = next(arg for arg in args if 'Exponent' in arg.source.names)
            self.assertIn('Exponent', dict(aliased.aliases))
            fixed = info.get_node_arguments(operation='POWER', fixed_sockets={'Exponent': 3})
            exponent = next(arg for arg in fixed if arg.role == 'FIXED' and arg._is_socket)
            self.assertEqual(exponent.get_node_call().named_sockets, {'Exponent': '3'})

    def test_non_enum_parameters_are_included_and_fixed(self):
        with Tree() as tree:
            info = NodeInfo(tree.btree, tree.create_node('Noise Texture'))
            non_enums = {name: p for name, p in info.snapshot_params().items() if p['type'] != 'ENUM'}
            self.assertTrue(non_enums)
            name, snapshot = next(iter(non_enums.items()))
            initial = info.snapshot_params()
            value = not snapshot['value'] if isinstance(snapshot['value'], bool) else snapshot['value']
            args = info.get_node_arguments(**{name: value})
            parameter = next(arg for arg in args if arg.source.name == name)
            self.assertEqual(parameter.role, 'FIXED')
            self.assertEqual(info.snapshot_params(), initial)

    def test_auto_type_uses_final_receiver_and_fixed_type_wins(self):
        with Tree() as tree:
            info = NodeInfo(tree.btree, tree.create_node('Map Range'))
            args = info.get_node_arguments(self_socket='Value', auto_data_type='Value')
            parameter = next(arg for arg in args if not arg._is_socket and arg.source.name == 'data_type')
            self.assertEqual(parameter.role, 'COMPUTED')
            self.assertIn('get_data_type_for_node(self,', parameter.computation)
            fixed = info.get_node_arguments(self_socket='Value', auto_data_type='missing', data_type='FLOAT')
            self.assertEqual(next(arg for arg in fixed if not arg._is_socket and arg.source.name == 'data_type').role, 'FIXED')

    def test_multi_input_receiver_can_assemble_a_valid_function(self):
        with Tree() as tree:
            info = NodeInfo(tree.btree, tree.create_node('Join Geometry'))
            args = info.get_node_arguments(self_socket='Geometry')
            receiver = args[0]
            self.assertEqual(receiver.role, 'SELF')
            self.assertEqual(receiver.get_node_call().positional, ['self', f'*{receiver.name}'])
            headers = [fragment for arg in args for fragment in arg.get_header()]
            positional = [fragment for arg in args for fragment in arg.get_node_call().positional]
            code = f"def example(self, {', '.join(headers)}):\n    return collect({', '.join(positional)})"
            env = {'collect': lambda *values: values}
            exec('from __future__ import annotations\n' + code, env)
            marker = object()
            self.assertEqual(env['example'](marker, 1, 2), (marker, 1, 2))

    def test_validation_and_node_restoration(self):
        with Tree() as tree:
            info = NodeInfo(tree.btree, tree.create_node('Map Range'))
            initial = info.snapshot_params()
            for options in ({'unknown_parameter': 3}, {'fixed_sockets': {'missing': 3}},
                            {'self_socket': 'missing'}, {'auto_data_type': 'missing'},
                            {'data_type': 'BAD_TYPE'}):
                with self.subTest(options=options):
                    with self.assertRaises((ValueError, TypeError)):
                        info.get_node_arguments(**options)
                    self.assertEqual(info.snapshot_params(), initial)

    def test_items_roles_follow_the_introspected_item_collection(self):
        with Tree() as tree:
            for node_name, role in (('Menu Switch', 'NAMED_ITEMS'),
                                    ('Index Switch', 'ANONYMOUS_ITEMS')):
                info = NodeInfo(tree.btree, tree.create_node(node_name))
                initial = info.snapshot_params()
                args = info.get_node_arguments()
                items = [arg for arg in args if arg.role in ('NAMED_ITEMS', 'ANONYMOUS_ITEMS')]
                self.assertEqual(len(items), 1)
                self.assertEqual(items[0].role, role)
                self.assertIsNone(items[0].source)
                self.assertIs(args[-1], items[0])
                self.assertEqual(info.snapshot_params(), initial)
                self.assertTrue(items[0].get_header())
                self.assertTrue(items[0].get_arg_doc())


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
