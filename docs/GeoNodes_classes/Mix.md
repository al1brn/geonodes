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

o functions : [mix](/docs/GeoNodes_classes/mix.md)
o Float : [mix](#mix) [mix](#mix) 
o Int : [mix](#mix) 
o Col : [mix_mix](#mix_mix) [mix_darken](#mix_darken) [mix_multiply](#mix_multiply) [mix_burn](#mix_burn) [mix_lighten](#mix_lighten) [mix_screen](#mix_screen) [mix_dodge](#mix_dodge) [mix_add](#mix_add) [mix_overlay](#mix_overlay) [mix_soft_light](#mix_soft_light) [mix_linear_light](#mix_linear_light) [mix_difference](#mix_difference) [mix_exclusion](#mix_exclusion) [mix_subtract](#mix_subtract) [mix_divide](#mix_divide) [mix_hue](#mix_hue) [mix_saturation](#mix_saturation) [mix_color](#mix_color) [mix_value](#mix_value) [mix](#mix) 
o Vect : [mix](#mix) 
o Rot : [mix](#mix) 

