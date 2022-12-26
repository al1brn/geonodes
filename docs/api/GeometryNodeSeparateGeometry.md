# Node *Separate Geometry*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)
- geonodes name: `SeparateGeometry`
- bl_idname: `GeometryNodeSeparateGeometry`

```python
from geonodes import nodes

node = nodes.SeparateGeometry(geometry=None, selection=None, domain='POINT')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)

#### Node parameter arguments:

- **domain** (str): default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

### Output sockets:

- **selection** : [Geometry](Geometry.md)
- **inverted** : [Geometry](Geometry.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[ControlPoint](ControlPoint.md)** |
| [separate](ControlPoint.md#separate) | `def separate(self):` |
| **[Edge](Edge.md)** |
| [separate](Edge.md#separate) | `def separate(self):` |
| **[Face](Face.md)** |
| [separate](Face.md#separate) | `def separate(self):` |
| **[Geometry](Geometry.md)** |
| [separate](Geometry.md#separate) | `def separate(self, selection=None, domain='POINT'):` |
| **[Instance](Instance.md)** |
| [separate](Instance.md#separate) | `def separate(self):` |
| **[Spline](Spline.md)** |
| [separate](Spline.md#separate) | `def separate(self):` |
| **[Vertex](Vertex.md)** |
| [separate](Vertex.md#separate) | `def separate(self):` |

<sub>Go to [top](#node-Separate-Geometry) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

