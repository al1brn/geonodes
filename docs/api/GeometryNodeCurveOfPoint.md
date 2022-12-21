# Node Curve of Point

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/curve_of_point.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveOfPoint.html)
- geonodes name: `CurveOfPoint`
- bl_idname: `GeometryNodeCurveOfPoint`

```python
from geonodes import nodes

node = nodes.CurveOfPoint(point_index=None)
```

### Args:

#### Input socket arguments:

- **point_index**: [Integer](Integer.md)

### Output sockets:

- **curve_index** : [Integer](Integer.md)
- **index_in_curve** : [Integer](Integer.md)

## Implementation

#### class [Curve](Curve.md)

 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x16d4f9ea0>>](Curve.md#curve_of_point)
#### class [ControlPoint](ControlPoint.md)

 - [<bound method Generator.fname of <generator.code_gen.DomAttribute object at 0x16d4f9e70>>](ControlPoint.md#curve)
