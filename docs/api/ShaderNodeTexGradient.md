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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b0370>>](Texture.md#gradient-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b3cd0>>](Texture.md#gradient_linear-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b3c40>>](Texture.md#gradient_quadratic-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b0df0>>](Texture.md#gradient_easing-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b08e0>>](Texture.md#gradient_diagonal-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b1870>>](Texture.md#gradient_spherical-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b1840>>](Texture.md#gradient_quadratic_sphere-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x1683b3940>>](Texture.md#gradient_radial-staticmethod)
