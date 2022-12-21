# Node 'Mesh to Points'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_points.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToPoints.html)
- geonodes name: `MeshToPoints`
- bl_idname: `GeometryNodeMeshToPoints`

```python
from geonodes import nodes

node = nodes.MeshToPoints(mesh=None, selection=None, position=None, radius=None, mode='VERTICES')
```

### Args:

#### Input socket arguments:

- **mesh**: [Mesh](Mesh.md)
- **selection**: [Boolean](Boolean.md)
- **position**: [Vector](Vector.md)
- **radius**: [Float](Float.md)

#### Node parameter arguments:

- **mode** (str): default = 'VERTICES' in ('VERTICES', 'EDGES', 'FACES', 'CORNERS')

### Output sockets:

- **points** : [Points](Points.md)

## Implementation

### [Mesh](Mesh.md)

| Name | Definition |
|------|------------|
 | [to_points](Mesh.md#to_points) | `def to_points(self, selection=None, position=None, radius=None, mode='VERTICES'):` |

### [Vertex](Vertex.md)

| Name | Definition |
|------|------------|
 | [to_points](Vertex.md#to_points) | `def to_points(self, position=None, radius=None, mode='VERTICES'):` |

<sub>Go to [top](#node-Mesh-to-Points) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

