# Node *Mesh Boolean*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)
- geonodes name: `MeshBoolean`
- bl_idname: `GeometryNodeMeshBoolean`

```python
from geonodes import nodes

node = nodes.MeshBoolean(*mesh_2, mesh_1=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshBoolean.webp)

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

| Class or method name | Definition |
|----------------------|------------|
| **[Mesh](Mesh.md)** |
| [boolean_intersect](Mesh.md#boolean_intersect) | `def boolean_intersect(*mesh_2, self_intersection=None, hole_tolerant=None):` |
| [boolean_union](Mesh.md#boolean_union) | `def boolean_union(*mesh_2, self_intersection=None, hole_tolerant=None):` |
| [boolean_difference](Mesh.md#boolean_difference) | `def boolean_difference(self, *mesh_2, self_intersection=None, hole_tolerant=None):` |

<sub>Go to [top](#node-Mesh-Boolean) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

