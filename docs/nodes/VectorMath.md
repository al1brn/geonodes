
# Class VectorMath

> Geometry node name: _'Vector Math'_<br>Blender type:  **ShaderNodeVectorMath**


[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.VectorMath(vector0=None, vector1=None, vector2=None, scale=None, operation='ADD', label=None)
```


### Arguments


#### Input sockets



- **vector0** : _Vector_
- **vector1** : _Vector_
- **vector2** : _Vector_
- **scale** : _Float_



#### Parameters



- **operation** : _'ADD'_ in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT')



#### Node label



- **label** : Geometry node label



## Output sockets



- **vector** : _Vector_
- **value** : _Float_



## Data sockets

> Data socket classes implementing this node




- [Vector](../sockets/Vector.md) [absolute](../sockets/Vector.md#absolute) : Method
- [Vector](../sockets/Vector.md) [add](../sockets/Vector.md#add) : Method
- [Vector](../sockets/Vector.md) [ceil](../sockets/Vector.md#ceil) : Method
- [Vector](../sockets/Vector.md) [cos](../sockets/Vector.md#cos) : Method
- [Vector](../sockets/Vector.md) [cross](../sockets/Vector.md#cross) : Method
- [Vector](../sockets/Vector.md) [distance](../sockets/Vector.md#distance) : Method
- [Vector](../sockets/Vector.md) [divide](../sockets/Vector.md#divide) : Method
- [Vector](../sockets/Vector.md) [dot](../sockets/Vector.md#dot) : Method
- [Vector](../sockets/Vector.md) [faceforward](../sockets/Vector.md#faceforward) : Method
- [Vector](../sockets/Vector.md) [floor](../sockets/Vector.md#floor) : Method
- [Vector](../sockets/Vector.md) [fraction](../sockets/Vector.md#fraction) : Method
- [Vector](../sockets/Vector.md) [length](../sockets/Vector.md#length) : Method
- [Vector](../sockets/Vector.md) [max](../sockets/Vector.md#max) : Method
- [Vector](../sockets/Vector.md) [min](../sockets/Vector.md#min) : Method
- [Vector](../sockets/Vector.md) [modulo](../sockets/Vector.md#modulo) : Method
- [Vector](../sockets/Vector.md) [multiply](../sockets/Vector.md#multiply) : Method
- [Vector](../sockets/Vector.md) [multiply_add](../sockets/Vector.md#multiply_add) : Method
- [Vector](../sockets/Vector.md) [normalize](../sockets/Vector.md#normalize) : Method
- [Vector](../sockets/Vector.md) [project](../sockets/Vector.md#project) : Method
- [Vector](../sockets/Vector.md) [reflect](../sockets/Vector.md#reflect) : Method
- [Vector](../sockets/Vector.md) [refract](../sockets/Vector.md#refract) : Method
- [Vector](../sockets/Vector.md) [scale](../sockets/Vector.md#scale) : Method
- [Vector](../sockets/Vector.md) [sin](../sockets/Vector.md#sin) : Method
- [Vector](../sockets/Vector.md) [snap](../sockets/Vector.md#snap) : Method
- [Vector](../sockets/Vector.md) [subtract](../sockets/Vector.md#subtract) : Method
- [Vector](../sockets/Vector.md) [tan](../sockets/Vector.md#tan) : Method
- [Vector](../sockets/Vector.md) [wrap](../sockets/Vector.md#wrap) : Method
- [functions](../sockets/functions.md) [cross](../sockets/functions.md#cross) : Function
- [functions](../sockets/functions.md) [distance](../sockets/functions.md#distance) : Function
- [functions](../sockets/functions.md) [dot](../sockets/functions.md#dot) : Function
- [functions](../sockets/functions.md) [faceforward](../sockets/functions.md#faceforward) : Function
- [functions](../sockets/functions.md) [fraction](../sockets/functions.md#fraction) : Function
- [functions](../sockets/functions.md) [length](../sockets/functions.md#length) : Function
- [functions](../sockets/functions.md) [normalize](../sockets/functions.md#normalize) : Function
- [functions](../sockets/functions.md) [project](../sockets/functions.md#project) : Function
- [functions](../sockets/functions.md) [reflect](../sockets/functions.md#reflect) : Function
- [functions](../sockets/functions.md) [refract](../sockets/functions.md#refract) : Function
- [functions](../sockets/functions.md) [scale](../sockets/functions.md#scale) : Function
- [functions](../sockets/functions.md) [vector_absolute](../sockets/functions.md#vector_absolute) : Function
- [functions](../sockets/functions.md) [vector_add](../sockets/functions.md#vector_add) : Function
- [functions](../sockets/functions.md) [vector_ceil](../sockets/functions.md#vector_ceil) : Function
- [functions](../sockets/functions.md) [vector_cos](../sockets/functions.md#vector_cos) : Function
- [functions](../sockets/functions.md) [vector_divide](../sockets/functions.md#vector_divide) : Function
- [functions](../sockets/functions.md) [vector_floor](../sockets/functions.md#vector_floor) : Function
- [functions](../sockets/functions.md) [vector_max](../sockets/functions.md#vector_max) : Function
- [functions](../sockets/functions.md) [vector_min](../sockets/functions.md#vector_min) : Function
- [functions](../sockets/functions.md) [vector_modulo](../sockets/functions.md#vector_modulo) : Function
- [functions](../sockets/functions.md) [vector_multiply](../sockets/functions.md#vector_multiply) : Function
- [functions](../sockets/functions.md) [vector_multiply_add](../sockets/functions.md#vector_multiply_add) : Function
- [functions](../sockets/functions.md) [vector_sin](../sockets/functions.md#vector_sin) : Function
- [functions](../sockets/functions.md) [vector_snap](../sockets/functions.md#vector_snap) : Function
- [functions](../sockets/functions.md) [vector_subtract](../sockets/functions.md#vector_subtract) : Function
- [functions](../sockets/functions.md) [vector_tan](../sockets/functions.md#vector_tan) : Function
- [functions](../sockets/functions.md) [vector_wrap](../sockets/functions.md#vector_wrap) : Function


