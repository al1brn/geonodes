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

- [RGBA](/docs/Shader/socket_RGBA.md) : [mix](/docs/Shader/socket_RGBA.md#mix) [mix_add](/docs/Shader/socket_RGBA.md#mix_add) [mix_burn](/docs/Shader/socket_RGBA.md#mix_burn) [mix_color](/docs/Shader/socket_RGBA.md#mix_color) [mix_darken](/docs/Shader/socket_RGBA.md#mix_darken) [mix_difference](/docs/Shader/socket_RGBA.md#mix_difference) [mix_divide](/docs/Shader/socket_RGBA.md#mix_divide) [mix_dodge](/docs/Shader/socket_RGBA.md#mix_dodge) [mix_exclusion](/docs/Shader/socket_RGBA.md#mix_exclusion) [mix_hue](/docs/Shader/socket_RGBA.md#mix_hue) [mix_lighten](/docs/Shader/socket_RGBA.md#mix_lighten) [mix_linear_light](/docs/Shader/socket_RGBA.md#mix_linear_light) [mix_mix](/docs/Shader/socket_RGBA.md#mix_mix) [mix_multiply](/docs/Shader/socket_RGBA.md#mix_multiply) [mix_overlay](/docs/Shader/socket_RGBA.md#mix_overlay) [mix_saturation](/docs/Shader/socket_RGBA.md#mix_saturation) [mix_screen](/docs/Shader/socket_RGBA.md#mix_screen) [mix_soft_light](/docs/Shader/socket_RGBA.md#mix_soft_light) [mix_subtract](/docs/Shader/socket_RGBA.md#mix_subtract) [mix_value](/docs/Shader/socket_RGBA.md#mix_value)
- [VALUE](/docs/Shader/socket_VALUE.md) : [mix](/docs/Shader/socket_VALUE.md#mix)
- [VECTOR](/docs/Shader/socket_VECTOR.md) : [mix](/docs/Shader/socket_VECTOR.md#mix)

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
