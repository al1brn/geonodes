# Node Normal

- Node name : 'Normal'
- bl_idname : [CompositorNodeNormal](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
Normal(normal=None, tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- normal : None
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, normal=None, tag_need_exec=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeNormal', node_label=node_label, node_color=node_color)

    self.tag_need_exec   = tag_need_exec
    self.normal          = normal
```
