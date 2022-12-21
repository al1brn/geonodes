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

#### class [ControlPoint](ControlPoint.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4fa2c0>>](ControlPoint.md#set_handle_type_node)
 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x16d4fa290>>](ControlPoint.md#set_handle_type)
