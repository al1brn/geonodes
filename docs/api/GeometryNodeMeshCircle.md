# Node Mesh Circle

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_circle.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCircle.html)
- geonodes name: `MeshCircle`
- bl_idname: `GeometryNodeMeshCircle`

```python
from geonodes import nodes

node = nodes.MeshCircle(vertices=None, radius=None, fill_type='NONE')
```

### Args:

#### Input socket arguments:

- **vertices**: [Integer](Integer.md)
- **radius**: [Float](Float.md)

#### Node parameter arguments:

- **fill_type** (str): default = 'NONE' in ('NONE', 'NGON', 'TRIANGLE_FAN')

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Constructor object at 0x1683b3460>>](Mesh.md#Circle-classmethod)
