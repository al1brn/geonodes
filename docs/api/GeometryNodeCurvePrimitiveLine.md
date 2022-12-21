# Node Curve Line

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_line.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveLine.html)
- geonodes name: `CurveLine`
- bl_idname: `GeometryNodeCurvePrimitiveLine`

```python
from geonodes import nodes

node = nodes.CurveLine(start=None, end=None, direction=None, length=None, mode='POINTS')
```

#### Input socket arguments:

- start: Vector
- end: Vector
- direction: Vector
- length: Float

#### Node parameter arguments:

- mode (str): Node parameter, default = 'POINTS' in ('POINTS', 'DIRECTION')

#### Output sockets:

- **curve** : Curve

