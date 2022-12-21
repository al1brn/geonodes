# Node Magic Texture

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/magic.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMagic.html)
- geonodes name: `MagicTexture`
- bl_idname: `ShaderNodeTexMagic`

```python
from geonodes import nodes

node = nodes.MagicTexture(vector=None, scale=None, distortion=None, turbulence_depth=2)
```

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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b0d60>>](Texture.md#magic-staticmethod)
