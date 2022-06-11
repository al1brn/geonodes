
# Node VectorMath

> Geometry node name: [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html)<br>
  Blender type: [Vector Math](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.VectorMath(vector0=None, vector1=None, vector2=None, scale=None, operation='ADD', label=None)
```



## Arguments


### Input sockets

vector0 : Vector
- vector1 : Vector
- vector2 : Vector
- scale : Float

### Parameters

operation : str (default = 'ADD') in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

vector : Vector
- value : Float

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Vector) [absolute](section:Data socket Vector/absolute) : Method
- [class_name](section:Data socket Vector) [add](section:Data socket Vector/add) : Method
- [class_name](section:Data socket Vector) [ceil](section:Data socket Vector/ceil) : Method
- [class_name](section:Data socket Vector) [cos](section:Data socket Vector/cos) : Method
- [class_name](section:Data socket Vector) [cross](section:Data socket Vector/cross) : Method
- [class_name](section:Data socket Vector) [distance](section:Data socket Vector/distance) : Method
- [class_name](section:Data socket Vector) [divide](section:Data socket Vector/divide) : Method
- [class_name](section:Data socket Vector) [dot](section:Data socket Vector/dot) : Method
- [class_name](section:Data socket Vector) [faceforward](section:Data socket Vector/faceforward) : Method
- [class_name](section:Data socket Vector) [floor](section:Data socket Vector/floor) : Method
- [class_name](section:Data socket Vector) [fraction](section:Data socket Vector/fraction) : Method
- [class_name](section:Data socket Vector) [length](section:Data socket Vector/length) : Method
- [class_name](section:Data socket Vector) [max](section:Data socket Vector/max) : Method
- [class_name](section:Data socket Vector) [min](section:Data socket Vector/min) : Method
- [class_name](section:Data socket Vector) [modulo](section:Data socket Vector/modulo) : Method
- [class_name](section:Data socket Vector) [multiply](section:Data socket Vector/multiply) : Method
- [class_name](section:Data socket Vector) [multiply_add](section:Data socket Vector/multiply_add) : Method
- [class_name](section:Data socket Vector) [normalize](section:Data socket Vector/normalize) : Method
- [class_name](section:Data socket Vector) [project](section:Data socket Vector/project) : Method
- [class_name](section:Data socket Vector) [reflect](section:Data socket Vector/reflect) : Method
- [class_name](section:Data socket Vector) [refract](section:Data socket Vector/refract) : Method
- [class_name](section:Data socket Vector) [scale](section:Data socket Vector/scale) : Method
- [class_name](section:Data socket Vector) [sin](section:Data socket Vector/sin) : Method
- [class_name](section:Data socket Vector) [snap](section:Data socket Vector/snap) : Method
- [class_name](section:Data socket Vector) [subtract](section:Data socket Vector/subtract) : Method
- [class_name](section:Data socket Vector) [tan](section:Data socket Vector/tan) : Method
- [class_name](section:Data socket Vector) [wrap](section:Data socket Vector/wrap) : Method
- [class_name](section:Data socket functions) [cross](section:Data socket functions/cross) : Function
- [class_name](section:Data socket functions) [distance](section:Data socket functions/distance) : Function
- [class_name](section:Data socket functions) [dot](section:Data socket functions/dot) : Function
- [class_name](section:Data socket functions) [faceforward](section:Data socket functions/faceforward) : Function
- [class_name](section:Data socket functions) [fraction](section:Data socket functions/fraction) : Function
- [class_name](section:Data socket functions) [length](section:Data socket functions/length) : Function
- [class_name](section:Data socket functions) [normalize](section:Data socket functions/normalize) : Function
- [class_name](section:Data socket functions) [project](section:Data socket functions/project) : Function
- [class_name](section:Data socket functions) [reflect](section:Data socket functions/reflect) : Function
- [class_name](section:Data socket functions) [refract](section:Data socket functions/refract) : Function
- [class_name](section:Data socket functions) [scale](section:Data socket functions/scale) : Function
- [class_name](section:Data socket functions) [vector_absolute](section:Data socket functions/vector_absolute) : Function
- [class_name](section:Data socket functions) [vector_add](section:Data socket functions/vector_add) : Function
- [class_name](section:Data socket functions) [vector_ceil](section:Data socket functions/vector_ceil) : Function
- [class_name](section:Data socket functions) [vector_cos](section:Data socket functions/vector_cos) : Function
- [class_name](section:Data socket functions) [vector_divide](section:Data socket functions/vector_divide) : Function
- [class_name](section:Data socket functions) [vector_floor](section:Data socket functions/vector_floor) : Function
- [class_name](section:Data socket functions) [vector_max](section:Data socket functions/vector_max) : Function
- [class_name](section:Data socket functions) [vector_min](section:Data socket functions/vector_min) : Function
- [class_name](section:Data socket functions) [vector_modulo](section:Data socket functions/vector_modulo) : Function
- [class_name](section:Data socket functions) [vector_multiply](section:Data socket functions/vector_multiply) : Function
- [class_name](section:Data socket functions) [vector_multiply_add](section:Data socket functions/vector_multiply_add) : Function
- [class_name](section:Data socket functions) [vector_sin](section:Data socket functions/vector_sin) : Function
- [class_name](section:Data socket functions) [vector_snap](section:Data socket functions/vector_snap) : Function
- [class_name](section:Data socket functions) [vector_subtract](section:Data socket functions/vector_subtract) : Function
- [class_name](section:Data socket functions) [vector_tan](section:Data socket functions/vector_tan) : Function
- [class_name](section:Data socket functions) [vector_wrap](section:Data socket functions/vector_wrap) : Function
  
