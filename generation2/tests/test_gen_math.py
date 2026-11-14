"""Run with Blender --background --python generation2/tests/test_gen_math.py."""
import ast
from pathlib import Path
import sys
import textwrap
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT.parent))
from geonodes.generation2.node_implementation import NodeImplementation
from geonodes.generation2.tree_class import TreeClass
from geonodes.generation2.output import render_modules
from geonodes.generation2.typealiases import TypeAliases


class MathGenerationTest(unittest.TestCase):
    def test_math_uses_specs_and_generates_both_environments(self):
        implementation = TreeClass('GeometryNodeTree')
        saved = (implementation.files, implementation.cross_refs,
                 implementation.tree_type, implementation.type_aliases)
        original = NodeImplementation.gen_node_call
        try:
            for tree_type in ('GeometryNodeTree', 'ShaderNodeTree'):
                with self.subTest(tree_type=tree_type):
                    implementation.tree_type = tree_type
                    implementation.files = {tree_type: {}}
                    implementation.cross_refs = {tree_type: {}}
                    implementation.type_aliases = TypeAliases()
                    specs = []
                    def generate(obj, spec):
                        specs.append(spec)
                        return original(obj, spec)
                    with patch.object(NodeImplementation, 'gen_node_call', generate):
                        implementation.gen_math()
                    sources = implementation.files[tree_type]
                    functions = {ast.parse(textwrap.dedent(source)).body[0].name: source
                                 for source in sources['gnmath.py']}
                    comparison = 'math_compare' if tree_type == 'GeometryNodeTree' else 'compare'
                    self.assertTrue({'add', 'sin', 'trunc', 'floor', 'ceil', 'vfloor', 'vceil',
                                     'vadd', 'iadd', 'band', comparison} <= functions.keys())
                    if tree_type == 'GeometryNodeTree':
                        self.assertIn('bw_shift', functions)
                    else:
                        self.assertNotIn('bw_shift', functions)
                    for spec in specs:
                        self.assertIn('operation', spec.parameters)
                        if spec.has_self:
                            self.assertIsNotNone(spec.self_socket)
                    # Execute a generated function and method using a Node recorder.
                    calls = []
                    marker = object()
                    def Node(*args, **kwargs):
                        calls.append((args, kwargs))
                        return SimpleNamespace(_out=marker)
                    env = {'Node': Node}
                    exec('from __future__ import annotations\n' + functions['add'], env)
                    self.assertIs(env['add'](value=2, value_1=3), marker)
                    self.assertEqual(calls[-1][1]['operation'], 'ADD')
                    self.assertEqual(list(calls[-1][1]['named_sockets'].values()), [2, 3])
                    method = next(source for source in sources['float.py']
                                  if ast.parse(textwrap.dedent(source)).body[0].name == 'add')
                    exec('from __future__ import annotations\nclass FloatMethods:\n' + method, env)
                    receiver = object()
                    self.assertIs(env['FloatMethods'].add(receiver, value_1=4), marker)
                    self.assertEqual(list(calls[-1][1]['named_sockets'].values()), [receiver, 4])
                    names = {ast.parse(textwrap.dedent(source)).body[0].name for source in sources['float.py']}
                    self.assertTrue({'__trunc__', '__floor__', '__ceil__', '__add__', '__radd__', '__iadd__'} <= names)
                    if tree_type == 'GeometryNodeTree':
                        integer_names = {ast.parse(textwrap.dedent(source)).body[0].name for source in sources['integer.py']}
                        self.assertTrue({'__rshift__', '__rrshift__', '__irshift__'} <= integer_names)
                    sources['type_aliases.py'] = [implementation.type_aliases.source]
                    modules = render_modules(ROOT / 'core_new', tree_type, sources)
                    for path, source in modules.items():
                        compile(source, str(path), 'exec')
                    print('MATH_VALIDATED', tree_type, len(functions), 'functions')
        finally:
            (implementation.files, implementation.cross_refs,
             implementation.tree_type, implementation.type_aliases) = saved


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
