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
            excluded = ('shader.py', 'volumeshader.py', 'texture.py') if environment == 'geonodes' else (
                'collection.py', 'font.py', 'image.py', 'material.py', 'matrix.py', 'object.py', 'rotation.py', 'sound.py', 'texture.py')
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
        names = ('gen_gnmath', 'gen_input_nodes', 'gen_default_implementation', 'gen_source_code', 'gen_static_nodes')
        from contextlib import ExitStack
        with ExitStack() as stack:
            for name in names:
                stack.enter_context(patch.object(Implementation, name, side_effect=lambda name=name: calls.append((name, Implementation.tree_type))))
            domains = stack.enter_context(patch.object(Implementation, 'gen_domain_implementations'))
            Implementation.generate(tree_type='ShaderNodeTree', write=False)
            domains.assert_not_called()
        self.assertEqual(calls, [(name, 'ShaderNodeTree') for name in names])
        self.assertEqual(set(Implementation.files), {'ShaderNodeTree'})
        self.assertEqual(Implementation.tree_type, self.tree_type)

    def test_fixed_domains_keep_docs_cross_refs_and_class_methods(self):
        import bpy
        from geonodes.generation2.node_info import NodeInfo
        tree = bpy.data.node_groups.new('Fixed-domain generation test', 'GeometryNodeTree')
        identifiers = ('GeometryNodeSetShadeSmooth', 'GeometryNodeToolActiveElement',
                       'GeometryNodeCaptureAttribute', 'GeometryNodeSampleIndex',
                       'GeometryNodeViewer', 'GeometryNodeForeachGeometryElementOutput')
        try:
            nodes = [NodeInfo(tree, tree.nodes.new(type=identifier)) for identifier in identifiers]
            Implementation.tree_type = 'GeometryNodeTree'
            with patch.object(NodeInfo, 'loop_on_nodes', side_effect=lambda func, **kwargs: [func(node) for node in nodes]):
                Implementation.gen_domain_implementations()
            refs = Implementation.cross_refs['GeometryNodeTree']
            self.assertEqual(set(refs['GeometryNodeSetShadeSmooth']), {'Edge', 'Face'})
            self.assertNotIn('GeometryNodeSampleIndex', refs)
            self.assertNotIn('GeometryNodeViewer', refs)
            self.assertNotIn('GeometryNodeForeachGeometryElementOutput', refs)
            self.assertEqual(set(refs['GeometryNodeToolActiveElement']), {'Point', 'Edge', 'Face', 'Layer'})
            for domain, domain_class in [('EDGE', 'Edge'), ('FACE', 'Face')]:
                name = refs['GeometryNodeSetShadeSmooth'][domain_class][0]['func_name']
                sources = Implementation.files['GeometryNodeTree']['dom_' + domain_class.lower() + '.py']
                source = next(source for source in sources if ast.parse(textwrap.dedent(source)).body[0].name == name)
                function = ast.parse(textwrap.dedent(source)).body[0]
                self.assertNotIn('domain', [argument.arg for argument in function.args.args])
                self.assertIn(f"domain='{domain}'", source)
                self.assertIn(f"| `domain` | `'{domain}'` |", ast.get_docstring(function))
            active = refs['GeometryNodeToolActiveElement']['Edge'][0]
            self.assertTrue(active['is_classmethod'])
            capture = refs['GeometryNodeCaptureAttribute']['Face'][0]
            self.assertIn('named_sockets', capture['signature'])
            self.assertIn('**sockets', capture['signature'])
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

    def test_copy_code_remains_available(self):
        implementation = object.__new__(Implementation)
        source = implementation.gen_source(kind='METHOD', copy_code=CopyCodeExample.passthrough)
        function = ast.parse(textwrap.dedent(source)).body[0]
        self.assertEqual(function.name, 'passthrough')
        self.assertIn('return value', source)

    def test_both_type_policy_uses_geometry_or_typed_class_methods(self):
        import bpy
        from geonodes.generation2.node_info import NodeInfo
        tree = bpy.data.node_groups.new('Input and output type policy test', 'GeometryNodeTree')
        try:
            raycast = NodeInfo(tree, tree.nodes.new(type='GeometryNodeRaycast'))
            proposal = raycast.default_implementation()
            self.assertEqual((proposal['kind'], proposal['class_name']), ('METHOD', 'Geometry'))
            self.assertEqual(raycast.inferred_data_type_socket, 'attribute')
            Implementation._gen_default_implementation(raycast, proposal)
            source = Implementation.files['GeometryNodeTree']['geometry.py'][0]
            function = ast.parse(textwrap.dedent(source)).body[0]
            self.assertNotIn('data_type', [arg.arg for arg in function.args.args])
            self.assertIn('get_data_type_for_node(attribute', source)
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
                Implementation._gen_default_implementation(node, node.default_implementation())
                self.assertEqual(node.snapshot_params(), initial)
                if identifier == 'ShaderNodeMapRange':
                    methods = Implementation.files['GeometryNodeTree']['vector.py']
                    method = next(ast.parse(textwrap.dedent(source)).body[0] for source in methods
                                  if ast.parse(textwrap.dedent(source)).body[0].name == 'map_range')
                    self.assertEqual([arg.arg for arg in method.args.args[:2]], ['self', 'from_min'])
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
                Implementation._gen_default_implementation(node, node.default_implementation())
                methods = Implementation.files['GeometryNodeTree']['float.py']
                method = next(ast.parse(textwrap.dedent(source)).body[0] for source in methods
                              if ast.parse(textwrap.dedent(source)).body[0].name == expected_name)
                arguments = [argument.arg for argument in method.args.args]
                self.assertEqual(arguments[0], 'self')
                self.assertNotIn('value', arguments)
                self.assertNotIn('data_type', arguments)
                if identifier == 'NodeEnableOutput':
                    self.assertIn('enable', arguments)
        finally:
            bpy.data.node_groups.remove(tree)


if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ContextGenerationTest))
    if not result.wasSuccessful():
        raise SystemExit(1)
