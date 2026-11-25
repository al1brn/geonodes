"""Run with Blender --background --python core_5_2/tests/test_decorator_names.py."""
from pathlib import Path
import sys
import unittest

import bpy

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
import geonodes
from geonodes.core_5_2 import GeoNodes, Package, group, modifier, tool, shader, shader_group


class DecoratorNamesTest(unittest.TestCase):
    def tearDown(self):
        for collection in (bpy.data.node_groups, bpy.data.materials):
            for item in list(collection):
                if item.name.lstrip('.').startswith('Decorator Names Test'):
                    collection.remove(item)

    def test_public_names(self):
        for name in ('group', 'modifier', 'tool', 'shader', 'shader_group'):
            self.assertTrue(callable(getattr(geonodes, name)))
        for name in ('geo_group', 'geo_modifier', 'shader_material'):
            self.assertFalse(hasattr(geonodes, name))
        self.assertTrue(callable(geonodes.Group))
        self.assertTrue(callable(geonodes.Shader))

    def test_private_names_keep_dot_before_package_and_local_prefixes(self):
        calls = []

        class Project(Package):
            prefix = 'Decorator Names Test Class'

            @group(prefix='Local')
            def _private():
                calls.append('private')

            @group()
            def public():
                Project._private()
                Project._private()

            @tool()
            def _edit():
                pass

            @shader()
            def _material():
                pass

        self.assertEqual(Project._private.full_name, '.Decorator Names Test Class Local Private')
        self.assertEqual(Project.public.full_name, 'Decorator Names Test Class Public')
        Project.build(full=True)
        self.assertEqual(calls, ['private'])
        for builder in (Project._private, Project.public, Project._edit):
            self.assertIn(builder.full_name, bpy.data.node_groups)
        self.assertIn(Project._material.full_name, bpy.data.materials)
        Project.public.build()
        self.assertEqual(calls, ['private'])

        package = Package('Instance', prefix='Decorator Names Test Instance')

        @package.group(prefix='Local')
        def _private():
            pass

        self.assertEqual(_private.full_name, '.Decorator Names Test Instance Local Private')
        with GeoNodes('Decorator Names Test Caller'):
            _private()
            _private()
        self.assertIn(_private.full_name, bpy.data.node_groups)
        self.assertEqual(group()(_private.function).full_name, '.Private')
        self.assertEqual(group('Explicit')(_private.function).full_name, 'Explicit')

    def test_tool_options_and_mixed_package(self):
        package = Package('Decorator Names Test', prefix='Decorator Names Test')
        built = []

        @package.group('Group')
        def make_group():
            built.append('group')

        @package.shader('Material')
        def make_material():
            built.append('shader')

        @package.modifier('Modifier')
        def make_modifier():
            built.append('modifier')

        @package.shader_group('Shader Group')
        def make_shader_group():
            built.append('shader_group')

        @package.tool('Tool', edit_mode=True, object_mode=False, mesh=False, curve=True)
        def make_tool():
            """A test tool."""
            built.append('tool')

        package.build()
        self.assertEqual(built, ['group', 'shader', 'modifier', 'shader_group', 'tool'])
        tree = bpy.data.node_groups[make_tool.full_name]
        self.assertTrue(tree.is_tool)
        self.assertTrue(tree.is_mode_edit)
        self.assertFalse(tree.is_mode_object)
        self.assertFalse(tree.is_type_mesh)
        self.assertTrue(tree.is_type_curve)
        self.assertEqual([n.text for n in tree.nodes if n.bl_idname == 'NodeComment'], ['A test tool.'])
        package._build()
        self.assertEqual(len(built), 5)
        self.assertEqual(make_tool.options['prefix'], 'Decorator Names Test')


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
