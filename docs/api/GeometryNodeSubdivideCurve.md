# Node Subdivide Curve

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/subdivide_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideCurve.html)
- geonodes name: `SubdivideCurve`
- bl_idname: `GeometryNodeSubdivideCurve`

```python
from geonodes import nodes

node = nodes.SubdivideCurve(curve=None, cuts=None)
```

#### Input socket arguments:

- curve: [Curve](Curve.md)
- cuts: [Integer](Integer.md)

#### Output sockets:

- **curve** : [Curve](Curve)

