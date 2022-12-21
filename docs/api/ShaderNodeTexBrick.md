# Node Brick Texture

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/brick.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexBrick.html)
- geonodes name: `BrickTexture`
- bl_idname: `ShaderNodeTexBrick`

```python
from geonodes import nodes

node = nodes.BrickTexture(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2)
```

#### Input socket arguments:

- vector: Vector
- color1: Color
- color2: Color
- mortar: Color
- scale: Float
- mortar_size: Float
- mortar_smooth: Float
- bias: Float
- brick_width: Float
- row_height: Float

#### Node parameter arguments:

- offset (float): Node parameter, default = 0.5
- offset_frequency (int): Node parameter, default = 2
- squash (float): Node parameter, default = 1.0
- squash_frequency (int): Node parameter, default = 2

#### Output sockets:

- **color** : Color
- **fac** : Float

