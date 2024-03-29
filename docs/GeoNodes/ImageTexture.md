# Node ImageTexture

- Node name : 'Image Texture'
- bl_idname : [GeometryNodeImageTexture](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageTexture.html)


``` python
ImageTexture(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- vector : None
- frame : None
- extension : 'REPEAT'
- interpolation : Linear

## Implementation

- [IMAGE](/docs/GeoNodes/socket_IMAGE.md) : [image_texture](/docs/GeoNodes/socket_IMAGE.md#image_texture)

## Init

``` python
def __init__(self, image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeImageTexture', node_label=node_label, node_color=node_color, **kwargs)

    self.extension       = extension
    self.interpolation   = interpolation
    self.image           = image
    self.vector          = vector
    self.frame           = frame
```
