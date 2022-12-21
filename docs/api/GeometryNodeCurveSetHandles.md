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

#### Input socket arguments:

- curve: [Curve](Curve.md)
- selection: [Boolean](Boolean.md)

#### Node parameter arguments:

- handle_type (str): Node parameter, default = 'AUTO' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
- mode (set): Node parameter, default = {'RIGHT', 'LEFT'}

#### Output sockets:

- **curve** : Curve

