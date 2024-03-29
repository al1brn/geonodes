# Node NoiseTexture

- Node name : 'Noise Texture'
- bl_idname : [ShaderNodeTexNoise](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)


``` python
NoiseTexture(vector=None, scale=None, detail=None, roughness=None, lacunarity=None, distortion=None, w=None, offset=None, gain=None, color_mapping=None, noise_dimensions='3D', noise_type='FBM', normalize=True, texture_mapping=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vector : None
- scale : None
- detail : None
- roughness : None
- lacunarity : None
- distortion : None
- w : None
- offset : None
- gain : None
- color_mapping : None
- noise_dimensions : '3D'
- noise_type : 'FBM'
- normalize : True
- texture_mapping : None

## Implementation

- Functions : [noise_texture](/docs/GeoNodes/GeoNodesTree.md#noise_texture)

## Init

``` python
def __init__(self, vector=None, scale=None, detail=None, roughness=None, lacunarity=None, distortion=None, w=None, offset=None, gain=None, color_mapping=None, noise_dimensions='3D', noise_type='FBM', normalize=True, texture_mapping=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeTexNoise', node_label=node_label, node_color=node_color, **kwargs)

    self.color_mapping   = color_mapping
    self.noise_dimensions = noise_dimensions
    self.noise_type      = noise_type
    self.normalize       = normalize
    self.texture_mapping = texture_mapping
    self.vector          = vector
    self.scale           = scale
    self.detail          = detail
    self.roughness       = roughness
    self.lacunarity      = lacunarity
    self.distortion      = distortion
    self.w               = w
    self.offset          = offset
    self.gain            = gain
```
