# Node Cone

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cone.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCone.html)
- geonodes name: `Cone`
- bl_idname: `GeometryNodeMeshCone`

```python
from geonodes import nodes

node = nodes.Cone(vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON')
```

### Args:

#### Input socket arguments:

- **vertices**: [Integer](Integer.md)
- **side_segments**: [Integer](Integer.md)
- **fill_segments**: [Integer](Integer.md)
- **radius_top**: [Float](Float.md)
- **radius_bottom**: [Float](Float.md)
- **depth**: [Float](Float.md)

#### Node parameter arguments:

- **fill_type** (str): default = 'NGON' in ('NONE', 'NGON', 'TRIANGLE_FAN')

### Output sockets:

- **mesh** : [Mesh](Mesh.md)
- **top** : [Boolean](Boolean.md)
- **bottom** : [Boolean](Boolean.md)
- **side** : [Boolean](Boolean.md)

## Implementation

#### class [Mesh](Mesh.md)

 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x16e378100>>](Mesh.md#Cone-staticmethod)
