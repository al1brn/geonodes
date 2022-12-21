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

#### class [Mesh](Mesh.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x16d4f8520>>](Mesh.md#extrude)
#### class [Vertex](Vertex.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4f8490>>](Vertex.md#extrude)
#### class [Face](Face.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4f84f0>>](Face.md#extrude)
#### class [Edge](Edge.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4f84c0>>](Edge.md#extrude)
