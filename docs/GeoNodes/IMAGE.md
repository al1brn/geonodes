# Node Image

- Node name : 'Image'
- bl_idname : [GeometryNodeInputImage](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputImage.html)


``` python
Image(image=None, node_label=None, node_color=None)
```
##### Arguments

- image : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeInputImage', node_label=node_label, node_color=node_color)

    self.image           = image
```
