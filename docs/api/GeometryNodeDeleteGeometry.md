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

#### class [Geometry](Geometry.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x16d4f9d20>>](Geometry.md#delete)
#### class [Domain](Domain.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4f9c60>>](Domain.md#delete)
#### class [Mesh](Mesh.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x16d4f9cf0>>](Mesh.md#delete_all)
 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x16d4f9cc0>>](Mesh.md#delete_edges)
 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x16d4f9c90>>](Mesh.md#delete_faces)
#### class [Vertex](Vertex.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4f9c30>>](Vertex.md#delete_all)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4f9c00>>](Vertex.md#delete_edges)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4f9bd0>>](Vertex.md#delete_faces)
#### class [Face](Face.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4f9b10>>](Face.md#delete_all)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4f9ae0>>](Face.md#delete_edges)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4f9ab0>>](Face.md#delete_faces)
#### class [Edge](Edge.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4f9ba0>>](Edge.md#delete_all)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4f9b70>>](Edge.md#delete_edges)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4f9b40>>](Edge.md#delete_faces)
