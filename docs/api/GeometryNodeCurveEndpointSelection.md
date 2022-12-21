# Node Endpoint Selection

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/endpoint_selection.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveEndpointSelection.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeCurveEndpointSelection`

```python
from geonodes import nodes

node = nodes.EndpointSelection(start_size=None, end_size=None)
```

#### Input socket arguments:

- start_size: Integer
- end_size: Integer

#### Output sockets:

- **selection** : Boolean

