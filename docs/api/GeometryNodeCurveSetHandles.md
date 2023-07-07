# Node *Set Handle Type*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_type.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html)
- geonodes name: `SetHandleType`
- bl_idname: `GeometryNodeCurveSetHandles`

```python
from geonodes import nodes

node = nodes.SetHandleType(curve=None, selection=None, handle_type='AUTO', mode={'RIGHT', 'LEFT'})
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveSetHandles.webp)

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

| Class or method name | Definition |
|----------------------|------------|
| **[ControlPoint](ControlPoint.md)** |
| [set_handle_type_node](ControlPoint.md#set_handle_type_node) | `def set_handle_type_node(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):` |
| [set_handle_type](ControlPoint.md#set_handle_type) | `def set_handle_type(self, left=True, right=True, handle_type='AUTO'):` |

<sub>Go to [top](#node-Set-Handle-Type) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

