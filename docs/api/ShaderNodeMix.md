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
  def float_mix(factor=None, a=None, b=None, clamp_factor=True)
  ```

 - [vector_mix](A.md#vector_mix)
  ```python
  def vector_mix(factor=None, a=None, b=None, clamp_factor=True, factor_mode='UNIFORM')
  ```

 - [color_mix](A.md#color_mix)
  ```python
  def color_mix(factor=None, a=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False)
  ```

 - [color_darken](A.md#color_darken)
  ```python
  def color_darken(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
  ```

 - [color_multiply](A.md#color_multiply)
  ```python
  def color_multiply(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
  ```

 - [color_burn](A.md#color_burn)
  ```python
  def color_burn(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
  ```

 - [color_lighten](A.md#color_lighten)
  ```python
  def color_lighten(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
  ```

 - [color_screen](A.md#color_screen)
  ```python
  def color_screen(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
  ```

 - [color_dodge](A.md#color_dodge)
  ```python
  def color_dodge(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
  ```

 - [color_add](A.md#color_add)
  ```python
  def color_add(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
  ```

 - [color_overlay](A.md#color_overlay)
  ```python
  def color_overlay(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
  ```

 - [color_soft_light](A.md#color_soft_light)
  ```python
  def color_soft_light(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
  ```

 - [color_linear_light](A.md#color_linear_light)
  ```python
  def color_linear_light(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
  ```

 - [color_difference](A.md#color_difference)
  ```python
  def color_difference(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
  ```

 - [color_subtract](A.md#color_subtract)
  ```python
  def color_subtract(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
  ```

 - [color_divide](A.md#color_divide)
  ```python
  def color_divide(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
  ```

 - [color_hue](A.md#color_hue)
  ```python
  def color_hue(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
  ```

 - [color_saturation](A.md#color_saturation)
  ```python
  def color_saturation(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
  ```

 - [color_color](A.md#color_color)
  ```python
  def color_color(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
  ```

 - [color_value](A.md#color_value)
  ```python
  def color_value(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
  ```

#### [Color](Color.md)

 - [mix](Color.md#mix)
  ```python
  def mix(self, factor=None, color=None, blend_type='MIX', clamp_factor=True, clamp_result=False)
  ```

 - [mix_darken](Color.md#mix_darken)
  ```python
  def mix_darken(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
  ```

 - [mix_multiply](Color.md#mix_multiply)
  ```python
  def mix_multiply(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
  ```

 - [mix_burn](Color.md#mix_burn)
  ```python
  def mix_burn(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
  ```

 - [mix_lighten](Color.md#mix_lighten)
  ```python
  def mix_lighten(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
  ```

 - [mix_screen](Color.md#mix_screen)
  ```python
  def mix_screen(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
  ```

 - [mix_dodge](Color.md#mix_dodge)
  ```python
  def mix_dodge(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
  ```

 - [mix_add](Color.md#mix_add)
  ```python
  def mix_add(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
  ```

 - [mix_overlay](Color.md#mix_overlay)
  ```python
  def mix_overlay(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
  ```

 - [mix_soft_light](Color.md#mix_soft_light)
  ```python
  def mix_soft_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
  ```

 - [mix_linear_light](Color.md#mix_linear_light)
  ```python
  def mix_linear_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
  ```

 - [mix_difference](Color.md#mix_difference)
  ```python
  def mix_difference(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
  ```

 - [mix_subtract](Color.md#mix_subtract)
  ```python
  def mix_subtract(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
  ```

 - [mix_divide](Color.md#mix_divide)
  ```python
  def mix_divide(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
  ```

 - [mix_hue](Color.md#mix_hue)
  ```python
  def mix_hue(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
  ```

 - [mix_saturation](Color.md#mix_saturation)
  ```python
  def mix_saturation(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
  ```

 - [mix_color](Color.md#mix_color)
  ```python
  def mix_color(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
  ```

 - [mix_value](Color.md#mix_value)
  ```python
  def mix_value(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
  ```

#### [Float](Float.md)

 - [mix](Float.md#mix)
  ```python
  def mix(self, factor=None, value=None, clamp_factor=True)
  ```

#### [Vector](Vector.md)

 - [mix](Vector.md#mix)
  ```python
  def mix(self, factor=None, vector=None, clamp_factor=True, factor_mode='UNIFORM')
  ```

 - [mix_uniform](Vector.md#mix_uniform)
  ```python
  def mix_uniform(self, vector=None, clamp_factor=True)
  ```

 - [mix_non_uniform](Vector.md#mix_non_uniform)
  ```python
  def mix_non_uniform(self, factor=None, vector=None, clamp_factor=True)
  ```

