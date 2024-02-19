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

o functions : [mix](/docs/Shader_classes/mix.md)
o Float : [mix](/docs/Shader_classes/mix.md) [mix](/docs/Shader_classes/mix.md) 
o Col : [mix_mix](/docs/Shader_classes/mix_mix.md) [mix_darken](/docs/Shader_classes/mix_darken.md) [mix_multiply](/docs/Shader_classes/mix_multiply.md) [mix_burn](/docs/Shader_classes/mix_burn.md) [mix_lighten](/docs/Shader_classes/mix_lighten.md) [mix_screen](/docs/Shader_classes/mix_screen.md) [mix_dodge](/docs/Shader_classes/mix_dodge.md) [mix_add](/docs/Shader_classes/mix_add.md) [mix_overlay](/docs/Shader_classes/mix_overlay.md) [mix_soft_light](/docs/Shader_classes/mix_soft_light.md) [mix_linear_light](/docs/Shader_classes/mix_linear_light.md) [mix_difference](/docs/Shader_classes/mix_difference.md) [mix_exclusion](/docs/Shader_classes/mix_exclusion.md) [mix_subtract](/docs/Shader_classes/mix_subtract.md) [mix_divide](/docs/Shader_classes/mix_divide.md) [mix_hue](/docs/Shader_classes/mix_hue.md) [mix_saturation](/docs/Shader_classes/mix_saturation.md) [mix_color](/docs/Shader_classes/mix_color.md) [mix_value](/docs/Shader_classes/mix_value.md) [mix](/docs/Shader_classes/mix.md) 
o Vect : [mix](/docs/Shader_classes/mix.md) 

