# Node Set Position

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)
- geonodes name: `SetPosition`
- bl_idname: `GeometryNodeSetPosition`

```python
from geonodes import nodes

node = nodes.SetPosition(geometry=None, selection=None, position=None, offset=None)
```

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **position**: [Vector](Vector.md)
- **offset**: [Vector](Vector.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

#### class [Geometry](Geometry.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x16d4f9480>>](Geometry.md#set_position)
#### class [Domain](Domain.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4f9450>>](Domain.md#set_position)
 - [<bound method Generator.fname of <generator.code_gen.DomSetter object at 0x16d4f9420>>](Domain.md#position)
