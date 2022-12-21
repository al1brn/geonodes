# Node Mix

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)
- geonodes name: `Mix`
- bl_idname: `ShaderNodeMix`

```python
from geonodes import nodes

node = nodes.Mix(factor=None, a=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False, data_type='FLOAT', factor_mode='UNIFORM')
```

### Args:

#### Input socket arguments:

- **factor**: **data_type** dependant
- **a**: **data_type** dependant
- **b**: **data_type** dependant

#### Node parameter arguments:

- **blend_type** (str): default = 'MIX' in ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE')
- **clamp_factor** (bool): default = True
- **clamp_result** (bool): default = False
- **data_type** (str): default = 'FLOAT' in ('FLOAT', 'VECTOR', 'RGBA')
- **factor_mode** (str): default = 'UNIFORM' in ('UNIFORM', 'NON_UNIFORM')

### Output sockets:

- **result** : ``data_type`` dependant

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'VECTOR', 'RGBA')
- Input sockets  : ['factor', 'a', 'b']
- Output sockets : ['result']
## Implementation

#### Global functions

 - [float_mix](A.md#float_mix)
 - [vector_mix](A.md#vector_mix)
 - [color_mix](A.md#color_mix)
 - [color_darken](A.md#color_darken)
 - [color_multiply](A.md#color_multiply)
 - [color_burn](A.md#color_burn)
 - [color_lighten](A.md#color_lighten)
 - [color_screen](A.md#color_screen)
 - [color_dodge](A.md#color_dodge)
 - [color_add](A.md#color_add)
 - [color_overlay](A.md#color_overlay)
 - [color_soft_light](A.md#color_soft_light)
 - [color_linear_light](A.md#color_linear_light)
 - [color_difference](A.md#color_difference)
 - [color_subtract](A.md#color_subtract)
 - [color_divide](A.md#color_divide)
 - [color_hue](A.md#color_hue)
 - [color_saturation](A.md#color_saturation)
 - [color_color](A.md#color_color)
 - [color_value](A.md#color_value)
#### class [Color](Color.md)

 - [mix](Color.md#mix)
 - [mix_darken](Color.md#mix_darken)
 - [mix_multiply](Color.md#mix_multiply)
 - [mix_burn](Color.md#mix_burn)
 - [mix_lighten](Color.md#mix_lighten)
 - [mix_screen](Color.md#mix_screen)
 - [mix_dodge](Color.md#mix_dodge)
 - [mix_add](Color.md#mix_add)
 - [mix_overlay](Color.md#mix_overlay)
 - [mix_soft_light](Color.md#mix_soft_light)
 - [mix_linear_light](Color.md#mix_linear_light)
 - [mix_difference](Color.md#mix_difference)
 - [mix_subtract](Color.md#mix_subtract)
 - [mix_divide](Color.md#mix_divide)
 - [mix_hue](Color.md#mix_hue)
 - [mix_saturation](Color.md#mix_saturation)
 - [mix_color](Color.md#mix_color)
 - [mix_value](Color.md#mix_value)
#### class [Float](Float.md)

 - [mix](Float.md#mix)
#### class [Vector](Vector.md)

 - [mix](Vector.md#mix)
 - [mix_uniform](Vector.md#mix_uniform)
 - [mix_non_uniform](Vector.md#mix_non_uniform)
