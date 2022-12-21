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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomAttribute object at 0x164097700>>](ControlPoint.md#handle_type_selection_node)
 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x164097790>>](ControlPoint.md#handle_type_selection)
 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x1640970a0>>](ControlPoint.md#handle_type_selection)
 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x1640971c0>>](ControlPoint.md#handle_type_selection)
 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x164097130>>](ControlPoint.md#handle_type_selection)
 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x164097be0>>](ControlPoint.md#handle_type_selection)
