# Node *Mix*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)
- geonodes name: `Mix`
- bl_idname: `ShaderNodeMix`

```python
from geonodes import nodes

node = nodes.Mix(factor=None, a=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False, data_type='FLOAT', factor_mode='UNIFORM')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeMix.webp)

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

| Class or method name | Definition |
|----------------------|------------|
| **[Color](Color.md)** |
| [mix](Color.md#mix) | `def mix(self, factor=None, color=None, blend_type='MIX', clamp_factor=True, clamp_result=False):` |
| [mix_darken](Color.md#mix_darken) | `def mix_darken(self, factor=None, color=None, clamp_factor=True, clamp_result=False):` |
| [mix_multiply](Color.md#mix_multiply) | `def mix_multiply(self, factor=None, color=None, clamp_factor=True, clamp_result=False):` |
| [mix_burn](Color.md#mix_burn) | `def mix_burn(self, factor=None, color=None, clamp_factor=True, clamp_result=False):` |
| [mix_lighten](Color.md#mix_lighten) | `def mix_lighten(self, factor=None, color=None, clamp_factor=True, clamp_result=False):` |
| [mix_screen](Color.md#mix_screen) | `def mix_screen(self, factor=None, color=None, clamp_factor=True, clamp_result=False):` |
| [mix_dodge](Color.md#mix_dodge) | `def mix_dodge(self, factor=None, color=None, clamp_factor=True, clamp_result=False):` |
| [mix_add](Color.md#mix_add) | `def mix_add(self, factor=None, color=None, clamp_factor=True, clamp_result=False):` |
| [mix_overlay](Color.md#mix_overlay) | `def mix_overlay(self, factor=None, color=None, clamp_factor=True, clamp_result=False):` |
| [mix_soft_light](Color.md#mix_soft_light) | `def mix_soft_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False):` |
| [mix_linear_light](Color.md#mix_linear_light) | `def mix_linear_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False):` |
| [mix_difference](Color.md#mix_difference) | `def mix_difference(self, factor=None, color=None, clamp_factor=True, clamp_result=False):` |
| [mix_subtract](Color.md#mix_subtract) | `def mix_subtract(self, factor=None, color=None, clamp_factor=True, clamp_result=False):` |
| [mix_divide](Color.md#mix_divide) | `def mix_divide(self, factor=None, color=None, clamp_factor=True, clamp_result=False):` |
| [mix_hue](Color.md#mix_hue) | `def mix_hue(self, factor=None, color=None, clamp_factor=True, clamp_result=False):` |
| [mix_saturation](Color.md#mix_saturation) | `def mix_saturation(self, factor=None, color=None, clamp_factor=True, clamp_result=False):` |
| [mix_color](Color.md#mix_color) | `def mix_color(self, factor=None, color=None, clamp_factor=True, clamp_result=False):` |
| [mix_value](Color.md#mix_value) | `def mix_value(self, factor=None, color=None, clamp_factor=True, clamp_result=False):` |
| **[Float](Float.md)** |
| [mix](Float.md#mix) | `def mix(self, factor=None, value=None, clamp_factor=True):` |
| **[Vector](Vector.md)** |
| [mix](Vector.md#mix) | `def mix(self, factor=None, vector=None, clamp_factor=True, factor_mode='UNIFORM'):` |
| [mix_uniform](Vector.md#mix_uniform) | `def mix_uniform(self, vector=None, clamp_factor=True):` |
| [mix_non_uniform](Vector.md#mix_non_uniform) | `def mix_non_uniform(self, factor=None, vector=None, clamp_factor=True):` |
| Global functions |
| [float_mix](functions.md#float_mix) | `def float_mix(factor=None, a=None, b=None, clamp_factor=True):` |
| [vector_mix](functions.md#vector_mix) | `def vector_mix(factor=None, a=None, b=None, clamp_factor=True, factor_mode='UNIFORM'):` |
| [color_mix](functions.md#color_mix) | `def color_mix(factor=None, a=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False):` |
| [color_darken](functions.md#color_darken) | `def color_darken(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):` |
| [color_multiply](functions.md#color_multiply) | `def color_multiply(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):` |
| [color_burn](functions.md#color_burn) | `def color_burn(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):` |
| [color_lighten](functions.md#color_lighten) | `def color_lighten(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):` |
| [color_screen](functions.md#color_screen) | `def color_screen(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):` |
| [color_dodge](functions.md#color_dodge) | `def color_dodge(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):` |
| [color_add](functions.md#color_add) | `def color_add(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):` |
| [color_overlay](functions.md#color_overlay) | `def color_overlay(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):` |
| [color_soft_light](functions.md#color_soft_light) | `def color_soft_light(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):` |
| [color_linear_light](functions.md#color_linear_light) | `def color_linear_light(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):` |
| [color_difference](functions.md#color_difference) | `def color_difference(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):` |
| [color_subtract](functions.md#color_subtract) | `def color_subtract(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):` |
| [color_divide](functions.md#color_divide) | `def color_divide(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):` |
| [color_hue](functions.md#color_hue) | `def color_hue(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):` |
| [color_saturation](functions.md#color_saturation) | `def color_saturation(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):` |
| [color_color](functions.md#color_color) | `def color_color(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):` |
| [color_value](functions.md#color_value) | `def color_value(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):` |

<sub>Go to [top](#node-Mix) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

