# Node CombineXYZ

- Node name : 'Combine XYZ'
- bl_idname : [CompositorNodeCombineXYZ](https://docs.blender.org/api/current/bpy.types.CompositorNodeCombineXYZ.html)


``` python
CombineXYZ(x=None, y=None, z=None, tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- x : None
- y : None
- z : None
- tag_need_exec : None

## Implementation

- Functions : [combine_xyz](/docs/Compositor/CompositorTree.md#combine_xyz)

## Init

``` python
def __init__(self, x=None, y=None, z=None, tag_need_exec=None, node_label=None, node_color=None):

    Node.__init__(self, 'CompositorNodeCombineXYZ', node_label=node_label, node_color=node_color)

    self.tag_need_exec   = tag_need_exec
    self.x               = x
    self.y               = y
    self.z               = z
```