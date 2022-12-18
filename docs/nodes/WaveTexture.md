
# Node WaveTexture

> Geometry node name: [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html)<br>
  Blender type: [Wave Texture](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.WaveTexture(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS', label=None, node_color=None)
```



## Arguments


### Input sockets

- vector : Vector
- scale : Float
- distortion : Float
- detail : Float
- detail_scale : Float
- detail_roughness : Float
- phase_offset : Float

### Parameters

- bands_direction : str (default = 'X') in ('X', 'Y', 'Z', 'DIAGONAL')
- rings_direction : str (default = 'X') in ('X', 'Y', 'Z', 'SPHERICAL')
- wave_profile : str (default = 'SIN') in ('SIN', 'SAW', 'TRI')
- wave_type : str (default = 'BANDS') in ('BANDS', 'RINGS')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- color : Color
- fac : Float
