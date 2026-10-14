"""Regression checks for skipped builds and nested context cleanup (requires Blender)."""
import bpy

from core import GeoNodes, ShaderNodes, Float, Node, Tree, Layout, Panel


def snapshot(tree):
    return (
        [(node.as_pointer(), node.name) for node in tree.nodes],
        [(item.identifier, item.name) for item in tree.interface.items_tree],
        tree.color_tag,
        tree.use_fake_user,
    )


def test_rebuild_policy_and_nested_contexts():
    cases = [(GeoNodes, {}), (GeoNodes, {'is_group': True}),
             (ShaderNodes, {'is_group': True}), (ShaderNodes, {})]
    for index, (cls, options) in enumerate(cases):
        name = f'_test_rebuild_{index}'
        try:
            with cls(name, rebuild=False, **options) as tree:
                assert tree._rebuild
                Node('ShaderNodeValue')
            btree = tree._btree
            before = snapshot(btree)
            for trigger in (lambda: Float(1), lambda: Node('ShaderNodeValue'),
                            lambda: Layout('Ignored'), lambda: Panel('Ignored')):
                with GeoNodes('_test_rebuild_outer') as outer:
                    with cls(name, rebuild=False, **options) as ignored:
                        assert not ignored._rebuild
                        trigger()
                        raise AssertionError('Skipped build did not interrupt the block')
                    assert Tree.current_tree() is outer
                assert snapshot(btree) == before
                assert not Tree.TREE_STACK
            with cls(name, rebuild=False, **options):
                pass
            assert snapshot(btree) == before
            assert not Tree.TREE_STACK
            rebuild_options = dict(options)
            if cls is ShaderNodes and not options:
                rebuild_options['replace_material'] = True
            with cls(name, **rebuild_options) as rebuilt:
                assert rebuilt._rebuild
                assert len(rebuilt._btree.nodes) == 0
            assert not Tree.TREE_STACK
        finally:
            if cls is ShaderNodes and not options:
                bpy.data.materials.remove(bpy.data.materials[name])
            else:
                bpy.data.node_groups.remove(bpy.data.node_groups[name])
            outer_group = bpy.data.node_groups.get('_test_rebuild_outer')
            if outer_group is not None:
                bpy.data.node_groups.remove(outer_group)


def test_loaded_tree_preserves_nodes_interface_and_stack():
    btree = bpy.data.node_groups.new('_test_rebuild_loaded', 'GeometryNodeTree')
    try:
        btree.nodes.new('ShaderNodeValue')
        btree.interface.new_socket(name='Keep', in_out='INPUT', socket_type='NodeSocketFloat')
        before = snapshot(btree)
        with Tree(btree, tree_type=None) as loaded:
            assert loaded._loaded
            assert Tree.current_tree() is loaded
        assert snapshot(btree) == before
        assert not Tree.TREE_STACK
    finally:
        bpy.data.node_groups.remove(btree)


def test_tool_rebuild_preserves_settings():
    name = '_test_rebuild_tool'
    settings = ('is_tool', 'is_modifier', 'is_mode_object', 'is_mode_edit',
                'is_mode_sculpt', 'is_type_mesh', 'is_type_curve',
                'is_type_pointcloud', 'use_wait_for_click')
    try:
        with GeoNodes.Tool(name, rebuild=False, object_mode=False,
                           edit_mode=True, curve=True, wait_for_click=True) as tool:
            assert tool._rebuild
            Node('ShaderNodeValue')
        btree = tool._btree
        before = snapshot(btree)
        flags = tuple(getattr(btree, key) for key in settings)
        with GeoNodes.Tool(name, rebuild=False) as skipped:
            assert not skipped._rebuild
            Float(1)
            raise AssertionError('Skipped tool did not interrupt the block')
        assert snapshot(btree) == before
        assert tuple(getattr(btree, key) for key in settings) == flags
        assert not Tree.TREE_STACK
        with GeoNodes.Tool(name) as rebuilt:
            assert rebuilt._rebuild
            assert len(rebuilt._btree.nodes) == 0
            assert rebuilt._btree.is_mode_object
            assert not rebuilt._btree.is_mode_edit
            assert not rebuilt._btree.use_wait_for_click
        assert not Tree.TREE_STACK
    finally:
        bpy.data.node_groups.remove(bpy.data.node_groups[name])
