# Node Handle Type Selection

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)
- geonodes name: `HandleTypeSelection`
- bl_idname: `GeometryNodeCurveHandleTypeSelection`

```python
from geonodes import nodes

node = nodes.HandleTypeSelection(handle_type='AUTO', mode={'RIGHT', 'LEFT'})
```

### Args:

#### Node parameter arguments:

- **handle_type** (str): default = 'AUTO' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
- **mode** (set): default = {'RIGHT', 'LEFT'}

### Output sockets:

- **selection** : [Boolean](Boolean.md)

## Implementation

#### class [ControlPoint](ControlPoint.md)

 - [<bound method Generator.fname of <generator.code_gen.DomAttribute object at 0x16d4fa7a0>>](ControlPoint.md#handle_type_selection_node)
 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x16d4fa770>>](ControlPoint.md#handle_type_selection)
 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x16d4fa740>>](ControlPoint.md#handle_type_selection)
 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x16d4fa710>>](ControlPoint.md#handle_type_selection)
 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x16d4fa6e0>>](ControlPoint.md#handle_type_selection)
 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x16d4fa6b0>>](ControlPoint.md#handle_type_selection)
