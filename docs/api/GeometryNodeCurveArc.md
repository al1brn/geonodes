# Node Arc

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/arc.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeCurveArc`

```python
from geonodes import nodes

node = nodes.Arc(resolution=None, start=None, middle=None, end=None, radius=None, start_angle=None, sweep_angle=None, offset_angle=None, connect_center=None, invert_arc=None, mode='RADIUS')
```

#### Input socket arguments:

- resolution: Integer
- start: Vector
- middle: Vector
- end: Vector
- radius: Float
- start_angle: Float
- sweep_angle: Float
- offset_angle: Float
- connect_center: Boolean
- invert_arc: Boolean

#### Node parameter arguments:

- mode (str): Node parameter, default = 'RADIUS' in ('POINTS', 'RADIUS')

#### Output sockets:

- **curve** : Curve
- **center** : Vector
- **normal** : Vector
- **radius** : Float

