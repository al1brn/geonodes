# Node Cylinder

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cylinder.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCylinder.html)
- geonodes name: `Cylinder`
- bl_idname: `GeometryNodeMeshCylinder`

```python
from geonodes import nodes

node = nodes.Cylinder(vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON')
```

### Args:

#### Input socket arguments:

- **vertices**: [Integer](Integer.md)
- **side_segments**: [Integer](Integer.md)
- **fill_segments**: [Integer](Integer.md)
- **radius**: [Float](Float.md)
- **depth**: [Float](Float.md)

#### Node parameter arguments:

- **fill_type** (str): default = 'NGON' in ('NONE', 'NGON', 'TRIANGLE_FAN')

### Output sockets:

- **mesh** : [Mesh](Mesh.md)
- **top** : [Boolean](Boolean.md)
- **side** : [Boolean](Boolean.md)
- **bottom** : [Boolean](Boolean.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b05b0>>](Mesh.md#Cylinder-staticmethod)
