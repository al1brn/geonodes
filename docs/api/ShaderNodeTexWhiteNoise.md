# Node White Noise Texture

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)
- geonodes name: `WhiteNoiseTexture`
- bl_idname: `ShaderNodeTexWhiteNoise`

```python
from geonodes import nodes

node = nodes.WhiteNoiseTexture(vector=None, w=None, noise_dimensions='3D')
```

### Args:

#### Input socket arguments:

- **vector**: [Vector](Vector.md)
- **w**: [Float](Float.md)

#### Node parameter arguments:

- **noise_dimensions** (str): default = '3D' in ('1D', '2D', '3D', '4D')

### Output sockets:

- **value** : [Float](Float.md)
- **color** : [Color](Color.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b19c0>>](Texture.md#white_noise-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b1480>>](Texture.md#white_noise_1D-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b0b50>>](Texture.md#white_noise_2D-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b1420>>](Texture.md#white_noise_3D-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b1b10>>](Texture.md#white_noise_4D-staticmethod)
