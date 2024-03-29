# Node Transform

- Node name : 'Transform'
- bl_idname : [CompositorNodeTransform](https://docs.blender.org/api/current/bpy.types.CompositorNodeTransform.html)


``` python
Transform(image=None, x=None, y=None, angle=None, scale=None, filter_type='NEAREST', tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- x : None
- y : None
- angle : None
- scale : None
- filter_type : 'NEAREST'
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, x=None, y=None, angle=None, scale=None, filter_type='NEAREST', tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeTransform', node_label=node_label, node_color=node_color, **kwargs)

    self.filter_type     = filter_type
    self.tag_need_exec   = tag_need_exec
    self.image           = image
    self.x               = x
    self.y               = y
    self.angle           = angle
    self.scale           = scale
```
