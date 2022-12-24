# Node *Cylinder*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cylinder.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCylinder.html)
- geonodes name: `Cylinder`
- bl_idname: `GeometryNodeMeshCylinder`

```python
from geonodes import nodes

node = nodes.Cylinder(vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshCylinder.webp)

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

| Class or method name | Definition |
|----------------------|------------|
| **[Mesh](Mesh.md)** |
| [Cylinder](Mesh.md#Cylinder) | `@staticmethod`<br> `def Cylinder(vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON'):` |

<sub>Go to [top](#node-Cylinder) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

