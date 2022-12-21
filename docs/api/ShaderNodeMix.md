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

#### class [Float](Float.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb190>>](Float.md#mix)
#### class [Vector](Vector.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb160>>](Vector.md#mix)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb130>>](Vector.md#mix_uniform)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb100>>](Vector.md#mix_non_uniform)
#### class [Color](Color.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb4f0>>](Color.md#mix)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb4c0>>](Color.md#mix_darken)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb490>>](Color.md#mix_multiply)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb460>>](Color.md#mix_burn)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb430>>](Color.md#mix_lighten)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb400>>](Color.md#mix_screen)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb3d0>>](Color.md#mix_dodge)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb3a0>>](Color.md#mix_add)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb370>>](Color.md#mix_overlay)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb340>>](Color.md#mix_soft_light)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb310>>](Color.md#mix_linear_light)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb2e0>>](Color.md#mix_difference)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb2b0>>](Color.md#mix_subtract)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb280>>](Color.md#mix_divide)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb250>>](Color.md#mix_hue)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb220>>](Color.md#mix_saturation)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb1f0>>](Color.md#mix_color)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fb1c0>>](Color.md#mix_value)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb8b0>>](function.md#float_mix)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb880>>](function.md#vector_mix)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb850>>](function.md#color_mix)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb820>>](function.md#color_darken)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb7f0>>](function.md#color_multiply)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb7c0>>](function.md#color_burn)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb790>>](function.md#color_lighten)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb760>>](function.md#color_screen)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb730>>](function.md#color_dodge)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb700>>](function.md#color_add)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb6d0>>](function.md#color_overlay)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb6a0>>](function.md#color_soft_light)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb670>>](function.md#color_linear_light)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb640>>](function.md#color_difference)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb610>>](function.md#color_subtract)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb5e0>>](function.md#color_divide)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb5b0>>](function.md#color_hue)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb580>>](function.md#color_saturation)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb550>>](function.md#color_color)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb520>>](function.md#color_value)
