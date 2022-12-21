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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x1683b1ae0>>](Geometry.md#delete)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1683b2740>>](Domain.md#delete)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x1683b1ff0>>](Mesh.md#delete_all)
 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x1683b20e0>>](Mesh.md#delete_edges)
 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x1683b2770>>](Mesh.md#delete_faces)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1683b1d50>>](Vertex.md#delete_all)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1683b32e0>>](Vertex.md#delete_edges)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1683b3a30>>](Vertex.md#delete_faces)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1683b2b00>>](Face.md#delete_all)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1683b2050>>](Face.md#delete_edges)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1683b3a90>>](Face.md#delete_faces)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1683b1ed0>>](Edge.md#delete_all)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1683b1e40>>](Edge.md#delete_edges)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1683b1d20>>](Edge.md#delete_faces)
