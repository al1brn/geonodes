"""Run with Blender --background --python generation2/tests/test_additional.py."""
import ast
from copy import deepcopy
from pathlib import Path
import sys
import textwrap
from types import SimpleNamespace as NS
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT.parent))
from geonodes.generation2.tree_class import TreeClass
from geonodes.generation2.node_implementation import NodeImplementation
Implementation = TreeClass('GeometryNodeTree')
from geonodes.generation2 import config
from geonodes.generation2.output import render_modules
from geonodes.generation2.typealiases import TypeAliases


class AdditionalTest(unittest.TestCase):
    def test_standard_calls_preserve_receivers_and_configuration(self):
        saved = (Implementation.files, Implementation.cross_refs,
                 Implementation.tree_type, Implementation.type_aliases)
        configured = deepcopy(config.ADDITIONAL_IMPLEMENTATIONS)
        original = NodeImplementation.gen_node_call
        try:
            for tree_type in ('GeometryNodeTree', 'ShaderNodeTree'):
                Implementation.files, Implementation.cross_refs = {}, {}
                Implementation.tree_type = tree_type
                Implementation.type_aliases = TypeAliases()
                calls = []
                def generate(obj, call):
                    calls.append(call)
                    return original(obj, call)
                with patch.object(NodeImplementation, 'gen_node_call', generate):
                    Implementation.gen_additional()
                maps = [call for call in calls if call.method_name == 'interpolate_NEW']
                self.assertEqual({call.class_name: call.self_socket for call in maps},
                                 {'Float': 'Value', 'Vector': 'Vector'})
                switches = [call for call in calls if call.method_name == 'switch_false']
                self.assertTrue(switches)
                self.assertTrue(all(call.self_socket == 'True' for call in switches))
                for call in calls:
                    call._check()
                    self.assertFalse(call.class_name.startswith('LOOP '))
                for methods in Implementation.files[tree_type].values():
                    for source in methods:
                        function = ast.parse(textwrap.dedent(source)).body[0]
                        # Execute generated methods with a Node recorder.
                        recorded = []
                        marker = object()
                        def node(*args, **kwargs):
                            recorded.append((args, kwargs))
                            return NS(_out=marker)
                        env = {'Node': node}
                        exec('from __future__ import annotations\nclass Methods:\n' + source, env)
                        receiver = object()
                        self.assertIs(getattr(env['Methods'], function.name)(receiver), marker)
                        sockets = recorded[0][1]['named_sockets']
                        if function.name == 'switch_false':
                            self.assertIs(sockets['ID_True'], receiver)
                        else:
                            key = 'ID_Vector' if recorded[0][1]['data_type'] == 'FLOAT_VECTOR' else 'ID_Value'
                            self.assertIs(sockets[key], receiver)
                Implementation.files[tree_type]['type_aliases.py'] = [Implementation.type_aliases.source]
                render_modules(ROOT / 'core_new', tree_type, Implementation.files[tree_type])
            self.assertEqual(config.ADDITIONAL_IMPLEMENTATIONS, configured)
        finally:
            (Implementation.files, Implementation.cross_refs,
             Implementation.tree_type, Implementation.type_aliases) = saved


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
