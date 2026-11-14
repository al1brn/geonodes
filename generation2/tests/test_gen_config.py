"""Run with Blender --background --python generation2/tests/test_gen_config.py."""
from pathlib import Path
from copy import deepcopy
from tempfile import TemporaryDirectory
import sys
import unittest
from unittest.mock import patch
import bpy

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from geonodes.generation2 import gen_config, config
from geonodes.generation2.generate import generate
from geonodes.generation2.tree_class import TreeClass


class ConfigPreflightTest(unittest.TestCase):
    def resources(self):
        return ({group.as_pointer() for group in bpy.data.node_groups},
                {material.as_pointer() for material in bpy.data.materials})

    def test_build_cleans_temporary_trees_and_preserves_existing_data(self):
        existing = bpy.data.node_groups.new('Temp GeometryNodeTree', 'GeometryNodeTree')
        try:
            before = self.resources()
            gen_config.build()
            self.assertEqual(self.resources(), before)
        finally:
            bpy.data.node_groups.remove(existing)

    def test_failed_introspection_also_cleans_temporary_trees(self):
        before = self.resources()
        with patch.object(gen_config, 'get_enum', side_effect=RuntimeError('probe failed')):
            with self.assertRaisesRegex(RuntimeError, 'probe failed'):
                gen_config.build()
        self.assertEqual(self.resources(), before)

    def test_build_and_export_leave_manual_configuration_unchanged(self):
        original = deepcopy(config.INPUT_SOCKETS_PROPS)
        gen_config.build()
        self.assertEqual(config.INPUT_SOCKETS_PROPS, original)
        self.assertEqual(set(config.TREE_MODULES), set(config.TREE_TYPES))
        with TemporaryDirectory() as folder, patch.object(gen_config, 'target_core', return_value=Path(folder)):
            gen_config.write_file()
            path, = Path(folder).glob('config_*.py')
            exported = {}
            exec(compile(path.read_text(), str(path), 'exec'), exported)
            self.assertEqual(exported['GEOMETRY_CLASSES'], config.GEOMETRY_CLASSES)
            self.assertEqual(exported['PYTHON_TYPES'], config.PYTHON_TYPES)

    def test_new_socket_stops_before_collecting_or_writing(self):
        known = dict(config.SOCKET_BLID_TO_TYPE)
        known.pop('NodeSocketFloat')
        with patch.dict(config.SOCKET_BLID_TO_TYPE, known, clear=True):
            with patch.object(TreeClass, 'generate') as collect, patch.object(Path, 'write_text') as write:
                with self.assertRaisesRegex(RuntimeError, 'NodeSocketFloat'):
                    generate()
                collect.assert_not_called()
                write.assert_not_called()

    def test_missing_class_stops_before_remaining_tables(self):
        unknown = {'NEW': {'class_name': 'UnknownClass',
                          'GeometryNodeTree': 'NodeSocketNew', 'ShaderNodeTree': None}}
        with patch.object(gen_config, 'check_socket_types'), patch.object(gen_config, 'get_sockets', return_value=unknown):
            with patch.object(gen_config, 'get_node_info') as node_info:
                with self.assertRaisesRegex(RuntimeError, 'NEW -> UnknownClass'):
                    gen_config.build()
                node_info.assert_not_called()
        # A rejected build must not be mistaken for a usable cached configuration.
        self.assertNotEqual(gen_config.SOCKETS, unknown)


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
