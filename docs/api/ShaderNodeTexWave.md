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

### [Texture](Texture.md)

| Name | Definition |
|------|------------|
 | [wave](Texture.md#wave-staticmethod) | `def wave(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS'):` |
 | [wave_bands](Texture.md#wave_bands-staticmethod) | `def wave_bands(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X', wave_profile='SIN'):` |
 | [wave_rings](Texture.md#wave_rings-staticmethod) | `def wave_rings(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X', wave_profile='SIN'):` |
 | [wave_bands_sine](Texture.md#wave_bands_sine-staticmethod) | `def wave_bands_sine(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):` |
 | [wave_bands_saw](Texture.md#wave_bands_saw-staticmethod) | `def wave_bands_saw(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):` |
 | [wave_bands_triangle](Texture.md#wave_bands_triangle-staticmethod) | `def wave_bands_triangle(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):` |
 | [wave_rings_sine](Texture.md#wave_rings_sine-staticmethod) | `def wave_rings_sine(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):` |
 | [wave_rings_saw](Texture.md#wave_rings_saw-staticmethod) | `def wave_rings_saw(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):` |
 | [wave_rings_triangle](Texture.md#wave_rings_triangle-staticmethod) | `def wave_rings_triangle(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):` |

