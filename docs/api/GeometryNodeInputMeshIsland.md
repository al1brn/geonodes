# Node Mesh Island

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)
- geonodes name: `MeshIsland`
- bl_idname: `GeometryNodeInputMeshIsland`

```python
from geonodes import nodes

node = nodes.MeshIsland()
```

### Output sockets:

- **island_index** : [Integer](Integer.md)
- **island_count** : [Integer](Integer.md)

## Implementation

#### class [Mesh](Mesh.md)

 - [<bound method Generator.fname of <generator.code_gen.PropAttribute object at 0x16e378a30>>](Mesh.md#island-property)
 - [<bound method Generator.fname of <generator.code_gen.PropAttribute object at 0x16e378f10>>](Mesh.md#island_index-property)
 - [<bound method Generator.fname of <generator.code_gen.PropAttribute object at 0x16e378fa0>>](Mesh.md#island_count-property)
#### class [Face](Face.md)

 - [<bound method Generator.fname of <generator.code_gen.DomPropAttribute object at 0x16e3791e0>>](Face.md#island-property)
 - [<bound method Generator.fname of <generator.code_gen.DomPropAttribute object at 0x16e379210>>](Face.md#island_index-property)
 - [<bound method Generator.fname of <generator.code_gen.DomPropAttribute object at 0x16e378e50>>](Face.md#island_count-property)
