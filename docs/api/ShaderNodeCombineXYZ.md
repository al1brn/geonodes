# Node *Combine XYZ*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/combine_xyz.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineXYZ.html)
- geonodes name: `CombineXyz`
- bl_idname: `ShaderNodeCombineXYZ`

```python
from geonodes import nodes

node = nodes.CombineXyz(x=None, y=None, z=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeCombineXYZ.webp)

### Args:

#### Input socket arguments:

- **x**: [Float](Float.md)
- **y**: [Float](Float.md)
- **z**: [Float](Float.md)

### Output sockets:

- **vector** : [Vector](Vector.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Vector](Vector.md)** |
| [Combine](Vector.md#Combine) | `@classmethod`<br> `def Combine(cls, x=None, y=None, z=None):` |

<sub>Go to [top](#node-Combine-XYZ) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

