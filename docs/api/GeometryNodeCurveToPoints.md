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

#### [Curve](Curve.md)

 - [to_points](Curve.md#to_points) ```python nodes.CurveToPoints(curve=self, count=count, length=length, mode=mode````
 - [to_points_count](Curve.md#to_points_count) ```python nodes.CurveToPoints(curve=self, count=count, length=0.1, mode='COUNT'````
 - [to_points_length](Curve.md#to_points_length) ```python nodes.CurveToPoints(curve=self, count=10, length=length, mode='LENGTH'````
 - [to_points_evaluated](Curve.md#to_points_evaluated) ```python nodes.CurveToPoints(curve=self, count=10, length=0.1, mode='EVALUATED'````
