# Node Curve Handle Positions

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)
- geonodes name: `CurveHandlePositions`
- bl_idname: `GeometryNodeInputCurveHandlePositions`

```python
from geonodes import nodes

node = nodes.CurveHandlePositions(relative=None)
```

### Args:

#### Input socket arguments:

- **relative**: [Boolean](Boolean.md)

### Output sockets:

- **left** : [Vector](Vector.md)
- **right** : [Vector](Vector.md)

## Implementation

#### class [ControlPoint](ControlPoint.md)

 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x16d4fa8c0>>](ControlPoint.md#handle_positions)
 - [<bound method Generator.fname of <generator.code_gen.DomPropAttribute object at 0x16d4fa890>>](ControlPoint.md#left_handle_positions-property)
 - [<bound method Generator.fname of <generator.code_gen.DomPropAttribute object at 0x16d4fa860>>](ControlPoint.md#right_handle_positions-property)
