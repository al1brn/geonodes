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

#### [Texture](Texture.md)

 - [gradient](Texture.md#gradient-staticmethod) ```python nodes.GradientTexture(vector=vector, gradient_type=gradient_type````
 - [gradient_linear](Texture.md#gradient_linear-staticmethod) ```python nodes.GradientTexture(vector=vector, gradient_type='LINEAR'````
 - [gradient_quadratic](Texture.md#gradient_quadratic-staticmethod) ```python nodes.GradientTexture(vector=vector, gradient_type='QUADRATIC'````
 - [gradient_easing](Texture.md#gradient_easing-staticmethod) ```python nodes.GradientTexture(vector=vector, gradient_type='EASING'````
 - [gradient_diagonal](Texture.md#gradient_diagonal-staticmethod) ```python nodes.GradientTexture(vector=vector, gradient_type='DIAGONAL'````
 - [gradient_spherical](Texture.md#gradient_spherical-staticmethod) ```python nodes.GradientTexture(vector=vector, gradient_type='SPHERICAL'````
 - [gradient_quadratic_sphere](Texture.md#gradient_quadratic_sphere-staticmethod) ```python nodes.GradientTexture(vector=vector, gradient_type='QUADRATIC_SPHERE'````
 - [gradient_radial](Texture.md#gradient_radial-staticmethod) ```python nodes.GradientTexture(vector=vector, gradient_type='RADIAL'````
