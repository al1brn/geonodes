# Node *Mesh Island*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)
- geonodes name: `MeshIsland`
- bl_idname: `GeometryNodeInputMeshIsland`

```python
from geonodes import nodes

node = nodes.MeshIsland()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshIsland.webp)

### Output sockets:

- **island_index** : [Integer](Integer.md)
- **island_count** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Face](Face.md)** |
| [island](Face.md#island) | `@property`<br> `def island(self):` |
| [island_index](Face.md#island_index) | `@property`<br> `def island_index(self):` |
| [island_count](Face.md#island_count) | `@property`<br> `def island_count(self):` |
| **[Mesh](Mesh.md)** |
| [island](Mesh.md#island) | `@property`<br> `def island(self):` |
| [island_index](Mesh.md#island_index) | `@property`<br> `def island_index(self):` |
| [island_count](Mesh.md#island_count) | `@property`<br> `def island_count(self):` |

<sub>Go to [top](#node-Mesh-Island) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

