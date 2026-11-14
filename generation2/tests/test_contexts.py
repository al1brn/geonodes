"""Run with Blender --background --python generation2/tests/test_contexts.py."""
import ast
from pathlib import Path
import sys
import textwrap
from types import SimpleNamespace as NS
import unittest
from unittest.mock import patch

workspace = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(workspace.parent))
from geonodes.generation2.node_implementation import NodeImplementation
from geonodes.generation2.tree_class import TreeClass
from geonodes.generation2.generate import generate, write_files
from geonodes.generation2.output import render_modules
from geonodes.generation2.node_call import NodeCall


class ContextGenerationTest(unittest.TestCase):
    def setUp(self):
        self.registry = TreeClass('GeometryNodeTree')

    def test_fixed_configurations_use_the_central_socket_explorer(self):
        import bpy
        from geonodes.generation2.node_info import NodeInfo
        tree = bpy.data.node_groups.new('Socket exploration test', 'GeometryNodeTree')
        try:
            node = NodeInfo(tree, tree.nodes.new('FunctionNodeCompare'))
            initial = node.snapshot_params()
            for data_type in ('FLOAT', 'VECTOR', 'INT'):
                parameters = {'data_type': data_type, 'operation': 'EQUAL', 'mode': 'ELEMENT'}
                node.set_params(**parameters)
                expected = node.snapshot_sockets()
                for inout, direction in (('INPUT', 'inputs'), ('OUTPUT', 'outputs')):
                    sockets = node.get_possible_sockets(inout=inout, group=False, **parameters)
                    self.assertEqual({s.identifier: s.socket_type for s in sockets},
                                     {key: s.socket_type for key, s in expected[direction].items()})
            self.assertEqual(node.snapshot_params(), initial)
        finally:
            bpy.data.node_groups.remove(tree)


    def test_same_method_in_two_contexts_is_not_a_collision(self):
        for tree_type in ('GeometryNodeTree', 'ShaderNodeTree'):
            node = NS(btree=NS(bl_idname=tree_type), bnode=NS(bl_idname='ShaderNodeMath', name='Math'))
            self.registry.register_source(node, NodeCall.method('test', class_name='Float', self_socket='Value'), '    def test(self):\n        return self\n')
        self.assertEqual(set(self.registry.files), {'GeometryNodeTree', 'ShaderNodeTree'})
        with patch('geonodes.generation2.tree_class.utils.get_node_names', return_value={'ShaderNodeMath': 'Math'}):
            with self.assertRaisesRegex(ValueError, 'Duplicate implementation: Float.test'):
                self.registry.register_source(node, NodeCall.method('test', class_name='Float', self_socket='Value'), '    def test(self):\n        return self\n')

    def test_render_targets_and_intermediate_bases(self):
        for tree_type, environment in [('GeometryNodeTree', 'geonodes'), ('ShaderNodeTree', 'shadernodes')]:
            modules = render_modules(workspace / 'core_new', tree_type, {})
            self.assertTrue(all(path.parent == workspace / 'core_new' / environment / 'generated' for path in modules))
            float_code = modules[workspace / 'core_new' / environment / 'generated/float.py']
            self.assertIn(f'from ...{environment}.sockets.float import Float as BaseFloat', float_code)
            self.assertIn('class Float(BaseFloat)', float_code)
            self.assertEqual(any(path.name.startswith('dom_') for path in modules), environment == 'geonodes')
            self.assertIn(workspace / 'core_new' / environment / 'generated/texture.py', modules)
            excluded = ('shader.py', 'volumeshader.py') if environment == 'geonodes' else (
                'collection.py', 'font.py', 'image.py', 'material.py', 'matrix.py', 'object.py', 'rotation.py', 'sound.py')
            self.assertFalse(set(excluded) & {path.name for path in modules})
            for path, code in modules.items():
                compile(code, str(path), 'exec')

    def test_every_context_validates_before_any_write(self):
        trees = {tree_type: TreeClass(tree_type) for tree_type in ('GeometryNodeTree', 'ShaderNodeTree')}
        module_name = 'geonodes.generation2.tree_class'
        with patch(module_name + '.render_modules', side_effect=[{Path('/tmp/never_written.py'): 'pass'}, ValueError('invalid shader')]):
            with patch.object(Path, 'write_text') as write:
                with self.assertRaisesRegex(ValueError, 'invalid shader'):
                    write_files(trees)
                write.assert_not_called()

    def test_single_context_orchestration_and_restore(self):
        calls = []
        names = ('gen_static_code', 'gen_math', 'gen_compare', 'gen_mix', 'gen_nodes',
                 'gen_properties', 'gen_typed_constructors', 'gen_additional')
        from contextlib import ExitStack
        with ExitStack() as stack:
            stack.enter_context(patch('geonodes.generation2.generate.gen_config.build'))
            for name in names:
                stack.enter_context(patch.object(TreeClass, name, autospec=True,
                    side_effect=lambda obj, name=name: calls.append((name, obj.tree_type))))
            trees = generate(tree_type='ShaderNodeTree', write=False)
        self.assertEqual(calls, [(name, 'ShaderNodeTree') for name in names])
        self.assertEqual(set(trees), {'ShaderNodeTree'})
        self.assertEqual(self.registry.tree_type, 'GeometryNodeTree')

    def test_gen_nodes_domain_variants_keep_docs_and_cross_references(self):
        import bpy
        from geonodes.generation2.node_info import NodeInfo
        tree = bpy.data.node_groups.new('Domain generation test', 'GeometryNodeTree')
        try:
            identifiers = ('GeometryNodeSetShadeSmooth', 'GeometryNodeSampleIndex',
                           'GeometryNodeViewer', 'GeometryNodeForeachGeometryElementOutput')
            nodes = [NodeInfo(tree, tree.nodes.new(identifier)) for identifier in identifiers]
            self.registry.tree_type = 'GeometryNodeTree'
            with patch.object(NodeInfo, 'loop_on_nodes', side_effect=lambda function, **kwargs: [function(node) for node in nodes]):
                self.registry.gen_nodes()
            refs = self.registry.cross_refs['GeometryNodeTree']
            self.assertEqual(set(refs['GeometryNodeSetShadeSmooth']), {'Mesh', 'Edge', 'Face'})
            self.assertEqual(set(refs['GeometryNodeSampleIndex']),
                             {'Geometry', 'Point', 'Edge', 'Face', 'Corner', 'Spline', 'Instance', 'Layer'})
            sample = refs['GeometryNodeSampleIndex']['Face'][0]
            self.assertFalse(sample['is_classmethod'])
            self.assertNotIn('data_type', sample['signature'])
            self.assertNotIn('domain', sample['signature'])
            source = next(source for source in self.registry.files['GeometryNodeTree']['dom_face.py']
                          if ast.parse(textwrap.dedent(source)).body[0].name == sample['func_name'])
            self.assertIn("domain='FACE'", source)
            self.assertIn('Derived parameters', ast.get_docstring(ast.parse(textwrap.dedent(source)).body[0]))
            self.assertIn('get_data_type_for_node', source)
            default = refs['GeometryNodeSampleIndex']['Geometry'][0]
            self.assertIn('domain', default['signature'])
            self.assertNotIn('GeometryNodeViewer', refs)
            self.assertNotIn('GeometryNodeForeachGeometryElementOutput', refs)
        finally:
            bpy.data.node_groups.remove(tree)


    def test_math_comparisons_follow_context_names_without_exclusions(self):
        for tree_type, prefix in (('GeometryNodeTree', 'm'), ('ShaderNodeTree', '')):
            self.registry.files, self.registry.cross_refs = {}, {}
            self.registry.tree_type = tree_type
            self.registry.gen_math()
            references = self.registry.cross_refs[tree_type]['ShaderNodeMath']
            for destination in ('Float', 'gnmath'):
                by_name = {ref['func_name']: ref for ref in references[destination]}
                for name in ('less_than', 'greater_than', 'compare'):
                    self.assertIn(prefix + name, by_name)
                    self.assertNotIn(('' if prefix else 'm') + name, by_name)
            modules = render_modules(workspace / 'core_new', tree_type, self.registry.files[tree_type])
            path = workspace / 'core_new' / ('geonodes' if prefix else 'shadernodes') / 'generated/float.py'
            generated = next(node for node in ast.parse(modules[path]).body if isinstance(node, ast.ClassDef))
            self.assertIn(prefix + 'compare', {node.name for node in generated.body if isinstance(node, ast.FunctionDef)})


    def test_anonymous_items_generate_index_switch_and_keep_manual_menu(self):
        import bpy
        from geonodes.generation2.node_info import NodeInfo
        tree = bpy.data.node_groups.new('Index Switch exclusions', 'GeometryNodeTree')
        try:
            node = NodeInfo(tree, tree.nodes.new('GeometryNodeIndexSwitch'))
            self.assertEqual(node.default_implementation()['kind'], 'CONSTRUCTOR')
            self.registry.tree_type = 'GeometryNodeTree'
            self.registry.gen_handwritten_references()
            self.assertEqual(self.registry.files['GeometryNodeTree'], {})
            refs = self.registry.cross_refs['GeometryNodeTree']['GeometryNodeIndexSwitch']['Socket']
            self.assertEqual([reference['func_name'] for reference in refs], ['index_switch'])
            self.assertIn('*values', refs[0]['signature'])
            with patch.object(NodeInfo, 'loop_on_nodes', side_effect=lambda func, **kwargs: func(node)):
                self.registry.gen_static_code()
            self.assertIn('static_nd.py', self.registry.files['GeometryNodeTree'])
            source = self.registry.files['GeometryNodeTree']['static_nd.py'][0]
            function = ast.parse(textwrap.dedent(source)).body[0]
            self.assertEqual(function.args.vararg.arg, 'values')
            self.assertFalse(function.args.kwarg)
            self.assertNotIn('_0', {argument.arg for argument in function.args.kwonlyargs})
            self.assertIn("Node('Index Switch', *values", source)
            menu = NodeInfo(tree, tree.nodes.new('GeometryNodeMenuSwitch'))
            self.assertEqual(menu.default_implementation()['kind'], 'NONE')
            references = self.registry.cross_refs['GeometryNodeTree']['GeometryNodeMenuSwitch']['Socket']
            self.assertEqual([reference['func_name'] for reference in references], ['MenuSwitch', 'menu_switch'])
            self.assertIn('default_menu', references[0]['signature'])
            with patch.object(NodeInfo, 'loop_on_nodes', side_effect=lambda func, **kwargs: func(menu)):
                self.registry.gen_static_code()
            self.assertTrue(any('def menu_switch(' in source for source in
                                self.registry.files['GeometryNodeTree']['static_nd.py']))
        finally:
            bpy.data.node_groups.remove(tree)


    def test_item_access_delegates_to_generated_methods(self):
        import bpy
        from unittest.mock import Mock
        from geonodes.generation2.node_info import NodeInfo
        tree = bpy.data.node_groups.new('Item delegates', 'GeometryNodeTree')
        try:
            nodes = [NodeInfo(tree, tree.nodes.new(identifier)) for identifier in
                     ('NodeGetBundleItem', 'NodeStoreBundleItem')]
            for node, operation in zip(nodes, ('get', 'set')):
                spec = NodeImplementation(node).get_node_implementation()
                self.assertIn(operation, spec['item_implementation'])
            self.registry.tree_type = 'GeometryNodeTree'
            with patch.object(NodeInfo, 'loop_on_nodes', side_effect=lambda function, **kwargs: [function(node) for node in nodes]):
                self.registry.gen_nodes()
            namespace = {}
            exec('from __future__ import annotations\nclass Generated:\n' +
                 '\n'.join(self.registry.files['GeometryNodeTree']['bundle.py']), namespace)
            instance = namespace['Generated']()
            result = object()
            instance.get_bundle_item = Mock(return_value=result)
            instance.store_bundle_item = Mock(return_value='ignored')
            self.assertIs(instance['path'], result)
            instance.get_bundle_item.assert_called_once_with('path', remove=False)
            self.assertIsNone(instance.__setitem__('path', 42))
            instance.store_bundle_item.assert_called_once_with('path', 42)
            refs = self.registry.cross_refs['GeometryNodeTree']
            self.assertEqual([ref['func_name'] for ref in refs['NodeGetBundleItem']['Bundle']],
                             ['get_bundle_item', '__getitem__'])
            self.assertEqual([ref['func_name'] for ref in refs['NodeStoreBundleItem']['Bundle']],
                             ['store_bundle_item', '__setitem__'])
        finally:
            bpy.data.node_groups.remove(tree)

    def test_item_access_skips_selection_and_follows_type_loops(self):
        import bpy
        from unittest.mock import Mock, PropertyMock
        from geonodes.generation2.node_info import NodeInfo
        tree = bpy.data.node_groups.new('Item selection and types', 'GeometryNodeTree')
        try:
            node = NodeInfo(tree, tree.nodes.new('GeometryNodeStoreNamedAttribute'))
            self.registry.tree_type = 'GeometryNodeTree'
            spec = {'class_name': None, 'method_name': 'store', 'data_type_loop': True,
                    'item_implementation': {'set': {}}}
            with patch.object(NodeImplementation, 'get_node_implementation', return_value=spec), \
                 patch.object(NodeInfo, 'loop_on_nodes', side_effect=lambda function, **kwargs: function(node)), \
                 patch.object(NodeInfo, 'data_type_parameter', new_callable=PropertyMock,
                              return_value=NS(name='data_type', enums=('FLOAT', 'FLOAT_VECTOR'))):
                self.registry.gen_nodes()
            for destination, refs in self.registry.cross_refs['GeometryNodeTree'][node.bl_idname].items():
                self.assertEqual([ref['func_name'] for ref in refs], ['store', '__setitem__'])
                source = self.registry.files['GeometryNodeTree'][destination.lower() + '.py'][0]
                function = ast.parse(textwrap.dedent(source)).body[0]
                self.assertEqual([arg.arg for arg in function.args.args[:3]], ['self', 'name', 'value'])
                self.assertIn('selection = self.get_selection()', source)
                namespace = {}
                exec('class Generated:\n' + self.registry.files['GeometryNodeTree'][destination.lower() + '.py'][1], namespace)
                instance = namespace['Generated']()
                instance.store = Mock()
                instance['attribute'] = 42
                instance.store.assert_called_once_with('attribute', 42)
        finally:
            bpy.data.node_groups.remove(tree)

    def test_invalid_item_specs_abort_generation(self):
        import bpy
        from geonodes.generation2.node_info import NodeInfo
        tree = bpy.data.node_groups.new('Invalid item specs', 'GeometryNodeTree')
        try:
            node = NodeInfo(tree, tree.nodes.new('NodeGetBundleItem'))
            for items, class_method, error in (({'other': {}}, False, KeyError),
                                               ({'get': {'unknown': False}}, False, TypeError),
                                               ({'get': {'path': 'duplicate'}}, False, TypeError),
                                               ({'get': {}}, True, ValueError)):
                with self.subTest(items=items, class_method=class_method):
                    self.registry.files, self.registry.cross_refs = {}, {}
                    self.registry.tree_type = 'GeometryNodeTree'
                    spec = {'class_name': 'Bundle', 'method_name': 'read',
                            'is_class_method': class_method, 'item_implementation': items}
                    with patch.object(NodeImplementation, 'get_node_implementation', return_value=spec), \
                         patch.object(NodeInfo, 'loop_on_nodes', side_effect=lambda function, **kwargs: function(node)):
                        with self.assertRaises(error):
                            self.registry.gen_nodes()
        finally:
            bpy.data.node_groups.remove(tree)

    def test_declared_properties_keep_getter_and_setter_references(self):
        from geonodes.generation2 import config
        self.registry.tree_type = 'GeometryNodeTree'
        properties = {'Point': {
            'position': config.PROPERTIES['Point']['position'],
            'offset': config.PROPERTIES['Point']['offset']}}
        with patch.object(config, 'PROPERTIES', properties):
            self.registry.gen_properties()
        sources = self.registry.files['GeometryNodeTree']['dom_point.py']
        functions = [ast.parse(textwrap.dedent(source)).body[0] for source in sources]
        self.assertEqual([function.name for function in functions], ['position', 'position', 'offset', 'offset'])
        self.assertEqual(len(functions[1].args.args), 2)
        self.assertFalse(functions[1].args.defaults)
        self.assertIn('self.get_selection()', sources[1])
        self.assertIn('self._jump(', sources[1])
        self.assertIn('raise NodeError', sources[2])
        refs = self.registry.cross_refs['GeometryNodeTree']
        self.assertTrue(refs['GeometryNodeInputPosition']['Point'][0]['is_get'])
        self.assertTrue(refs['GeometryNodeSetPosition']['Point'][0]['is_set'])
        node = NS(btree=NS(bl_idname='GeometryNodeTree'),
                  bnode=NS(bl_idname='GeometryNodeSetPosition', name='Set Position'))
        with self.assertRaisesRegex(ValueError, 'Duplicate implementation'):
            self.registry.register_source(node, NodeCall.setter('position', class_name='Point', self_socket='Geometry'), sources[1])


if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ContextGenerationTest))
    if not result.wasSuccessful():
        raise SystemExit(1)
