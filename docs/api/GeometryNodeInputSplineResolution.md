# Node *Spline Resolution*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_resolution.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineResolution.html)
- geonodes name: `SplineResolution`
- bl_idname: `GeometryNodeInputSplineResolution`

```python
from geonodes import nodes

node = nodes.SplineResolution()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputSplineResolution.webp)

### Output sockets:

- **resolution** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Spline](Spline.md)** |
| [resolution](Spline.md#resolution) | `@property`<br> `def resolution(self):` |

<sub>Go to [top](#node-Spline-Resolution) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

