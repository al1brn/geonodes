
# Class VectorMath

> Geometry node name: _'Vector Math'_<br>Blender type:  **ShaderNodeVectorMath**

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


- [Vector](aaa). [absolute](bbb) : Method
- [Vector](aaa). [add](bbb) : Method
- [Vector](aaa). [ceil](bbb) : Method
- [Vector](aaa). [cos](bbb) : Method
- [Vector](aaa). [cross](bbb) : Method
- [Vector](aaa). [distance](bbb) : Method
- [Vector](aaa). [divide](bbb) : Method
- [Vector](aaa). [dot](bbb) : Method
- [Vector](aaa). [faceforward](bbb) : Method
- [Vector](aaa). [floor](bbb) : Method
- [Vector](aaa). [fraction](bbb) : Method
- [Vector](aaa). [length](bbb) : Method
- [Vector](aaa). [max](bbb) : Method
- [Vector](aaa). [min](bbb) : Method
- [Vector](aaa). [modulo](bbb) : Method
- [Vector](aaa). [multiply](bbb) : Method
- [Vector](aaa). [multiply_add](bbb) : Method
- [Vector](aaa). [normalize](bbb) : Method
- [Vector](aaa). [project](bbb) : Method
- [Vector](aaa). [reflect](bbb) : Method
- [Vector](aaa). [refract](bbb) : Method
- [Vector](aaa). [scale](bbb) : Method
- [Vector](aaa). [sin](bbb) : Method
- [Vector](aaa). [snap](bbb) : Method
- [Vector](aaa). [subtract](bbb) : Method
- [Vector](aaa). [tan](bbb) : Method
- [Vector](aaa). [wrap](bbb) : Method
- [functions](aaa). [cross](bbb) : Function
- [functions](aaa). [distance](bbb) : Function
- [functions](aaa). [dot](bbb) : Function
- [functions](aaa). [faceforward](bbb) : Function
- [functions](aaa). [fraction](bbb) : Function
- [functions](aaa). [length](bbb) : Function
- [functions](aaa). [normalize](bbb) : Function
- [functions](aaa). [project](bbb) : Function
- [functions](aaa). [reflect](bbb) : Function
- [functions](aaa). [refract](bbb) : Function
- [functions](aaa). [scale](bbb) : Function
- [functions](aaa). [vector_absolute](bbb) : Function
- [functions](aaa). [vector_add](bbb) : Function
- [functions](aaa). [vector_ceil](bbb) : Function
- [functions](aaa). [vector_cos](bbb) : Function
- [functions](aaa). [vector_divide](bbb) : Function
- [functions](aaa). [vector_floor](bbb) : Function
- [functions](aaa). [vector_max](bbb) : Function
- [functions](aaa). [vector_min](bbb) : Function
- [functions](aaa). [vector_modulo](bbb) : Function
- [functions](aaa). [vector_multiply](bbb) : Function
- [functions](aaa). [vector_multiply_add](bbb) : Function
- [functions](aaa). [vector_sin](bbb) : Function
- [functions](aaa). [vector_snap](bbb) : Function
- [functions](aaa). [vector_subtract](bbb) : Function
- [functions](aaa). [vector_tan](bbb) : Function
- [functions](aaa). [vector_wrap](bbb) : Function


