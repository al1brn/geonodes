# Node SeparateXYZ

- Node name : 'Separate XYZ'
- bl_idname : [CompositorNodeSeparateXYZ](https://docs.blender.org/api/current/bpy.types.CompositorNodeSeparateXYZ.html)


``` python
SeparateXYZ(vector=None, tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- vector : None
- tag_need_exec : None

## Implementation

- [VECTOR](/docs/Compositor/socket_VECTOR.md) : [separate_xyz](/docs/Compositor/socket_VECTOR.md#separate_xyz)

## Init

``` python
def __init__(self, vector=None, tag_need_exec=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeSeparateXYZ', node_label=node_label, node_color=node_color)

    self.tag_need_exec   = tag_need_exec
    self.vector          = vector
```
