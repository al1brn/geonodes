# Node Quadrilateral

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/quadrilateral.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveQuadrilateral.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeCurvePrimitiveQuadrilateral`

```python
from geonodes import nodes

node = nodes.Quadrilateral(width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE')
```

#### Input socket arguments:

- width: Float
- height: Float
- bottom_width: Float
- top_width: Float
- offset: Float
- bottom_height: Float
- top_height: Float
- point_1: Vector
- point_2: Vector
- point_3: Vector
- point_4: Vector

#### Node parameter arguments:

- mode (str): Node parameter, default = 'RECTANGLE' in ('RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS')

#### Output sockets:

- **curve** : Curve

