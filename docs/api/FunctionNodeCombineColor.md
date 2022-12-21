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

### Global functions

| Name | Definition |
|------|------------|
 | [combine_rgb](A.md#combine_rgb) | `def combine_rgb(red=None, green=None, blue=None, alpha=None): |
 | [combine_hsv](A.md#combine_hsv) | `def combine_hsv(hue=None, saturation=None, value=None, alpha=None): |
 | [combine_hsl](A.md#combine_hsl) | `def combine_hsl(hue=None, saturation=None, lightness=None, alpha=None): |

### [Color](Color.md)

| Name | Definition |
|------|------------|
 | [RGB](Color.md#RGB-classmethod) | `def RGB(cls, red=None, green=None, blue=None, alpha=None): |
 | [HSV](Color.md#HSV-classmethod) | `def HSV(cls, hue=None, saturation=None, value=None, alpha=None): |
 | [HSL](Color.md#HSL-classmethod) | `def HSL(cls, hue=None, saturation=None, lightness=None, alpha=None): |

