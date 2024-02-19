# class Mix (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : Mix
 - bl_idname : ShaderNodeMix

Node parameters
 - blend_type : 'MIX'
 - clamp_factor : True
 - clamp_result : False
 - data_type : 'FLOAT'
 - factor_mode : 'UNIFORM'

Input sockets
 - factor : Float
 - factor_1 : Vect
 - a : Float
 - b : Float
 - a_1 : Vect
 - b_1 : Vect
 - a_2 : Col
 - b_2 : Col
 - a_3 : Rot
 - b_3 : Rot

Output sockets
 - result : Float
 - result_1 : Vect
 - result_2 : Col
 - result_3 : Rot

### Header

``` python
def Mix(self, factor=None, a=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False, data_type='FLOAT', factor_mode='UNIFORM', node_label=None, node_color=None):
```

## Implementations

o functions : [mix](/docs/Shader_classes/GLOBAL.md#mix)
o Float : [mix](/docs/Shader_classes/Float.md#mix) [mix](/docs/Shader_classes/Float.md#mix)

o Col : [mix_mix](/docs/Shader_classes/Col.md#mix_mix) [mix_darken](/docs/Shader_classes/Col.md#mix_darken) [mix_multiply](/docs/Shader_classes/Col.md#mix_multiply) [mix_burn](/docs/Shader_classes/Col.md#mix_burn) [mix_lighten](/docs/Shader_classes/Col.md#mix_lighten) [mix_screen](/docs/Shader_classes/Col.md#mix_screen) [mix_dodge](/docs/Shader_classes/Col.md#mix_dodge) [mix_add](/docs/Shader_classes/Col.md#mix_add) [mix_overlay](/docs/Shader_classes/Col.md#mix_overlay) [mix_soft_light](/docs/Shader_classes/Col.md#mix_soft_light) [mix_linear_light](/docs/Shader_classes/Col.md#mix_linear_light) [mix_difference](/docs/Shader_classes/Col.md#mix_difference) [mix_exclusion](/docs/Shader_classes/Col.md#mix_exclusion) [mix_subtract](/docs/Shader_classes/Col.md#mix_subtract) [mix_divide](/docs/Shader_classes/Col.md#mix_divide) [mix_hue](/docs/Shader_classes/Col.md#mix_hue) [mix_saturation](/docs/Shader_classes/Col.md#mix_saturation) [mix_color](/docs/Shader_classes/Col.md#mix_color) [mix_value](/docs/Shader_classes/Col.md#mix_value) [mix](/docs/Shader_classes/Col.md#mix)

o Vect : [mix](/docs/Shader_classes/Vect.md#mix)


