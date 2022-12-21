# Node Endpoint Selection

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/endpoint_selection.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveEndpointSelection.html)
- geonodes name: `EndpointSelection`
- bl_idname: `GeometryNodeCurveEndpointSelection`

```python
from geonodes import nodes

node = nodes.EndpointSelection(start_size=None, end_size=None)
```

### Args:

#### Input socket arguments:

- **start_size**: [Integer](Integer.md)
- **end_size**: [Integer](Integer.md)

### Output sockets:

- **selection** : [Boolean](Boolean.md)

## Implementation

#### class [ControlPoint](ControlPoint.md)

 - [endpoint_selection](ControlPoint.md#endpoint_selection)