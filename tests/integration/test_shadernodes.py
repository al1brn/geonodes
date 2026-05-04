"""Tests for core/shadernodes.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.shadernodes import ShaderNodes


# ---------------------------------------------------------------------------
# Fixtures

@pytest.fixture(autouse=True)
def clean_tree_stack():
    Tree.TREE_STACK.clear()
    yield
    Tree.TREE_STACK.clear()


@pytest.fixture(autouse=True)
def clean_test_groups():
    yield
    for name in list(bpy.data.node_groups.keys()):
        if name.startswith("_test_"):
            grp = bpy.data.node_groups.get(name)
            if grp is not None:
                bpy.data.node_groups.remove(grp)
    for name in list(bpy.data.materials.keys()):
        if name.startswith("_test_"):
            mat = bpy.data.materials.get(name)
            if mat is not None:
                bpy.data.materials.remove(mat)


# ---------------------------------------------------------------------------
# Import checks

class TestShaderNodesImport:

    def test_importable(self):
        import core.shadernodes
        assert hasattr(core.shadernodes, 'ShaderNodes')

    def test_no_constants_import(self):
        import core.shadernodes
        assert not hasattr(core.shadernodes, 'constants')

    def test_no_treeinterface_import(self):
        import core.shadernodes
        assert not hasattr(core.shadernodes, 'TreeInterface')

    def test_no_literal_import(self):
        import core.shadernodes
        assert not hasattr(core.shadernodes, 'Literal')

    def test_no_callable_import(self):
        import core.shadernodes
        assert not hasattr(core.shadernodes, 'Callable')

    def test_is_tree_subclass(self):
        assert issubclass(ShaderNodes, Tree)


# ---------------------------------------------------------------------------
# ShaderNodes creation

class TestShaderNodesCreation:

    def test_material_tree(self):
        with ShaderNodes("_test_sn_mat", replace_material=True) as tree:
            assert tree._btree.bl_idname == 'ShaderNodeTree'

    def test_group_tree(self):
        with ShaderNodes("_test_sn_grp", is_group=True) as tree:
            assert tree._btree.bl_idname == 'ShaderNodeTree'
            assert tree._is_group is True

    def test_is_group_false_by_default(self):
        with ShaderNodes("_test_sn_def", replace_material=True) as tree:
            assert tree._is_group is False


# ---------------------------------------------------------------------------
# input_node

class TestShaderNodesInputNode:

    def test_input_node_raises_for_non_group(self):
        from core.scripterror import NodeError
        with pytest.raises(NodeError):
            with ShaderNodes("_test_sn_inp_ng", replace_material=True) as tree:
                _ = tree.input_node

    def test_input_node_ok_for_group(self):
        with ShaderNodes("_test_sn_inp_grp", is_group=True) as tree:
            node = tree.input_node
            assert node is not None


# ---------------------------------------------------------------------------
# output_node

class TestShaderNodesOutputNode:

    def test_output_node_non_group(self):
        with ShaderNodes("_test_sn_out_ng", replace_material=True) as tree:
            node = tree.output_node
            assert node is not None
            assert node._bnode.bl_idname == 'ShaderNodeOutputMaterial'

    def test_output_node_group(self):
        with ShaderNodes("_test_sn_out_grp", is_group=True) as tree:
            node = tree.output_node
            assert node is not None


# ---------------------------------------------------------------------------
# get_output_node with target

class TestShaderNodesGetOutputNode:

    def test_get_output_node_default(self):
        with ShaderNodes("_test_sn_gon_def", replace_material=True) as tree:
            node = tree.get_output_node()
            assert node._bnode.bl_idname == 'ShaderNodeOutputMaterial'

    def test_get_output_node_cycles(self):
        with ShaderNodes("_test_sn_gon_cy", replace_material=True) as tree:
            node = tree.get_output_node(target='CYCLES')
            assert node._bnode.target == 'CYCLES'

    def test_get_output_node_eevee(self):
        with ShaderNodes("_test_sn_gon_ev", replace_material=True) as tree:
            node = tree.get_output_node(target='EEVEE')
            assert node._bnode.target == 'EEVEE'


# ---------------------------------------------------------------------------
# Surface / volume / displacement setters

class TestShaderNodesSetters:

    def test_set_surface(self):
        from core.sock_shader import Shader
        with ShaderNodes("_test_sn_surf", replace_material=True) as tree:
            s = Shader.Principled()
            tree.set_surface(s)

    def test_set_volume(self):
        from core.sock_shader import VolumeShader
        with ShaderNodes("_test_sn_vol", replace_material=True) as tree:
            v = VolumeShader.Principled()
            tree.set_volume(v)

    def test_set_displacement(self):
        from core.sock_vector import Vector
        with ShaderNodes("_test_sn_disp", replace_material=True) as tree:
            v = Vector.NormalMap()
            tree.set_displacement(v)

    def test_surface_setter(self):
        from core.sock_shader import Shader
        with ShaderNodes("_test_sn_surf_set", replace_material=True) as tree:
            tree.surface = Shader.Principled()

    def test_volume_setter(self):
        from core.sock_shader import VolumeShader
        with ShaderNodes("_test_sn_vol_set", replace_material=True) as tree:
            tree.volume = VolumeShader.Principled()

    def test_displacement_setter(self):
        from core.sock_vector import Vector
        with ShaderNodes("_test_sn_disp_set", replace_material=True) as tree:
            tree.displacement = Vector.NormalMap()

    def test_surface_getter_raises(self):
        from core.scripterror import NodeError
        with pytest.raises(NodeError):
            with ShaderNodes("_test_sn_surf_get", replace_material=True) as tree:
                _ = tree.surface

    def test_volume_getter_raises(self):
        from core.scripterror import NodeError
        with pytest.raises(NodeError):
            with ShaderNodes("_test_sn_vol_get", replace_material=True) as tree:
                _ = tree.volume

    def test_displacement_getter_raises(self):
        from core.scripterror import NodeError
        with pytest.raises(NodeError):
            with ShaderNodes("_test_sn_disp_get", replace_material=True) as tree:
                _ = tree.displacement

    def test_thickness_getter_raises(self):
        from core.scripterror import NodeError
        with pytest.raises(NodeError, match="thickness"):
            with ShaderNodes("_test_sn_thick_get", replace_material=True) as tree:
                _ = tree.thickness


# ---------------------------------------------------------------------------
# aov_output

class TestShaderNodesAovOutput:

    def test_aov_output_color(self):
        from core.sock_color import Color
        with ShaderNodes("_test_sn_aov_c", replace_material=True) as tree:
            c = Color()
            tree.aov_output(name="MyAOV", color=c)

    def test_aov_output_value(self):
        from core.sock_float import Float
        with ShaderNodes("_test_sn_aov_v", replace_material=True) as tree:
            f = Float()
            tree.aov_output(name="MyVal", value=f)
