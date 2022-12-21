# Node Fillet Curve

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fillet_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html)
- geonodes name: `FilletCurve`
- bl_idname: `GeometryNodeFilletCurve`

```python
from geonodes import nodes

node = nodes.FilletCurve(curve=None, count=None, radius=None, limit_radius=None, mode='BEZIER')
```

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

#### [Curve](Curve.md)

 - [fillet](Curve.md#fillet) ```python nodes.FilletCurve(curve=self, count=count, radius=radius, limit_radius=limit_radius, mode=mode````
 - [fillet_bezier](Curve.md#fillet_bezier) ```python nodes.FilletCurve(curve=self, count=1, radius=radius, limit_radius=limit_radius, mode='BEZIER'````
 - [fillet_poly](Curve.md#fillet_poly) ```python nodes.FilletCurve(curve=self, count=count, radius=radius, limit_radius=limit_radius, mode='POLY'````
