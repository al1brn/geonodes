# Node *Checker Texture*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/checker.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexChecker.html)
- geonodes name: `CheckerTexture`
- bl_idname: `ShaderNodeTexChecker`

```python
from geonodes import nodes

node = nodes.CheckerTexture(vector=None, color1=None, color2=None, scale=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexChecker.webp)

### Args:

#### Input socket arguments:

- **vector**: [Vector](Vector.md)
- **color1**: [Color](Color.md)
- **color2**: [Color](Color.md)
- **scale**: [Float](Float.md)

### Output sockets:

- **color** : [Color](Color.md)
- **fac** : [Float](Float.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Texture](Texture.md)** |
| [checker](Texture.md#checker) | `@staticmethod`<br> `def checker(vector=None, color1=None, color2=None, scale=None):` |

<sub>Go to [top](#node-Checker-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

