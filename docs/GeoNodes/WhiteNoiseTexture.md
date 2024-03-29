# Node WhiteNoiseTexture

- Node name : 'White Noise Texture'
- bl_idname : [ShaderNodeTexWhiteNoise](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)


``` python
WhiteNoiseTexture(vector=None, w=None, noise_dimensions='3D', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vector : None
- w : None
- noise_dimensions : '3D'

## Implementation

- Functions : [white_noise_texture](/docs/GeoNodes/GeoNodesTree.md#white_noise_texture)

## Init

``` python
def __init__(self, vector=None, w=None, noise_dimensions='3D', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeTexWhiteNoise', node_label=node_label, node_color=node_color, **kwargs)

    self.noise_dimensions = noise_dimensions
    self.vector          = vector
    self.w               = w
```
