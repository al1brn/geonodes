# Node RGB

- Node name : 'RGB'
- bl_idname : [CompositorNodeRGB](https://docs.blender.org/api/current/bpy.types.CompositorNodeRGB.html)


``` python
RGB(tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeRGB', node_label=node_label, node_color=node_color, **kwargs)

    self.tag_need_exec   = tag_need_exec
```
