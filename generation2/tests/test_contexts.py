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
from geonodes.generation2.node_implementation import NodeImplementation as Implementation
from geonodes.generation2.output import render_modules


class CopyCodeExample:
    def passthrough(self, value):
        return value


class ContextGenerationTest(unittest.TestCase):
    def setUp(self):
        self.files, self.refs, self.tree_type = Implementation.files, Implementation.cross_refs, Implementation.tree_type
        Implementation.files, Implementation.cross_refs = {}, {}

    def tearDown(self):
        Implementation.files, Implementation.cross_refs, Implementation.tree_type = self.files, self.refs, self.tree_type

    def test_declared_enum_order_preserves_all_socket_configurations(self):
        import bpy
        from geonodes.generation2.node_info import NodeInfo
        from geonodes.generation2.node_param import NodeParam
        tree = bpy.data.node_groups.new('Ordered socket exploration test', 'GeometryNodeTree')
        try:
            bnode = tree.nodes.new('FunctionNodeCompare')
            bnode.data_type = 'RGBA'
            bnode.operation = 'BRIGHTER'
            node = NodeInfo(tree, bnode)
            initial = node.snapshot_params()
            # A declared order must bypass automatic dependency detection.
            with patch.object(NodeParam, 'dependance_with', side_effect=AssertionError('unexpected inference')):
                configurations = node.configurations
            self.assertTrue(configurations)
            self.assertEqual(node.enum_parameters[:3], ('data_type', 'operation', 'mode'))
            self.assertEqual(node.snapshot_params(), initial)

            def check_configuration():
                params = node.snapshot_params()
                keys = node.param_filter(**{
                    name: params[name]['value'] for name in node.enum_parameters
                })
                self.assertEqual(len(keys), 1)
                key = keys[0]
                for direction, current in node.all_sockets().items():
                    for identifier, captured in getattr(node, direction).items():
                        socket = current.get(identifier)
                        self.assertEqual(captured.dependencies[key], {
                            'exists': socket is not None,
                            'enabled': socket.enabled if socket else False,
                            'name': (socket.label or socket.name) if socket else None,
                            'socket_type': socket.socket_type if socket else None,
                            'index': socket.index if socket else None,
                        })

            for data_type in NodeParam.Parameter(bnode, 'data_type').enums:
                bnode.data_type = data_type
                for operation in NodeParam.Parameter(bnode, 'operation').enums:
                    bnode.operation = operation
                    for mode in NodeParam.Parameter(bnode, 'mode').enums:
                        bnode.mode = mode
                        check_configuration()
        finally:
            bpy.data.node_groups.remove(tree)

    def test_socket_names_are_explicit_in_max_inputs_and_filtered_headers(self):
        import bpy
        from geonodes.generation2.node_info import NodeInfo
        tree = bpy.data.node_groups.new('Socket names test', 'GeometryNodeTree')
        try:
            node = NodeInfo(tree, tree.nodes.new('ShaderNodeMath'))
            _ = node.configurations
            self.assertTrue(all(isinstance(socket['name'], str) for socket in node.max_inputs))
            self.assertTrue({'Base', 'Exponent'} <= set(node.inputs['Value_001'].names))
            self.assertEqual(node.inputs['Value_001'].identifier, 'Value_001')

            def generate(implementation):
                code = ('from __future__ import annotations\nclass Example:\n' +
                        '\n'.join(implementation._gen_source('example', return_kind='NODE')))
                namespace = {'Node': lambda *args, **kwargs: (args, kwargs)}
                exec(compile(code, '<generated>', 'exec'), namespace)
                return namespace['Example'].example, code

            implementation = Implementation(node)
            implementation['operation'] = 'POWER'
            method, code = generate(implementation)
            _, values = method(2.5, exponent=3)
            self.assertEqual(values['named_sockets'], {'Base': 2.5, 'Exponent': 3})
            self.assertNotIn('base:', code)

            implementation['operation'] = None
            method, _ = generate(implementation)
            _, values = method(2.5, operation='POWER', exponent=3)
            self.assertEqual(values['named_sockets'], {'Base': 2.5, 'Exponent': 3})
            _, values = method(2.5, operation='LOGARITHM', base=10)
            self.assertEqual(values['named_sockets'], {'Value': 2.5, 'Base': 10})
            _, values = method(2.5, operation='ADD', value_1=4)
            self.assertEqual(values['named_sockets'], {'Value': 2.5, 'Value_1': 4})
        finally:
            bpy.data.node_groups.remove(tree)

    def test_same_method_in_two_contexts_is_not_a_collision(self):
        for tree_type in ('GeometryNodeTree', 'ShaderNodeTree'):
            node = NS(btree=NS(bl_idname=tree_type), bnode=NS(bl_idname='ShaderNodeMath', name='Math'))
            Implementation.register_source(node, 'float.py', 'Float', '    def test(self):\n        return self\n')
        self.assertEqual(set(Implementation.files), {'GeometryNodeTree', 'ShaderNodeTree'})
        with patch('geonodes.generation2.node_implementation.utils.get_node_names', return_value={'ShaderNodeMath': 'Math'}):
            with self.assertRaisesRegex(ValueError, 'Duplicate implementation: Float.test'):
                Implementation.register_source(node, 'float.py', 'Float', '    def test(self):\n        return self\n')

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
        Implementation.files = {'GeometryNodeTree': {}, 'ShaderNodeTree': {}}
        module_name = 'geonodes.generation2.node_implementation'
        with patch(module_name + '.render_modules', side_effect=[{Path('/tmp/never_written.py'): 'pass'}, ValueError('invalid shader')]):
            with patch.object(Path, 'write_text') as write:
                with self.assertRaisesRegex(ValueError, 'invalid shader'):
                    Implementation.write_files()
                write.assert_not_called()

    def test_single_context_orchestration_and_restore(self):
        calls = []
        names = ('gen_static_code', 'gen_gnmath', 'gen_nodes')
        from contextlib import ExitStack
        with ExitStack() as stack:
            for name in names:
                stack.enter_context(patch.object(Implementation, name, side_effect=lambda name=name: calls.append((name, Implementation.tree_type))))
            Implementation.generate(tree_type='ShaderNodeTree', write=False)
        self.assertEqual(calls, [(name, 'ShaderNodeTree') for name in names])
        self.assertEqual(set(Implementation.files), {'ShaderNodeTree'})
        self.assertEqual(Implementation.tree_type, self.tree_type)

    def test_gen_nodes_only_expands_the_supplied_description(self):
        import bpy
        from contextlib import ExitStack
        from geonodes.generation2 import config
        from geonodes.generation2.node_info import NodeInfo
        tree = bpy.data.node_groups.new('Simple node generation', 'GeometryNodeTree')
        try:
            nodes = [NodeInfo(tree, tree.nodes.new(identifier)) for identifier in
                     ('GeometryNodeSetShadeSmooth', 'ShaderNodeMapRange')]
            descriptions = {
                'GeometryNodeSetShadeSmooth': {'class_name': 'Mesh', 'method_name': 'shade', 'domain_loop': True},
                'ShaderNodeMapRange': {'class_name': None, 'method_name': 'map_range', 'data_type_loop': True},
            }
            emitted = []
            def source(implementation, name, **options):
                emitted.append((name, implementation.parameters.copy(), options))
                return iter([f'    def {name}(self):', '        pass'])
            Implementation.tree_type = 'GeometryNodeTree'
            with ExitStack() as stack:
                stack.enter_context(patch.object(NodeInfo, 'loop_on_nodes',
                    side_effect=lambda function, **kwargs: [function(node) for node in nodes]))
                describe = stack.enter_context(patch.object(Implementation, 'get_node_implementation',
                    autospec=True, side_effect=lambda implementation: descriptions[implementation.node.bl_idname]))
                stack.enter_context(patch.object(Implementation, '_gen_source', autospec=True, side_effect=source))
                for name in ('NO_DEFAULT_IMPLEMENTATION', 'DATA_TYPE_IMPLEMENTATIONS',
                             'REPLACE_DEFAULT_IMPLEMENTATIONS', 'ADDITIONAL_IMPLEMENTATIONS',
                             'INPUT_IMPLEMENTATIONS', 'PROPERTIES',
                             'HANDWRITTEN_IMPLEMENTATIONS'):
                    stack.enter_context(patch.object(config, name, None))
                Implementation.gen_nodes()
            self.assertEqual(describe.call_count, 2)
            self.assertEqual([(name, parameters.get('domain'), parameters.get('data_type'))
                              for name, parameters, _ in emitted],
                             [('shade', None, None), ('shade', 'EDGE', None), ('shade', 'FACE', None),
                              ('map_range', None, 'FLOAT'), ('map_range', None, 'FLOAT_VECTOR')])
            references = Implementation.cross_refs['GeometryNodeTree']
            self.assertEqual(set(references['GeometryNodeSetShadeSmooth']), {'Mesh', 'Edge', 'Face'})
            self.assertEqual(set(references['ShaderNodeMapRange']), {'Float', 'Vector'})
        finally:
            bpy.data.node_groups.remove(tree)

    def test_gen_nodes_domain_variants_keep_docs_and_cross_references(self):
        import bpy
        from geonodes.generation2.node_info import NodeInfo
        tree = bpy.data.node_groups.new('Domain generation test', 'GeometryNodeTree')
        try:
            identifiers = ('GeometryNodeSetShadeSmooth', 'GeometryNodeSampleIndex',
                           'GeometryNodeViewer', 'GeometryNodeForeachGeometryElementOutput')
            nodes = [NodeInfo(tree, tree.nodes.new(identifier)) for identifier in identifiers]
            Implementation.tree_type = 'GeometryNodeTree'
            with patch.object(NodeInfo, 'loop_on_nodes', side_effect=lambda function, **kwargs: [function(node) for node in nodes]):
                Implementation.gen_nodes()
            refs = Implementation.cross_refs['GeometryNodeTree']
            self.assertEqual(set(refs['GeometryNodeSetShadeSmooth']), {'Mesh', 'Edge', 'Face'})
            self.assertEqual(set(refs['GeometryNodeSampleIndex']),
                             {'Geometry', 'Point', 'Edge', 'Face', 'Corner', 'Spline', 'Instance', 'Layer'})
            sample = refs['GeometryNodeSampleIndex']['Face'][0]
            self.assertFalse(sample['is_classmethod'])
            self.assertNotIn('data_type', sample['signature'])
            self.assertNotIn('domain', sample['signature'])
            source = next(source for source in Implementation.files['GeometryNodeTree']['dom_face.py']
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

    def test_data_type_inference_is_instance_only(self):
        import bpy
        from geonodes import core_module
        from geonodes.generation2.node_info import NodeInfo
        from geonodes.core_new.common.sockettype import SocketType
        tree = bpy.data.node_groups.new('Type inference test', 'GeometryNodeTree')
        try:
            node = NodeInfo(tree, tree.nodes.new(type='GeometryNodeStoreNamedGrid'))
            self.assertEqual(node.inferred_data_type_socket, 'grid')
            proposal = node.default_implementation()
            source = Implementation(node).gen_source(
                kind='METHOD', name=proposal['name'], self_socket=proposal['self_socket'],
                return_socket=proposal['return_socket'], is_jump=True, data_type_socket='grid')
            function = ast.parse(textwrap.dedent(source)).body[0]
            self.assertNotIn('data_type', [arg.arg for arg in function.args.args])
            self.assertIn('Derived parameters', ast.get_docstring(function))
            static = Implementation(node).gen_source(kind='STATIC_METHOD', name='store_named_grid', data_type_socket='grid')
            self.assertIn('data_type', [arg.arg for arg in ast.parse(textwrap.dedent(static)).body[0].args.args])
            calls = []
            def make_node(*args, **kwargs):
                calls.append(kwargs)
                return NS(_out=object())
            namespace = dict(vars(core_module), Node=make_node, SocketType=SocketType)
            exec('from __future__ import annotations\nclass Generated:\n' + source, namespace)
            receiver = NS(_jump=lambda value: None, _domain_to_geometry='geometry')
            for value, expected in ((1., 'FLOAT'), (True, 'BOOLEAN'), ((1., 2., 3.), 'VECTOR_FLOAT')):
                namespace['Generated'].store_named_grid(receiver, grid=value)
                self.assertEqual(calls[-1]['data_type'], expected)
        finally:
            bpy.data.node_groups.remove(tree)

    def test_math_families_use_standard_generator_and_bind_active_sockets(self):
        import contextlib
        import io
        from geonodes import core_module as core
        families = ('gen_math_functions', 'gen_integer_math_functions',
                    'gen_boolean_math_functions', 'gen_vector_math_functions',
                    'gen_bit_math_functions')
        values = {'Float': 2., 'Integer': 2, 'Boolean': True, 'Vector': (1., 2., 3.)}
        for tree_type, factory in (('GeometryNodeTree', core.GeoNodes),
                                   ('ShaderNodeTree', core.ShaderNodes)):
            Implementation.files, Implementation.cross_refs = {}, {}
            Implementation.tree_type = tree_type
            with contextlib.redirect_stdout(io.StringIO()), factory('Standard math generation'):
                # No migrated family may fall back to the legacy generator.
                with patch.object(Implementation, 'gen_source', side_effect=AssertionError('legacy generator')):
                    for family in families:
                        if tree_type == 'ShaderNodeTree' and family not in ('gen_math_functions', 'gen_vector_math_functions'):
                            continue
                        getattr(Implementation, family)()
                sources = Implementation.files[tree_type]
                for filename, entries in sources.items():
                    for source in entries:
                        function = ast.parse(textwrap.dedent(source)).body[0]
                        if function.name.startswith('__'):
                            continue
                        with self.subTest(tree_type=tree_type, file=filename, name=function.name):
                            namespace = {'Node': core.Node}
                            prefix = 'from __future__ import annotations\n'
                            if filename == 'gnmath.py':
                                exec(prefix + source, namespace)
                                result = namespace[function.name]()
                            else:
                                exec(prefix + 'class Generated:\n' + source, namespace)
                                class_name = filename[:-3].capitalize()
                                receiver = getattr(core, class_name)(values[class_name])
                                result = getattr(namespace['Generated'], function.name)(receiver)
                            self.assertIsNotNone(result)
                            bnode = result._bsocket.node
                            output = next(sock for sock in bnode.outputs
                                          if sock.enabled and sock.is_icon_visible and sock.type != 'CUSTOM')
                            self.assertEqual(result._bsocket, output)
                            if filename != 'gnmath.py':
                                first_input = next(sock for sock in bnode.inputs
                                                   if sock.enabled and sock.is_icon_visible and sock.type != 'CUSTOM')
                                self.assertTrue(first_input.is_linked)
                                self.assertEqual(first_input.links[0].from_socket, receiver._bsocket)

    def test_math_comparisons_follow_context_names_without_exclusions(self):
        for tree_type, prefix in (('GeometryNodeTree', 'm'), ('ShaderNodeTree', '')):
            Implementation.files, Implementation.cross_refs = {}, {}
            Implementation.tree_type = tree_type
            Implementation.gen_gnmath()
            references = Implementation.cross_refs[tree_type]['ShaderNodeMath']
            for destination in ('Float', 'gnmath'):
                by_name = {ref['func_name']: ref for ref in references[destination]}
                for name in ('less_than', 'greater_than', 'compare'):
                    self.assertIn(prefix + name, by_name)
                    self.assertNotIn(('' if prefix else 'm') + name, by_name)
            modules = render_modules(workspace / 'core_new', tree_type, Implementation.files[tree_type])
            path = workspace / 'core_new' / ('geonodes' if prefix else 'shadernodes') / 'generated/float.py'
            generated = next(node for node in ast.parse(modules[path]).body if isinstance(node, ast.ClassDef))
            self.assertIn(prefix + 'compare', {node.name for node in generated.body if isinstance(node, ast.FunctionDef)})

    def test_copy_code_remains_available(self):
        implementation = object.__new__(Implementation)
        source = implementation.gen_source(kind='METHOD', copy_code=CopyCodeExample.passthrough)
        function = ast.parse(textwrap.dedent(source)).body[0]
        self.assertEqual(function.name, 'passthrough')
        self.assertIn('return value', source)

    def test_anonymous_items_generate_index_switch_and_keep_manual_menu(self):
        import bpy
        from geonodes.generation2.node_info import NodeInfo
        tree = bpy.data.node_groups.new('Index Switch exclusions', 'GeometryNodeTree')
        try:
            node = NodeInfo(tree, tree.nodes.new('GeometryNodeIndexSwitch'))
            self.assertEqual(node.default_implementation()['kind'], 'CONSTRUCTOR')
            Implementation.tree_type = 'GeometryNodeTree'
            Implementation.gen_handwritten_references()
            self.assertEqual(Implementation.files['GeometryNodeTree'], {})
            refs = Implementation.cross_refs['GeometryNodeTree']['GeometryNodeIndexSwitch']['Socket']
            self.assertEqual([reference['func_name'] for reference in refs], ['index_switch'])
            self.assertIn('*values', refs[0]['signature'])
            with patch.object(NodeInfo, 'loop_on_nodes', side_effect=lambda func, **kwargs: func(node)):
                Implementation.gen_static_code()
            self.assertIn('static_nd.py', Implementation.files['GeometryNodeTree'])
            source = Implementation.files['GeometryNodeTree']['static_nd.py'][0]
            function = ast.parse(textwrap.dedent(source)).body[0]
            self.assertEqual(function.args.vararg.arg, 'values')
            self.assertFalse(function.args.kwarg)
            self.assertNotIn('_0', {argument.arg for argument in function.args.kwonlyargs})
            self.assertIn("Node('Index Switch', *values", source)
            menu = NodeInfo(tree, tree.nodes.new('GeometryNodeMenuSwitch'))
            self.assertEqual(menu.default_implementation()['kind'], 'NONE')
            references = Implementation.cross_refs['GeometryNodeTree']['GeometryNodeMenuSwitch']['Socket']
            self.assertEqual([reference['func_name'] for reference in references], ['MenuSwitch', 'menu_switch'])
            self.assertIn('default_menu', references[0]['signature'])
            with patch.object(NodeInfo, 'loop_on_nodes', side_effect=lambda func, **kwargs: func(menu)):
                Implementation.gen_static_code()
            self.assertTrue(any('def menu_switch(' in source for source in
                                Implementation.files['GeometryNodeTree']['static_nd.py']))
        finally:
            bpy.data.node_groups.remove(tree)

    def test_multi_input_receivers_and_renamed_variants(self):
        import bpy
        from geonodes.generation2.node_info import NodeInfo
        tree = bpy.data.node_groups.new('Multi-input signatures', 'GeometryNodeTree')
        try:
            for identifier in ('GeometryNodeJoinGeometry', 'GeometryNodeGeometryToInstance', 'NodeJoinBundle'):
                node = NodeInfo(tree, tree.nodes.new(identifier))
                proposal = node.default_implementation()
                source = Implementation(node).gen_source(kind='METHOD', name=proposal['name'],
                                                        self_socket=proposal['self_socket'], return_socket='OUT')
                function = ast.parse(textwrap.dedent(source)).body[0]
                self.assertIsNotNone(function.args.vararg)
                self.assertIn('self, *' + function.args.vararg.arg, source)
            node = NodeInfo(tree, tree.nodes.new('GeometryNodeMeshBoolean'))
            proposal = node.default_implementation()
            source = Implementation(node).gen_source(kind='METHOD', name='boolean',
                                                    self_socket=proposal['self_socket'], return_socket='OUT')
            self.assertIsNotNone(ast.parse(textwrap.dedent(source)).body[0].args.vararg)
            static = Implementation(node).gen_source(kind='STATIC_METHOD', name='mesh_boolean')
            function = ast.parse(textwrap.dedent(static)).body[0]
            self.assertIsNotNone(function.args.vararg)
            self.assertNotIn('mesh', {argument.arg for argument in function.args.kwonlyargs})
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
                spec = Implementation(node).get_node_implementation()
                self.assertIn(operation, spec['item_implementation'])
            Implementation.tree_type = 'GeometryNodeTree'
            with patch.object(NodeInfo, 'loop_on_nodes', side_effect=lambda function, **kwargs: [function(node) for node in nodes]):
                Implementation.gen_nodes()
            namespace = {}
            exec('from __future__ import annotations\nclass Generated:\n' +
                 '\n'.join(Implementation.files['GeometryNodeTree']['bundle.py']), namespace)
            instance = namespace['Generated']()
            result = object()
            instance.get_bundle_item = Mock(return_value=result)
            instance.store_bundle_item = Mock(return_value='ignored')
            self.assertIs(instance['path'], result)
            instance.get_bundle_item.assert_called_once_with('path', remove=False)
            self.assertIsNone(instance.__setitem__('path', 42))
            instance.store_bundle_item.assert_called_once_with('path', 42)
            refs = Implementation.cross_refs['GeometryNodeTree']
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
            Implementation.tree_type = 'GeometryNodeTree'
            spec = {'class_name': None, 'method_name': 'store', 'data_type_loop': True,
                    'item_implementation': {'set': {}}}
            with patch.object(Implementation, 'get_node_implementation', return_value=spec), \
                 patch.object(NodeInfo, 'loop_on_nodes', side_effect=lambda function, **kwargs: function(node)), \
                 patch.object(NodeInfo, 'data_type_parameter', new_callable=PropertyMock,
                              return_value=NS(name='data_type', enums=('FLOAT', 'FLOAT_VECTOR'))):
                Implementation.gen_nodes()
            for destination, refs in Implementation.cross_refs['GeometryNodeTree'][node.bl_idname].items():
                self.assertEqual([ref['func_name'] for ref in refs], ['store', '__setitem__'])
                source = Implementation.files['GeometryNodeTree'][destination.lower() + '.py'][0]
                function = ast.parse(textwrap.dedent(source)).body[0]
                self.assertEqual([arg.arg for arg in function.args.args[:3]], ['self', 'name', 'value'])
                self.assertIn('selection = self.get_selection()', source)
                namespace = {}
                exec('class Generated:\n' + Implementation.files['GeometryNodeTree'][destination.lower() + '.py'][1], namespace)
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
                    Implementation.files, Implementation.cross_refs = {}, {}
                    Implementation.tree_type = 'GeometryNodeTree'
                    spec = {'class_name': 'Bundle', 'method_name': 'read',
                            'is_class_method': class_method, 'item_implementation': items}
                    with patch.object(Implementation, 'get_node_implementation', return_value=spec), \
                         patch.object(NodeInfo, 'loop_on_nodes', side_effect=lambda function, **kwargs: function(node)):
                        with self.assertRaises(error):
                            Implementation.gen_nodes()
        finally:
            bpy.data.node_groups.remove(tree)

    def test_declared_properties_keep_getter_and_setter_references(self):
        from geonodes.generation2 import config
        Implementation.tree_type = 'GeometryNodeTree'
        properties = {'Point': {
            'position': config.PROPERTIES['Point']['position'],
            'offset': config.PROPERTIES['Point']['offset']}}
        with patch.object(config, 'PROPERTIES', properties):
            Implementation.gen_properties()
        sources = Implementation.files['GeometryNodeTree']['dom_point.py']
        functions = [ast.parse(textwrap.dedent(source)).body[0] for source in sources]
        self.assertEqual([function.name for function in functions], ['position', 'position', 'offset', 'offset'])
        self.assertEqual(len(functions[1].args.args), 2)
        self.assertFalse(functions[1].args.defaults)
        self.assertIn('self.get_selection()', sources[1])
        self.assertIn('self._jump(', sources[1])
        self.assertIn('raise NodeError', sources[2])
        refs = Implementation.cross_refs['GeometryNodeTree']
        self.assertTrue(refs['GeometryNodeInputPosition']['Point'][0]['is_get'])
        self.assertTrue(refs['GeometryNodeSetPosition']['Point'][0]['is_set'])
        node = NS(btree=NS(bl_idname='GeometryNodeTree'),
                  bnode=NS(bl_idname='GeometryNodeSetPosition', name='Set Position'))
        with self.assertRaisesRegex(ValueError, 'Duplicate implementation'):
            Implementation.register_source(node, 'dom_point.py', 'Point', sources[1])

    def test_both_type_policy_uses_geometry_or_typed_class_methods(self):
        import bpy
        from geonodes.generation2.node_info import NodeInfo
        tree = bpy.data.node_groups.new('Input and output type policy test', 'GeometryNodeTree')
        try:
            raycast = NodeInfo(tree, tree.nodes.new(type='GeometryNodeRaycast'))
            proposal = raycast.default_implementation()
            self.assertEqual((proposal['kind'], proposal['class_name']), ('METHOD', 'Geometry'))
            self.assertEqual(raycast.inferred_data_type_socket, 'attribute')
            static = Implementation(raycast).gen_source(kind='STATIC_METHOD', name='raycast')
            self.assertIn('data_type', [arg.arg for arg in ast.parse(textwrap.dedent(static)).body[0].args.args])
            for identifier, name, kind, expected in (
                    ('ShaderNodeMapRange', 'map_range', 'METHOD', {'Float', 'Vector'}),
                    ('FunctionNodeRandomValue', 'Random', 'CONSTRUCTOR', {'Float', 'Integer', 'Boolean', 'Vector'}),
                    ('GeometryNodeGridInfo', 'GridInfo', 'CONSTRUCTOR', {'Float', 'Integer', 'Boolean', 'Vector'}),
                    ('ShaderNodeMix', 'mix', 'METHOD', {'Float', 'Vector', 'Color', 'Rotation'})):
                node = NodeInfo(tree, tree.nodes.new(type=identifier))
                initial = node.snapshot_params()
                variants = node.default_implementation()['implementations']
                self.assertEqual({variant['class_name'] for variant in variants}, expected)
                self.assertEqual(len(variants), len(expected))
                for variant in variants:
                    self.assertEqual((variant['kind'], variant['name']), (kind, name))
                    self.assertIn('data_type', variant['parameters'])
                self.assertEqual(node.snapshot_params(), initial)
            switch = NodeInfo(tree, tree.nodes.new(type='GeometryNodeSwitch'))
            self.assertEqual(switch.data_type_implementation(), {})
            self.assertNotIn('implementations', switch.default_implementation())
            from geonodes.generation2 import config
            self.assertNotIn('NodeImplicitConversion', config.DATA_TYPE_IMPLEMENTATIONS)
            for identifier, expected_name in (('NodeEnableOutput', 'enable_output'),
                                               ('NodeImplicitConversion', 'implicit_conversion')):
                node = NodeInfo(tree, tree.nodes.new(type=identifier))
                variants = node.default_implementation()['implementations']
                variant = next(variant for variant in variants if variant['class_name'] == 'Float')
                self.assertEqual((variant['kind'], variant['name']), ('METHOD', expected_name))
        finally:
            bpy.data.node_groups.remove(tree)


if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ContextGenerationTest))
    if not result.wasSuccessful():
        raise SystemExit(1)
