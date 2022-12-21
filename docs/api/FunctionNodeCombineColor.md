# Node Combine Color

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)
- geonodes name: `CombineColor`
- bl_idname: `FunctionNodeCombineColor`

```python
from geonodes import nodes

node = nodes.CombineColor(red=None, green=None, blue=None, alpha=None, mode='RGB')
```

### Args:

#### Input socket arguments:

- **red**: [Float](Float.md)
- **green**: [Float](Float.md)
- **blue**: [Float](Float.md)
- **alpha**: [Float](Float.md)

#### Node parameter arguments:

- **mode** (str): default = 'RGB' in ('RGB', 'HSV', 'HSL')

### Output sockets:

- **color** : [Color](Color.md)

## Implementation

#### Global functions

 - [combine_rgb](A.md#combine_rgb) ```python nodes.CombineColor(red=red, green=green, blue=blue, alpha=alpha, mode='RGB'````
 - [combine_hsv](A.md#combine_hsv) ```python nodes.CombineColor(red=hue, green=saturation, blue=value, alpha=alpha, mode='HSV'````
 - [combine_hsl](A.md#combine_hsl) ```python nodes.CombineColor(red=hue, green=saturation, blue=lightness, alpha=alpha, mode='HSL'````
#### [Color](Color.md)

 - [RGB](Color.md#RGB-classmethod) ```python nodes.CombineColor(red=red, green=green, blue=blue, alpha=alpha, mode='RGB'````
 - [HSV](Color.md#HSV-classmethod) ```python nodes.CombineColor(red=hue, green=saturation, blue=value, alpha=alpha, mode='HSV'````
 - [HSL](Color.md#HSL-classmethod) ```python nodes.CombineColor(red=hue, green=saturation, blue=lightness, alpha=alpha, mode='HSV'````
