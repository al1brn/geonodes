# Node MagicTexture

- Node name : 'Magic Texture'
- bl_idname : ShaderNodeTexMagic


``` python
MagicTexture(vector=None, scale=None, distortion=None, color_mapping=None, texture_mapping=None, turbulence_depth=2, node_label=None, node_color=None)
```
##### Arguments

- vector : None
- scale : None
- distortion : None
- color_mapping : None
- texture_mapping : None
- turbulence_depth : 2

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, vector=None, scale=None, distortion=None, color_mapping=None, texture_mapping=None, turbulence_depth=2, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeTexMagic', node_label=node_label, node_color=node_color)

    self.color_mapping   = color_mapping
    self.texture_mapping = texture_mapping
    self.turbulence_depth = turbulence_depth
    self.vector          = vector
    self.scale           = scale
    self.distortion      = distortion
```
