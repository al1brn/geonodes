# Node *Mesh Line*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)
- geonodes name: `MeshLine`
- bl_idname: `GeometryNodeMeshLine`

```python
from geonodes import nodes

node = nodes.MeshLine(count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshLine.webp)

### Args:

#### Input socket arguments:

- **count**: [Integer](Integer.md)
- **resolution**: [Float](Float.md)
- **start_location**: [Vector](Vector.md)
- **offset**: [Vector](Vector.md)

#### Node parameter arguments:

- **count_mode** (str): default = 'TOTAL' in ('TOTAL', 'RESOLUTION')
- **mode** (str): default = 'OFFSET' in ('OFFSET', 'END_POINTS')

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Mesh](Mesh.md)** |
| [Line](Mesh.md#Line) | `@classmethod`<br> `def Line(cls, count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET'):` |
| [LineEndPoints](Mesh.md#LineEndPoints) | `@classmethod`<br> `def LineEndPoints(cls, count=None, start_location=None, end_location=None):` |
| [LineEndPointsResolution](Mesh.md#LineEndPointsResolution) | `@classmethod`<br> `def LineEndPointsResolution(cls, resolution=None, start_location=None, end_location=None):` |
| [LineOffset](Mesh.md#LineOffset) | `@classmethod`<br> `def LineOffset(cls, count=None, start_location=None, offset=None):` |

<sub>Go to [top](#node-Mesh-Line) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

