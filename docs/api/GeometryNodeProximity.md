# Node *Geometry Proximity*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)
- geonodes name: `GeometryProximity`
- bl_idname: `GeometryNodeProximity`

```python
from geonodes import nodes

node = nodes.GeometryProximity(target=None, source_position=None, target_element='FACES')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeProximity.webp)

### Args:

#### Input socket arguments:

- **target**: [Geometry](Geometry.md)
- **source_position**: [Vector](Vector.md)

#### Node parameter arguments:

- **target_element** (str): default = 'FACES' in ('POINTS', 'EDGES', 'FACES')

### Output sockets:

- **position** : [Vector](Vector.md)
- **distance** : [Float](Float.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[CloudPoint](CloudPoint.md)** |
| [proximity](CloudPoint.md#proximity) | `def proximity(self, target=None, source_position=None):` |
| **[ControlPoint](ControlPoint.md)** |
| [proximity](ControlPoint.md#proximity) | `def proximity(self, target=None, source_position=None):` |
| **[Edge](Edge.md)** |
| [proximity](Edge.md#proximity) | `def proximity(self, target=None, source_position=None):` |
| **[Face](Face.md)** |
| [proximity](Face.md#proximity) | `def proximity(self, target=None, source_position=None):` |
| **[Geometry](Geometry.md)** |
| [proximity](Geometry.md#proximity) | `def proximity(self, target=None, source_position=None, target_element='FACES'):` |
| [proximity_points](Geometry.md#proximity_points) | `def proximity_points(self, target=None, source_position=None):` |
| [proximity_edges](Geometry.md#proximity_edges) | `def proximity_edges(self, target=None, source_position=None):` |
| [proximity_faces](Geometry.md#proximity_faces) | `def proximity_faces(self, target=None, source_position=None):` |
| **[Vertex](Vertex.md)** |
| [proximity](Vertex.md#proximity) | `def proximity(self, target=None, source_position=None):` |

<sub>Go to [top](#node-Geometry-Proximity) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

