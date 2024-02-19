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

o functions : [mix](/docs/GeoNodes_classes/GLOBAL.md#mix)

o Float : [mix](/docs/GeoNodes_classes/Float.md#mix) [mix](/docs/GeoNodes_classes/Float.md#mix)

o Int : [mix](/docs/GeoNodes_classes/Int.md#mix)

o Col : [mix_mix](/docs/GeoNodes_classes/Col.md#mix_mix) [mix_darken](/docs/GeoNodes_classes/Col.md#mix_darken) [mix_multiply](/docs/GeoNodes_classes/Col.md#mix_multiply) [mix_burn](/docs/GeoNodes_classes/Col.md#mix_burn) [mix_lighten](/docs/GeoNodes_classes/Col.md#mix_lighten) [mix_screen](/docs/GeoNodes_classes/Col.md#mix_screen) [mix_dodge](/docs/GeoNodes_classes/Col.md#mix_dodge) [mix_add](/docs/GeoNodes_classes/Col.md#mix_add) [mix_overlay](/docs/GeoNodes_classes/Col.md#mix_overlay) [mix_soft_light](/docs/GeoNodes_classes/Col.md#mix_soft_light) [mix_linear_light](/docs/GeoNodes_classes/Col.md#mix_linear_light) [mix_difference](/docs/GeoNodes_classes/Col.md#mix_difference) [mix_exclusion](/docs/GeoNodes_classes/Col.md#mix_exclusion) [mix_subtract](/docs/GeoNodes_classes/Col.md#mix_subtract) [mix_divide](/docs/GeoNodes_classes/Col.md#mix_divide) [mix_hue](/docs/GeoNodes_classes/Col.md#mix_hue) [mix_saturation](/docs/GeoNodes_classes/Col.md#mix_saturation) [mix_color](/docs/GeoNodes_classes/Col.md#mix_color) [mix_value](/docs/GeoNodes_classes/Col.md#mix_value) [mix](/docs/GeoNodes_classes/Col.md#mix)

o Vect : [mix](/docs/GeoNodes_classes/Vect.md#mix)

o Rot : [mix](/docs/GeoNodes_classes/Rot.md#mix)


