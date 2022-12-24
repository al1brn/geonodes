# Node *Fillet Curve*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fillet_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html)
- geonodes name: `FilletCurve`
- bl_idname: `GeometryNodeFilletCurve`

```python
from geonodes import nodes

node = nodes.FilletCurve(curve=None, count=None, radius=None, limit_radius=None, mode='BEZIER')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFilletCurve.webp)

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)
- **count**: [Integer](Integer.md)
- **radius**: [Float](Float.md)
- **limit_radius**: [Boolean](Boolean.md)

#### Node parameter arguments:

- **mode** (str): default = 'BEZIER' in ('BEZIER', 'POLY')

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Curve](Curve.md)** |
| [fillet](Curve.md#fillet) | `def fillet(self, count=None, radius=None, limit_radius=None, mode='BEZIER'):` |
| [fillet_bezier](Curve.md#fillet_bezier) | `def fillet_bezier(self, radius=None, limit_radius=None):` |
| [fillet_poly](Curve.md#fillet_poly) | `def fillet_poly(self, count=None, radius=None, limit_radius=None):` |

<sub>Go to [top](#node-Fillet-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

