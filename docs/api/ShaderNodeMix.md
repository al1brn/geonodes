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
  ```python
  nodes.Mix(factor=factor, a=a, b=b, blend_type=MIX, clamp_factor=clamp_factor, clamp_result=False, data_type='FLOAT', factor_mode='UNIFORM'  ```

 - [vector_mix](A.md#vector_mix)
  ```python
  nodes.Mix(factor=factor, a=a, b=b, blend_type=MIX, clamp_factor=clamp_factor, clamp_result=False, data_type='VECTOR', factor_mode=factor_mode  ```

 - [color_mix](A.md#color_mix)
  ```python
  nodes.Mix(factor=factor, a=a, b=b, blend_type=blend_type, clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [color_darken](A.md#color_darken)
  ```python
  nodes.Mix(factor=factor, a=a, b=b, blend_type='DARKEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [color_multiply](A.md#color_multiply)
  ```python
  nodes.Mix(factor=factor, a=a, b=b, blend_type='MULTIPLY', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [color_burn](A.md#color_burn)
  ```python
  nodes.Mix(factor=factor, a=a, b=b, blend_type='BURN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [color_lighten](A.md#color_lighten)
  ```python
  nodes.Mix(factor=factor, a=a, b=b, blend_type='LIGHTEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [color_screen](A.md#color_screen)
  ```python
  nodes.Mix(factor=factor, a=a, b=b, blend_type='SCREEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [color_dodge](A.md#color_dodge)
  ```python
  nodes.Mix(factor=factor, a=a, b=b, blend_type='DODGE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [color_add](A.md#color_add)
  ```python
  nodes.Mix(factor=factor, a=a, b=b, blend_type='ADD', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [color_overlay](A.md#color_overlay)
  ```python
  nodes.Mix(factor=factor, a=a, b=b, blend_type='OVERLAY', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [color_soft_light](A.md#color_soft_light)
  ```python
  nodes.Mix(factor=factor, a=a, b=b, blend_type='SOFT_LIGHT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [color_linear_light](A.md#color_linear_light)
  ```python
  nodes.Mix(factor=factor, a=a, b=b, blend_type='LINEAR_LIGHT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [color_difference](A.md#color_difference)
  ```python
  nodes.Mix(factor=factor, a=a, b=b, blend_type='DIFFERENCE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [color_subtract](A.md#color_subtract)
  ```python
  nodes.Mix(factor=factor, a=a, b=b, blend_type='SUBTRACT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [color_divide](A.md#color_divide)
  ```python
  nodes.Mix(factor=factor, a=a, b=b, blend_type='DIVIDE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [color_hue](A.md#color_hue)
  ```python
  nodes.Mix(factor=factor, a=a, b=b, blend_type='HUE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [color_saturation](A.md#color_saturation)
  ```python
  nodes.Mix(factor=factor, a=a, b=b, blend_type='SATURATION', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [color_color](A.md#color_color)
  ```python
  nodes.Mix(factor=factor, a=a, b=b, blend_type='COLOR', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [color_value](A.md#color_value)
  ```python
  nodes.Mix(factor=factor, a=a, b=b, blend_type='VALUE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

#### [Color](Color.md)

 - [mix](Color.md#mix)
  ```python
  nodes.Mix(factor=factor, a=self, b=color, blend_type=blend_type, clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [mix_darken](Color.md#mix_darken)
  ```python
  nodes.Mix(factor=factor, a=self, b=color, blend_type='DARKEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [mix_multiply](Color.md#mix_multiply)
  ```python
  nodes.Mix(factor=factor, a=self, b=color, blend_type='MULTIPLY', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [mix_burn](Color.md#mix_burn)
  ```python
  nodes.Mix(factor=factor, a=self, b=color, blend_type='BURN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [mix_lighten](Color.md#mix_lighten)
  ```python
  nodes.Mix(factor=factor, a=self, b=color, blend_type='LIGHTEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [mix_screen](Color.md#mix_screen)
  ```python
  nodes.Mix(factor=factor, a=self, b=color, blend_type='SCREEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [mix_dodge](Color.md#mix_dodge)
  ```python
  nodes.Mix(factor=factor, a=self, b=color, blend_type='DODGE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [mix_add](Color.md#mix_add)
  ```python
  nodes.Mix(factor=factor, a=self, b=color, blend_type='ADD', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [mix_overlay](Color.md#mix_overlay)
  ```python
  nodes.Mix(factor=factor, a=self, b=color, blend_type='OVERLAY', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [mix_soft_light](Color.md#mix_soft_light)
  ```python
  nodes.Mix(factor=factor, a=self, b=color, blend_type='SOFT_LIGHT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [mix_linear_light](Color.md#mix_linear_light)
  ```python
  nodes.Mix(factor=factor, a=self, b=color, blend_type='LINEAR_LIGHT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [mix_difference](Color.md#mix_difference)
  ```python
  nodes.Mix(factor=factor, a=self, b=color, blend_type='DIFFERENCE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [mix_subtract](Color.md#mix_subtract)
  ```python
  nodes.Mix(factor=factor, a=self, b=color, blend_type='SUBTRACT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [mix_divide](Color.md#mix_divide)
  ```python
  nodes.Mix(factor=factor, a=self, b=color, blend_type='DIVIDE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [mix_hue](Color.md#mix_hue)
  ```python
  nodes.Mix(factor=factor, a=self, b=color, blend_type='HUE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [mix_saturation](Color.md#mix_saturation)
  ```python
  nodes.Mix(factor=factor, a=self, b=color, blend_type='SATURATION', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [mix_color](Color.md#mix_color)
  ```python
  nodes.Mix(factor=factor, a=self, b=color, blend_type='COLOR', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

 - [mix_value](Color.md#mix_value)
  ```python
  nodes.Mix(factor=factor, a=self, b=color, blend_type='VALUE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='COLOR', factor_mode='UNIFORM'  ```

#### [Float](Float.md)

 - [mix](Float.md#mix)
  ```python
  nodes.Mix(factor=factor, a=self, b=value, blend_type=MIX, clamp_factor=clamp_factor, clamp_result=False, data_type='FLOAT', factor_mode='UNIFORM'  ```

#### [Vector](Vector.md)

 - [mix](Vector.md#mix)
  ```python
  nodes.Mix(factor=factor, a=self, b=vector, blend_type=MIX, clamp_factor=clamp_factor, clamp_result=False, data_type='VECTOR', factor_mode=factor_mode  ```

 - [mix_uniform](Vector.md#mix_uniform)
  ```python
  nodes.Mix(factor=None, a=self, b=vector, blend_type=MIX, clamp_factor=clamp_factor, clamp_result=False, data_type='VECTOR', factor_mode='UNIFORM'  ```

 - [mix_non_uniform](Vector.md#mix_non_uniform)
  ```python
  nodes.Mix(factor=factor, a=self, b=vector, blend_type=MIX, clamp_factor=clamp_factor, clamp_result=False, data_type='VECTOR', factor_mode='NON_UNIFORM'  ```

