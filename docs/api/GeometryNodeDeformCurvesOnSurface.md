# Node *Deform Curves on Surface*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/deform_curves_on_surface.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeformCurvesOnSurface.html)
- geonodes name: `DeformCurvesOnSurface`
- bl_idname: `GeometryNodeDeformCurvesOnSurface`

```python
from geonodes import nodes

node = nodes.DeformCurvesOnSurface(curves=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDeformCurvesOnSurface.webp)

### Args:

#### Input socket arguments:

- **curves**: [Curve](Curve.md)

### Output sockets:

- **curves** : [Curve](Curve.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Curve](Curve.md)** |
| [deform_on_surface](Curve.md#deform_on_surface) | `def deform_on_surface(self):` |

<sub>Go to [top](#node-Deform-Curves-on-Surface) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

