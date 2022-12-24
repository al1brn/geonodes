# Node *Set Spline Resolution*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_resolution.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html)
- geonodes name: `SetSplineResolution`
- bl_idname: `GeometryNodeSetSplineResolution`

```python
from geonodes import nodes

node = nodes.SetSplineResolution(geometry=None, selection=None, resolution=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetSplineResolution.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **resolution**: [Integer](Integer.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Spline](Spline.md)** |
| [set_resolution](Spline.md#set_resolution) | `def set_resolution(self, resolution=None):` |
| [resolution](Spline.md#resolution) | `@resolution.setter
`<br> `def resolution(self, attr_value):` |

<sub>Go to [top](#node-Set-Spline-Resolution) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

