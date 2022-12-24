# Node *Is Viewport*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/is_viewport.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeIsViewport.html)
- geonodes name: `IsViewport`
- bl_idname: `GeometryNodeIsViewport`

```python
from geonodes import nodes

node = nodes.IsViewport()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeIsViewport.webp)

### Output sockets:

- **is_viewport** : [Boolean](Boolean.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Geometry](Geometry.md)** |
| [is_viewport](Geometry.md#is_viewport) | `@property`<br> `def is_viewport(self):` |

<sub>Go to [top](#node-Is-Viewport) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

