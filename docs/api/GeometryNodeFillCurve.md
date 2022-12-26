# Node *Fill Curve*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)
- geonodes name: `FillCurve`
- bl_idname: `GeometryNodeFillCurve`

```python
from geonodes import nodes

node = nodes.FillCurve(curve=None, mode='TRIANGLES')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFillCurve.webp)

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)

#### Node parameter arguments:

- **mode** (str): default = 'TRIANGLES' in ('TRIANGLES', 'NGONS')

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Curve](Curve.md)** |
| [fill](Curve.md#fill) | `def fill(self, mode='TRIANGLES'):` |
| [fill_triangles](Curve.md#fill_triangles) | `def fill_triangles(self):` |
| [fill_ngons](Curve.md#fill_ngons) | `def fill_ngons(self):` |

<sub>Go to [top](#node-Fill-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

