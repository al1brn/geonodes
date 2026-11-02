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
                result = a.compare(2, epsilon=.01)
                self.assertNotIn('compare', type(a).__dict__)
                self.assertIn(environment.replace('.generated', '.sockets.float'), type(a).compare.__module__)
                self.assertEqual(result._bsocket.node.bl_idname, compare_node)
                expected = 'BOOLEAN' if factory is core.GeoNodes else 'VALUE'
                self.assertEqual(result.SOCKET_TYPE, expected)
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
            for name in ('Collection', 'Object', 'Image', 'Material', 'Matrix', 'Rotation', 'Font', 'Sound', 'Texture'):
                self.assertFalse(hasattr(core.shadernodes.generated, name), name)
                self.assertFalse(hasattr(core.shadernodes.sockets, name), name)
            value = core.Float(1)._convert_to_class('Vector')
            self.assertIsInstance(value, core.Vector)
        with core.GeoNodes('Geometry registry test'):
            self.assertNotIn('SHADER', core.utils.SOCKET_CLASSES)
            for name in ('Shader', 'VolumeShader', 'Texture'):
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
