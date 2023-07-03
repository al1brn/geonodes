# Node *Wave Texture*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)
- geonodes name: `WaveTexture`
- bl_idname: `ShaderNodeTexWave`

```python
from geonodes import nodes

node = nodes.WaveTexture(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

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

| Class or method name | Definition |
|----------------------|------------|
| **[Texture](Texture.md)** |
| [Wave](Texture.md#Wave) | `@classmethod`<br> `def Wave(cls, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS'):` |
| [WaveBands](Texture.md#WaveBands) | `@classmethod`<br> `def WaveBands(cls, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X', wave_profile='SIN'):` |
| [WaveRings](Texture.md#WaveRings) | `@classmethod`<br> `def WaveRings(cls, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X', wave_profile='SIN'):` |
| [WaveBands_sine](Texture.md#WaveBands_sine) | `@classmethod`<br> `def WaveBands_sine(cls, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):` |
| [WaveBands_saw](Texture.md#WaveBands_saw) | `@classmethod`<br> `def WaveBands_saw(cls, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):` |
| [WaveBands_triangle](Texture.md#WaveBands_triangle) | `@classmethod`<br> `def WaveBands_triangle(cls, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):` |
| [WaveRings_sine](Texture.md#WaveRings_sine) | `@classmethod`<br> `def WaveRings_sine(cls, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):` |
| [WaveRings_saw](Texture.md#WaveRings_saw) | `@classmethod`<br> `def WaveRings_saw(cls, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):` |
| [WaveRings_triangle](Texture.md#WaveRings_triangle) | `@classmethod`<br> `def WaveRings_triangle(cls, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):` |

<sub>Go to [top](#node-Wave-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

