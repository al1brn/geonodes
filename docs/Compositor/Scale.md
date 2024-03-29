# Node Scale

- Node name : 'Scale'
- bl_idname : [CompositorNodeScale](https://docs.blender.org/api/current/bpy.types.CompositorNodeScale.html)


``` python
Scale(image=None, x=None, y=None, frame_method='STRETCH', offset_x=0.0, offset_y=0.0, space='RELATIVE', tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- x : None
- y : None
- frame_method : 'STRETCH'
- offset_x : 0.0
- offset_y : 0.0
- space : 'RELATIVE'
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, x=None, y=None, frame_method='STRETCH', offset_x=0.0, offset_y=0.0, space='RELATIVE', tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeScale', node_label=node_label, node_color=node_color, **kwargs)

    self.frame_method    = frame_method
    self.offset_x        = offset_x
    self.offset_y        = offset_y
    self.space           = space
    self.tag_need_exec   = tag_need_exec
    self.image           = image
    self.x               = x
    self.y               = y
```
