# Node ImageInfo

- Node name : 'Image Info'
- bl_idname : [GeometryNodeImageInfo](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
ImageInfo(image=None, frame=None, node_label=None, node_color=None)
```
##### Arguments

- image : None
- frame : None

## Implementation

- [Img](/docs/GeoNodes/Img.md) : [image_info](/docs/GeoNodes/Img.md#image_info)

## Init

``` python
def __init__(self, image=None, frame=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeImageInfo', node_label=node_label, node_color=node_color)

    self.image           = image
    self.frame           = frame
```
