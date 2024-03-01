# Node Inpaint

- Node name : 'Inpaint'
- bl_idname : [CompositorNodeInpaint](https://docs.blender.org/api/current/bpy.types.CompositorNodeInpaint.html)


``` python
Inpaint(image=None, distance=0, tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- image : None
- distance : 0
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, distance=0, tag_need_exec=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeInpaint', node_label=node_label, node_color=node_color)

    self.distance        = distance
    self.tag_need_exec   = tag_need_exec
    self.image           = image
```
