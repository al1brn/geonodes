# Node *Radius*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)
- geonodes name: `Radius`
- bl_idname: `GeometryNodeInputRadius`

```python
from geonodes import nodes

node = nodes.Radius()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputRadius.webp)

### Output sockets:

- **radius** : [Float](Float.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[CloudPoint](CloudPoint.md)** |
| [radius](CloudPoint.md#radius) | `@property`<br> `def radius(self):` |
| **[ControlPoint](ControlPoint.md)** |
| [radius](ControlPoint.md#radius) | `@property`<br> `def radius(self):` |
| **[Curve](Curve.md)** |
| [radius](Curve.md#radius) | `@property`<br> `def radius(self):` |
| **[Points](Points.md)** |
| [radius](Points.md#radius) | `@property`<br> `def radius(self):` |

<sub>Go to [top](#node-Radius) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

