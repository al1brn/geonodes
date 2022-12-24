# Node *Points of Curve*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/points_of_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsOfCurve.html)
- geonodes name: `PointsOfCurve`
- bl_idname: `GeometryNodePointsOfCurve`

```python
from geonodes import nodes

node = nodes.PointsOfCurve(curve_index=None, weights=None, sort_index=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePointsOfCurve.webp)

### Args:

#### Input socket arguments:

- **curve_index**: [Integer](Integer.md)
- **weights**: [Float](Float.md)
- **sort_index**: [Integer](Integer.md)

### Output sockets:

- **point_index** : [Integer](Integer.md)
- **total** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Curve](Curve.md)** |
| [points_of_curve](Curve.md#points_of_curve) | `def points_of_curve(self, curve_index=None, weights=None, sort_index=None):` |
| **[Spline](Spline.md)** |
| [points](Spline.md#points) | `def points(self, weights=None, sort_index=None):` |

<sub>Go to [top](#node-Points-of-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

