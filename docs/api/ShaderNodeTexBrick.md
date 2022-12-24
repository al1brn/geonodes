# Node *Brick Texture*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/brick.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexBrick.html)
- geonodes name: `BrickTexture`
- bl_idname: `ShaderNodeTexBrick`

```python
from geonodes import nodes

node = nodes.BrickTexture(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexBrick.webp)

### Args:

#### Input socket arguments:

- **vector**: [Vector](Vector.md)
- **color1**: [Color](Color.md)
- **color2**: [Color](Color.md)
- **mortar**: [Color](Color.md)
- **scale**: [Float](Float.md)
- **mortar_size**: [Float](Float.md)
- **mortar_smooth**: [Float](Float.md)
- **bias**: [Float](Float.md)
- **brick_width**: [Float](Float.md)
- **row_height**: [Float](Float.md)

#### Node parameter arguments:

- **offset** (float): default = 0.5
- **offset_frequency** (int): default = 2
- **squash** (float): default = 1.0
- **squash_frequency** (int): default = 2

### Output sockets:

- **color** : [Color](Color.md)
- **fac** : [Float](Float.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Texture](Texture.md)** |
| [brick](Texture.md#brick) | `@staticmethod`<br> `def brick(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2):` |

<sub>Go to [top](#node-Brick-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

