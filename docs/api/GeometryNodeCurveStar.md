# Node Star

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/star.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveStar.html)
- geonodes name: `Star`
- bl_idname: `GeometryNodeCurveStar`

```python
from geonodes import nodes

node = nodes.Star(points=None, inner_radius=None, outer_radius=None, twist=None)
```

### Args:

#### Input socket arguments:

- **points**: [Integer](Integer.md)
- **inner_radius**: [Float](Float.md)
- **outer_radius**: [Float](Float.md)
- **twist**: [Float](Float.md)

### Output sockets:

- **curve** : [Curve](Curve.md)
- **outer_points** : [Boolean](Boolean.md)

## Implementation

#### class [Curve](Curve.md)

 - [Star](Curve.md#Star-classmethod)