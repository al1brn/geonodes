# Node Curve Circle

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_circle.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveCircle.html)
- geonodes name: `CurveCircle`
- bl_idname: `GeometryNodeCurvePrimitiveCircle`

```python
from geonodes import nodes

node = nodes.CurveCircle(resolution=None, point_1=None, point_2=None, point_3=None, radius=None, mode='RADIUS')
```

#### Input socket arguments:

- resolution: Integer
- point_1: Vector
- point_2: Vector
- point_3: Vector
- radius: Float

#### Node parameter arguments:

- mode (str): Node parameter, default = 'RADIUS' in ('POINTS', 'RADIUS')

#### Output sockets:

- **curve** : Curve
- **center** : Vector

