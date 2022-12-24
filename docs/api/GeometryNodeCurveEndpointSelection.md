# Node *Endpoint Selection*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/endpoint_selection.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveEndpointSelection.html)
- geonodes name: `EndpointSelection`
- bl_idname: `GeometryNodeCurveEndpointSelection`

```python
from geonodes import nodes

node = nodes.EndpointSelection(start_size=None, end_size=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveEndpointSelection.webp)

### Args:

#### Input socket arguments:

- **start_size**: [Integer](Integer.md)
- **end_size**: [Integer](Integer.md)

### Output sockets:

- **selection** : [Boolean](Boolean.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[ControlPoint](ControlPoint.md)** |
| [endpoint_selection](ControlPoint.md#endpoint_selection) | `def endpoint_selection(self, start_size=None, end_size=None):` |

<sub>Go to [top](#node-Endpoint-Selection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

