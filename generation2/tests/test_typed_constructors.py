"""Run with Blender --background --python generation2/tests/test_typed_constructors.py."""
import ast
from pathlib import Path
import sys
import textwrap
import unittest
from unittest.mock import patch
from types import SimpleNamespace as NS

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT.parent))
from geonodes.generation2.tree_class import TreeClass
from geonodes.generation2.node_implementation import NodeImplementation
Implementation = TreeClass('GeometryNodeTree')
from geonodes.generation2.output import render_modules
from geonodes.generation2 import gen_config
from geonodes.core_new.root.tree import Tree


class TypedConstructorsTest(unittest.TestCase):
    def test_collect_render_and_call_in_each_environment(self):
        saved = Implementation.files, Implementation.cross_refs, Implementation.tree_type
        try:
            Implementation.files, Implementation.cross_refs = {}, {}
            for tree_type in ('GeometryNodeTree', 'ShaderNodeTree'):
                Implementation.tree_type = tree_type
                specs = []
                original = Implementation.register_source
                def register(node, call, source, **kwargs):
                    self.assertIsNone(node)
                    self.assertEqual(call.in_line, source)
                    call._check()
                    specs.append(call)
                    return original(node, call, source, **kwargs)
                with patch.object(Implementation, 'register_source', side_effect=register):
                    Implementation.gen_typed_constructors()
                self.assertTrue(specs)
                sources = Implementation.files[tree_type]
                render_modules(ROOT / 'core_new', tree_type, sources)
                for filename, methods in sources.items():
                    names = [ast.parse(textwrap.dedent(s)).body[0].name for s in methods]
                    self.assertEqual(len(names), len(set(names)))
                    self.assertIn('_create_input_socket', names)
                    # Execute every generated constructor, recording its final call.
                    env = {'__name__': 'geonodes.core_new.geonodes.generated.probe',
                           '__package__': 'geonodes.core_new.geonodes.generated',
                           'utils': NS(python_value_for_socket=lambda value, kind: value)}
                    exec('from __future__ import annotations\nclass Probe:\n'
                         '    SOCKET_TYPE = "TEST"\n'
                         '    def __new__(cls, **kwargs):\n        return kwargs\n'
                         + '\n'.join(methods), env)
                    probe = env['Probe']
                    descriptor = next(d for d in gen_config.SOCKETS.values()
                                      if d['class_name'].lower() + '.py' == filename)
                    recorder = NS(create_input_socket=lambda *a, **kw: (a, kw))
                    with patch.object(Tree, 'current_tree', return_value=recorder):
                        args, kwargs = probe._create_input_socket(name='Test', panel='Settings')
                    self.assertEqual(args, (descriptor[tree_type],))
                    self.assertEqual(kwargs['name'], 'Test')
                    self.assertEqual(kwargs['panel'], 'Settings')
                    if 'default' in descriptor['props']:
                        self.assertIn('default_value', kwargs)
                        self.assertNotIn('value', kwargs)
                        if descriptor['class_name'] == 'String':
                            self.assertEqual(kwargs['default_value'], '')
                    for subtype in descriptor.get('subtypes', ()):
                        if subtype == 'NONE':
                            continue
                        name = ''.join(part.title() for part in subtype.split('_'))
                        forwarded = getattr(probe, name)(name='Typed', panel='Panel')
                        self.assertEqual(forwarded['subtype'], subtype)
                        self.assertEqual(forwarded['name'], 'Typed')
                        self.assertEqual(forwarded['panel'], 'Panel')
                self.assertEqual(set(Implementation.files),
                                 {'GeometryNodeTree'} if tree_type == 'GeometryNodeTree'
                                 else {'GeometryNodeTree', 'ShaderNodeTree'})
        finally:
            Implementation.files, Implementation.cross_refs, Implementation.tree_type = saved


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
