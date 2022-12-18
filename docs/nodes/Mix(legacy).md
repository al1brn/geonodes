
# Node Mix(legacy)

> Geometry node name: [Mix (Legacy)](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/i.html)<br>
  Blender type: [Mix (Legacy)](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Mix(legacy)(color1=None, color2=None, fac=None, blend_type='MIX', use_alpha=False, label=None, node_color=None)
```



## Arguments


### Input sockets

- fac : Float
- color1 : Color
- color2 : Color

### Parameters

- blend_type : str (default = 'MIX') in ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE')
- use_alpha : bool (default = False)

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- color : Color

## Data sockets

> Data socket classes implementing this node.
  
  
- [Color](/docs/sockets/Color.md).[add](/docs/sockets/Color.md#add) : Method
- [Color](/docs/sockets/Color.md).[burn](/docs/sockets/Color.md#burn) : Method
- [Color](/docs/sockets/Color.md).[darken](/docs/sockets/Color.md#darken) : Method
- [Color](/docs/sockets/Color.md).[difference](/docs/sockets/Color.md#difference) : Method
- [Color](/docs/sockets/Color.md).[divide](/docs/sockets/Color.md#divide) : Method
- [Color](/docs/sockets/Color.md).[dodge](/docs/sockets/Color.md#dodge) : Method
- [Color](/docs/sockets/Color.md).[lighten](/docs/sockets/Color.md#lighten) : Method
- [Color](/docs/sockets/Color.md).[linear_light](/docs/sockets/Color.md#linear_light) : Method
- [Color](/docs/sockets/Color.md).[mix](/docs/sockets/Color.md#mix) : Method
- [Color](/docs/sockets/Color.md).[mix](/docs/sockets/Color.md#mix) : Method
- [Color](/docs/sockets/Color.md).[mix_color](/docs/sockets/Color.md#mix_color) : Method
- [Color](/docs/sockets/Color.md).[mix_hue](/docs/sockets/Color.md#mix_hue) : Method
- [Color](/docs/sockets/Color.md).[mix_saturation](/docs/sockets/Color.md#mix_saturation) : Method
- [Color](/docs/sockets/Color.md).[mix_value](/docs/sockets/Color.md#mix_value) : Method
- [Color](/docs/sockets/Color.md).[multiply](/docs/sockets/Color.md#multiply) : Method
- [Color](/docs/sockets/Color.md).[overlay](/docs/sockets/Color.md#overlay) : Method
- [Color](/docs/sockets/Color.md).[screen](/docs/sockets/Color.md#screen) : Method
- [Color](/docs/sockets/Color.md).[soft_light](/docs/sockets/Color.md#soft_light) : Method
- [Color](/docs/sockets/Color.md).[subtract](/docs/sockets/Color.md#subtract) : Method
- [functions](/docs/sockets/functions.md).[color_add](/docs/sockets/functions.md#color_add) : Function
- [functions](/docs/sockets/functions.md).[color_burn](/docs/sockets/functions.md#color_burn) : Function
- [functions](/docs/sockets/functions.md).[color_darken](/docs/sockets/functions.md#color_darken) : Function
- [functions](/docs/sockets/functions.md).[color_difference](/docs/sockets/functions.md#color_difference) : Function
- [functions](/docs/sockets/functions.md).[color_divide](/docs/sockets/functions.md#color_divide) : Function
- [functions](/docs/sockets/functions.md).[color_dodge](/docs/sockets/functions.md#color_dodge) : Function
- [functions](/docs/sockets/functions.md).[color_lighten](/docs/sockets/functions.md#color_lighten) : Function
- [functions](/docs/sockets/functions.md).[color_linear_light](/docs/sockets/functions.md#color_linear_light) : Function
- [functions](/docs/sockets/functions.md).[color_mix](/docs/sockets/functions.md#color_mix) : Function
- [functions](/docs/sockets/functions.md).[color_mix_color](/docs/sockets/functions.md#color_mix_color) : Function
- [functions](/docs/sockets/functions.md).[color_mix_hue](/docs/sockets/functions.md#color_mix_hue) : Function
- [functions](/docs/sockets/functions.md).[color_mix_saturation](/docs/sockets/functions.md#color_mix_saturation) : Function
- [functions](/docs/sockets/functions.md).[color_mix_value](/docs/sockets/functions.md#color_mix_value) : Function
- [functions](/docs/sockets/functions.md).[color_multiply](/docs/sockets/functions.md#color_multiply) : Function
- [functions](/docs/sockets/functions.md).[color_overlay](/docs/sockets/functions.md#color_overlay) : Function
- [functions](/docs/sockets/functions.md).[color_screen](/docs/sockets/functions.md#color_screen) : Function
- [functions](/docs/sockets/functions.md).[color_soft_light](/docs/sockets/functions.md#color_soft_light) : Function
- [functions](/docs/sockets/functions.md).[color_subtract](/docs/sockets/functions.md#color_subtract) : Function
  
