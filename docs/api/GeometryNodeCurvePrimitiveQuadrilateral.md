# Node *Quadrilateral*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/quadrilateral.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveQuadrilateral.html)
- geonodes name: `Quadrilateral`
- bl_idname: `GeometryNodeCurvePrimitiveQuadrilateral`

```python
from geonodes import nodes

node = nodes.Quadrilateral(width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurvePrimitiveQuadrilateral.webp)

### Args:

#### Input socket arguments:

- **width**: [Float](Float.md)
- **height**: [Float](Float.md)
- **bottom_width**: [Float](Float.md)
- **top_width**: [Float](Float.md)
- **offset**: [Float](Float.md)
- **bottom_height**: [Float](Float.md)
- **top_height**: [Float](Float.md)
- **point_1**: [Vector](Vector.md)
- **point_2**: [Vector](Vector.md)
- **point_3**: [Vector](Vector.md)
- **point_4**: [Vector](Vector.md)

#### Node parameter arguments:

- **mode** (str): default = 'RECTANGLE' in ('RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS')

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Curve](Curve.md)** |
| [Quadrilateral](Curve.md#Quadrilateral) | `@classmethod`<br> `def Quadrilateral(cls, width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE'):` |

<sub>Go to [top](#node-Quadrilateral) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

