
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


- [Color](aaa). [add](bbb) : Method
- [Color](aaa). [burn](bbb) : Method
- [Color](aaa). [darken](bbb) : Method
- [Color](aaa). [difference](bbb) : Method
- [Color](aaa). [divide](bbb) : Method
- [Color](aaa). [dodge](bbb) : Method
- [Color](aaa). [hue](bbb) : Method
- [Color](aaa). [lighten](bbb) : Method
- [Color](aaa). [linear_light](bbb) : Method
- [Color](aaa). [mix](bbb) : Method
- [Color](aaa). [mix](bbb) : Method
- [Color](aaa). [mix_color](bbb) : Method
- [Color](aaa). [multiply](bbb) : Method
- [Color](aaa). [overlay](bbb) : Method
- [Color](aaa). [saturation](bbb) : Method
- [Color](aaa). [screen](bbb) : Method
- [Color](aaa). [soft_light](bbb) : Method
- [Color](aaa). [subtract](bbb) : Method
- [Color](aaa). [value](bbb) : Method
- [functions](aaa). [color_add](bbb) : Function
- [functions](aaa). [color_burn](bbb) : Function
- [functions](aaa). [color_darken](bbb) : Function
- [functions](aaa). [color_difference](bbb) : Function
- [functions](aaa). [color_divide](bbb) : Function
- [functions](aaa). [color_dodge](bbb) : Function
- [functions](aaa). [color_hue](bbb) : Function
- [functions](aaa). [color_lighten](bbb) : Function
- [functions](aaa). [color_linear_light](bbb) : Function
- [functions](aaa). [color_mix](bbb) : Function
- [functions](aaa). [color_mix_color](bbb) : Function
- [functions](aaa). [color_multiply](bbb) : Function
- [functions](aaa). [color_overlay](bbb) : Function
- [functions](aaa). [color_saturation](bbb) : Function
- [functions](aaa). [color_screen](bbb) : Function
- [functions](aaa). [color_soft_light](bbb) : Function
- [functions](aaa). [color_subtract](bbb) : Function
- [functions](aaa). [color_value](bbb) : Function


