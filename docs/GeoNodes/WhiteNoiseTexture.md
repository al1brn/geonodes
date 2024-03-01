# Node WhiteNoiseTexture

- Node name : 'White Noise Texture'
- bl_idname : [ShaderNodeTexWhiteNoise](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
WhiteNoiseTexture(vector=None, w=None, noise_dimensions='3D', node_label=None, node_color=None)
```
##### Arguments

- vector : None
- w : None
- noise_dimensions : '3D'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, vector=None, w=None, noise_dimensions='3D', node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeTexWhiteNoise', node_label=node_label, node_color=node_color)

    self.noise_dimensions = noise_dimensions
    self.vector          = vector
    self.w               = w
```
