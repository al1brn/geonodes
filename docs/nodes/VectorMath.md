
# Node VectorMath

> Geometry node name: [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)<br>
  Blender type: [Vector Math](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------
        
        ```python
        from geonodes import nodes
        node = nodes.VectorMath(vector0=None, vector1=None, vector2=None, scale=None, operation='ADD', label=None)
        ```



## Arguments


### Input sockets

- vector0 : Vector
- vector1 : Vector
- vector2 : Vector
- scale : Float

### Parameters

- operation : str (default = 'ADD') in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- vector : Vector
- value : Float

## Data sockets

> Data socket classes implementing this node.
  
  
- [Vector](/docs/sockets/Vector.md).[absolute](/docs/sockets/Vector.md#absolute) : Method
- [Vector](/docs/sockets/Vector.md).[add](/docs/sockets/Vector.md#add) : Method
- [Vector](/docs/sockets/Vector.md).[ceil](/docs/sockets/Vector.md#ceil) : Method
- [Vector](/docs/sockets/Vector.md).[cos](/docs/sockets/Vector.md#cos) : Method
- [Vector](/docs/sockets/Vector.md).[cross](/docs/sockets/Vector.md#cross) : Method
- [Vector](/docs/sockets/Vector.md).[distance](/docs/sockets/Vector.md#distance) : Method
- [Vector](/docs/sockets/Vector.md).[divide](/docs/sockets/Vector.md#divide) : Method
- [Vector](/docs/sockets/Vector.md).[dot](/docs/sockets/Vector.md#dot) : Method
- [Vector](/docs/sockets/Vector.md).[faceforward](/docs/sockets/Vector.md#faceforward) : Method
- [Vector](/docs/sockets/Vector.md).[floor](/docs/sockets/Vector.md#floor) : Method
- [Vector](/docs/sockets/Vector.md).[fraction](/docs/sockets/Vector.md#fraction) : Method
- [Vector](/docs/sockets/Vector.md).[length](/docs/sockets/Vector.md#length) : Method
- [Vector](/docs/sockets/Vector.md).[max](/docs/sockets/Vector.md#max) : Method
- [Vector](/docs/sockets/Vector.md).[min](/docs/sockets/Vector.md#min) : Method
- [Vector](/docs/sockets/Vector.md).[modulo](/docs/sockets/Vector.md#modulo) : Method
- [Vector](/docs/sockets/Vector.md).[multiply](/docs/sockets/Vector.md#multiply) : Method
- [Vector](/docs/sockets/Vector.md).[multiply_add](/docs/sockets/Vector.md#multiply_add) : Method
- [Vector](/docs/sockets/Vector.md).[normalize](/docs/sockets/Vector.md#normalize) : Method
- [Vector](/docs/sockets/Vector.md).[project](/docs/sockets/Vector.md#project) : Method
- [Vector](/docs/sockets/Vector.md).[reflect](/docs/sockets/Vector.md#reflect) : Method
- [Vector](/docs/sockets/Vector.md).[refract](/docs/sockets/Vector.md#refract) : Method
- [Vector](/docs/sockets/Vector.md).[scale](/docs/sockets/Vector.md#scale) : Method
- [Vector](/docs/sockets/Vector.md).[sin](/docs/sockets/Vector.md#sin) : Method
- [Vector](/docs/sockets/Vector.md).[snap](/docs/sockets/Vector.md#snap) : Method
- [Vector](/docs/sockets/Vector.md).[subtract](/docs/sockets/Vector.md#subtract) : Method
- [Vector](/docs/sockets/Vector.md).[tan](/docs/sockets/Vector.md#tan) : Method
- [Vector](/docs/sockets/Vector.md).[wrap](/docs/sockets/Vector.md#wrap) : Method
- [functions](/docs/sockets/functions.md).[cross](/docs/sockets/functions.md#cross) : Function
- [functions](/docs/sockets/functions.md).[distance](/docs/sockets/functions.md#distance) : Function
- [functions](/docs/sockets/functions.md).[dot](/docs/sockets/functions.md#dot) : Function
- [functions](/docs/sockets/functions.md).[faceforward](/docs/sockets/functions.md#faceforward) : Function
- [functions](/docs/sockets/functions.md).[fraction](/docs/sockets/functions.md#fraction) : Function
- [functions](/docs/sockets/functions.md).[length](/docs/sockets/functions.md#length) : Function
- [functions](/docs/sockets/functions.md).[normalize](/docs/sockets/functions.md#normalize) : Function
- [functions](/docs/sockets/functions.md).[project](/docs/sockets/functions.md#project) : Function
- [functions](/docs/sockets/functions.md).[reflect](/docs/sockets/functions.md#reflect) : Function
- [functions](/docs/sockets/functions.md).[refract](/docs/sockets/functions.md#refract) : Function
- [functions](/docs/sockets/functions.md).[scale](/docs/sockets/functions.md#scale) : Function
- [functions](/docs/sockets/functions.md).[vector_absolute](/docs/sockets/functions.md#vector_absolute) : Function
- [functions](/docs/sockets/functions.md).[vector_add](/docs/sockets/functions.md#vector_add) : Function
- [functions](/docs/sockets/functions.md).[vector_ceil](/docs/sockets/functions.md#vector_ceil) : Function
- [functions](/docs/sockets/functions.md).[vector_cos](/docs/sockets/functions.md#vector_cos) : Function
- [functions](/docs/sockets/functions.md).[vector_divide](/docs/sockets/functions.md#vector_divide) : Function
- [functions](/docs/sockets/functions.md).[vector_floor](/docs/sockets/functions.md#vector_floor) : Function
- [functions](/docs/sockets/functions.md).[vector_max](/docs/sockets/functions.md#vector_max) : Function
- [functions](/docs/sockets/functions.md).[vector_min](/docs/sockets/functions.md#vector_min) : Function
- [functions](/docs/sockets/functions.md).[vector_modulo](/docs/sockets/functions.md#vector_modulo) : Function
- [functions](/docs/sockets/functions.md).[vector_multiply](/docs/sockets/functions.md#vector_multiply) : Function
- [functions](/docs/sockets/functions.md).[vector_multiply_add](/docs/sockets/functions.md#vector_multiply_add) : Function
- [functions](/docs/sockets/functions.md).[vector_sin](/docs/sockets/functions.md#vector_sin) : Function
- [functions](/docs/sockets/functions.md).[vector_snap](/docs/sockets/functions.md#vector_snap) : Function
- [functions](/docs/sockets/functions.md).[vector_subtract](/docs/sockets/functions.md#vector_subtract) : Function
- [functions](/docs/sockets/functions.md).[vector_tan](/docs/sockets/functions.md#vector_tan) : Function
- [functions](/docs/sockets/functions.md).[vector_wrap](/docs/sockets/functions.md#vector_wrap) : Function
  
