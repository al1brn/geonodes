# Node 'Fill Curve'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)
- geonodes name: `FillCurve`
- bl_idname: `GeometryNodeFillCurve`

```python
from geonodes import nodes

node = nodes.FillCurve(curve=None, mode='TRIANGLES')
```

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)

#### Node parameter arguments:

- **mode** (str): default = 'TRIANGLES' in ('TRIANGLES', 'NGONS')

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

### [Curve](Curve.md)

| Name | Definition |
|------|------------|
 | [fill](Curve.md#fill) | `def fill(self, curve=None, mode='TRIANGLES'):` |
 | [fill_triangles](Curve.md#fill_triangles) | `def fill_triangles(self, curve=None):` |
 | [fill_ngons](Curve.md#fill_ngons) | `def fill_ngons(self, curve=None):` |

<sub>Go to [top](#node-Fill-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

