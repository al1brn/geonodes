# Node Wave Texture

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)
- geonodes name: `WaveTexture`
- bl_idname: `ShaderNodeTexWave`

```python
from geonodes import nodes

node = nodes.WaveTexture(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS')
```

### Args:

#### Input socket arguments:

- **vector**: [Vector](Vector.md)
- **scale**: [Float](Float.md)
- **distortion**: [Float](Float.md)
- **detail**: [Float](Float.md)
- **detail_scale**: [Float](Float.md)
- **detail_roughness**: [Float](Float.md)
- **phase_offset**: [Float](Float.md)

#### Node parameter arguments:

- **bands_direction** (str): default = 'X' in ('X', 'Y', 'Z', 'DIAGONAL')
- **rings_direction** (str): default = 'X' in ('X', 'Y', 'Z', 'SPHERICAL')
- **wave_profile** (str): default = 'SIN' in ('SIN', 'SAW', 'TRI')
- **wave_type** (str): default = 'BANDS' in ('BANDS', 'RINGS')

### Output sockets:

- **color** : [Color](Color.md)
- **fac** : [Float](Float.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b1090>>](Texture.md#wave-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b01f0>>](Texture.md#wave_bands-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b08b0>>](Texture.md#wave_rings-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b0e50>>](Texture.md#wave_bands_sine-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b09d0>>](Texture.md#wave_bands_saw-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b3010>>](Texture.md#wave_bands_triangle-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b0d90>>](Texture.md#wave_rings_sine-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b07f0>>](Texture.md#wave_rings_saw-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b2500>>](Texture.md#wave_rings_triangle-staticmethod)
