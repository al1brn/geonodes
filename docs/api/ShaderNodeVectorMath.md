# Node Vector Math

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
- geonodes name: `VectorMath`
- bl_idname: `ShaderNodeVectorMath`

```python
from geonodes import nodes

node = nodes.VectorMath(vector0=None, vector1=None, vector2=None, scale=None, operation='ADD')
```

### Args:

#### Input socket arguments:

- **vector0**: [Vector](Vector.md)
- **vector1**: [Vector](Vector.md)
- **vector2**: [Vector](Vector.md)
- **scale**: [Float](Float.md)

#### Node parameter arguments:

- **operation** (str): default = 'ADD' in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT')

### Output sockets:

- **vector** : [Vector](Vector.md)
- **value** : [Float](Float.md)

## Implementation

#### [Vector](Vector.md)

 - [add](Vector.md#add)
  ```python
  def add(self, vector=None)
  ```

 - [subtract](Vector.md#subtract)
  ```python
  def subtract(self, vector=None)
  ```

 - [sub](Vector.md#sub)
  ```python
  def sub(self, vector=None)
  ```

 - [multiply](Vector.md#multiply)
  ```python
  def multiply(self, vector=None)
  ```

 - [mul](Vector.md#mul)
  ```python
  def mul(self, vector=None)
  ```

 - [divide](Vector.md#divide)
  ```python
  def divide(self, vector=None)
  ```

 - [div](Vector.md#div)
  ```python
  def div(self, vector=None)
  ```

 - [multiply_add](Vector.md#multiply_add)
  ```python
  def multiply_add(self, multiplier=None, addend=None)
  ```

 - [mul_add](Vector.md#mul_add)
  ```python
  def mul_add(self, multiplier=None, addend=None)
  ```

 - [cross_product](Vector.md#cross_product)
  ```python
  def cross_product(self, vector=None)
  ```

 - [cross](Vector.md#cross)
  ```python
  def cross(self, vector=None)
  ```

 - [project](Vector.md#project)
  ```python
  def project(self, vector=None)
  ```

 - [reflect](Vector.md#reflect)
  ```python
  def reflect(self, vector=None)
  ```

 - [refract](Vector.md#refract)
  ```python
  def refract(self, vector=None, ior=None)
  ```

 - [face_forward](Vector.md#face_forward)
  ```python
  def face_forward(self, incident=None, reference=None)
  ```

 - [dot_product](Vector.md#dot_product)
  ```python
  def dot_product(self, vector=None)
  ```

 - [dot](Vector.md#dot)
  ```python
  def dot(self, vector=None)
  ```

 - [distance](Vector.md#distance)
  ```python
  def distance(self, vector=None)
  ```

 - [length](Vector.md#length-property)
  ```python
  def length(self)
  ```

 - [scale](Vector.md#scale)
  ```python
  def scale(self, scale=None)
  ```

 - [normalize](Vector.md#normalize)
  ```python
  def normalize(self)
  ```

 - [absolute](Vector.md#absolute)
  ```python
  def absolute(self)
  ```

 - [abs](Vector.md#abs)
  ```python
  def abs(self)
  ```

 - [minimum](Vector.md#minimum)
  ```python
  def minimum(self, vector=None)
  ```

 - [min](Vector.md#min)
  ```python
  def min(self, vector=None)
  ```

 - [maximum](Vector.md#maximum)
  ```python
  def maximum(self, vector=None)
  ```

 - [max](Vector.md#max)
  ```python
  def max(self, vector=None)
  ```

 - [floor](Vector.md#floor)
  ```python
  def floor(self)
  ```

 - [ceil](Vector.md#ceil)
  ```python
  def ceil(self)
  ```

 - [fraction](Vector.md#fraction)
  ```python
  def fraction(self)
  ```

 - [fract](Vector.md#fract)
  ```python
  def fract(self)
  ```

 - [modulo](Vector.md#modulo)
  ```python
  def modulo(self, vector=None)
  ```

 - [wrap](Vector.md#wrap)
  ```python
  def wrap(self, max=None, min=None)
  ```

 - [snap](Vector.md#snap)
  ```python
  def snap(self, increment=None)
  ```

 - [sine](Vector.md#sine)
  ```python
  def sine(self)
  ```

 - [sin](Vector.md#sin)
  ```python
  def sin(self)
  ```

 - [cosine](Vector.md#cosine)
  ```python
  def cosine(self)
  ```

 - [cos](Vector.md#cos)
  ```python
  def cos(self)
  ```

 - [tangent](Vector.md#tangent)
  ```python
  def tangent(self)
  ```

 - [tan](Vector.md#tan)
  ```python
  def tan(self)
  ```

