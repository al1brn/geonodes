# Node *Points*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePoints.html)
- geonodes name: `Points`
- bl_idname: `GeometryNodePoints`

```python
from geonodes import nodes

node = nodes.Points(count=None, position=None, radius=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePoints.webp)

### Args:

#### Input socket arguments:

- **count**: [Integer](Integer.md)
- **position**: [Vector](Vector.md)
- **radius**: [Float](Float.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Points](Points.md)** |
| [Points](Points.md#Points) | `@classmethod`<br> `def Points(cls, count=None, position=None, radius=None):` |

<sub>Go to [top](#node-Points) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

