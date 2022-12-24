# Node *Cone*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cone.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCone.html)
- geonodes name: `Cone`
- bl_idname: `GeometryNodeMeshCone`

```python
from geonodes import nodes

node = nodes.Cone(vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshCone.webp)

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

| Class or method name | Definition |
|----------------------|------------|
| **[Mesh](Mesh.md)** |
| [Cone](Mesh.md#Cone) | `@staticmethod`<br> `def Cone(vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON'):` |

<sub>Go to [top](#node-Cone) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

