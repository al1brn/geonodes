# Node BrickTexture

- Node name : 'Brick Texture'
- bl_idname : [ShaderNodeTexBrick](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexBrick.html)


``` python
BrickTexture(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, color_mapping=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2, texture_mapping=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vector : None
- color1 : None
- color2 : None
- mortar : None
- scale : None
- mortar_size : None
- mortar_smooth : None
- bias : None
- brick_width : None
- row_height : None
- color_mapping : None
- offset : 0.5
- offset_frequency : 2
- squash : 1.0
- squash_frequency : 2
- texture_mapping : None

## Implementation

- Functions : [brick_texture](/docs/Shader/ShaderTree.md#brick_texture)

## Init

``` python
def __init__(self, vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, color_mapping=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2, texture_mapping=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeTexBrick', node_label=node_label, node_color=node_color, **kwargs)

    self.color_mapping   = color_mapping
    self.offset          = offset
    self.offset_frequency = offset_frequency
    self.squash          = squash
    self.squash_frequency = squash_frequency
    self.texture_mapping = texture_mapping
    self.vector          = vector
    self.color1          = color1
    self.color2          = color2
    self.mortar          = mortar
    self.scale           = scale
    self.mortar_size     = mortar_size
    self.mortar_smooth   = mortar_smooth
    self.bias            = bias
    self.brick_width     = brick_width
    self.row_height      = row_height
```
