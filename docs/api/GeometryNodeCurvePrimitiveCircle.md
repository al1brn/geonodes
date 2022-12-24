# Node *Curve Circle*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_circle.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveCircle.html)
- geonodes name: `CurveCircle`
- bl_idname: `GeometryNodeCurvePrimitiveCircle`

```python
from geonodes import nodes

node = nodes.CurveCircle(resolution=None, point_1=None, point_2=None, point_3=None, radius=None, mode='RADIUS')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurvePrimitiveCircle.webp)

### Args:

#### Input socket arguments:

- **resolution**: [Integer](Integer.md)
- **point_1**: [Vector](Vector.md)
- **point_2**: [Vector](Vector.md)
- **point_3**: [Vector](Vector.md)
- **radius**: [Float](Float.md)

#### Node parameter arguments:

- **mode** (str): default = 'RADIUS' in ('POINTS', 'RADIUS')

### Output sockets:

- **curve** : [Curve](Curve.md)
- **center** : [Vector](Vector.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Curve](Curve.md)** |
| [Circle](Curve.md#Circle) | `@classmethod`<br> `def Circle(cls, resolution=None, radius=None):` |
| [CircleFromPoints](Curve.md#CircleFromPoints) | `@staticmethod`<br> `def CircleFromPoints(resolution=None, point_1=None, point_2=None, point_3=None):` |

<sub>Go to [top](#node-Curve-Circle) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

