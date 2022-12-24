# Node *Separate XYZ*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/separate_xyz.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html)
- geonodes name: `SeparateXyz`
- bl_idname: `ShaderNodeSeparateXYZ`

```python
from geonodes import nodes

node = nodes.SeparateXyz(vector=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeSeparateXYZ.webp)

### Args:

#### Input socket arguments:

- **vector**: [Vector](Vector.md)

### Output sockets:

- **x** : [Float](Float.md)
- **y** : [Float](Float.md)
- **z** : [Float](Float.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Vector](Vector.md)** |
| [separate](Vector.md#separate) | `@property`<br> `def separate(self):` |

<sub>Go to [top](#node-Separate-XYZ) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

