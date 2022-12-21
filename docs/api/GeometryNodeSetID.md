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

#### [Domain](Domain.md)

 - [set_ID](Domain.md#set_ID) ```python nodes.SetID(geometry=self.data_socket, selection=self.selection, ID=ID````
 - [ID](Domain.md#ID) ```python nodes.SetID(geometry=self.data_socket, selection=self.selection, ID=attr_value````
#### [Geometry](Geometry.md)

 - [set_ID](Geometry.md#set_ID) ```python nodes.SetID(geometry=self, selection=selection, ID=ID````
