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

 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b15d0>>](Texture.md#noise-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x16e37bbe0>>](Texture.md#noise_1D-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x16e37a980>>](Texture.md#noise_2D-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x16e3785e0>>](Texture.md#noise_3D-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x16e378550>>](Texture.md#noise_4D-staticmethod)
