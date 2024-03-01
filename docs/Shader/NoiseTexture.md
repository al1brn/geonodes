# Node NoiseTexture

- Node name : 'Noise Texture'
- bl_idname : [Noise Texture](https://docs.blender.org/api/current/bpy.types.Noise Texture.html)


``` python
NoiseTexture(vector=None, scale=None, detail=None, roughness=None, lacunarity=None, distortion=None, w=None, color_mapping=None, noise_dimensions='3D', normalize=True, texture_mapping=None, node_label=None, node_color=None)
```
##### Arguments

- vector : None
- scale : None
- detail : None
- roughness : None
- lacunarity : None
- distortion : None
- w : None
- color_mapping : None
- noise_dimensions : '3D'
- normalize : True
- texture_mapping : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, vector=None, scale=None, detail=None, roughness=None, lacunarity=None, distortion=None, w=None, color_mapping=None, noise_dimensions='3D', normalize=True, texture_mapping=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeTexNoise', node_label=node_label, node_color=node_color)

    self.color_mapping   = color_mapping
    self.noise_dimensions = noise_dimensions
    self.normalize       = normalize
    self.texture_mapping = texture_mapping
    self.vector          = vector
    self.scale           = scale
    self.detail          = detail
    self.roughness       = roughness
    self.lacunarity      = lacunarity
    self.distortion      = distortion
    self.w               = w
```
