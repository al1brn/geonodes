# class NoiseTexture (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : NoiseTexture
 - bl_idname : ShaderNodeTexNoise

Node parameters
 - color_mapping
 - noise_dimensions : '3D'
 - normalize : True
 - texture_mapping

Input sockets
 - vector : Vect
 - w : Float
 - scale : Float
 - detail : Float
 - roughness : Float
 - lacunarity : Float
 - distortion : Float

Output sockets
 - fac : Float
 - color : Col

### Header

``` python
def NoiseTexture(self, vector=None, scale=None, detail=None, roughness=None, lacunarity=None, distortion=None, w=None, color_mapping=None, noise_dimensions='3D', normalize=True, texture_mapping=None, node_label=None, node_color=None):
```

## Implementations


