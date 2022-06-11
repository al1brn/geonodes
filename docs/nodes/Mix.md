
# Node Mix

> Geometry node name: [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/mix.html)<br>
  Blender type: [Mix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Mix(color1=None, color2=None, fac=None, blend_type='MIX', use_alpha=False, label=None)
```



## Arguments


### Input sockets

fac : Float
- color1 : Color
- color2 : Color

### Parameters

blend_type : str (default = 'MIX') in ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE')
- use_alpha : bool (default = False)

### Node label

- label : Geometry node display label (default=None)

## Output sockets

color : Color

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Color) [add](section:Data socket Color/add) : Method
- [class_name](section:Data socket Color) [burn](section:Data socket Color/burn) : Method
- [class_name](section:Data socket Color) [darken](section:Data socket Color/darken) : Method
- [class_name](section:Data socket Color) [difference](section:Data socket Color/difference) : Method
- [class_name](section:Data socket Color) [divide](section:Data socket Color/divide) : Method
- [class_name](section:Data socket Color) [dodge](section:Data socket Color/dodge) : Method
- [class_name](section:Data socket Color) [hue](section:Data socket Color/hue) : Method
- [class_name](section:Data socket Color) [lighten](section:Data socket Color/lighten) : Method
- [class_name](section:Data socket Color) [linear_light](section:Data socket Color/linear_light) : Method
- [class_name](section:Data socket Color) [mix](section:Data socket Color/mix) : Method
- [class_name](section:Data socket Color) [mix](section:Data socket Color/mix) : Method
- [class_name](section:Data socket Color) [mix_color](section:Data socket Color/mix_color) : Method
- [class_name](section:Data socket Color) [multiply](section:Data socket Color/multiply) : Method
- [class_name](section:Data socket Color) [overlay](section:Data socket Color/overlay) : Method
- [class_name](section:Data socket Color) [saturation](section:Data socket Color/saturation) : Method
- [class_name](section:Data socket Color) [screen](section:Data socket Color/screen) : Method
- [class_name](section:Data socket Color) [soft_light](section:Data socket Color/soft_light) : Method
- [class_name](section:Data socket Color) [subtract](section:Data socket Color/subtract) : Method
- [class_name](section:Data socket Color) [value](section:Data socket Color/value) : Method
- [class_name](section:Data socket functions) [color_add](section:Data socket functions/color_add) : Function
- [class_name](section:Data socket functions) [color_burn](section:Data socket functions/color_burn) : Function
- [class_name](section:Data socket functions) [color_darken](section:Data socket functions/color_darken) : Function
- [class_name](section:Data socket functions) [color_difference](section:Data socket functions/color_difference) : Function
- [class_name](section:Data socket functions) [color_divide](section:Data socket functions/color_divide) : Function
- [class_name](section:Data socket functions) [color_dodge](section:Data socket functions/color_dodge) : Function
- [class_name](section:Data socket functions) [color_hue](section:Data socket functions/color_hue) : Function
- [class_name](section:Data socket functions) [color_lighten](section:Data socket functions/color_lighten) : Function
- [class_name](section:Data socket functions) [color_linear_light](section:Data socket functions/color_linear_light) : Function
- [class_name](section:Data socket functions) [color_mix](section:Data socket functions/color_mix) : Function
- [class_name](section:Data socket functions) [color_mix_color](section:Data socket functions/color_mix_color) : Function
- [class_name](section:Data socket functions) [color_multiply](section:Data socket functions/color_multiply) : Function
- [class_name](section:Data socket functions) [color_overlay](section:Data socket functions/color_overlay) : Function
- [class_name](section:Data socket functions) [color_saturation](section:Data socket functions/color_saturation) : Function
- [class_name](section:Data socket functions) [color_screen](section:Data socket functions/color_screen) : Function
- [class_name](section:Data socket functions) [color_soft_light](section:Data socket functions/color_soft_light) : Function
- [class_name](section:Data socket functions) [color_subtract](section:Data socket functions/color_subtract) : Function
- [class_name](section:Data socket functions) [color_value](section:Data socket functions/color_value) : Function
  
