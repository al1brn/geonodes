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

### Args:

#### Input socket arguments:

- **resolution**: [Integer](Integer.md)
- **point_1**: [Vector](Vector.md)
- **point_2**: [Vector](Vector.md)
- **point_3**: [Vector](Vector.md)
- **radius**: [Float](Float.md)

#### Node parameter arguments:

- **mode** (str): default = 'RADIUS' in ('POINTS', 'RADIUS')

### Output sockets:

- **curve** : [Curve](Curve.md)
- **center** : [Vector](Vector.md)

## Implementation

#### [Curve](Curve.md)

 - [Circle](Curve.md#Circle-classmethod) ```python nodes.CurveCircle(resolution=resolution, point_1=None, point_2=None, point_3=None, radius=radius, mode='RADIUS'````
 - [CircleFromPoints](Curve.md#CircleFromPoints-classmethod) ```python nodes.CurveCircle(resolution=resolution, point_1=point_1, point_2=point_2, point_3=point_3, radius=None, mode=POINT````
