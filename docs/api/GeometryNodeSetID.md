# Node Set ID

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)
- geonodes name: `SetID`
- bl_idname: `GeometryNodeSetID`

```python
from geonodes import nodes

node = nodes.SetID(geometry=None, selection=None, ID=None)
```

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **ID**: [Integer](Integer.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

#### class [Geometry](Geometry.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x16d4f9510>>](Geometry.md#set_ID)
#### class [Domain](Domain.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4f94e0>>](Domain.md#set_ID)
 - [<bound method Generator.fname of <generator.code_gen.DomSetter object at 0x16d4f94b0>>](Domain.md#ID)
