"""Run with Blender --background --python core_new/tests/test_decorator_docstrings.py."""
from inspect import cleandoc
from pathlib import Path
import sys
import unittest

import bpy

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from geonodes.core_new.decorators import group, modifier, tool, shader_group, shader
from geonodes.kernel.colors import SysColor


class DecoratorDocstringsTest(unittest.TestCase):
    def tearDown(self):
        for collection in (bpy.data.node_groups, bpy.data.materials):
            for item in list(collection):
                if item.name.startswith('Docstring Test '):
                    collection.remove(item)

    def test_docstring_on_all_builder_types_and_rebuild(self):
        for decorator in (group, modifier, tool, shader_group, shader):
            with self.subTest(decorator=decorator.__name__):
                name = 'Docstring Test ' + decorator.__name__
                calls = []

                def function():
                    """Description du groupe.

                    Deuxième paragraphe avec indentation.
                    """
                    calls.append(True)
                    return 42

                builder = decorator(name)(function)
                self.assertEqual(builder.build(), 42)
                tree = (bpy.data.materials[name].node_tree if decorator is shader
                        else bpy.data.node_groups[name])
                comments = [n for n in tree.nodes if n.bl_idname == 'NodeComment']
                self.assertEqual(len(comments), 1)
                self.assertEqual(comments[0].text, cleandoc(function.__doc__))
                self.assertEqual(comments[0]['arrange_horizontal'], 'left')
                self.assertEqual(comments[0]['arrange_vertical'], 'outer_top')
                function.__doc__ = 'Updated description.'
                self.assertIsNone(builder._build())
                self.assertEqual(len(calls), 1)
                self.assertNotEqual(comments[0].text, function.__doc__)
                builder.build()
                tree = (bpy.data.materials[name].node_tree if decorator is shader
                        else bpy.data.node_groups[name])
                comments = [n for n in tree.nodes if n.bl_idname == 'NodeComment']
                self.assertEqual(len(comments), 1)
                self.assertEqual(comments[0].text, function.__doc__)

    def test_no_comment_for_missing_or_empty_docstring(self):
        for index, doc in enumerate((None, '', '   \n  ')):
            def function():
                pass
            function.__doc__ = doc
            name = f'Docstring Test empty {index}'
            group(name)(function).build()
            self.assertFalse(any(n.bl_idname == 'NodeComment'
                                 for n in bpy.data.node_groups[name].nodes))

    def test_color_directive_is_applied_and_removed_from_text(self):
        for decorator in (group, modifier, tool, shader_group, shader):
            name = 'Docstring Test color ' + decorator.__name__

            @decorator(name)
            def function():
                """
                :color: #405a80

                Description du groupe.

                Deuxième paragraphe.
                """
                pass

            function.build()
            tree = (bpy.data.materials[name].node_tree if decorator is shader
                    else bpy.data.node_groups[name])
            comment, = (n for n in tree.nodes if n.bl_idname == 'NodeComment')
            self.assertEqual(comment.text, 'Description du groupe.\n\nDeuxième paragraphe.')
            self.assertTrue(comment.use_custom_color)
            for actual, expected in zip(comment.color, SysColor('#405a80').bcolor):
                self.assertAlmostEqual(actual, expected, places=6)

    def test_invalid_color_is_reported(self):
        @group('Docstring Test invalid color')
        def function():
            """:color: notacolor

            Description.
            """
            pass

        with self.assertRaisesRegex(ValueError, 'notacolor'):
            function.build()

    def test_named_color_after_description(self):
        @modifier('Docstring Test named color')
        def function():
            """Hello les poteaux

            :color: red
            """
            pass

        function.build()
        tree = bpy.data.node_groups[function.full_name]
        comment, = (n for n in tree.nodes if n.bl_idname == 'NodeComment')
        self.assertEqual(comment.text, 'Hello les poteaux')
        self.assertTrue(comment.use_custom_color)
        self.assertEqual(tuple(comment.color), tuple(SysColor('red').bcolor))

    def test_width_and_color_on_all_builder_types(self):
        for decorator in (group, modifier, tool, shader_group, shader):
            name = 'Docstring Test width ' + decorator.__name__

            @decorator(name)
            def function():
                """Description.

                :color: red
                :width: 200
                """
                pass

            function.build()
            tree = (bpy.data.materials[name].node_tree if decorator is shader
                    else bpy.data.node_groups[name])
            comment, = (n for n in tree.nodes if n.bl_idname == 'NodeComment')
            self.assertEqual(comment.text, 'Description.')
            self.assertEqual(comment.width, 200)
            self.assertTrue(comment.use_custom_color)

    def test_invalid_width_is_reported(self):
        for index, value in enumerate(('large', '-1', '0', 'nan', 'inf')):
            def function():
                pass
            function.__doc__ = f'Description.\n\n:width: {value}'
            builder = group(f'Docstring Test invalid width {index}')(function)
            with self.assertRaisesRegex(ValueError, ':width: expects a positive number'):
                builder.build()

    def test_arrange_metadata_is_removed_and_stored(self):
        @group('Docstring Test arrange')
        def function():
            """Description.

            :horizontal: outer_right
            :vertical: mid
            """
            pass

        function.build()
        tree = bpy.data.node_groups[function.full_name]
        comment, = (n for n in tree.nodes if n.bl_idname == 'NodeComment')
        self.assertEqual(comment.text, 'Description.')
        self.assertEqual(comment['arrange_horizontal'], 'outer_right')
        self.assertEqual(comment['arrange_vertical'], 'mid')


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
