# Node *Gradient Texture*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)
- geonodes name: `GradientTexture`
- bl_idname: `ShaderNodeTexGradient`

```python
from geonodes import nodes

node = nodes.GradientTexture(vector=None, gradient_type='LINEAR')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

### Args:

#### Input socket arguments:

- **vector**: [Vector](Vector.md)

#### Node parameter arguments:

- **gradient_type** (str): default = 'LINEAR' in ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL')

### Output sockets:

- **color** : [Color](Color.md)
- **fac** : [Float](Float.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Texture](Texture.md)** |
| [gradient](Texture.md#gradient) | `@staticmethod`<br> `def gradient(vector=None, gradient_type='LINEAR'):` |
| [gradient_linear](Texture.md#gradient_linear) | `@staticmethod`<br> `def gradient_linear(vector=None):` |
| [gradient_quadratic](Texture.md#gradient_quadratic) | `@staticmethod`<br> `def gradient_quadratic(vector=None):` |
| [gradient_easing](Texture.md#gradient_easing) | `@staticmethod`<br> `def gradient_easing(vector=None):` |
| [gradient_diagonal](Texture.md#gradient_diagonal) | `@staticmethod`<br> `def gradient_diagonal(vector=None):` |
| [gradient_spherical](Texture.md#gradient_spherical) | `@staticmethod`<br> `def gradient_spherical(vector=None):` |
| [gradient_quadratic_sphere](Texture.md#gradient_quadratic_sphere) | `@staticmethod`<br> `def gradient_quadratic_sphere(vector=None):` |
| [gradient_radial](Texture.md#gradient_radial) | `@staticmethod`<br> `def gradient_radial(vector=None):` |

<sub>Go to [top](#node-Gradient-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

