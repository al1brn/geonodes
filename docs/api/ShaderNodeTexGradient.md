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
| [Gradient](Texture.md#Gradient) | `@staticmethod`<br> `def Gradient(vector=None, gradient_type='LINEAR'):` |
| [GradientLinear](Texture.md#GradientLinear) | `@staticmethod`<br> `def GradientLinear(vector=None):` |
| [GradientQuadratic](Texture.md#GradientQuadratic) | `@staticmethod`<br> `def GradientQuadratic(vector=None):` |
| [GradientEeasing](Texture.md#GradientEeasing) | `@staticmethod`<br> `def GradientEeasing(vector=None):` |
| [GradientDiagonal](Texture.md#GradientDiagonal) | `@staticmethod`<br> `def GradientDiagonal(vector=None):` |
| [GradientSpherical](Texture.md#GradientSpherical) | `@staticmethod`<br> `def GradientSpherical(vector=None):` |
| [GradientQuadratic_sphere](Texture.md#GradientQuadratic_sphere) | `@staticmethod`<br> `def GradientQuadratic_sphere(vector=None):` |
| [GradientRadial](Texture.md#GradientRadial) | `@staticmethod`<br> `def GradientRadial(vector=None):` |

<sub>Go to [top](#node-Gradient-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

