"""Run with Blender --background --python core_5_3/tests/test_material_ownership.py."""
from pathlib import Path
import sys
import unittest
import bpy

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from geonodes.core_5_3 import ShaderNodes, GeoNodes, Mesh, Shader, Package, shader
from geonodes.core_5_3.common import blender


class MaterialOwnershipTest(unittest.TestCase):
    root = 'API Ownership Test'

    def tearDown(self):
        for collection in (bpy.data.materials, bpy.data.node_groups):
            for item in list(collection):
                if item.name.startswith(self.root):
                    collection.remove(item)

    def test_unmarked_material_is_preserved_and_suffixed_material_reused(self):
        user = bpy.data.materials.new(self.root)
        user.use_nodes = True
        user.node_tree.nodes.new('ShaderNodeValue')
        before = tuple(n.as_pointer() for n in user.node_tree.nodes)
        with ShaderNodes(self.root) as tree:
            Shader.Diffuse().out()
        owned = tree._material
        self.assertEqual(owned.name, self.root + '.001')
        self.assertEqual(owned['geonodes_api'], self.root)
        self.assertEqual(tuple(n.as_pointer() for n in user.node_tree.nodes), before)
        with ShaderNodes(self.root) as rebuilt:
            Shader.Principled().out()
        self.assertIs(rebuilt._material, owned)
        self.assertEqual(len([m for m in bpy.data.materials if m.name.startswith(self.root)]), 2)
        self.assertIs(blender.get_resource('MATERIAL', self.root), owned)
        self.assertIs(blender.get_resource('MATERIAL', user), user)
        with GeoNodes(self.root + ' geometry'):
            mesh = Mesh.Cube()
            mesh.faces.material = self.root
            material_input = mesh._bsocket.node.inputs['Material']
            self.assertIs(material_input.default_value, owned)
            mesh.out()

    def test_removing_marker_protects_material_and_next_build_creates_new_one(self):
        with ShaderNodes(self.root) as tree:
            Shader.Diffuse().out()
        first = tree._material
        del first['geonodes_api']
        before = tuple(n.as_pointer() for n in first.node_tree.nodes)
        with ShaderNodes(self.root) as rebuilt:
            Shader.Principled().out()
        self.assertIsNot(rebuilt._material, first)
        self.assertEqual(rebuilt._material.name, self.root + '.001')
        self.assertEqual(tuple(n.as_pointer() for n in first.node_tree.nodes), before)
        # A user can also take ownership of the suffixed variant.
        del rebuilt._material['geonodes_api']
        with ShaderNodes(self.root) as third:
            Shader.Diffuse().out()
        self.assertEqual(third._material.name, self.root + '.002')

    def test_renamed_owned_material_and_skipped_build(self):
        with ShaderNodes(self.root, rebuild=False) as tree:
            Shader.Diffuse().out()
        material = tree._material
        material.name = self.root + ' Renamed'
        sentinel = material.node_tree.nodes.new('ShaderNodeValue')
        with ShaderNodes(self.root, rebuild=False) as skipped:
            self.assertFalse(skipped._rebuild)
            Shader.Diffuse()
            self.fail('Existing material should skip this body')
        self.assertIs(skipped._material, material)
        self.assertIn(sentinel, list(material.node_tree.nodes))
        with ShaderNodes(self.root) as rebuilt:
            Shader.Principled().out()
        self.assertIs(rebuilt._material, material)
        self.assertNotIn('ShaderNodeBsdfDiffuse', [n.bl_idname for n in material.node_tree.nodes])

    def test_package_shader_obeys_ownership(self):
        user = bpy.data.materials.new(self.root + ' Surface')
        calls = []
        class Project(Package):
            prefix = self.root
            @shader()
            def surface():
                calls.append(1)
                Shader.Diffuse().out()
        Project.build()
        owned = blender.get_api_material(Project.surface.full_name)
        self.assertIsNot(owned, user)
        Project.build(full=True)
        self.assertIs(blender.get_api_material(Project.surface.full_name), owned)
        self.assertEqual(len(calls), 2)
        self.assertNotIn('geonodes_api', user)


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
