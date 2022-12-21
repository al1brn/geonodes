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
  nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='ADD'  ```

 - [subtract](Vector.md#subtract)
  ```python
  nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='SUBTRACT'  ```

 - [sub](Vector.md#sub)
  ```python
  nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='SUBTRACT'  ```

 - [multiply](Vector.md#multiply)
  ```python
  nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='MULTIPLY'  ```

 - [mul](Vector.md#mul)
  ```python
  nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='MULTIPLY'  ```

 - [divide](Vector.md#divide)
  ```python
  nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='DIVIDE'  ```

 - [div](Vector.md#div)
  ```python
  nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='DIVIDE'  ```

 - [multiply_add](Vector.md#multiply_add)
  ```python
  nodes.VectorMath(vector0=self, vector1=multiplier, vector2=addend, scale=None, operation='MULTIPLY_ADD'  ```

 - [mul_add](Vector.md#mul_add)
  ```python
  nodes.VectorMath(vector0=self, vector1=multiplier, vector2=addend, scale=None, operation='MULTIPLY_ADD'  ```

 - [cross_product](Vector.md#cross_product)
  ```python
  nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='CROSS_PRODUCT'  ```

 - [cross](Vector.md#cross)
  ```python
  nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='CROSS_PRODUCT'  ```

 - [project](Vector.md#project)
  ```python
  nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='PROJECT'  ```

 - [reflect](Vector.md#reflect)
  ```python
  nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='REFLECT'  ```

 - [refract](Vector.md#refract)
  ```python
  nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=ior, operation='REFRACT'  ```

 - [face_forward](Vector.md#face_forward)
  ```python
  nodes.VectorMath(vector0=self, vector1=incident, vector2=reference, scale=None, operation='FACEFORWARD'  ```

 - [dot_product](Vector.md#dot_product)
  ```python
  nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='DOT_PRODUCT'  ```

 - [dot](Vector.md#dot)
  ```python
  nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='DOT_PRODUCT'  ```

 - [distance](Vector.md#distance)
  ```python
  nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='DISTANCE'  ```

 - [length](Vector.md#length-property)
  ```python
  nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='LENGTH'  ```

 - [scale](Vector.md#scale)
  ```python
  nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=scale, operation='SCALE'  ```

 - [normalize](Vector.md#normalize)
  ```python
  nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='NORMALIZE'  ```

 - [absolute](Vector.md#absolute)
  ```python
  nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='ABSOLUTE'  ```

 - [abs](Vector.md#abs)
  ```python
  nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='ABSOLUTE'  ```

 - [minimum](Vector.md#minimum)
  ```python
  nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='MINIMUM'  ```

 - [min](Vector.md#min)
  ```python
  nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='MINIMUM'  ```

 - [maximum](Vector.md#maximum)
  ```python
  nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='MAXIMUM'  ```

 - [max](Vector.md#max)
  ```python
  nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='MAXIMUM'  ```

 - [floor](Vector.md#floor)
  ```python
  nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='FLOOR'  ```

 - [ceil](Vector.md#ceil)
  ```python
  nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='CEIL'  ```

 - [fraction](Vector.md#fraction)
  ```python
  nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='FRACTION'  ```

 - [fract](Vector.md#fract)
  ```python
  nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='FRACTION'  ```

 - [modulo](Vector.md#modulo)
  ```python
  nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='MODULO'  ```

 - [wrap](Vector.md#wrap)
  ```python
  nodes.VectorMath(vector0=self, vector1=max, vector2=min, scale=None, operation='WRAP'  ```

 - [snap](Vector.md#snap)
  ```python
  nodes.VectorMath(vector0=self, vector1=increment, vector2=None, scale=None, operation='SNAP'  ```

 - [sine](Vector.md#sine)
  ```python
  nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='SINE'  ```

 - [sin](Vector.md#sin)
  ```python
  nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='SINE'  ```

 - [cosine](Vector.md#cosine)
  ```python
  nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='COSINE'  ```

 - [cos](Vector.md#cos)
  ```python
  nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='COSINE'  ```

 - [tangent](Vector.md#tangent)
  ```python
  nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='TANGENT'  ```

 - [tan](Vector.md#tan)
  ```python
  nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='TANGENT'  ```

