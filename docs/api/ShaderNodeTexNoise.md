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

#### [Texture](Texture.md)

 - [noise](Texture.md#noise-staticmethod) ```python nodes.NoiseTexture(vector=vector, w=w, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions=noise_dimensions````
 - [noise_1D](Texture.md#noise_1D-staticmethod) ```python nodes.NoiseTexture(vector=None, w=w, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions='1D'````
 - [noise_2D](Texture.md#noise_2D-staticmethod) ```python nodes.NoiseTexture(vector=vector, w=None, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions='2D'````
 - [noise_3D](Texture.md#noise_3D-staticmethod) ```python nodes.NoiseTexture(vector=vector, w=None, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions='3D'````
 - [noise_4D](Texture.md#noise_4D-staticmethod) ```python nodes.NoiseTexture(vector=vector, w=w, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions='4D'````
