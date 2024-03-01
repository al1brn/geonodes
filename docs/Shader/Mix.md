# Node Mix

- Node name : 'Mix'
- bl_idname : ShaderNodeMix


``` python
Mix(factor=None, a=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False, data_type='FLOAT', factor_mode='UNIFORM', node_label=None, node_color=None)
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

- [Col](/docs/Shader/Col.md) : [mix](/docs/Shader/Col.md#mix) [mix_add](/docs/Shader/Col.md#mix_add) [mix_burn](/docs/Shader/Col.md#mix_burn) [mix_color](/docs/Shader/Col.md#mix_color) [mix_darken](/docs/Shader/Col.md#mix_darken) [mix_difference](/docs/Shader/Col.md#mix_difference) [mix_divide](/docs/Shader/Col.md#mix_divide) [mix_dodge](/docs/Shader/Col.md#mix_dodge) [mix_exclusion](/docs/Shader/Col.md#mix_exclusion) [mix_hue](/docs/Shader/Col.md#mix_hue) [mix_lighten](/docs/Shader/Col.md#mix_lighten) [mix_linear_light](/docs/Shader/Col.md#mix_linear_light) [mix_mix](/docs/Shader/Col.md#mix_mix) [mix_multiply](/docs/Shader/Col.md#mix_multiply) [mix_overlay](/docs/Shader/Col.md#mix_overlay) [mix_saturation](/docs/Shader/Col.md#mix_saturation) [mix_screen](/docs/Shader/Col.md#mix_screen) [mix_soft_light](/docs/Shader/Col.md#mix_soft_light) [mix_subtract](/docs/Shader/Col.md#mix_subtract) [mix_value](/docs/Shader/Col.md#mix_value)
- [Float](/docs/Shader/Float.md) : [mix](/docs/Shader/Float.md#mix)
- [Vect](/docs/Shader/Vect.md) : [mix](/docs/Shader/Vect.md#mix)

## Init

``` python
def __init__(self, factor=None, a=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False, data_type='FLOAT', factor_mode='UNIFORM', node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeMix', node_label=node_label, node_color=node_color)

    self.blend_type      = blend_type
    self.clamp_factor    = clamp_factor
    self.clamp_result    = clamp_result
    self.data_type       = data_type
    self.factor_mode     = factor_mode
    self.factor          = factor
    self.a               = a
    self.b               = b
```
