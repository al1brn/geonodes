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

 - [gradient](Texture.md#gradient-staticmethod)
 - [gradient_linear](Texture.md#gradient_linear-staticmethod)
 - [gradient_quadratic](Texture.md#gradient_quadratic-staticmethod)
 - [gradient_easing](Texture.md#gradient_easing-staticmethod)
 - [gradient_diagonal](Texture.md#gradient_diagonal-staticmethod)
 - [gradient_spherical](Texture.md#gradient_spherical-staticmethod)
 - [gradient_quadratic_sphere](Texture.md#gradient_quadratic_sphere-staticmethod)
 - [gradient_radial](Texture.md#gradient_radial-staticmethod)
