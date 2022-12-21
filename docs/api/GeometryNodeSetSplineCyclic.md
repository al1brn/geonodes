# Node Set Spline Cyclic

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_cyclic.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html)
- geonodes name: `SetSplineCyclic`
- bl_idname: `GeometryNodeSetSplineCyclic`

```python
from geonodes import nodes

node = nodes.SetSplineCyclic(geometry=None, selection=None, cyclic=None)
```

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **cyclic**: [Boolean](Boolean.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

#### [Spline](Spline.md)

 - [set_cyclic](Spline.md#set_cyclic) ```python nodes.SetSplineCyclic(geometry=self.data_socket, selection=self.selection, cyclic=cyclic````
 - [cyclic](Spline.md#cyclic) ```python nodes.SetSplineCyclic(geometry=self.data_socket, selection=self.selection, cyclic=attr_value````
