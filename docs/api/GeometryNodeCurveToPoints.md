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

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)
- **count**: [Integer](Integer.md)
- **length**: [Float](Float.md)

#### Node parameter arguments:

- **mode** (str): default = 'COUNT' in ('EVALUATED', 'COUNT', 'LENGTH')

### Output sockets:

- **points** : [Points](Points.md)
- **tangent** : [Vector](Vector.md)
- **normal** : [Vector](Vector.md)
- **rotation** : [Vector](Vector.md)

## Implementation

#### class [Curve](Curve.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fad70>>](Curve.md#to_points)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fad40>>](Curve.md#to_points_count)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4fad10>>](Curve.md#to_points_length)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4face0>>](Curve.md#to_points_evaluated)
