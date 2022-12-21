# Node Arc

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/arc.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html)
- geonodes name: `Arc`
- bl_idname: `GeometryNodeCurveArc`

```python
from geonodes import nodes

node = nodes.Arc(resolution=None, start=None, middle=None, end=None, radius=None, start_angle=None, sweep_angle=None, offset_angle=None, connect_center=None, invert_arc=None, mode='RADIUS')
```

#### Input socket arguments:

- resolution: [Integer](Integer.md)
- start: [Vector](Vector.md)
- middle: [Vector](Vector.md)
- end: [Vector](Vector.md)
- radius: [Float](Float.md)
- start_angle: [Float](Float.md)
- sweep_angle: [Float](Float.md)
- offset_angle: [Float](Float.md)
- connect_center: [Boolean](Boolean.md)
- invert_arc: [Boolean](Boolean.md)

#### Node parameter arguments:

- mode (str): Node parameter, default = 'RADIUS' in ('POINTS', 'RADIUS')

#### Output sockets:

- **curve** : [Curve](Curve.md)
- **center** : [Vector](Vector.md)
- **normal** : [Vector](Vector.md)
- **radius** : [Float](Float.md)

