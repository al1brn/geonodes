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

 - [gradient](Texture.md#gradient-staticmethod)
  ```python
  def gradient(vector=None, gradient_type='LINEAR')
  ```

 - [gradient_linear](Texture.md#gradient_linear-staticmethod)
  ```python
  def gradient_linear(vector=None)
  ```

 - [gradient_quadratic](Texture.md#gradient_quadratic-staticmethod)
  ```python
  def gradient_quadratic(vector=None)
  ```

 - [gradient_easing](Texture.md#gradient_easing-staticmethod)
  ```python
  def gradient_easing(vector=None)
  ```

 - [gradient_diagonal](Texture.md#gradient_diagonal-staticmethod)
  ```python
  def gradient_diagonal(vector=None)
  ```

 - [gradient_spherical](Texture.md#gradient_spherical-staticmethod)
  ```python
  def gradient_spherical(vector=None)
  ```

 - [gradient_quadratic_sphere](Texture.md#gradient_quadratic_sphere-staticmethod)
  ```python
  def gradient_quadratic_sphere(vector=None)
  ```

 - [gradient_radial](Texture.md#gradient_radial-staticmethod)
  ```python
  def gradient_radial(vector=None)
  ```

