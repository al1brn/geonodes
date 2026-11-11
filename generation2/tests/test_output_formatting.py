"""Run without Blender: python3 -B generation2/tests/test_output_formatting.py."""
from pathlib import Path
import runpy
import unittest

specialize = runpy.run_path(str(Path(__file__).resolve().parents[1] / 'output.py'))['specialize_source']


class OutputFormattingTest(unittest.TestCase):
    def execute(self, source, tree_type):
        output = specialize(source, tree_type)
        namespace = {}
        exec(compile(output, '<specialized>', 'exec'), namespace)
        return output, namespace

    def test_unchanged_source_is_preserved_exactly(self):
        source = "# Header\ndef build(\n    value = 1,\n):\n    # Keep layout\n    return dict(\n        value=value,\n    )\n"
        self.assertEqual(specialize(source, 'GeometryNodeTree'), source)

    def test_selected_branches_keep_comments_and_layout(self):
        source = '''# Header
if tree.bl_idname == 'GeometryNodeTree':
    # Geometry comment
    value = dict(
        number = 1,
    )
else:
    # Shader comment
    value = dict(
        number = 2,
    )
# Footer
'''
        for tree_type, number, comment in [('GeometryNodeTree', 1, 'Geometry'), ('ShaderNodeTree', 2, 'Shader')]:
            output, namespace = self.execute(source, tree_type)
            self.assertEqual(namespace['value'], {'number': number})
            self.assertIn(f'# {comment} comment', output)
            self.assertIn(f'value = dict(\n    number = {number},\n)', output)
            self.assertTrue(output.startswith('# Header\n'))
            self.assertTrue(output.endswith('# Footer\n'))

    def test_nested_branches_and_multiline_header(self):
        source = '''def build():
    if (
        tree.bl_idname != 'ShaderNodeTree'
    ):
        if tree.bl_idname == 'GeometryNodeTree':
            return 1
        else:
            return 2
    else:
        return 3
value = build()
'''
        for tree_type, expected in [('GeometryNodeTree', 1), ('ShaderNodeTree', 3)]:
            _, namespace = self.execute(source, tree_type)
            self.assertEqual(namespace['value'], expected)

    def test_multiline_string_value_is_preserved(self):
        source = "if tree.bl_idname == 'GeometryNodeTree':\n    value = '''first\n        middle\n    last'''\nelse:\n    value = 'shader'\n"
        _, namespace = self.execute(source, 'GeometryNodeTree')
        self.assertEqual(namespace['value'], 'first\n        middle\n    last')

    def test_elif_and_empty_suite(self):
        source = "def build(flag):\n    if flag:\n        return 0\n    elif tree.bl_idname == 'GeometryNodeTree':\n        return 1\n    else:\n        return 2\nvalue = build(False)\n"
        for tree_type, expected in [('GeometryNodeTree', 1), ('ShaderNodeTree', 2)]:
            _, namespace = self.execute(source, tree_type)
            self.assertEqual(namespace['value'], expected)
        source = "def build():\n    if tree.bl_idname == 'GeometryNodeTree':\n        return 1\nvalue = build()\n"
        _, namespace = self.execute(source, 'ShaderNodeTree')
        self.assertIsNone(namespace['value'])

    def test_inline_and_elif_alternative(self):
        source = "if tree.bl_idname == 'GeometryNodeTree': value = 1 # Keep\nelif True:\n    value = 2\nelse:\n    value = 3\n"
        for tree_type, expected in [('GeometryNodeTree', 1), ('ShaderNodeTree', 2)]:
            _, namespace = self.execute(source, tree_type)
            self.assertEqual(namespace['value'], expected)

    def test_elif_selection_keeps_multiline_string_value(self):
        source = "if False:\n    value = None\nelif tree.bl_idname == 'GeometryNodeTree':\n    value = '''first\n        middle\n    last'''\n"
        _, namespace = self.execute(source, 'GeometryNodeTree')
        self.assertEqual(namespace['value'], 'first\n        middle\n    last')

    def test_render_modules_keeps_generated_layout(self):
        root = Path(__file__).resolve().parents[2]
        render = runpy.run_path(str(root / 'generation2/output.py'))['render_modules']
        method = "    @classmethod\n    def example(\n        cls,\n        value = None,\n    ):\n        # Preserve this comment\n        return value\n"
        modules = render(root / 'core_new', 'GeometryNodeTree', {'static_nd.py': [method]})
        source = modules[root / 'core_new/geonodes/generated/static_nd.py']
        self.assertIn(method, source)
        compile(source, '<rendered>', 'exec')


if __name__ == '__main__':
    unittest.main()
