# Node *Set Spline Cyclic*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_cyclic.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html)
- geonodes name: `SetSplineCyclic`
- bl_idname: `GeometryNodeSetSplineCyclic`

```python
from geonodes import nodes

node = nodes.SetSplineCyclic(geometry=None, selection=None, cyclic=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetSplineCyclic.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **cyclic**: [Boolean](Boolean.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Spline](Spline.md)** |
| [set_cyclic](Spline.md#set_cyclic) | `def set_cyclic(self, cyclic=None):` |
| [cyclic](Spline.md#cyclic) | `@cyclic.setter
`<br> `def cyclic(self, attr_value):` |

<sub>Go to [top](#node-Set-Spline-Cyclic) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

