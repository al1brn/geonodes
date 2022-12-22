# Node *Sample Nearest*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_nearest.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html)
- geonodes name: `SampleNearest`
- bl_idname: `GeometryNodeSampleNearest`

```python
from geonodes import nodes

node = nodes.SampleNearest(geometry=None, sample_position=None, domain='POINT')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleNearest.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **sample_position**: [Vector](Vector.md)

#### Node parameter arguments:

- **domain** (str): default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER')

### Output sockets:

- **index** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Corner](Corner.md)** |
| [sample_nearest](Corner.md#sample_nearest) | `def sample_nearest(self, sample_position=None):` |
| **[Edge](Edge.md)** |
| [sample_nearest](Edge.md#sample_nearest) | `def sample_nearest(self, sample_position=None):` |
| **[Face](Face.md)** |
| [sample_nearest](Face.md#sample_nearest) | `def sample_nearest(self, sample_position=None):` |
| **[Geometry](Geometry.md)** |
| [sample_nearest](Geometry.md#sample_nearest) | `def sample_nearest(self, sample_position=None, domain='POINT'):` |
| **[Vertex](Vertex.md)** |
| [sample_nearest](Vertex.md#sample_nearest) | `def sample_nearest(self, sample_position=None):` |

<sub>Go to [top](#node-Sample-Nearest) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

