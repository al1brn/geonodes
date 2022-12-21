# Node Mesh Boolean

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)
- geonodes name: `MeshBoolean`
- bl_idname: `GeometryNodeMeshBoolean`

```python
from geonodes import nodes

node = nodes.MeshBoolean(*mesh_2, mesh_1=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE')
```

### Args:

#### Input socket arguments:

- **mesh_1**: [Geometry](Geometry.md)
- **mesh_2**: *[Geometry](Geometry.md)
- **self_intersection**: [Boolean](Boolean.md)
- **hole_tolerant**: [Boolean](Boolean.md)

#### Node parameter arguments:

- **operation** (str): default = 'DIFFERENCE' in ('INTERSECT', 'UNION', 'DIFFERENCE')

### Output sockets:

- **mesh** : [Mesh](Mesh.md)
- **intersecting_edges** : [Boolean](Boolean.md)

## Implementation

#### [Mesh](Mesh.md)

 - [boolean_intersect](Mesh.md#boolean_intersect)
  ```python
  nodes.MeshBoolean(*mesh_2, mesh_1=None, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='INTERSECT'  ```

 - [boolean_union](Mesh.md#boolean_union)
  ```python
  nodes.MeshBoolean(*mesh_2, mesh_1=None, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='UNION'  ```

 - [boolean_difference](Mesh.md#boolean_difference)
  ```python
  nodes.MeshBoolean(*mesh_2, mesh_1=self, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='DIFFERENCE'  ```

