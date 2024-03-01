# Node ImageTexture

- Node name : 'Image Texture'
- bl_idname : ShaderNodeTexImage


``` python
ImageTexture(vector=None, color_mapping=None, extension='REPEAT', image=None, image_user=None, interpolation='Linear', projection='FLAT', projection_blend=0.0, texture_mapping=None, node_label=None, node_color=None)
```
##### Arguments

- vector : None
- color_mapping : None
- extension : 'REPEAT'
- image : None
- image_user : None
- interpolation : Linear
- projection : 'FLAT'
- projection_blend : 0.0
- texture_mapping : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, vector=None, color_mapping=None, extension='REPEAT', image=None, image_user=None, interpolation='Linear', projection='FLAT', projection_blend=0.0, texture_mapping=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeTexImage', node_label=node_label, node_color=node_color)

    self.color_mapping   = color_mapping
    self.extension       = extension
    self.image           = image
    self.image_user      = image_user
    self.interpolation   = interpolation
    self.projection      = projection
    self.projection_blend = projection_blend
    self.texture_mapping = texture_mapping
    self.vector          = vector
```
