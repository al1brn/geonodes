# Node BoxMask

- Node name : 'Box Mask'
- bl_idname : [CompositorNodeBoxMask](https://docs.blender.org/api/current/bpy.types.CompositorNodeBoxMask.html)


``` python
BoxMask(mask=None, value=None, mask_type='ADD', rotation=0.0, tag_need_exec=None, x=0.5, y=0.5, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- mask : None
- value : None
- mask_type : 'ADD'
- rotation : 0.0
- tag_need_exec : None
- x : 0.5
- y : 0.5

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, mask=None, value=None, mask_type='ADD', rotation=0.0, tag_need_exec=None, x=0.5, y=0.5, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeBoxMask', node_label=node_label, node_color=node_color, **kwargs)

    self.mask_type       = mask_type
    self.rotation        = rotation
    self.tag_need_exec   = tag_need_exec
    self.x               = x
    self.y               = y
    self.mask            = mask
    self.value           = value
```
