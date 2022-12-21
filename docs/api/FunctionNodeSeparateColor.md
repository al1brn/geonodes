# Node 'Separate Color'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

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
| Global functions |
| [separate_rgb](A.md#separate_rgb) | `def separate_rgb(color=None):` |
| [separate_hsv](A.md#separate_hsv) | `def separate_hsv(color=None):` |
| [separate_hsl](A.md#separate_hsl) | `def separate_hsl(color=None):` |
| **[Color](Color.md)** |
| [rgb](Color.md#rgb-property) | `@property`<br> `def rgb(self):` |
| [hsv](Color.md#hsv-property) | `@property`<br> `def hsv(self):` |
| [hsl](Color.md#hsl-property) | `@property`<br> `def hsl(self):` |
| [alpha](Color.md#alpha-property) | `@property`<br> `def alpha(self):` |
| [red](Color.md#red-property) | `@property`<br> `def red(self):` |
| [green](Color.md#green-property) | `@property`<br> `def green(self):` |
| [blue](Color.md#blue-property) | `@property`<br> `def blue(self):` |
| [hue](Color.md#hue-property) | `@property`<br> `def hue(self):` |
| [saturation](Color.md#saturation-property) | `@property`<br> `def saturation(self):` |
| [value](Color.md#value-property) | `@property`<br> `def value(self):` |
| [lightness](Color.md#lightness-property) | `@property`<br> `def lightness(self):` |

<sub>Go to [top](#node-Separate-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

