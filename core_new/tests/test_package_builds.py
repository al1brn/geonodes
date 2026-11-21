"""Run with Blender --background --python core_new/tests/test_package_builds.py."""
from pathlib import Path
import sys
import unittest
from collections import Counter

import bpy

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from geonodes.core_new import Mesh, Float, Vector, GeoNodes, Package, group, modifier, shader, tool
from geonodes.core_new.decorators import _TreeBuilder


class PackageBuildTest(unittest.TestCase):
    def tearDown(self):
        for collection in (bpy.data.node_groups, bpy.data.materials):
            for item in list(collection):
                if item.name.startswith('Builder Session'):
                    collection.remove(item)

    def test_static_package_and_symbolic_inputs(self):
        calls = []

        class Project(Package):
            prefix = 'Builder Session Project'

            @group()
            def shift(mesh: Mesh, position: Vector = (1, 2, 3)):
                calls.append((mesh.SOCKET_TYPE, position.SOCKET_TYPE))
                mesh.set_position(offset=position).out()

            @modifier()
            def result():
                Project.shift(Mesh.Cube(), position=(2, 3, 4)).out()

        self.assertEqual(Project.shift.full_name, 'Builder Session Project Shift')
        Project.result._build()
        self.assertEqual(calls, [('GEOMETRY', 'VECTOR')])
        tree = bpy.data.node_groups[Project.shift.full_name]
        inputs = [s for s in tree.interface.items_tree if s.item_type == 'SOCKET' and s.in_out == 'INPUT']
        self.assertEqual([(s.name, s.socket_type) for s in inputs],
                         [('mesh', 'NodeSocketGeometry'), ('position', 'NodeSocketVector')])
        self.assertEqual(tuple(inputs[1].default_value), (1, 2, 3))
        Project.result._build()
        self.assertEqual(len(calls), 1)
        self.assertIs(Project.shift, Project.shift)

    def test_build_and_rebuild_with_dependencies_shared_with_free_functions(self):
        calls = Counter()

        @group('Builder Session Low')
        def low(value: float = 1):
            calls['low'] += 1
            value.out()

        class Project(Package):
            prefix = 'Builder Session'

            @group('Middle')
            def middle(value: Float = 2):
                calls['middle'] += 1
                low(value).out()

            @group('Top')
            def top(value: Float = 3):
                calls['top'] += 1
                (Project.middle(value) + low(value) + low(value)).out()

        Project.top._build()
        self.assertEqual(calls, {'low': 1, 'middle': 1, 'top': 1})
        Project.top._build()
        self.assertEqual(calls, {'low': 1, 'middle': 1, 'top': 1})
        Project.top.build()
        self.assertEqual(calls, {'low': 1, 'middle': 1, 'top': 2})
        Project.top.build(full=True)
        self.assertEqual(calls, {'low': 2, 'middle': 2, 'top': 3})
        Project.build(full=True)
        self.assertEqual(calls, {'low': 3, 'middle': 3, 'top': 4})
        self.assertIsNone(_TreeBuilder._session)

    def test_automatic_build_and_internal_full_without_rebuild(self):
        calls = Counter()

        @group('Builder Session Automatic Low')
        def low():
            calls['low'] += 1

        @modifier('Builder Session Automatic Top')
        def top():
            calls['top'] += 1
            low()
            low()

        with GeoNodes('Builder Session Automatic Outer'):
            top()
            top()
        self.assertEqual(calls, {'top': 1, 'low': 1})
        top._build(full=True)
        self.assertEqual(calls, {'top': 2, 'low': 2})
        top.build()
        self.assertEqual(calls, {'top': 3, 'low': 2})
        self.assertIsNone(_TreeBuilder._session)

    def test_package_inheritance_does_not_change_parent_prefix(self):
        class Parent(Package):
            prefix = 'Builder Session Parent'

            @group()
            def value(number: int = 2):
                number.out()

        class Child(Parent):
            prefix = 'Builder Session Child'

        self.assertIsNot(Parent.value, Child.value)
        Parent._build()
        Child._build()
        self.assertIn(Parent.value.full_name, bpy.data.node_groups)
        self.assertIn(Child.value.full_name, bpy.data.node_groups)

    def test_reserved_names_and_invalid_modes(self):
        for name in ('_build', 'build'):
            with self.assertRaisesRegex(TypeError, 'reserved'):
                type('Invalid', (Package,), {name: group()(lambda: None)})
        @group('Builder Session Invalid')
        def invalid():
            pass
        for mode in ('', 'ALL', None, 0, 1):
            with self.assertRaises(TypeError):
                invalid._build(rebuild=mode)
            with self.assertRaises(TypeError):
                invalid.build(full=mode)
            with self.assertRaises(TypeError):
                Package('Invalid').build(full=mode)
        self.assertFalse(hasattr(invalid, 'rebuild'))
        self.assertFalse(hasattr(Package('Invalid'), 'rebuild'))

    def test_class_package_can_mix_materials_and_tools(self):
        calls = Counter()

        class Project(Package):
            prefix = 'Builder Session Mixed'

            @shader()
            def material():
                calls['material'] += 1

            @tool(edit_mode=True)
            def edit():
                calls['tool'] += 1

        Project._build()
        Project._build()
        self.assertEqual(calls, {'material': 1, 'tool': 1})
        Project.build(full=True)
        self.assertEqual(calls, {'material': 2, 'tool': 2})
        self.assertIn(Project.material.full_name, bpy.data.materials)
        self.assertTrue(bpy.data.node_groups[Project.edit.full_name].is_tool)

    def test_defaults_and_parameter_kinds(self):
        @group('Builder Session Signature')
        def function(number: int, /, amount=2.5, *, enabled: bool=True):
            number.out('Number')
            amount.out('Amount')
            enabled.out('Enabled')

        function._build()
        tree = bpy.data.node_groups[function.full_name]
        inputs = [s for s in tree.interface.items_tree if s.item_type == 'SOCKET' and s.in_out == 'INPUT']
        self.assertEqual([s.socket_type for s in inputs],
                         ['NodeSocketInt', 'NodeSocketFloat', 'NodeSocketBool'])
        self.assertEqual(inputs[1].default_value, 2.5)
        self.assertTrue(inputs[2].default_value)

    def test_circular_dependency_cleans_build_state(self):
        @group('Builder Session Circular A')
        def first():
            second()

        @group('Builder Session Circular B')
        def second():
            first()

        with self.assertRaisesRegex(Exception, 'Circular build dependency'):
            first.build(full=True)
        self.assertIsNone(_TreeBuilder._session)
        self.assertFalse(_TreeBuilder._building)


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
