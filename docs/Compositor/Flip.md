# Node Flip

- Node name : 'Flip'
- bl_idname : [CompositorNodeFlip](https://docs.blender.org/api/current/bpy.types.CompositorNodeFlip.html)


``` python
Flip(image=None, axis='X', tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- image : None
- axis : 'X'
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, axis='X', tag_need_exec=None, node_label=None, node_color=None):

    Node.__init__(self, 'CompositorNodeFlip', node_label=node_label, node_color=node_color)

    self.axis            = axis
    self.tag_need_exec   = tag_need_exec
    self.image           = image
```
