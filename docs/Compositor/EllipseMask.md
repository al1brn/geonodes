# Node EllipseMask

- Node name : 'Ellipse Mask'
- bl_idname : [Ellipse Mask](https://docs.blender.org/api/current/bpy.types.Ellipse Mask.html)


``` python
EllipseMask(mask=None, value=None, mask_type='ADD', rotation=0.0, tag_need_exec=None, x=0.5, y=0.5, node_label=None, node_color=None)
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
def __init__(self, mask=None, value=None, mask_type='ADD', rotation=0.0, tag_need_exec=None, x=0.5, y=0.5, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeEllipseMask', node_label=node_label, node_color=node_color)

    self.mask_type       = mask_type
    self.rotation        = rotation
    self.tag_need_exec   = tag_need_exec
    self.x               = x
    self.y               = y
    self.mask            = mask
    self.value           = value
```
