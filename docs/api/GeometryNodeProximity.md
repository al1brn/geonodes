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
| [proximity](CloudPoint.md#proximity) | `def proximity(self, target=None, source_position=None, target_element='FACES'):` |
| [proximity_points](CloudPoint.md#proximity_points) | `def proximity_points(self, target=None, source_position=None):` |
| [proximity_edges](CloudPoint.md#proximity_edges) | `def proximity_edges(self, target=None, source_position=None):` |
| [proximity_faces](CloudPoint.md#proximity_faces) | `def proximity_faces(self, target=None, source_position=None):` |
| **[ControlPoint](ControlPoint.md)** |
| [proximity](ControlPoint.md#proximity) | `def proximity(self, target=None, source_position=None, target_element='FACES'):` |
| [proximity_points](ControlPoint.md#proximity_points) | `def proximity_points(self, target=None, source_position=None):` |
| [proximity_edges](ControlPoint.md#proximity_edges) | `def proximity_edges(self, target=None, source_position=None):` |
| [proximity_faces](ControlPoint.md#proximity_faces) | `def proximity_faces(self, target=None, source_position=None):` |
| **[Curve](Curve.md)** |
| [proximity](Curve.md#proximity) | `def proximity(self, target=None, source_position=None, target_element='FACES'):` |
| [proximity_points](Curve.md#proximity_points) | `def proximity_points(self, target=None, source_position=None):` |
| [proximity_edges](Curve.md#proximity_edges) | `def proximity_edges(self, target=None, source_position=None):` |
| [proximity_faces](Curve.md#proximity_faces) | `def proximity_faces(self, target=None, source_position=None):` |
| **[Edge](Edge.md)** |
| [proximity](Edge.md#proximity) | `def proximity(self, target=None, source_position=None, target_element='FACES'):` |
| [proximity_points](Edge.md#proximity_points) | `def proximity_points(self, target=None, source_position=None):` |
| [proximity_edges](Edge.md#proximity_edges) | `def proximity_edges(self, target=None, source_position=None):` |
| [proximity_faces](Edge.md#proximity_faces) | `def proximity_faces(self, target=None, source_position=None):` |
| **[Face](Face.md)** |
| [proximity](Face.md#proximity) | `def proximity(self, target=None, source_position=None, target_element='FACES'):` |
| [proximity_points](Face.md#proximity_points) | `def proximity_points(self, target=None, source_position=None):` |
| [proximity_edges](Face.md#proximity_edges) | `def proximity_edges(self, target=None, source_position=None):` |
| [proximity_faces](Face.md#proximity_faces) | `def proximity_faces(self, target=None, source_position=None):` |
| **[Instances](Instances.md)** |
| [proximity](Instances.md#proximity) | `def proximity(self, target=None, source_position=None, target_element='FACES'):` |
| [proximity_points](Instances.md#proximity_points) | `def proximity_points(self, target=None, source_position=None):` |
| [proximity_edges](Instances.md#proximity_edges) | `def proximity_edges(self, target=None, source_position=None):` |
| [proximity_faces](Instances.md#proximity_faces) | `def proximity_faces(self, target=None, source_position=None):` |
| **[Mesh](Mesh.md)** |
| [proximity](Mesh.md#proximity) | `def proximity(self, target=None, source_position=None, target_element='FACES'):` |
| [proximity_points](Mesh.md#proximity_points) | `def proximity_points(self, target=None, source_position=None):` |
| [proximity_edges](Mesh.md#proximity_edges) | `def proximity_edges(self, target=None, source_position=None):` |
| [proximity_faces](Mesh.md#proximity_faces) | `def proximity_faces(self, target=None, source_position=None):` |
| **[Points](Points.md)** |
| [proximity](Points.md#proximity) | `def proximity(self, target=None, source_position=None, target_element='FACES'):` |
| [proximity_points](Points.md#proximity_points) | `def proximity_points(self, target=None, source_position=None):` |
| [proximity_edges](Points.md#proximity_edges) | `def proximity_edges(self, target=None, source_position=None):` |
| [proximity_faces](Points.md#proximity_faces) | `def proximity_faces(self, target=None, source_position=None):` |
| **[Vertex](Vertex.md)** |
| [proximity](Vertex.md#proximity) | `def proximity(self, target=None, source_position=None, target_element='FACES'):` |
| [proximity_points](Vertex.md#proximity_points) | `def proximity_points(self, target=None, source_position=None):` |
| [proximity_edges](Vertex.md#proximity_edges) | `def proximity_edges(self, target=None, source_position=None):` |
| [proximity_faces](Vertex.md#proximity_faces) | `def proximity_faces(self, target=None, source_position=None):` |

<sub>Go to [top](#node-Geometry-Proximity) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

