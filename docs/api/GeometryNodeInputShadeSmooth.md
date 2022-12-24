# Node *Is Shade Smooth*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/is_shade_smooth.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShadeSmooth.html)
- geonodes name: `IsShadeSmooth`
- bl_idname: `GeometryNodeInputShadeSmooth`

```python
from geonodes import nodes

node = nodes.IsShadeSmooth()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputShadeSmooth.webp)

### Output sockets:

- **smooth** : [Boolean](Boolean.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Face](Face.md)** |
| [shade_smooth](Face.md#shade_smooth) | `@property`<br> `def shade_smooth(self):` |
| **[Mesh](Mesh.md)** |
| [is_shade_smooth](Mesh.md#is_shade_smooth) | `def is_shade_smooth(self):` |

<sub>Go to [top](#node-Is-Shade-Smooth) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

