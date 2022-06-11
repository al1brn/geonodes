
# Node Math

> Geometry node name: [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html)<br>
  Blender type: [Math](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Math(value0=None, value1=None, value2=None, operation='ADD', label=None)
```



## Arguments


### Input sockets

value0 : Float
- value1 : Float
- value2 : Float

### Parameters

operation : str (default = 'ADD') in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

value : Float

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Float) [abs](section:Data socket Float/abs) : Method
- [class_name](section:Data socket Float) [add](section:Data socket Float/add) : Method
- [class_name](section:Data socket Float) [arccos](section:Data socket Float/arccos) : Method
- [class_name](section:Data socket Float) [arcsin](section:Data socket Float/arcsin) : Method
- [class_name](section:Data socket Float) [arctan](section:Data socket Float/arctan) : Method
- [class_name](section:Data socket Float) [arctan2](section:Data socket Float/arctan2) : Method
- [class_name](section:Data socket Float) [ceil](section:Data socket Float/ceil) : Method
- [class_name](section:Data socket Float) [compare](section:Data socket Float/compare) : Method
- [class_name](section:Data socket Float) [cos](section:Data socket Float/cos) : Method
- [class_name](section:Data socket Float) [cosh](section:Data socket Float/cosh) : Method
- [class_name](section:Data socket Float) [degrees](section:Data socket Float/degrees) : Method
- [class_name](section:Data socket Float) [divide](section:Data socket Float/divide) : Method
- [class_name](section:Data socket Float) [exp](section:Data socket Float/exp) : Method
- [class_name](section:Data socket Float) [floor](section:Data socket Float/floor) : Method
- [class_name](section:Data socket Float) [fract](section:Data socket Float/fract) : Method
- [class_name](section:Data socket Float) [greater_than](section:Data socket Float/greater_than) : Method
- [class_name](section:Data socket Float) [inverse_sqrt](section:Data socket Float/inverse_sqrt) : Method
- [class_name](section:Data socket Float) [less_than](section:Data socket Float/less_than) : Method
- [class_name](section:Data socket Float) [log](section:Data socket Float/log) : Method
- [class_name](section:Data socket Float) [max](section:Data socket Float/max) : Method
- [class_name](section:Data socket Float) [min](section:Data socket Float/min) : Method
- [class_name](section:Data socket Float) [modulo](section:Data socket Float/modulo) : Method
- [class_name](section:Data socket Float) [multiply](section:Data socket Float/multiply) : Method
- [class_name](section:Data socket Float) [multiply_add](section:Data socket Float/multiply_add) : Method
- [class_name](section:Data socket Float) [pingpong](section:Data socket Float/pingpong) : Method
- [class_name](section:Data socket Float) [pow](section:Data socket Float/pow) : Method
- [class_name](section:Data socket Float) [radians](section:Data socket Float/radians) : Method
- [class_name](section:Data socket Float) [round](section:Data socket Float/round) : Method
- [class_name](section:Data socket Float) [sign](section:Data socket Float/sign) : Method
- [class_name](section:Data socket Float) [sin](section:Data socket Float/sin) : Method
- [class_name](section:Data socket Float) [sinh](section:Data socket Float/sinh) : Method
- [class_name](section:Data socket Float) [smooth_max](section:Data socket Float/smooth_max) : Method
- [class_name](section:Data socket Float) [smooth_min](section:Data socket Float/smooth_min) : Method
- [class_name](section:Data socket Float) [snap](section:Data socket Float/snap) : Method
- [class_name](section:Data socket Float) [sqrt](section:Data socket Float/sqrt) : Method
- [class_name](section:Data socket Float) [subtract](section:Data socket Float/subtract) : Method
- [class_name](section:Data socket Float) [tan](section:Data socket Float/tan) : Method
- [class_name](section:Data socket Float) [tanh](section:Data socket Float/tanh) : Method
- [class_name](section:Data socket Float) [trunc](section:Data socket Float/trunc) : Method
- [class_name](section:Data socket Float) [wrap](section:Data socket Float/wrap) : Method
- [class_name](section:Data socket Integer) [abs](section:Data socket Integer/abs) : Method
- [class_name](section:Data socket Integer) [add](section:Data socket Integer/add) : Method
- [class_name](section:Data socket Integer) [arccos](section:Data socket Integer/arccos) : Method
- [class_name](section:Data socket Integer) [arcsin](section:Data socket Integer/arcsin) : Method
- [class_name](section:Data socket Integer) [arctan](section:Data socket Integer/arctan) : Method
- [class_name](section:Data socket Integer) [arctan2](section:Data socket Integer/arctan2) : Method
- [class_name](section:Data socket Integer) [ceil](section:Data socket Integer/ceil) : Method
- [class_name](section:Data socket Integer) [compare](section:Data socket Integer/compare) : Method
- [class_name](section:Data socket Integer) [cos](section:Data socket Integer/cos) : Method
- [class_name](section:Data socket Integer) [cosh](section:Data socket Integer/cosh) : Method
- [class_name](section:Data socket Integer) [degrees](section:Data socket Integer/degrees) : Method
- [class_name](section:Data socket Integer) [divide](section:Data socket Integer/divide) : Method
- [class_name](section:Data socket Integer) [exp](section:Data socket Integer/exp) : Method
- [class_name](section:Data socket Integer) [floor](section:Data socket Integer/floor) : Method
- [class_name](section:Data socket Integer) [fract](section:Data socket Integer/fract) : Method
- [class_name](section:Data socket Integer) [greater_than](section:Data socket Integer/greater_than) : Method
- [class_name](section:Data socket Integer) [inverse_sqrt](section:Data socket Integer/inverse_sqrt) : Method
- [class_name](section:Data socket Integer) [less_than](section:Data socket Integer/less_than) : Method
- [class_name](section:Data socket Integer) [log](section:Data socket Integer/log) : Method
- [class_name](section:Data socket Integer) [max](section:Data socket Integer/max) : Method
- [class_name](section:Data socket Integer) [min](section:Data socket Integer/min) : Method
- [class_name](section:Data socket Integer) [modulo](section:Data socket Integer/modulo) : Method
- [class_name](section:Data socket Integer) [multiply](section:Data socket Integer/multiply) : Method
- [class_name](section:Data socket Integer) [multiply_add](section:Data socket Integer/multiply_add) : Method
- [class_name](section:Data socket Integer) [pingpong](section:Data socket Integer/pingpong) : Method
- [class_name](section:Data socket Integer) [pow](section:Data socket Integer/pow) : Method
- [class_name](section:Data socket Integer) [radians](section:Data socket Integer/radians) : Method
- [class_name](section:Data socket Integer) [round](section:Data socket Integer/round) : Method
- [class_name](section:Data socket Integer) [sign](section:Data socket Integer/sign) : Method
- [class_name](section:Data socket Integer) [sin](section:Data socket Integer/sin) : Method
- [class_name](section:Data socket Integer) [sinh](section:Data socket Integer/sinh) : Method
- [class_name](section:Data socket Integer) [smooth_max](section:Data socket Integer/smooth_max) : Method
- [class_name](section:Data socket Integer) [smooth_min](section:Data socket Integer/smooth_min) : Method
- [class_name](section:Data socket Integer) [snap](section:Data socket Integer/snap) : Method
- [class_name](section:Data socket Integer) [sqrt](section:Data socket Integer/sqrt) : Method
- [class_name](section:Data socket Integer) [subtract](section:Data socket Integer/subtract) : Method
- [class_name](section:Data socket Integer) [tan](section:Data socket Integer/tan) : Method
- [class_name](section:Data socket Integer) [tanh](section:Data socket Integer/tanh) : Method
- [class_name](section:Data socket Integer) [trunc](section:Data socket Integer/trunc) : Method
- [class_name](section:Data socket Integer) [wrap](section:Data socket Integer/wrap) : Method
- [class_name](section:Data socket functions) [abs](section:Data socket functions/abs) : Function
- [class_name](section:Data socket functions) [add](section:Data socket functions/add) : Function
- [class_name](section:Data socket functions) [arccos](section:Data socket functions/arccos) : Function
- [class_name](section:Data socket functions) [arcsin](section:Data socket functions/arcsin) : Function
- [class_name](section:Data socket functions) [arctan](section:Data socket functions/arctan) : Function
- [class_name](section:Data socket functions) [arctan2](section:Data socket functions/arctan2) : Function
- [class_name](section:Data socket functions) [ceil](section:Data socket functions/ceil) : Function
- [class_name](section:Data socket functions) [compare](section:Data socket functions/compare) : Function
- [class_name](section:Data socket functions) [cos](section:Data socket functions/cos) : Function
- [class_name](section:Data socket functions) [cosh](section:Data socket functions/cosh) : Function
- [class_name](section:Data socket functions) [degrees](section:Data socket functions/degrees) : Function
- [class_name](section:Data socket functions) [divide](section:Data socket functions/divide) : Function
- [class_name](section:Data socket functions) [exp](section:Data socket functions/exp) : Function
- [class_name](section:Data socket functions) [floor](section:Data socket functions/floor) : Function
- [class_name](section:Data socket functions) [fract](section:Data socket functions/fract) : Function
- [class_name](section:Data socket functions) [greater_than](section:Data socket functions/greater_than) : Function
- [class_name](section:Data socket functions) [inverse_sqrt](section:Data socket functions/inverse_sqrt) : Function
- [class_name](section:Data socket functions) [less_than](section:Data socket functions/less_than) : Function
- [class_name](section:Data socket functions) [log](section:Data socket functions/log) : Function
- [class_name](section:Data socket functions) [max](section:Data socket functions/max) : Function
- [class_name](section:Data socket functions) [min](section:Data socket functions/min) : Function
- [class_name](section:Data socket functions) [modulo](section:Data socket functions/modulo) : Function
- [class_name](section:Data socket functions) [multiply](section:Data socket functions/multiply) : Function
- [class_name](section:Data socket functions) [multiply_add](section:Data socket functions/multiply_add) : Function
- [class_name](section:Data socket functions) [pingpong](section:Data socket functions/pingpong) : Function
- [class_name](section:Data socket functions) [pow](section:Data socket functions/pow) : Function
- [class_name](section:Data socket functions) [radians](section:Data socket functions/radians) : Function
- [class_name](section:Data socket functions) [round](section:Data socket functions/round) : Function
- [class_name](section:Data socket functions) [sign](section:Data socket functions/sign) : Function
- [class_name](section:Data socket functions) [sin](section:Data socket functions/sin) : Function
- [class_name](section:Data socket functions) [sinh](section:Data socket functions/sinh) : Function
- [class_name](section:Data socket functions) [smooth_max](section:Data socket functions/smooth_max) : Function
- [class_name](section:Data socket functions) [smooth_min](section:Data socket functions/smooth_min) : Function
- [class_name](section:Data socket functions) [snap](section:Data socket functions/snap) : Function
- [class_name](section:Data socket functions) [sqrt](section:Data socket functions/sqrt) : Function
- [class_name](section:Data socket functions) [subtract](section:Data socket functions/subtract) : Function
- [class_name](section:Data socket functions) [tan](section:Data socket functions/tan) : Function
- [class_name](section:Data socket functions) [tanh](section:Data socket functions/tanh) : Function
- [class_name](section:Data socket functions) [trunc](section:Data socket functions/trunc) : Function
- [class_name](section:Data socket functions) [wrap](section:Data socket functions/wrap) : Function
  
