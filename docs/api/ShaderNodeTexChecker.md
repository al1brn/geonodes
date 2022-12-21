# Node Checker Texture

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/checker.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexChecker.html)
- geonodes name: `CheckerTexture`
- bl_idname: `ShaderNodeTexChecker`

```python
from geonodes import nodes

node = nodes.CheckerTexture(vector=None, color1=None, color2=None, scale=None)
```

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

### [Texture](Texture.md)

| Name | Definition |
|------|------------|
 | [checker](Texture.md#checker-staticmethod) | `def checker(vector=None, color1=None, color2=None, scale=None):` |

