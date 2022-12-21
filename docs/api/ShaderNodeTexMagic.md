# Node Magic Texture

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/magic.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMagic.html)
- geonodes name: `WNode`
- bl_idname: `ShaderNodeTexMagic`

```python
from geonodes import nodes

node = nodes.MagicTexture(vector=None, scale=None, distortion=None, turbulence_depth=2)
```

#### Input socket arguments:

- vector: Vector
- scale: Float
- distortion: Float

#### Node parameter arguments:

- turbulence_depth (int): Node parameter, default = 2

#### Output sockets:

- **color** : Color
- **fac** : Float

