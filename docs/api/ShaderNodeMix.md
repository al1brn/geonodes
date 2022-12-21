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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x164097070>>](Float.md#mix)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x1640977f0>>](Vector.md#mix)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x164096200>>](Vector.md#mix_uniform)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x1640960e0>>](Vector.md#mix_non_uniform)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x164097e50>>](Color.md#mix)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x164097eb0>>](Color.md#mix_darken)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x1640969b0>>](Color.md#mix_multiply)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x1640961a0>>](Color.md#mix_burn)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x164096230>>](Color.md#mix_lighten)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x164097250>>](Color.md#mix_screen)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x164096260>>](Color.md#mix_dodge)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x164097ac0>>](Color.md#mix_add)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x164097a30>>](Color.md#mix_overlay)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x164097610>>](Color.md#mix_soft_light)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x164097bb0>>](Color.md#mix_linear_light)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x164096da0>>](Color.md#mix_difference)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x164096e00>>](Color.md#mix_subtract)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x164096e90>>](Color.md#mix_divide)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x164096fe0>>](Color.md#mix_hue)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x164097040>>](Color.md#mix_saturation)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x164096f50>>](Color.md#mix_color)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x164097f10>>](Color.md#mix_value)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x1639dc070>>](function.md#float_mix)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x1639dc790>>](function.md#vector_mix)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x1639dc670>>](function.md#color_mix)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x1639dddb0>>](function.md#color_darken)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x164096440>>](function.md#color_multiply)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x164096d70>>](function.md#color_burn)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x164094e50>>](function.md#color_lighten)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x164094130>>](function.md#color_screen)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x164096c80>>](function.md#color_dodge)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x164097fd0>>](function.md#color_add)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x164097580>>](function.md#color_overlay)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x164096290>>](function.md#color_soft_light)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x164096fb0>>](function.md#color_linear_light)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x164097910>>](function.md#color_difference)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x164097c10>>](function.md#color_subtract)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x164097c40>>](function.md#color_divide)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x164097ca0>>](function.md#color_hue)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x164097cd0>>](function.md#color_saturation)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x164097d30>>](function.md#color_color)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x164097dc0>>](function.md#color_value)
