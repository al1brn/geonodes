# Node *Set Spline Type*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html)
- geonodes name: `SetSplineType`
- bl_idname: `GeometryNodeCurveSplineType`

```python
from geonodes import nodes

node = nodes.SetSplineType(curve=None, selection=None, spline_type='POLY')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveSplineType.webp)

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)
- **selection**: [Boolean](Boolean.md)

#### Node parameter arguments:

- **spline_type** (str): default = 'POLY' in ('CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS')

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Spline](Spline.md)** |
| [set_type](Spline.md#set_type) | `def set_type(self, spline_type='POLY'):` |
| [type](Spline.md#type) | `@property`<br> `def type(self):` |
| [type](Spline.md#type) | `@type.setter
`<br> `def type(self, attr_value):` |

<sub>Go to [top](#node-Set-Spline-Type) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

