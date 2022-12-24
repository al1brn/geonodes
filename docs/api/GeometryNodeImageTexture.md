# Node *Image Texture*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/image.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageTexture.html)
- geonodes name: `ImageTexture`
- bl_idname: `GeometryNodeImageTexture`

```python
from geonodes import nodes

node = nodes.ImageTexture(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeImageTexture.webp)

### Args:

#### Input socket arguments:

- **image**: [Image](Image.md)
- **vector**: [Vector](Vector.md)
- **frame**: [Integer](Integer.md)

#### Node parameter arguments:

- **extension** (str): default = 'REPEAT' in ('REPEAT', 'EXTEND', 'CLIP')
- **interpolation** (str): default = 'Linear' in ('Linear', 'Closest', 'Cubic')

### Output sockets:

- **color** : [Color](Color.md)
- **alpha** : [Float](Float.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Image](Image.md)** |
| [texture](Image.md#texture) | `def texture(self, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):` |
| **[Texture](Texture.md)** |
| [image](Texture.md#image) | `@staticmethod`<br> `def image(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):` |

<sub>Go to [top](#node-Image-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

