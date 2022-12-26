# Node *Separate Color*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)
- geonodes name: `SeparateColor`
- bl_idname: `FunctionNodeSeparateColor`

```python
from geonodes import nodes

node = nodes.SeparateColor(color=None, mode='RGB')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeSeparateColor.webp)

### Args:

#### Input socket arguments:

- **color**: [Color](Color.md)

#### Node parameter arguments:

- **mode** (str): default = 'RGB' in ('RGB', 'HSV', 'HSL')

### Output sockets:

- **red** : [Float](Float.md)
- **green** : [Float](Float.md)
- **blue** : [Float](Float.md)
- **alpha** : [Float](Float.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Color](Color.md)** |
| [separate_color](Color.md#separate_color) | `def separate_color(self, mode='RGB'):` |
| Global functions |
| [separate_rgb](functions.md#separate_rgb) | `def separate_rgb(color=None):` |
| [separate_hsv](functions.md#separate_hsv) | `def separate_hsv(color=None):` |
| [separate_hsl](functions.md#separate_hsl) | `def separate_hsl(color=None):` |

<sub>Go to [top](#node-Separate-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

