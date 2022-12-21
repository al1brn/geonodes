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

#### class [Vector](Vector.md)

 - [add](Vector.md#add)
 - [subtract](Vector.md#subtract)
 - [sub](Vector.md#sub)
 - [multiply](Vector.md#multiply)
 - [mul](Vector.md#mul)
 - [divide](Vector.md#divide)
 - [div](Vector.md#div)
 - [multiply_add](Vector.md#multiply_add)
 - [mul_add](Vector.md#mul_add)
 - [cross_product](Vector.md#cross_product)
 - [cross](Vector.md#cross)
 - [project](Vector.md#project)
 - [reflect](Vector.md#reflect)
 - [refract](Vector.md#refract)
 - [face_forward](Vector.md#face_forward)
 - [dot_product](Vector.md#dot_product)
 - [dot](Vector.md#dot)
 - [distance](Vector.md#distance)
 - [length](Vector.md#length-property)
 - [scale](Vector.md#scale)
 - [normalize](Vector.md#normalize)
 - [absolute](Vector.md#absolute)
 - [abs](Vector.md#abs)
 - [minimum](Vector.md#minimum)
 - [min](Vector.md#min)
 - [maximum](Vector.md#maximum)
 - [max](Vector.md#max)
 - [floor](Vector.md#floor)
 - [ceil](Vector.md#ceil)
 - [fraction](Vector.md#fraction)
 - [fract](Vector.md#fract)
 - [modulo](Vector.md#modulo)
 - [wrap](Vector.md#wrap)
 - [snap](Vector.md#snap)
 - [sine](Vector.md#sine)
 - [sin](Vector.md#sin)
 - [cosine](Vector.md#cosine)
 - [cos](Vector.md#cos)
 - [tangent](Vector.md#tangent)
 - [tan](Vector.md#tan)
