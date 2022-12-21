# Node Curve of Point

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/curve_of_point.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveOfPoint.html)
- geonodes name: `CurveOfPoint`
- bl_idname: `GeometryNodeCurveOfPoint`

```python
from geonodes import nodes

node = nodes.CurveOfPoint(point_index=None)
```

### Args:

#### Input socket arguments:

- **point_index**: [Integer](Integer.md)

### Output sockets:

- **curve_index** : [Integer](Integer.md)
- **index_in_curve** : [Integer](Integer.md)

## Implementation

#### [ControlPoint](ControlPoint.md)

 - [curve](ControlPoint.md#curve)
  ```python
  nodes.CurveOfPoint(point_index=self.selection_index  ```

#### [Curve](Curve.md)

 - [curve_of_point](Curve.md#curve_of_point)
  ```python
  nodes.CurveOfPoint(point_index=point_index  ```

