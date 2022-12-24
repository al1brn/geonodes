# Node *Curve Line*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_line.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveLine.html)
- geonodes name: `CurveLine`
- bl_idname: `GeometryNodeCurvePrimitiveLine`

```python
from geonodes import nodes

node = nodes.CurveLine(start=None, end=None, direction=None, length=None, mode='POINTS')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurvePrimitiveLine.webp)

### Args:

#### Input socket arguments:

- **start**: [Vector](Vector.md)
- **end**: [Vector](Vector.md)
- **direction**: [Vector](Vector.md)
- **length**: [Float](Float.md)

#### Node parameter arguments:

- **mode** (str): default = 'POINTS' in ('POINTS', 'DIRECTION')

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Curve](Curve.md)** |
| [Line](Curve.md#Line) | `@classmethod`<br> `def Line(cls, start=None, end=None):` |
| [LineDirection](Curve.md#LineDirection) | `@classmethod`<br> `def LineDirection(cls, start=None, direction=None, length=None):` |

<sub>Go to [top](#node-Curve-Line) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

