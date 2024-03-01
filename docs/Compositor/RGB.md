# Node RGB

- Node name : 'RGB'
- bl_idname : [RGB](https://docs.blender.org/api/current/bpy.types.RGB.html)


``` python
RGB(tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, tag_need_exec=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeRGB', node_label=node_label, node_color=node_color)

    self.tag_need_exec   = tag_need_exec
```
