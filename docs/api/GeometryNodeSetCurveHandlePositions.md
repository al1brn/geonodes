# Node Set Handle Positions

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)
- geonodes name: `SetHandlePositions`
- bl_idname: `GeometryNodeSetCurveHandlePositions`

```python
from geonodes import nodes

node = nodes.SetHandlePositions(curve=None, selection=None, position=None, offset=None, mode='LEFT')
```

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)
- **selection**: [Boolean](Boolean.md)
- **position**: [Vector](Vector.md)
- **offset**: [Vector](Vector.md)

#### Node parameter arguments:

- **mode** (str): default = 'LEFT' in ('LEFT', 'RIGHT')

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x164097850>>](ControlPoint.md#set_handle_positions)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1640979d0>>](ControlPoint.md#set_handle_positions_left)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x164097460>>](ControlPoint.md#set_handle_positions_right)
 - [<bound method Generator.fname of <generator.code_gen.DomSetter object at 0x164097280>>](ControlPoint.md#left_handle_positions)
 - [<bound method Generator.fname of <generator.code_gen.DomSetter object at 0x164097160>>](ControlPoint.md#right_handle_positions)
