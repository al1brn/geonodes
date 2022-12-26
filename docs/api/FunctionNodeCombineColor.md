# Node *Combine Color*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)
- geonodes name: `CombineColor`
- bl_idname: `FunctionNodeCombineColor`

```python
from geonodes import nodes

node = nodes.CombineColor(red=None, green=None, blue=None, alpha=None, mode='RGB')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeCombineColor.webp)

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

| Class or method name | Definition |
|----------------------|------------|
| **[Color](Color.md)** |
| [RGB](Color.md#RGB) | `@classmethod`<br> `def RGB(cls, red=None, green=None, blue=None, alpha=None):` |
| [HSV](Color.md#HSV) | `@classmethod`<br> `def HSV(cls, hue=None, saturation=None, value=None, alpha=None):` |
| [HSL](Color.md#HSL) | `@classmethod`<br> `def HSL(cls, hue=None, saturation=None, lightness=None, alpha=None):` |
| Global functions |
| [combine_rgb](functions.md#combine_rgb) | `def combine_rgb(red=None, green=None, blue=None, alpha=None):` |
| [combine_hsv](functions.md#combine_hsv) | `def combine_hsv(hue=None, saturation=None, value=None, alpha=None):` |
| [combine_hsl](functions.md#combine_hsl) | `def combine_hsl(hue=None, saturation=None, lightness=None, alpha=None):` |

<sub>Go to [top](#node-Combine-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

