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

- [Col](/docs/GeoNodes/Col.md) : [mix](/docs/GeoNodes/Col.md#mix) [mix_add](/docs/GeoNodes/Col.md#mix_add) [mix_burn](/docs/GeoNodes/Col.md#mix_burn) [mix_color](/docs/GeoNodes/Col.md#mix_color) [mix_darken](/docs/GeoNodes/Col.md#mix_darken) [mix_difference](/docs/GeoNodes/Col.md#mix_difference) [mix_divide](/docs/GeoNodes/Col.md#mix_divide) [mix_dodge](/docs/GeoNodes/Col.md#mix_dodge) [mix_exclusion](/docs/GeoNodes/Col.md#mix_exclusion) [mix_hue](/docs/GeoNodes/Col.md#mix_hue) [mix_lighten](/docs/GeoNodes/Col.md#mix_lighten) [mix_linear_light](/docs/GeoNodes/Col.md#mix_linear_light) [mix_mix](/docs/GeoNodes/Col.md#mix_mix) [mix_multiply](/docs/GeoNodes/Col.md#mix_multiply) [mix_overlay](/docs/GeoNodes/Col.md#mix_overlay) [mix_saturation](/docs/GeoNodes/Col.md#mix_saturation) [mix_screen](/docs/GeoNodes/Col.md#mix_screen) [mix_soft_light](/docs/GeoNodes/Col.md#mix_soft_light) [mix_subtract](/docs/GeoNodes/Col.md#mix_subtract) [mix_value](/docs/GeoNodes/Col.md#mix_value)
- [Float](/docs/GeoNodes/Float.md) : [mix](/docs/GeoNodes/Float.md#mix)
- [Int](/docs/GeoNodes/Int.md) : [mix](/docs/GeoNodes/Int.md#mix)
- [Rot](/docs/GeoNodes/Rot.md) : [mix](/docs/GeoNodes/Rot.md#mix)
- [Vect](/docs/GeoNodes/Vect.md) : [mix](/docs/GeoNodes/Vect.md#mix)

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
