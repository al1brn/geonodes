# Node 'Delete Geometry'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)
- geonodes name: `DeleteGeometry`
- bl_idname: `GeometryNodeDeleteGeometry`

```python
from geonodes import nodes

node = nodes.DeleteGeometry(geometry=None, selection=None, domain='POINT', mode='ALL')
```

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)

#### Node parameter arguments:

- **domain** (str): default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')
- **mode** (str): default = 'ALL' in ('ALL', 'EDGE_FACE', 'ONLY_FACE')

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

### [Domain](Domain.md)

| Name | Definition |
|------|------------|
 | [delete](Domain.md#delete) | `def delete(self, mode='ALL'):` |

### [Edge](Edge.md)

| Name | Definition |
|------|------------|
 | [delete_all](Edge.md#delete_all) | `def delete_all(self):` |
 | [delete_edges](Edge.md#delete_edges) | `def delete_edges(self):` |
 | [delete_faces](Edge.md#delete_faces) | `def delete_faces(self):` |

### [Face](Face.md)

| Name | Definition |
|------|------------|
 | [delete_all](Face.md#delete_all) | `def delete_all(self):` |
 | [delete_edges](Face.md#delete_edges) | `def delete_edges(self):` |
 | [delete_faces](Face.md#delete_faces) | `def delete_faces(self):` |

### [Geometry](Geometry.md)

| Name | Definition |
|------|------------|
 | [delete](Geometry.md#delete) | `def delete(self, selection=None, domain='POINT', mode='ALL'):` |

### [Mesh](Mesh.md)

| Name | Definition |
|------|------------|
 | [delete_all](Mesh.md#delete_all) | `def delete_all(self, selection=None, domain='POINT'):` |
 | [delete_edges](Mesh.md#delete_edges) | `def delete_edges(self, selection=None, domain='POINT'):` |
 | [delete_faces](Mesh.md#delete_faces) | `def delete_faces(self, selection=None, domain='POINT'):` |

### [Vertex](Vertex.md)

| Name | Definition |
|------|------------|
 | [delete_all](Vertex.md#delete_all) | `def delete_all(self):` |
 | [delete_edges](Vertex.md#delete_edges) | `def delete_edges(self):` |
 | [delete_faces](Vertex.md#delete_faces) | `def delete_faces(self):` |

<sub>Go to [top](#node-{wnode.bnode.name}) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

