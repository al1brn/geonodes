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

#### Input socket arguments:

- curve: Curve

#### Node parameter arguments:

- mode (str): Node parameter, default = 'TRIANGLES' in ('TRIANGLES', 'NGONS')

#### Output sockets:

- **mesh** : Mesh

