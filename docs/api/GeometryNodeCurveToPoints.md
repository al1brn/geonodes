# Node Curve to Points

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html)
- geonodes name: `CurveToPoints`
- bl_idname: `GeometryNodeCurveToPoints`

```python
from geonodes import nodes

node = nodes.CurveToPoints(curve=None, count=None, length=None, mode='COUNT')
```

#### Input socket arguments:

- curve: [Curve](Curve.md)
- count: [Integer](Integer.md)
- length: [Float](Float.md)

#### Node parameter arguments:

- mode (str): Node parameter, default = 'COUNT' in ('EVALUATED', 'COUNT', 'LENGTH')

#### Output sockets:

- **points** : [Points](Points)
- **tangent** : [Vector](Vector)
- **normal** : [Vector](Vector)
- **rotation** : [Vector](Vector)

