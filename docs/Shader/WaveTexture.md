# Node WaveTexture

- Node name : 'Wave Texture'
- bl_idname : [ShaderNodeTexWave](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)


``` python
WaveTexture(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', color_mapping=None, rings_direction='X', texture_mapping=None, wave_profile='SIN', wave_type='BANDS', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vector : None
- scale : None
- distortion : None
- detail : None
- detail_scale : None
- detail_roughness : None
- phase_offset : None
- bands_direction : 'X'
- color_mapping : None
- rings_direction : 'X'
- texture_mapping : None
- wave_profile : 'SIN'
- wave_type : 'BANDS'

## Implementation

- Functions : [wave_texture](/docs/Shader/ShaderTree.md#wave_texture)

## Init

``` python
def __init__(self, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', color_mapping=None, rings_direction='X', texture_mapping=None, wave_profile='SIN', wave_type='BANDS', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeTexWave', node_label=node_label, node_color=node_color, **kwargs)

    self.bands_direction = bands_direction
    self.color_mapping   = color_mapping
    self.rings_direction = rings_direction
    self.texture_mapping = texture_mapping
    self.wave_profile    = wave_profile
    self.wave_type       = wave_type
    self.vector          = vector
    self.scale           = scale
    self.distortion      = distortion
    self.detail          = detail
    self.detail_scale    = detail_scale
    self.detail_roughness = detail_roughness
    self.phase_offset    = phase_offset
```
