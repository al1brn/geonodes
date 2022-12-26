# Node *ColorRamp*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/color_ramp.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html)
- geonodes name: `ColorRamp`
- bl_idname: `ShaderNodeValToRGB`

```python
from geonodes import nodes

node = nodes.ColorRamp(fac=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeValToRGB.webp)

### Args:

#### Input socket arguments:

- **fac**: [Float](Float.md)

### Output sockets:

- **color** : [Color](Color.md)
- **alpha** : [Float](Float.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Float](Float.md)** |
| [color_ramp](Float.md#color_ramp) | `@property`<br> `def color_ramp(self):` |
| Global functions |
| [color_ramp](functions.md#color_ramp) | `def color_ramp(fac=None):` |

<sub>Go to [top](#node-ColorRamp) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

