# Node *Spiral*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_spiral.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSpiral.html)
- geonodes name: `Spiral`
- bl_idname: `GeometryNodeCurveSpiral`

```python
from geonodes import nodes

node = nodes.Spiral(resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveSpiral.webp)

### Args:

#### Input socket arguments:

- **resolution**: [Integer](Integer.md)
- **rotations**: [Float](Float.md)
- **start_radius**: [Float](Float.md)
- **end_radius**: [Float](Float.md)
- **height**: [Float](Float.md)
- **reverse**: [Boolean](Boolean.md)

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Curve](Curve.md)** |
| [Spiral](Curve.md#Spiral) | `@classmethod`<br> `def Spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None):` |

<sub>Go to [top](#node-Spiral) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

