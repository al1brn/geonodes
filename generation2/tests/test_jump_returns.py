"""Run with Blender --background --python generation2/tests/test_jump_returns.py."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from geonodes.generation2.node_call import NodeCall
from geonodes.generation2.node_implementation import NodeImplementation
from geonodes.generation2.node_info import NodeInfo
from geonodes.generation2.tree import Tree


class JumpReturnsTest(unittest.TestCase):
    def test_domain_jump_returns_owner_and_can_be_assigned_to_repeat(self):
        import bpy
        from geonodes.core_new import GeoNodes, Mesh, repeat

        name = 'Self Return Domain Test'
        try:
            with GeoNodes(name):
                mesh = Mesh.Cube()
                domain = mesh.points
                self.assertIs(mesh.self_return, mesh)
                self.assertIs(domain.self_return, mesh)
                result = domain(True).delete()
                self.assertIs(result, mesh)
                self.assertEqual(mesh._bsocket.node.bl_idname, 'GeometryNodeDeleteGeometry')
                self.assertIs(mesh.set_position(offset=(1, 0, 0)), mesh)
                for rep in repeat(2, uv=mesh):
                    rep.uv = Mesh(rep.uv).points(True).delete()
                    self.assertIsInstance(rep.uv, Mesh)
                rep.uv.out()
        finally:
            tree = bpy.data.node_groups.get(name)
            if tree is not None:
                bpy.data.node_groups.remove(tree)

    def test_jump_and_return_are_independent(self):
        primary, secondary, explicit = object(), object(), object()
        owner = object()

        class RecordedNode:
            _out = primary

            def __init__(self, *args, **kwargs):
                pass

            def _second_out(self, fallback):
                return secondary

            def __getitem__(self, name):
                return explicit

        class Receiver:
            @property
            def self_return(self):
                return owner

            def get_selection(self):
                return None

            def _jump(self, value):
                self.updated = value

        with Tree('GeometryNodeTree') as tree:
            impl = NodeImplementation(NodeInfo(tree.btree, tree.create_node('Extrude Mesh')))
            cases = [('extrude', True, None, 'OUT', owner),
                     ('get_extrusion', True, None, 'OUT', secondary),
                     ('get_extrusion', False, None, 'OUT', primary),
                     ('extrude', True, 'Top', 'OUT', explicit),
                     ('extrude', True, None, 'SECOND_OUT', secondary),
                     ('extrude', False, None, 'SECOND_OUT', secondary),
                     ('extrude', True, 'Top', 'SECOND_OUT', explicit)]
            for name, jump, output, kind, expected in cases:
                with self.subTest(name=name, jump=jump, output=output):
                    call = NodeCall.method(name, self_socket='Mesh', is_jump=jump,
                                           return_socket=output, return_kind=kind)
                    source = impl._gen_source_code(call)
                    namespace = {'Node': RecordedNode}
                    exec('from __future__ import annotations\nclass Methods:\n' + source, namespace)
                    receiver = Receiver()
                    result = getattr(namespace['Methods'], name)(receiver)
                    self.assertIs(result, expected)
                    self.assertEqual(hasattr(receiver, 'updated'), jump)
                    if jump:
                        self.assertIs(receiver.updated, primary)


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
