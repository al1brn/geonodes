# Node Gradient Texture

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)
- geonodes name: `GradientTexture`
- bl_idname: `ShaderNodeTexGradient`

```python
from geonodes import nodes

node = nodes.GradientTexture(vector=None, gradient_type='LINEAR')
```

### Args:

#### Input socket arguments:

- **vector**: [Vector](Vector.md)

#### Node parameter arguments:

- **gradient_type** (str): default = 'LINEAR' in ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL')

### Output sockets:

- **color** : [Color](Color.md)
- **fac** : [Float](Float.md)

## Implementation

#### class [Texture](Texture.md)

 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b02b0>>](Texture.md#gradient-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b0040>>](Texture.md#gradient_linear-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b0190>>](Texture.md#gradient_quadratic-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b2bf0>>](Texture.md#gradient_easing-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b1a50>>](Texture.md#gradient_diagonal-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b31c0>>](Texture.md#gradient_spherical-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b0e80>>](Texture.md#gradient_quadratic_sphere-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b2920>>](Texture.md#gradient_radial-staticmethod)
