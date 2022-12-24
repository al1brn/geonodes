# Node *Set Point Radius*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html)
- geonodes name: `SetPointRadius`
- bl_idname: `GeometryNodeSetPointRadius`

```python
from geonodes import nodes

node = nodes.SetPointRadius(points=None, selection=None, radius=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetPointRadius.webp)

### Args:

#### Input socket arguments:

- **points**: [Points](Points.md)
- **selection**: [Boolean](Boolean.md)
- **radius**: [Float](Float.md)

### Output sockets:

- **points** : [Points](Points.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[CloudPoint](CloudPoint.md)** |
| [radius](CloudPoint.md#radius) | `@radius.setter
`<br> `def radius(self, attr_value):` |
| **[Points](Points.md)** |
| [set_point_radius](Points.md#set_point_radius) | `def set_point_radius(self, selection=None, radius=None):` |

<sub>Go to [top](#node-Set-Point-Radius) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

