# Node Displace

- Node name : 'Displace'
- bl_idname : [CompositorNodeDisplace](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
Displace(image=None, vector=None, x_scale=None, y_scale=None, tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- image : None
- vector : None
- x_scale : None
- y_scale : None
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, vector=None, x_scale=None, y_scale=None, tag_need_exec=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeDisplace', node_label=node_label, node_color=node_color)

    self.tag_need_exec   = tag_need_exec
    self.image           = image
    self.vector          = vector
    self.x_scale         = x_scale
    self.y_scale         = y_scale
```
