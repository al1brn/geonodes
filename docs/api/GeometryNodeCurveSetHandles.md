# Node Set Handle Type

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_type.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html)
- geonodes name: `SetHandleType`
- bl_idname: `GeometryNodeCurveSetHandles`

```python
from geonodes import nodes

node = nodes.SetHandleType(curve=None, selection=None, handle_type='AUTO', mode={'RIGHT', 'LEFT'})
```

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)
- **selection**: [Boolean](Boolean.md)

#### Node parameter arguments:

- **handle_type** (str): default = 'AUTO' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
- **mode** (set): default = {'RIGHT', 'LEFT'}

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

#### [ControlPoint](ControlPoint.md)

 - [set_handle_type_node](ControlPoint.md#set_handle_type_node)
  ```python
  nodes.SetHandleType(curve=self.data_socket, selection=self.selection, handle_type=handle_type, mode=mode  ```

 - [set_handle_type](ControlPoint.md#set_handle_type)
  ```python
  nodes.SetHandleType(curve=curve, selection=selection, handle_type=handle_type, mode=mode  ```

