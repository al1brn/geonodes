# Node *RGB Curves*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/rgb_curves.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBCurve.html)
- geonodes name: `RgbCurves`
- bl_idname: `ShaderNodeRGBCurve`

```python
from geonodes import nodes

node = nodes.RgbCurves(fac=None, color=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeRGBCurve.webp)

### Args:

#### Input socket arguments:

- **fac**: [Float](Float.md)
- **color**: [Color](Color.md)

### Output sockets:

- **color** : [Color](Color.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Color](Color.md)** |
| [rgb_curves](Color.md#rgb_curves) | `@property`<br> `def rgb_curves(self, fac=None):` |
| Global functions |
| [rgb_curves](functions.md#rgb_curves) | `def rgb_curves(fac=None, color=None):` |

<sub>Go to [top](#node-RGB-Curves) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

