# Node ImageInfo

- Node name : 'Image Info'
- bl_idname : [GeometryNodeImageInfo](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageInfo.html)


``` python
ImageInfo(image=None, frame=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- frame : None

## Implementation

- [IMAGE](/docs/GeoNodes/socket_IMAGE.md) : [image_info](/docs/GeoNodes/socket_IMAGE.md#image_info)

## Init

``` python
def __init__(self, image=None, frame=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeImageInfo', node_label=node_label, node_color=node_color, **kwargs)

    self.image           = image
    self.frame           = frame
```
