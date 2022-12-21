# Node Noise Texture

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)
- geonodes name: `NoiseTexture`
- bl_idname: `ShaderNodeTexNoise`

```python
from geonodes import nodes

node = nodes.NoiseTexture(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D')
```

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

#### class [Texture](Texture.md)

 - [noise](Texture.md#noise-staticmethod)
 - [noise_1D](Texture.md#noise_1D-staticmethod)
 - [noise_2D](Texture.md#noise_2D-staticmethod)
 - [noise_3D](Texture.md#noise_3D-staticmethod)
 - [noise_4D](Texture.md#noise_4D-staticmethod)
