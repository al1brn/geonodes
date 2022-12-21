# Node Trim Curve

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)
- geonodes name: `TrimCurve`
- bl_idname: `GeometryNodeTrimCurve`

```python
from geonodes import nodes

node = nodes.TrimCurve(curve=None, start0=None, start1=None, end0=None, end1=None, mode='FACTOR')
```

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)
- **start0**: [Float](Float.md)
- **start1**: [Float](Float.md)
- **end0**: [Float](Float.md)
- **end1**: [Float](Float.md)

#### Node parameter arguments:

- **mode** (str): default = 'FACTOR' in ('FACTOR', 'LENGTH')

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

#### class [Curve](Curve.md)

 - [trim](Curve.md#trim)
 - [trim_factor](Curve.md#trim_factor)
 - [trim_length](Curve.md#trim_length)