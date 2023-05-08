# Node *Interpolate Curves*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/n.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInterpolateCurves.html)
- geonodes name: `InterpolateCurves`
- bl_idname: `GeometryNodeInterpolateCurves`

```python
from geonodes import nodes

node = nodes.InterpolateCurves(guide_curves=None, guide_up=None, guide_group_id=None, points=None, point_up=None, point_group_id=None, max_neighbors=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateCurves.webp)

### Args:

#### Input socket arguments:

- **guide_curves**: [Geometry](Geometry.md)
- **guide_up**: [Vector](Vector.md)
- **guide_group_id**: [Integer](Integer.md)
- **points**: [Points](Points.md)
- **point_up**: [Vector](Vector.md)
- **point_group_id**: [Integer](Integer.md)
- **max_neighbors**: [Integer](Integer.md)

### Output sockets:

- **curves** : [Curve](Curve.md)
- **closest_index** : [Integer](Integer.md)
- **closest_weight** : [Float](Float.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[CloudPoint](CloudPoint.md)** |
| [interpolate](CloudPoint.md#interpolate) | `def interpolate(self, guide_curves=None, guide_up=None, guide_group_id=None, point_up=None, point_group_id=None, max_neighbors=None):` |
| **[ControlPoint](ControlPoint.md)** |
| [interpolate](ControlPoint.md#interpolate) | `def interpolate(self, guide_curves=None, guide_up=None, guide_group_id=None, point_up=None, point_group_id=None, max_neighbors=None):` |
| **[Curve](Curve.md)** |
| [interpolate](Curve.md#interpolate) | `def interpolate(self, guide_up=None, guide_group_id=None, points=None, point_up=None, point_group_id=None, max_neighbors=None):` |
| **[Points](Points.md)** |
| [interpolate](Points.md#interpolate) | `def interpolate(self, guide_curves=None, guide_up=None, guide_group_id=None, point_up=None, point_group_id=None, max_neighbors=None):` |
| **[Vertex](Vertex.md)** |
| [interpolate](Vertex.md#interpolate) | `def interpolate(self, guide_curves=None, guide_up=None, guide_group_id=None, point_up=None, point_group_id=None, max_neighbors=None):` |

<sub>Go to [top](#node-Interpolate-Curves) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

