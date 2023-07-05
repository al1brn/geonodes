# Node *Noise Texture*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)
- geonodes name: `NoiseTexture`
- bl_idname: `ShaderNodeTexNoise`

```python
from geonodes import nodes

node = nodes.NoiseTexture(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexNoise.webp)

### Args:

#### Input socket arguments:

- **vector**: [Vector](Vector.md)
- **w**: [Float](Float.md)
- **scale**: [Float](Float.md)
- **detail**: [Float](Float.md)
- **roughness**: [Float](Float.md)
- **distortion**: [Float](Float.md)

#### Node parameter arguments:

- **noise_dimensions** (str): default = '3D' in ('1D', '2D', '3D', '4D')

### Output sockets:

- **fac** : [Float](Float.md)
- **color** : [Color](Color.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Texture](Texture.md)** |
| [Noise](Texture.md#Noise) | `@staticmethod`<br> `def Noise(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D'):` |
| [Noise1D](Texture.md#Noise1D) | `@staticmethod`<br> `def Noise1D(w=None, scale=None, detail=None, roughness=None, distortion=None):` |
| [Noise2D](Texture.md#Noise2D) | `@staticmethod`<br> `def Noise2D(vector=None, scale=None, detail=None, roughness=None, distortion=None):` |
| [Noise3D](Texture.md#Noise3D) | `@staticmethod`<br> `def Noise3D(vector=None, scale=None, detail=None, roughness=None, distortion=None):` |
| [Noise4D](Texture.md#Noise4D) | `@staticmethod`<br> `def Noise4D(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None):` |

<sub>Go to [top](#node-Noise-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

