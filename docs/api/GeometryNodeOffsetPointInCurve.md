# Node Offset Point in Curve

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/offset_point_in_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetPointInCurve.html)
- geonodes name: `OffsetPointInCurve`
- bl_idname: `GeometryNodeOffsetPointInCurve`

```python
from geonodes import nodes

node = nodes.OffsetPointInCurve(point_index=None, offset=None)
```

#### Input socket arguments:

- point_index: [Integer](Integer.md)
- offset: [Integer](Integer.md)

#### Output sockets:

- **is_valid_offset** : [Boolean](Boolean)
- **point_index** : [Integer](Integer)

