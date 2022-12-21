# Node Quadratic Bezier

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/quadratic_bezier.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveQuadraticBezier.html)
- geonodes name: `QuadraticBezier`
- bl_idname: `GeometryNodeCurveQuadraticBezier`

```python
from geonodes import nodes

node = nodes.QuadraticBezier(resolution=None, start=None, middle=None, end=None)
```

### Args:

#### Input socket arguments:

- **resolution**: [Integer](Integer.md)
- **start**: [Vector](Vector.md)
- **middle**: [Vector](Vector.md)
- **end**: [Vector](Vector.md)

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

### [Curve](Curve.md)

| Name | Definition |
|------|------------|
 | [QuadraticBezier](Curve.md#QuadraticBezier-classmethod) | `def QuadraticBezier(cls, resolution=None, start=None, middle=None, end=None): |

