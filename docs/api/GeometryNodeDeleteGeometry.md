# Node Delete Geometry

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

#### [Domain](Domain.md)

 - [delete](Domain.md#delete) ```python nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode=mode````
#### [Edge](Edge.md)

 - [delete_all](Edge.md#delete_all) ```python nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ALL'````
 - [delete_edges](Edge.md#delete_edges) ```python nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='EDGE_FACE'````
 - [delete_faces](Edge.md#delete_faces) ```python nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ONLY_FACE'````
#### [Face](Face.md)

 - [delete_all](Face.md#delete_all) ```python nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ALL'````
 - [delete_edges](Face.md#delete_edges) ```python nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='EDGE_FACE'````
 - [delete_faces](Face.md#delete_faces) ```python nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ONLY_FACE'````
#### [Geometry](Geometry.md)

 - [delete](Geometry.md#delete) ```python nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode=mode````
#### [Mesh](Mesh.md)

 - [delete_all](Mesh.md#delete_all) ```python nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode='ALL'````
 - [delete_edges](Mesh.md#delete_edges) ```python nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode='EDGE_FACE'````
 - [delete_faces](Mesh.md#delete_faces) ```python nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode='ONLY_FACE'````
#### [Vertex](Vertex.md)

 - [delete_all](Vertex.md#delete_all) ```python nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ALL'````
 - [delete_edges](Vertex.md#delete_edges) ```python nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='EDGE_FACE'````
 - [delete_faces](Vertex.md#delete_faces) ```python nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ONLY_FACE'````
