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

#### class [Face](Face.md)

 - [island](Face.md#island-property)
 - [island_index](Face.md#island_index-property)
 - [island_count](Face.md#island_count-property)
#### class [Mesh](Mesh.md)

 - [island](Mesh.md#island-property)
 - [island_index](Mesh.md#island_index-property)
 - [island_count](Mesh.md#island_count-property)
