# Node Face Neighbors

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html)
- geonodes name: `FaceNeighbors`
- bl_idname: `GeometryNodeInputMeshFaceNeighbors`

```python
from geonodes import nodes

node = nodes.FaceNeighbors()
```

### Output sockets:

- **vertex_count** : [Integer](Integer.md)
- **face_count** : [Integer](Integer.md)

## Implementation

#### [Face](Face.md)

 - [neighbors](Face.md#neighbors-property)
  ```python
  nodes.FaceNeighbors(  ```

 - [neighbors_vertex_count](Face.md#neighbors_vertex_count-property)
  ```python
  nodes.FaceNeighbors(  ```

 - [neighbors_face_count](Face.md#neighbors_face_count-property)
  ```python
  nodes.FaceNeighbors(  ```

