# Node MagicTexture

- Node name : 'Magic Texture'
- bl_idname : [ShaderNodeTexMagic](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMagic.html)


``` python
MagicTexture(vector=None, scale=None, distortion=None, color_mapping=None, texture_mapping=None, turbulence_depth=2, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vector : None
- scale : None
- distortion : None
- color_mapping : None
- texture_mapping : None
- turbulence_depth : 2

## Implementation

- Functions : [magic_texture](/docs/GeoNodes/GeoNodesTree.md#magic_texture)

## Init

``` python
def __init__(self, vector=None, scale=None, distortion=None, color_mapping=None, texture_mapping=None, turbulence_depth=2, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeTexMagic', node_label=node_label, node_color=node_color, **kwargs)

    self.color_mapping   = color_mapping
    self.texture_mapping = texture_mapping
    self.turbulence_depth = turbulence_depth
    self.vector          = vector
    self.scale           = scale
    self.distortion      = distortion
```
