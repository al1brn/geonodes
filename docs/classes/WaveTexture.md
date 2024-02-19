# class WaveTexture (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : WaveTexture
 - bl_idname : ShaderNodeTexWave

Node parameters
 - bands_direction : 'X'
 - color_mapping
 - rings_direction : 'X'
 - texture_mapping
 - wave_profile : 'SIN'
 - wave_type : 'BANDS'

Input sockets
 - vector : Vect
 - scale : Float
 - distortion : Float
 - detail : Float
 - detail_scale : Float
 - detail_roughness : Float
 - phase_offset : Float

Output sockets
 - color : Col
 - fac : Float

### Header

``` python
def WaveTexture(self, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', color_mapping=None, rings_direction='X', texture_mapping=None, wave_profile='SIN',
wave_type='BANDS', node_label=None, node_color=None):
```

## Implementations


