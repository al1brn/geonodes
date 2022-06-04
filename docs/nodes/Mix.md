
# Class Mix

> Geometry node name: _'Mix'_<br>Blender type:  **ShaderNodeMixRGB**

## Initialization


```python
from geonodes import nodes
node = nodes.Mix(color1=None, color2=None, fac=None, blend_type='MIX', use_alpha=False, label=None)
```


### Arguments


#### Input sockets



- **fac** : _Float_
- **color1** : _Color_
- **color2** : _Color_



#### Parameters



- **blend_type** : _'MIX'_ in ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE')
- **use_alpha** : _False_ bool



#### Node label



- **label** : Geometry node label



## Output sockets



- **color** : _Color_



## Data sockets

> Data socket classes implementing this node


- [Color](../sockets/Color.md) [add](../sockets/Color.md#add) : Method
- [Color](../sockets/Color.md) [burn](../sockets/Color.md#burn) : Method
- [Color](../sockets/Color.md) [darken](../sockets/Color.md#darken) : Method
- [Color](../sockets/Color.md) [difference](../sockets/Color.md#difference) : Method
- [Color](../sockets/Color.md) [divide](../sockets/Color.md#divide) : Method
- [Color](../sockets/Color.md) [dodge](../sockets/Color.md#dodge) : Method
- [Color](../sockets/Color.md) [hue](../sockets/Color.md#hue) : Method
- [Color](../sockets/Color.md) [lighten](../sockets/Color.md#lighten) : Method
- [Color](../sockets/Color.md) [linear_light](../sockets/Color.md#linear_light) : Method
- [Color](../sockets/Color.md) [mix](../sockets/Color.md#mix) : Method
- [Color](../sockets/Color.md) [mix](../sockets/Color.md#mix) : Method
- [Color](../sockets/Color.md) [mix_color](../sockets/Color.md#mix_color) : Method
- [Color](../sockets/Color.md) [multiply](../sockets/Color.md#multiply) : Method
- [Color](../sockets/Color.md) [overlay](../sockets/Color.md#overlay) : Method
- [Color](../sockets/Color.md) [saturation](../sockets/Color.md#saturation) : Method
- [Color](../sockets/Color.md) [screen](../sockets/Color.md#screen) : Method
- [Color](../sockets/Color.md) [soft_light](../sockets/Color.md#soft_light) : Method
- [Color](../sockets/Color.md) [subtract](../sockets/Color.md#subtract) : Method
- [Color](../sockets/Color.md) [value](../sockets/Color.md#value) : Method
- [functions](../sockets/functions.md) [color_add](../sockets/functions.md#color_add) : Function
- [functions](../sockets/functions.md) [color_burn](../sockets/functions.md#color_burn) : Function
- [functions](../sockets/functions.md) [color_darken](../sockets/functions.md#color_darken) : Function
- [functions](../sockets/functions.md) [color_difference](../sockets/functions.md#color_difference) : Function
- [functions](../sockets/functions.md) [color_divide](../sockets/functions.md#color_divide) : Function
- [functions](../sockets/functions.md) [color_dodge](../sockets/functions.md#color_dodge) : Function
- [functions](../sockets/functions.md) [color_hue](../sockets/functions.md#color_hue) : Function
- [functions](../sockets/functions.md) [color_lighten](../sockets/functions.md#color_lighten) : Function
- [functions](../sockets/functions.md) [color_linear_light](../sockets/functions.md#color_linear_light) : Function
- [functions](../sockets/functions.md) [color_mix](../sockets/functions.md#color_mix) : Function
- [functions](../sockets/functions.md) [color_mix_color](../sockets/functions.md#color_mix_color) : Function
- [functions](../sockets/functions.md) [color_multiply](../sockets/functions.md#color_multiply) : Function
- [functions](../sockets/functions.md) [color_overlay](../sockets/functions.md#color_overlay) : Function
- [functions](../sockets/functions.md) [color_saturation](../sockets/functions.md#color_saturation) : Function
- [functions](../sockets/functions.md) [color_screen](../sockets/functions.md#color_screen) : Function
- [functions](../sockets/functions.md) [color_soft_light](../sockets/functions.md#color_soft_light) : Function
- [functions](../sockets/functions.md) [color_subtract](../sockets/functions.md#color_subtract) : Function
- [functions](../sockets/functions.md) [color_value](../sockets/functions.md#color_value) : Function


