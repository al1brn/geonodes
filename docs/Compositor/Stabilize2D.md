# Node Stabilize2D

- Node name : 'Stabilize 2D'
- bl_idname : [CompositorNodeStabilize](https://docs.blender.org/api/current/bpy.types.CompositorNodeStabilize.html)


``` python
Stabilize2D(image=None, clip=None, filter_type='BILINEAR', invert=False, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- clip : None
- filter_type : 'BILINEAR'
- invert : False
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, clip=None, filter_type='BILINEAR', invert=False, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeStabilize', node_label=node_label, node_color=node_color, **kwargs)

    self.clip            = clip
    self.filter_type     = filter_type
    self.invert          = invert
    self.tag_need_exec   = tag_need_exec
    self.image           = image
```
