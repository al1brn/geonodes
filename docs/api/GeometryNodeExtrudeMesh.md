# Node Extrude Mesh

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)
- geonodes name: `ExtrudeMesh`
- bl_idname: `GeometryNodeExtrudeMesh`

```python
from geonodes import nodes

node = nodes.ExtrudeMesh(mesh=None, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES')
```

### Args:

#### Input socket arguments:

- **mesh**: [Mesh](Mesh.md)
- **selection**: [Boolean](Boolean.md)
- **offset**: [Vector](Vector.md)
- **offset_scale**: [Float](Float.md)
- **individual**: [Boolean](Boolean.md)

#### Node parameter arguments:

- **mode** (str): default = 'FACES' in ('VERTICES', 'EDGES', 'FACES')

### Output sockets:

- **mesh** : [Mesh](Mesh.md)
- **top** : [Boolean](Boolean.md)
- **side** : [Boolean](Boolean.md)

## Implementation

#### class [Edge](Edge.md)

 - [extrude](Edge.md#extrude)
#### class [Face](Face.md)

 - [extrude](Face.md#extrude)
#### class [Mesh](Mesh.md)

 - [extrude](Mesh.md#extrude)
#### class [Vertex](Vertex.md)

 - [extrude](Vertex.md#extrude)
