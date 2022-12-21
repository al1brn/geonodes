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

 - [fillet](Curve.md#fillet)
  ```python
  def fillet(self, count=None, radius=None, limit_radius=None, mode='BEZIER')
  ```

 - [fillet_bezier](Curve.md#fillet_bezier)
  ```python
  def fillet_bezier(self, radius=None, limit_radius=None)
  ```

 - [fillet_poly](Curve.md#fillet_poly)
  ```python
  def fillet_poly(self, count=None, radius=None, limit_radius=None)
  ```

