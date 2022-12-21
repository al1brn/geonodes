# Node Points of Curve

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/points_of_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsOfCurve.html)
- geonodes name: `PointsOfCurve`
- bl_idname: `GeometryNodePointsOfCurve`

```python
from geonodes import nodes

node = nodes.PointsOfCurve(curve_index=None, weights=None, sort_index=None)
```

### Args:

#### Input socket arguments:

- **curve_index**: [Integer](Integer.md)
- **weights**: [Float](Float.md)
- **sort_index**: [Integer](Integer.md)

### Output sockets:

- **point_index** : [Integer](Integer.md)
- **total** : [Integer](Integer.md)

## Implementation

#### class [Curve](Curve.md)

 - [points_of_curve](Curve.md#points_of_curve)
#### class [Spline](Spline.md)

 - [points](Spline.md#points)