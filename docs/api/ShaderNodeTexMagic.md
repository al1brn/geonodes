# Node *Magic Texture*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/magic.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMagic.html)
- geonodes name: `MagicTexture`
- bl_idname: `ShaderNodeTexMagic`

```python
from geonodes import nodes

node = nodes.MagicTexture(vector=None, scale=None, distortion=None, turbulence_depth=2)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexMagic.webp)

### Args:

#### Input socket arguments:

- **vector**: [Vector](Vector.md)
- **scale**: [Float](Float.md)
- **distortion**: [Float](Float.md)

#### Node parameter arguments:

- **turbulence_depth** (int): default = 2

### Output sockets:

- **color** : [Color](Color.md)
- **fac** : [Float](Float.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Texture](Texture.md)** |
| [magic](Texture.md#magic) | `@staticmethod`<br> `def magic(vector=None, scale=None, distortion=None, turbulence_depth=2):` |

<sub>Go to [top](#node-Magic-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

