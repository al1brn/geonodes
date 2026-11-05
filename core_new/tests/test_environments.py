"""Run in Blender: blender --background --python core_new/tests/test_environments.py."""
import contextlib
import importlib.util
import io
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock, patch
from types import SimpleNamespace

root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('environment_test_core', root / '__init__.py', submodule_search_locations=[str(root)])
core = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = core
spec.loader.exec_module(core)


class EnvironmentsTest(unittest.TestCase):
    def setUp(self):
        self.output = contextlib.redirect_stdout(io.StringIO())
        self.output.__enter__()

    def tearDown(self):
        self.output.__exit__(None, None, None)

    def test_construction_results_and_comparisons(self):
        classes = []
        for factory, environment, compare_node in (
                (core.GeoNodes, 'geonodes.generated', 'FunctionNodeCompare'),
                (core.ShaderNodes, 'shadernodes.generated', 'ShaderNodeMath')):
            with factory('Environment types test') as tree:
                a, v = core.Float(2), core.Vector((1, 2, 3))
                classes.append((type(a), type(v)))
                self.assertIsInstance(a, core.Float)
                self.assertIsInstance(v, core.Vector)
                self.assertIn(environment, type(a).__module__)
                self.assertIs(type(a + 3), type(a))
                self.assertIs(type(3 - a), type(a))
                self.assertIs(type(v + v), type(v))
                self.assertIs(type(a + v), type(v))
                self.assertIs(type(a * v), type(v))
                self.assertIs(type((3, 2, 1) - v), type(v))
                method_name = 'mcompare' if factory is core.GeoNodes else 'compare'
                result = getattr(a, method_name)(2, epsilon=.01)
                self.assertIn(method_name, type(a).__dict__)
                self.assertEqual(result._bsocket.node.bl_idname, 'ShaderNodeMath')
                self.assertEqual(result.SOCKET_TYPE, 'VALUE')
                self.assertIn(environment, type(result).__module__)
                self.assertIn(environment, core.utils.get_socket_class('VECTOR').__module__)
        self.assertIsNot(classes[0][0], classes[1][0])
        self.assertIsNot(classes[0][1], classes[1][1])

    def test_class_methods_and_geometry_inheritance(self):
        with core.GeoNodes('Geometry hierarchy test'):
            mesh = core.Mesh.Cube()
            self.assertIsInstance(mesh, core.Mesh)
            # Mesh must inherit generated Geometry methods as well as its root.
            from environment_test_core.geonodes.generated.geometry import Geometry
            self.assertIsInstance(mesh, Geometry)
            self.assertIs(type(core.Float.Mix(a=0., b=1., factor=.5)), core.geonodes.generated.Float)
            self.assertIsInstance(mesh.points, core.Vertex)

    def test_nested_context_and_exception_restore(self):
        with core.GeoNodes('Outer environment'):
            outer = type(core.Float(1))
            with self.assertRaisesRegex(RuntimeError, 'restore'):
                with core.ShaderNodes('Inner environment'):
                    self.assertIsNot(type(core.Float(1)), outer)
                    raise RuntimeError('restore')
            self.assertIs(type(core.Float(1)), outer)

    def test_decorators(self):
        seen = []
        @core.geo_group('Environment decorated geometry')
        def geometry():
            seen.append(type(core.Vector((1, 2, 3))))
        @core.shader_group('Environment decorated shader')
        def shader():
            seen.append(type(core.Vector((1, 2, 3))))
        geometry.build()
        shader.build()
        self.assertIn('geonodes.generated', seen[0].__module__)
        self.assertIn('shadernodes.generated', seen[1].__module__)

    def test_intermediate_classes_and_initialization_hook(self):
        from environment_test_core.root.float import Float as RootFloat
        from environment_test_core.root.vector import Vector as RootVector
        from environment_test_core.geonodes.sockets.float import Float as GeometryFloat
        from environment_test_core.shadernodes.sockets.float import Float as ShaderFloat
        from environment_test_core import root as roots
        self.assertIs(roots.Float, RootFloat)
        self.assertIs(roots.Vector, RootVector)
        calls = []

        def initialize(self, *args, **kwargs):
            calls.append(type(self))
            RootFloat.__init__(self, *args, **kwargs)

        for factory, intermediate in ((core.GeoNodes, GeometryFloat), (core.ShaderNodes, ShaderFloat)):
            with factory('Intermediate initialization test'):
                with patch.object(intermediate, '__init__', initialize):
                    value = core.Float(1)
                self.assertIs(type(value).__bases__[0], intermediate)
                self.assertIs(intermediate.__bases__[0], RootFloat)
                self.assertIs(calls[-1], type(value))
                vector = core.Vector((1, 2, 3))
                self.assertIs(type(vector).__bases__[0].__bases__[0], RootVector)

    def test_shader_registry_has_no_geometry_or_domains(self):
        with core.ShaderNodes('Shader registry test'):
            self.assertNotIn('GEOMETRY', core.utils.SOCKET_CLASSES)
            self.assertEqual(dict(core.utils.GEOMETRY_CLASSES), {})
            self.assertFalse(issubclass(core.shadernodes.generated.Texture, core.Socket))
            for name in ('Collection', 'Object', 'Image', 'Material', 'Matrix', 'Rotation', 'Font', 'Sound'):
                self.assertFalse(hasattr(core.shadernodes.generated, name), name)
                self.assertFalse(hasattr(core.shadernodes.sockets, name), name)
            value = core.Float(1)._convert_to_class('Vector')
            self.assertIsInstance(value, core.Vector)
        with core.GeoNodes('Geometry registry test'):
            self.assertNotIn('SHADER', core.utils.SOCKET_CLASSES)
            self.assertFalse(issubclass(core.geonodes.generated.Texture, core.Socket))
            for name in ('Shader', 'VolumeShader'):
                self.assertFalse(hasattr(core.geonodes.generated, name), name)
                self.assertFalse(hasattr(core.geonodes.sockets, name), name)
        self.assertFalse((root / 'shadernodes/domains').exists())
        self.assertFalse(list((root / 'shadernodes/generated').glob('dom_*.py')))

    def test_shader_output_overrides(self):
        from environment_test_core.root.socket import Socket
        for name in ('Float', 'Vector', 'Color', 'Shader', 'VolumeShader'):
            cls = getattr(core.shadernodes.sockets, name)
            value = object.__new__(cls)
            object.__setattr__(value, '_tree', SimpleNamespace(_is_group=True))
            with patch.object(Socket, 'out') as output:
                value.out('Result', panel='Controls')
                output.assert_called_once()
                self.assertEqual(output.call_args.kwargs['panel'], 'Controls')
            tree = SimpleNamespace(_is_group=False, set_thickness=Mock(), set_displacement=Mock(),
                                   aov_output=Mock(), output_node=SimpleNamespace(set_input_socket=Mock()))
            object.__setattr__(value, '_tree', tree)
            value.out()
            if name == 'Float':
                tree.set_thickness.assert_called_once_with(value)
            elif name == 'Vector':
                tree.set_displacement.assert_called_once_with(value)
            elif name == 'Color':
                tree.aov_output.assert_called_once_with(name='Color', color=value)
            else:
                tree.output_node.set_input_socket.assert_called_once_with(
                    'Surface' if name == 'Shader' else 'Volume', value, create=False)
            if name in ('Float', 'Vector', 'Color'):
                tree.aov_output.reset_mock()
                value.out('Named output')
                tree.aov_output.assert_called_once_with(
                    name='Named output', **{'value' if name == 'Float' else 'color': value})

    def test_group_output_links_for_geometry_and_shader(self):
        for factory in (core.GeoNodes, core.ShaderNodes):
            with factory('Socket output groups', is_group=True) as tree:
                for name, value in (('Scalar', core.Float(1)), ('Vector', core.Vector((1, 2, 3))),
                                    ('Color', core.Color((.1, .2, .3, 1)))):
                    value.out(name, panel='Results')
                output = tree.get_output_node()._bnode
                self.assertTrue(all(output.inputs[name].is_linked for name in ('Scalar', 'Vector', 'Color')))

    def test_nd_selects_active_environment(self):
        self.assertFalse(hasattr(core, 'snd'))
        with core.GeoNodes('Unified nd geometry'):
            self.assertIn('.geonodes.generated.static_nd', core.nd.mesh_line.__module__)
            self.assertEqual(core.nd.mesh_line()._bnode.bl_idname, 'GeometryNodeMeshLine')
            with core.ShaderNodes('Unified nd shader'):
                self.assertIn('.shadernodes.generated.static_nd', core.nd.emission.__module__)
                self.assertEqual(core.nd.emission()._bnode.bl_idname, 'ShaderNodeEmission')
                self.assertFalse(hasattr(core.nd, 'mesh_line'))
            self.assertIn('.geonodes.generated.static_nd', core.nd.mesh_line.__module__)

    def test_handwritten_multiply_add_operators(self):
        for factory in (core.GeoNodes, core.ShaderNodes):
            with factory('Handwritten multiply-add test'):
                classes = (core.Float, core.Vector, core.Integer) if factory is core.GeoNodes else (core.Float, core.Vector)
                for cls in classes:
                    value = cls(2)
                    self.assertNotIn('__mul__', type(value).__dict__)
                    self.assertNotIn('__imul__', type(value).__dict__)
                    result = value * (3, 4)
                    self.assertEqual(result._bsocket.node.operation, 'MULTIPLY_ADD')
                    original = value
                    value *= (3, 4)
                    self.assertIs(value, original)
                    self.assertEqual(value._bsocket.node.operation, 'MULTIPLY_ADD')
                vector = core.Vector((1, 2, 3))
                self.assertEqual((vector * 2)._bsocket.node.operation, 'SCALE')
                self.assertEqual((vector * (2, 3, 4))._bsocket.node.operation, 'MULTIPLY')
                original = vector
                vector *= 2
                self.assertIs(vector, original)
                self.assertEqual(vector._bsocket.node.operation, 'SCALE')
                self.assertIsInstance(core.Float(2) * core.Vector((1, 2, 3)), core.Vector)

    def test_handwritten_join_operators(self):
        with core.GeoNodes('Handwritten join test'):
            a, b = core.Mesh.Cube(), core.Mesh.Cube()
            joined = a + b
            self.assertIs(type(joined), type(a))
            self.assertEqual(joined._bsocket.node.bl_idname, 'GeometryNodeJoinGeometry')
            self.assertEqual(len(joined._bsocket.node.inputs['Geometry'].links), 2)
            self.assertNotIn('__radd__', type(joined).__dict__)
            c = core.Mesh.Cube()
            for joined in (a + (b, c), (b, c) + a):
                self.assertEqual(len(joined._bsocket.node.inputs['Geometry'].links), 3)
            generic = core.Geometry(b)
            self.assertIs(type(a + generic), core.geonodes.generated.Geometry)
            original = a
            a += b
            self.assertIs(a, original)
            value = core.String('middle')
            self.assertNotIn('__add__', type(value).__dict__)
            self.assertNotIn('__radd__', type(value).__dict__)
            result = value + ('end', '!')
            self.assertEqual(result._bsocket.node.bl_idname, 'GeometryNodeStringJoin')
            self.assertEqual(len(result._bsocket.node.inputs['Strings'].links), 3)
            with patch('environment_test_core.root.string.Node') as make_node:
                value + ('end', '!')
                self.assertEqual(make_node.call_args.kwargs['named_sockets']['Strings'], [value, 'end', '!'])
                ('start', ':') + value
                self.assertEqual(make_node.call_args.kwargs['named_sockets']['Strings'], ['start', ':', value])
                'start' + value
                self.assertEqual(make_node.call_args.kwargs['named_sockets']['Strings'], ['start', value])

    def test_domain_and_data_type_variants(self):
        import inspect
        with core.GeoNodes('Domain and type variants test'):
            mesh = core.Mesh.Cube()
            self.assertIn('data_type', inspect.signature(mesh.sample_index).parameters)
            self.assertIn('domain', inspect.signature(mesh.sample_index).parameters)
            for domain, expected in ((mesh.faces, 'FACE'), (mesh.edges, 'EDGE'), (mesh.points, 'POINT')):
                self.assertNotIn('data_type', inspect.signature(domain.sample_index).parameters)
                self.assertNotIn('domain', inspect.signature(domain.sample_index).parameters)
                for value, data_type in ((1., 'FLOAT'), (True, 'BOOLEAN'), (core.Vector((1, 2, 3)), 'FLOAT_VECTOR')):
                    result = domain.sample_index(value=value, index=0)
                    self.assertEqual(result._bsocket.node.domain, expected)
                    self.assertEqual(result._bsocket.node.data_type, data_type)
            result = core.Face.EvaluateAtIndex(value=core.Vector((1, 2, 3)), index=0, data_type='FLOAT_VECTOR')
            self.assertEqual(result._bsocket.node.domain, 'FACE')
            self.assertEqual(result._bsocket.node.data_type, 'FLOAT_VECTOR')
            self.assertIn('data_type', inspect.signature(core.nd.sample_index).parameters)
            self.assertIn('domain', inspect.signature(core.nd.sample_index).parameters)

    def test_declared_geometry_properties(self):
        from environment_test_core.common.scripterror import NodeError
        def input_value(socket):
            if not socket.is_linked:
                return socket.default_value
            source = socket.links[0].from_socket
            return source.node.vector if hasattr(source.node, 'vector') else source.default_value
        with core.GeoNodes('Declared properties test') as tree:
            mesh = core.Mesh.Cube()
            bundle = core.nd.combine_bundle(value=core.Float(2))._out
            mesh.bundle = bundle
            setter = mesh._bsocket.node
            self.assertEqual(setter.bl_idname, 'GeometryNodeSetGeometryBundle')
            self.assertEqual(setter.inputs['Bundle'].links[0].from_socket, bundle._bsocket)
            geometry = mesh._bsocket
            result = mesh.bundle
            self.assertIsInstance(result, core.Bundle)
            self.assertEqual(result._bsocket.name, 'Bundle')
            self.assertEqual(result._bsocket.node.bl_idname, 'GeometryNodeGetGeometryBundle')
            self.assertFalse(input_value(result._bsocket.node.inputs['Remove']))
            self.assertEqual(mesh._bsocket, geometry)
            self.assertEqual(mesh.points.position._bsocket.node.bl_idname, 'GeometryNodeInputPosition')
            mesh.points[False].position = (1, 2, 3)
            node = mesh._bsocket.node
            self.assertEqual(node.bl_idname, 'GeometryNodeSetPosition')
            self.assertFalse(input_value(node.inputs['Selection']))
            self.assertEqual(tuple(input_value(node.inputs['Position'])), (1, 2, 3))
            mesh.points.offset = (0, 0, 1)
            self.assertEqual(tuple(input_value(mesh._bsocket.node.inputs['Offset'])), (0, 0, 1))
            with self.assertRaises(NodeError):
                mesh.points.offset
            mesh.faces.shade_smooth = True
            self.assertEqual(mesh._bsocket.node.domain, 'FACE')
            self.assertEqual(mesh.faces.shade_smooth._bsocket.node.bl_idname, 'GeometryNodeInputShadeSmooth')
            curve = core.Curve.Line()
            curve.type = 'BEZIER'
            self.assertEqual(curve._bsocket.node.spline_type, 'BEZIER')
            curve.left_handle_position = (1, 0, 0)
            self.assertEqual(curve._bsocket.node.mode, 'LEFT')
            self.assertEqual(curve.left_handle_offset._bsocket.node.bl_idname, 'GeometryNodeInputCurveHandlePositions')
            self.assertTrue(input_value(curve.left_handle_offset._bsocket.node.inputs['Relative']))

    def test_declared_bundle_item_access(self):
        for factory in (core.GeoNodes,):
            with factory('Bundle item operators test'):
                bundle = core.nd.combine_bundle()._out
                for value, value_type, identifier in ((1.5, core.Float, 'FLOAT'),
                                                       (2, core.Integer, 'INT'),
                                                       ((1, 2, 3), core.Vector, 'VECTOR'),
                                                       ('hello', core.String, 'STRING')):
                    previous = bundle._bsocket
                    bundle['item'] = value
                    setter = bundle._bsocket.node
                    self.assertEqual(setter.bl_idname, 'NodeStoreBundleItem')
                    self.assertEqual(setter.socket_type, identifier)
                    self.assertEqual(setter.inputs['Bundle'].links[0].from_socket, previous)
                    stored = bundle._bsocket
                    item = bundle['item', value_type]
                    self.assertIsInstance(item, value_type)
                    self.assertEqual(item._bsocket.node.bl_idname, 'NodeGetBundleItem')
                    self.assertEqual(item._bsocket.name, 'Item')
                    self.assertEqual(bundle._bsocket, stored)
                    self.assertFalse(item._bsocket.node.inputs['Remove'].default_value)
                with self.assertRaisesRegex(TypeError, 'bundle\\[path, Type\\]'):
                    bundle['item']
        with core.ShaderNodes('Unavailable bundle item operators'):
            bundle = core.nd.combine_bundle()._out
            self.assertNotIn('__setitem__', type(bundle).__dict__)

    def test_multi_input_instance_methods(self):
        import inspect
        with core.GeoNodes('Multi-input instance methods'):
            a, b, c = core.Mesh.Cube(), core.Mesh.Cube(), core.Mesh.Cube()
            a.join(b, c)
            self.assertEqual(len(a._bsocket.node.inputs['Geometry'].links), 3)
            instances = a.to_instance(b, c)
            self.assertEqual(len(instances._bsocket.node.inputs['Geometry'].links), 3)
            bundles = [core.nd.combine_bundle()._out for _ in range(3)]
            joined = bundles[0].join(*bundles[1:])
            self.assertEqual(len(joined._bsocket.node.inputs['Bundle'].links), 3)
            for operation in ('DIFFERENCE', 'UNION', 'INTERSECT'):
                mesh = core.Mesh.Cube()
                mesh.boolean(b, c, operation=operation)
                node = mesh._bsocket.node
                self.assertEqual(node.operation, operation)
                links = [len(socket.links) for socket in node.inputs if socket.enabled and socket.type == 'GEOMETRY']
                self.assertEqual(sum(links), 3)
            self.assertTrue(any(parameter.kind == inspect.Parameter.VAR_POSITIONAL
                                for parameter in inspect.signature(core.nd.mesh_boolean).parameters.values()))
            union = core.nd.mesh_boolean(a, b, operation='UNION')
            self.assertEqual(len(union._bnode.inputs['Mesh'].links), 2)
            difference = core.nd.mesh_boolean(b, c, mesh_1=a, operation='DIFFERENCE')
            self.assertEqual(len(difference._bnode.inputs['Mesh 2'].links), 2)

    def test_vector_generated_methods_and_shader_specialization(self):
        from environment_test_core.root.vector import Vector as RootVector
        for name in ('FromRotation', 'mapping', 'normal', 'transform', 'Tangent', 'UVMap',
                     'NormalMap', 'bump', 'displacement', 'vector_displacement', 'displacement_out'):
            self.assertNotIn(name, vars(RootVector))
        with core.GeoNodes('Generated vector conversion'):
            result = core.Vector.FromRotation(core.Rotation())
            self.assertEqual(result._bsocket.node.bl_idname, 'FunctionNodeRotationToEuler')
            vector = core.Vector((1, 2, 3))
            self.assertNotIn('bump', dir(type(vector)))
            self.assertNotIn('UVMap', dir(type(vector)))
        with core.ShaderNodes('Shader vector specialization'):
            vector = core.Vector((1, 2, 3))
            self.assertEqual(vector.mapping()._bsocket.node.bl_idname, 'ShaderNodeMapping')
            self.assertEqual(vector.normal()._bsocket.node.bl_idname, 'ShaderNodeNormal')
            transformed = vector.transform()
            self.assertEqual(transformed._bsocket.node.bl_idname, 'ShaderNodeVectorTransform')
            self.assertEqual(transformed._bsocket.node.vector_type, 'VECTOR')
            for value, identifier in ((core.Vector.Tangent(), 'ShaderNodeTangent'),
                                      (core.Vector.UVMap(), 'ShaderNodeUVMap'),
                                      (core.Vector.NormalMap(), 'ShaderNodeNormalMap'),
                                      (vector.bump(), 'ShaderNodeBump'),
                                      (vector.displacement(), 'ShaderNodeDisplacement'),
                                      (vector.vector_displacement(), 'ShaderNodeVectorDisplacement')):
                self.assertEqual(value._bsocket.node.bl_idname, identifier)

    def test_generated_index_switch(self):
        with core.GeoNodes('Handwritten Index Switch'):
            for constructor, values in ((core.Float, (1., 2., 3.)),
                                         (core.Vector, ((1, 0, 0), (0, 1, 0), (0, 0, 1))),
                                         (core.Mesh, (core.Mesh.Cube(), core.Mesh.Cube(), core.Mesh.Cube()))):
                result = constructor.IndexSwitch(*values, index=2)
                node = result._bsocket.node
                self.assertEqual(node.bl_idname, 'GeometryNodeIndexSwitch')
                self.assertEqual(len(node.index_switch_items), 3)
                self.assertIn('.generated.', type(result).IndexSwitch.__module__)
            result = core.Float(1).index_switch(2., 3., index=1)
            self.assertEqual(len(result._bsocket.node.index_switch_items), 3)
            node = core.nd.index_switch(1., 2., 3., index=2)
            self.assertEqual(len(node._bnode.index_switch_items), 3)
            selector = core.Integer(name='Choice')
            result = core.Float.IndexSwitch(1., 2., 3., index=selector, default_index=2)
            self.assertEqual(selector._interface_socket.default_value, 2)
            self.assertEqual(result._bsocket.node.inputs['Index'].default_value, 2)
            result = core.Float.IndexSwitch(1., 2., 3., default_index=1)
            self.assertEqual(result._bsocket.node.inputs['Index'].default_value, 1)

    def test_handwritten_menu_switch(self):
        for factory in (core.GeoNodes, core.ShaderNodes):
            with factory('Handwritten Menu Switch'):
                result = core.Float.MenuSwitch({'First': 1., 'Second': 2., 'Third': 3.}, default_menu='Second')
                self.assertEqual(result._bsocket.node.bl_idname, 'GeometryNodeMenuSwitch')
                self.assertEqual([item.name for item in result._bsocket.node.enum_items], ['First', 'Second', 'Third'])
                self.assertEqual(result.node._default_menu, 'Second')
                self.assertNotIn('MenuSwitch', vars(type(result)))
                result = core.Float(1).menu_switch(self_name='Original', Other=2., default_menu='Other')
                self.assertEqual([item.name for item in result._bsocket.node.enum_items], ['Original', 'Other'])
                self.assertEqual(result.node._default_menu, 'Other')
                node = core.nd.menu_switch(named_sockets={'One': 1., 'Two': 2.}, data_type='FLOAT')
                self.assertEqual([item.name for item in node._bnode.enum_items], ['One', 'Two'])

    def test_node_positional_inputs(self):
        with core.GeoNodes('Node positional values'):
            a, b, c = core.Mesh.Cube(), core.Mesh.Cube(), core.Mesh.Cube()
            joined = core.Node('Join Geometry', a, b, c)
            self.assertEqual(len(joined._bnode.inputs['Geometry'].links), 3)
            for operation in ('DIFFERENCE', 'UNION'):
                named = {'Mesh 1': a} if operation == 'DIFFERENCE' else {}
                node = core.Node('Mesh Boolean', b, c, operation=operation, named_sockets=named)
                name = 'Mesh 2' if operation == 'DIFFERENCE' else 'Mesh'
                self.assertEqual(len(node._bnode.inputs[name].links), 2)
                self.assertEqual(named, {'Mesh 1': a} if operation == 'DIFFERENCE' else {})
            switch = core.Node('Index Switch', 1., 2., 3., data_type='FLOAT', Index=2)
            self.assertEqual(len(switch._bnode.index_switch_items), 3)
            selector = switch._bnode.inputs['Index']
            self.assertEqual(selector.links[0].from_node.integer if selector.is_linked else selector.default_value, 2)
            with self.assertRaisesRegex(TypeError, 'require one active'):
                core.Node('Math', 1., 2.)
            joined = core.Node('Join Geometry', a, named_sockets={'Geometry': [b]})
            self.assertEqual(len(joined._bnode.inputs['Geometry'].links), 2)
            node = core.Node('Join Strings', 'first', 'second', Delimiter=':')
            self.assertEqual(len(node._bnode.inputs['Strings'].links), 2)
        with core.ShaderNodes('Node positional bundles'):
            a, b = core.Node('Combine Bundle')._out, core.Node('Combine Bundle')._out
            node = core.Node('Join Bundle', a, b)
            self.assertEqual(len(node._bnode.inputs['Bundle'].links), 2)

    def test_typed_class_methods_and_geometry_type_inference(self):
        import inspect
        for factory in (core.GeoNodes, core.ShaderNodes):
            with factory('Typed class methods test'):
                scalar = core.Float(.5).map_range(to_min=2, to_max=4)
                vector = core.Vector((.2, .3, .4)).map_range()
                self.assertEqual(scalar._bsocket.node.data_type, 'FLOAT')
                self.assertEqual(vector._bsocket.node.data_type, 'FLOAT_VECTOR')
                input_socket = vector._bsocket.node.inputs['Vector']
                input_value = input_socket.links[0].from_node.vector if input_socket.is_linked else input_socket.default_value
                for actual, expected in zip(input_value, (.2, .3, .4)):
                    self.assertAlmostEqual(actual, expected)
                self.assertNotIn('data_type', inspect.signature(core.Vector((0, 0, 0)).map_range).parameters)
                self.assertEqual(core.Float(.5).interpolate()._bsocket.node.bl_idname, 'ShaderNodeMapRange')
                mixed = core.Float(1).mix(2, factor=.5)
                self.assertEqual(mixed._bsocket.node.data_type, 'FLOAT')
                b = next(socket for socket in mixed._bsocket.node.inputs if socket.enabled and socket.name == 'B')
                b_value = b.links[0].from_socket.default_value if b.is_linked else b.default_value
                self.assertEqual(b_value, 2)
                mixed_vector = core.Vector((1, 2, 3)).mix((4, 5, 6), factor=.5)
                self.assertEqual(mixed_vector._bsocket.node.data_type, 'VECTOR')
                enabled = core.Float(1).enable_output(enable=True)
                self.assertEqual(enabled._bsocket.node.bl_idname, 'NodeEnableOutput')
                self.assertEqual(enabled._bsocket.node.data_type, 'FLOAT')
                self.assertTrue(enabled._bsocket.node.inputs['Value'].is_linked)
                converted = core.Float(1).implicit_conversion()
                self.assertEqual(converted._bsocket.node.bl_idname, 'NodeImplicitConversion')
                self.assertEqual(converted._bsocket.node.data_type, 'FLOAT')
                self.assertTrue(converted._bsocket.node.inputs['Value'].is_linked)
        with core.GeoNodes('Geometry type inference test'):
            mesh = core.Mesh.Cube()
            self.assertNotIn('data_type', inspect.signature(mesh.raycast).parameters)
            self.assertIn('data_type', inspect.signature(core.nd.raycast).parameters)
            raycast = mesh.raycast(attribute=core.Vector((1, 2, 3)))
            self.assertEqual(raycast._bsocket.node.data_type, 'FLOAT_VECTOR')
            sample = core.Curve.Line().sample(value=core.Color((.1, .2, .3, 1)))
            self.assertEqual(sample._bsocket.node.data_type, 'FLOAT_COLOR')
            self.assertEqual(core.Boolean.Random()._bsocket.node.data_type, 'BOOLEAN')
            self.assertIsInstance(core.Float.GridToPoints(), core.Cloud)



if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(EnvironmentsTest))
    if not result.wasSuccessful():
        raise SystemExit(1)
