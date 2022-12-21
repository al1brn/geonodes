# Node Pack UV Islands

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/pack_uv_islands.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVPackIslands.html)
- geonodes name: `PackUvIslands`
- bl_idname: `GeometryNodeUVPackIslands`

```python
from geonodes import nodes

node = nodes.PackUvIslands(uv=None, selection=None, margin=None, rotate=None)
```

### Args:

#### Input socket arguments:

- **uv**: [Vector](Vector.md)
- **selection**: [Boolean](Boolean.md)
- **margin**: [Float](Float.md)
- **rotate**: [Boolean](Boolean.md)

### Output sockets:

- **uv** : [Vector](Vector.md)

## Implementation

#### class [Mesh](Mesh.md)

 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x16e3df070>>](Mesh.md#pack_uv_islands)
#### class [Face](Face.md)

 - [<bound method Generator.fname of <generator.code_gen.DomAttribute object at 0x16e3dcf10>>](Face.md#pack_uv_islands)
