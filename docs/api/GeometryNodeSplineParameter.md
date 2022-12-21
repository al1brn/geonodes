# Node Spline Parameter

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)
- geonodes name: `SplineParameter`
- bl_idname: `GeometryNodeSplineParameter`

```python
from geonodes import nodes

node = nodes.SplineParameter()
```

### Output sockets:

- **factor** : [Float](Float.md)
- **length** : [Float](Float.md)
- **index** : [Integer](Integer.md)

## Implementation

### [ControlPoint](ControlPoint.md)

| Name | Definition |
|------|------------|
 | [parameter](ControlPoint.md#parameter-property) | `def parameter(self):` |
 | [parameter_factor](ControlPoint.md#parameter_factor-property) | `def parameter_factor(self):` |
 | [parameter_length](ControlPoint.md#parameter_length-property) | `def parameter_length(self):` |
 | [parameter_index](ControlPoint.md#parameter_index-property) | `def parameter_index(self):` |

