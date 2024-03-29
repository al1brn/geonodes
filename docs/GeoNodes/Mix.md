# Node Mix

- Node name : 'Mix'
- bl_idname : [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)


``` python
Mix(factor=None, a=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False, data_type='FLOAT', factor_mode='UNIFORM', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- factor : None
- a : None
- b : None
- blend_type : 'MIX'
- clamp_factor : True
- clamp_result : False
- data_type : 'FLOAT'
- factor_mode : 'UNIFORM'

## Implementation

- [INT](/docs/GeoNodes/socket_INT.md) : [mix](/docs/GeoNodes/socket_INT.md#mix)
- [RGBA](/docs/GeoNodes/socket_RGBA.md) : [mix](/docs/GeoNodes/socket_RGBA.md#mix) [mix_add](/docs/GeoNodes/socket_RGBA.md#mix_add) [mix_burn](/docs/GeoNodes/socket_RGBA.md#mix_burn) [mix_color](/docs/GeoNodes/socket_RGBA.md#mix_color) [mix_darken](/docs/GeoNodes/socket_RGBA.md#mix_darken) [mix_difference](/docs/GeoNodes/socket_RGBA.md#mix_difference) [mix_divide](/docs/GeoNodes/socket_RGBA.md#mix_divide) [mix_dodge](/docs/GeoNodes/socket_RGBA.md#mix_dodge) [mix_exclusion](/docs/GeoNodes/socket_RGBA.md#mix_exclusion) [mix_hue](/docs/GeoNodes/socket_RGBA.md#mix_hue) [mix_lighten](/docs/GeoNodes/socket_RGBA.md#mix_lighten) [mix_linear_light](/docs/GeoNodes/socket_RGBA.md#mix_linear_light) [mix_mix](/docs/GeoNodes/socket_RGBA.md#mix_mix) [mix_multiply](/docs/GeoNodes/socket_RGBA.md#mix_multiply) [mix_overlay](/docs/GeoNodes/socket_RGBA.md#mix_overlay) [mix_saturation](/docs/GeoNodes/socket_RGBA.md#mix_saturation) [mix_screen](/docs/GeoNodes/socket_RGBA.md#mix_screen) [mix_soft_light](/docs/GeoNodes/socket_RGBA.md#mix_soft_light) [mix_subtract](/docs/GeoNodes/socket_RGBA.md#mix_subtract) [mix_value](/docs/GeoNodes/socket_RGBA.md#mix_value)
- [ROTATION](/docs/GeoNodes/socket_ROTATION.md) : [mix](/docs/GeoNodes/socket_ROTATION.md#mix)
- [VALUE](/docs/GeoNodes/socket_VALUE.md) : [mix](/docs/GeoNodes/socket_VALUE.md#mix)
- [VECTOR](/docs/GeoNodes/socket_VECTOR.md) : [mix](/docs/GeoNodes/socket_VECTOR.md#mix)

## Init

``` python
def __init__(self, factor=None, a=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False, data_type='FLOAT', factor_mode='UNIFORM', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeMix', node_label=node_label, node_color=node_color, **kwargs)

    self.blend_type      = blend_type
    self.clamp_factor    = clamp_factor
    self.clamp_result    = clamp_result
    self.data_type       = data_type
    self.factor_mode     = factor_mode
    self.factor          = factor
    self.a               = a
    self.b               = b
```
