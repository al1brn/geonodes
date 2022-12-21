# Node Fill Curve

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)
- geonodes name: `FillCurve`
- bl_idname: `GeometryNodeFillCurve`

```python
from geonodes import nodes

node = nodes.FillCurve(curve=None, mode='TRIANGLES')
```

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)

#### Node parameter arguments:

- **mode** (str): default = 'TRIANGLES' in ('TRIANGLES', 'NGONS')

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

#### [Curve](Curve.md)

 - [fill](Curve.md#fill)
  ```python
  nodes.FillCurve(curve=curve, mode=mode  ```

 - [fill_triangles](Curve.md#fill_triangles)
  ```python
  nodes.FillCurve(curve=curve, mode='TRIANGLES'  ```

 - [fill_ngons](Curve.md#fill_ngons)
  ```python
  nodes.FillCurve(curve=curve, mode='NGONS'  ```

