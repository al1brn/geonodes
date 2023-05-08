# Node *Image Info*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/m.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageInfo.html)
- geonodes name: `ImageInfo`
- bl_idname: `GeometryNodeImageInfo`

```python
from geonodes import nodes

node = nodes.ImageInfo(image=None, frame=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeImageInfo.webp)

### Args:

#### Input socket arguments:

- **image**: [Image](Image.md)
- **frame**: [Integer](Integer.md)

### Output sockets:

- **width** : [Integer](Integer.md)
- **height** : [Integer](Integer.md)
- **has_alpha** : [Boolean](Boolean.md)
- **frame_count** : [Integer](Integer.md)
- **fps** : [Float](Float.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Image](Image.md)** |
| [info](Image.md#info) | `def info(self, frame=None):` |
| [width](Image.md#width) | `def width(self, frame=None):` |
| [height](Image.md#height) | `def height(self, frame=None):` |
| [has_alpha](Image.md#has_alpha) | `def has_alpha(self, frame=None):` |
| [frame_count](Image.md#frame_count) | `def frame_count(self, frame=None):` |
| [fps](Image.md#fps) | `def fps(self, frame=None):` |

<sub>Go to [top](#node-Image-Info) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

