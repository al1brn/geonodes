# Node *Spline Length*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_length.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineLength.html)
- geonodes name: `SplineLength`
- bl_idname: `GeometryNodeSplineLength`

```python
from geonodes import nodes

node = nodes.SplineLength()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSplineLength.webp)

### Output sockets:

- **length** : [Float](Float.md)
- **point_count** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Spline](Spline.md)** |
| [length](Spline.md#length) | `@property`<br> `def length(self):` |

<sub>Go to [top](#node-Spline-Length) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

