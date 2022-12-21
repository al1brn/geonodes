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

#### Node parameter arguments:

- handle_type (str): Node parameter, default = 'AUTO' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
- mode (set): Node parameter, default = {'RIGHT', 'LEFT'}

#### Output sockets:

- **selection** : [Boolean](Boolean

