# Node Resample Curve

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)
- geonodes name: `ResampleCurve`
- bl_idname: `GeometryNodeResampleCurve`

```python
from geonodes import nodes

node = nodes.ResampleCurve(curve=None, selection=None, count=None, length=None, mode='COUNT')
```

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)
- **selection**: [Boolean](Boolean.md)
- **count**: [Integer](Integer.md)
- **length**: [Float](Float.md)

#### Node parameter arguments:

- **mode** (str): default = 'COUNT' in ('EVALUATED', 'COUNT', 'LENGTH')

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

#### class [Curve](Curve.md)

 - [resample](Curve.md#resample)
 - [resample_count](Curve.md#resample_count)
 - [resample_length](Curve.md#resample_length)
 - [resample_evaluated](Curve.md#resample_evaluated)
#### class [Spline](Spline.md)

 - [resample](Spline.md#resample)
 - [resample_count](Spline.md#resample_count)
 - [resample_length](Spline.md#resample_length)
 - [resample_evaluated](Spline.md#resample_evaluated)
