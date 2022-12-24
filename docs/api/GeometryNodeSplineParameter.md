# Node *Spline Parameter*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)
- geonodes name: `SplineParameter`
- bl_idname: `GeometryNodeSplineParameter`

```python
from geonodes import nodes

node = nodes.SplineParameter()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSplineParameter.webp)

### Output sockets:

- **factor** : [Float](Float.md)
- **length** : [Float](Float.md)
- **index** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[ControlPoint](ControlPoint.md)** |
| [parameter](ControlPoint.md#parameter) | `@property`<br> `def parameter(self):` |
| [parameter_factor](ControlPoint.md#parameter_factor) | `@property`<br> `def parameter_factor(self):` |
| [parameter_length](ControlPoint.md#parameter_length) | `@property`<br> `def parameter_length(self):` |
| [parameter_index](ControlPoint.md#parameter_index) | `@property`<br> `def parameter_index(self):` |

<sub>Go to [top](#node-Spline-Parameter) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

