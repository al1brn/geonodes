
# Class Math

> Geometry node name: _'Math'_<br>Blender type:  **ShaderNodeMath**

## Initialization


```python
from geonodes import nodes
node = nodes.Math(value0=None, value1=None, value2=None, operation='ADD', label=None)
```


### Arguments


#### Input sockets



- **value0** : _Float_
- **value1** : _Float_
- **value2** : _Float_



#### Parameters



- **operation** : _'ADD'_ in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES')



#### Node label



- **label** : Geometry node label



## Output sockets



- **value** : _Float_



## Data sockets

> Data socket classes implementing this node


- [Float](../sockets/Float.md) [abs](../sockets/Float.md#abs) : Method
- [Float](../sockets/Float.md) [add](../sockets/Float.md#add) : Method
- [Float](../sockets/Float.md) [arccos](../sockets/Float.md#arccos) : Method
- [Float](../sockets/Float.md) [arcsin](../sockets/Float.md#arcsin) : Method
- [Float](../sockets/Float.md) [arctan](../sockets/Float.md#arctan) : Method
- [Float](../sockets/Float.md) [arctan2](../sockets/Float.md#arctan2) : Method
- [Float](../sockets/Float.md) [ceil](../sockets/Float.md#ceil) : Method
- [Float](../sockets/Float.md) [compare](../sockets/Float.md#compare) : Method
- [Float](../sockets/Float.md) [cos](../sockets/Float.md#cos) : Method
- [Float](../sockets/Float.md) [cosh](../sockets/Float.md#cosh) : Method
- [Float](../sockets/Float.md) [degrees](../sockets/Float.md#degrees) : Method
- [Float](../sockets/Float.md) [divide](../sockets/Float.md#divide) : Method
- [Float](../sockets/Float.md) [exp](../sockets/Float.md#exp) : Method
- [Float](../sockets/Float.md) [floor](../sockets/Float.md#floor) : Method
- [Float](../sockets/Float.md) [fract](../sockets/Float.md#fract) : Method
- [Float](../sockets/Float.md) [greater_than](../sockets/Float.md#greater_than) : Method
- [Float](../sockets/Float.md) [inverse_sqrt](../sockets/Float.md#inverse_sqrt) : Method
- [Float](../sockets/Float.md) [less_than](../sockets/Float.md#less_than) : Method
- [Float](../sockets/Float.md) [log](../sockets/Float.md#log) : Method
- [Float](../sockets/Float.md) [max](../sockets/Float.md#max) : Method
- [Float](../sockets/Float.md) [min](../sockets/Float.md#min) : Method
- [Float](../sockets/Float.md) [modulo](../sockets/Float.md#modulo) : Method
- [Float](../sockets/Float.md) [multiply](../sockets/Float.md#multiply) : Method
- [Float](../sockets/Float.md) [multiply_add](../sockets/Float.md#multiply_add) : Method
- [Float](../sockets/Float.md) [pingpong](../sockets/Float.md#pingpong) : Method
- [Float](../sockets/Float.md) [pow](../sockets/Float.md#pow) : Method
- [Float](../sockets/Float.md) [radians](../sockets/Float.md#radians) : Method
- [Float](../sockets/Float.md) [round](../sockets/Float.md#round) : Method
- [Float](../sockets/Float.md) [sign](../sockets/Float.md#sign) : Method
- [Float](../sockets/Float.md) [sin](../sockets/Float.md#sin) : Method
- [Float](../sockets/Float.md) [sinh](../sockets/Float.md#sinh) : Method
- [Float](../sockets/Float.md) [smooth_max](../sockets/Float.md#smooth_max) : Method
- [Float](../sockets/Float.md) [smooth_min](../sockets/Float.md#smooth_min) : Method
- [Float](../sockets/Float.md) [snap](../sockets/Float.md#snap) : Method
- [Float](../sockets/Float.md) [sqrt](../sockets/Float.md#sqrt) : Method
- [Float](../sockets/Float.md) [subtract](../sockets/Float.md#subtract) : Method
- [Float](../sockets/Float.md) [tan](../sockets/Float.md#tan) : Method
- [Float](../sockets/Float.md) [tanh](../sockets/Float.md#tanh) : Method
- [Float](../sockets/Float.md) [trunc](../sockets/Float.md#trunc) : Method
- [Float](../sockets/Float.md) [wrap](../sockets/Float.md#wrap) : Method
- [Integer](../sockets/Integer.md) [abs](../sockets/Integer.md#abs) : Method
- [Integer](../sockets/Integer.md) [add](../sockets/Integer.md#add) : Method
- [Integer](../sockets/Integer.md) [arccos](../sockets/Integer.md#arccos) : Method
- [Integer](../sockets/Integer.md) [arcsin](../sockets/Integer.md#arcsin) : Method
- [Integer](../sockets/Integer.md) [arctan](../sockets/Integer.md#arctan) : Method
- [Integer](../sockets/Integer.md) [arctan2](../sockets/Integer.md#arctan2) : Method
- [Integer](../sockets/Integer.md) [ceil](../sockets/Integer.md#ceil) : Method
- [Integer](../sockets/Integer.md) [compare](../sockets/Integer.md#compare) : Method
- [Integer](../sockets/Integer.md) [cos](../sockets/Integer.md#cos) : Method
- [Integer](../sockets/Integer.md) [cosh](../sockets/Integer.md#cosh) : Method
- [Integer](../sockets/Integer.md) [degrees](../sockets/Integer.md#degrees) : Method
- [Integer](../sockets/Integer.md) [divide](../sockets/Integer.md#divide) : Method
- [Integer](../sockets/Integer.md) [exp](../sockets/Integer.md#exp) : Method
- [Integer](../sockets/Integer.md) [floor](../sockets/Integer.md#floor) : Method
- [Integer](../sockets/Integer.md) [fract](../sockets/Integer.md#fract) : Method
- [Integer](../sockets/Integer.md) [greater_than](../sockets/Integer.md#greater_than) : Method
- [Integer](../sockets/Integer.md) [inverse_sqrt](../sockets/Integer.md#inverse_sqrt) : Method
- [Integer](../sockets/Integer.md) [less_than](../sockets/Integer.md#less_than) : Method
- [Integer](../sockets/Integer.md) [log](../sockets/Integer.md#log) : Method
- [Integer](../sockets/Integer.md) [max](../sockets/Integer.md#max) : Method
- [Integer](../sockets/Integer.md) [min](../sockets/Integer.md#min) : Method
- [Integer](../sockets/Integer.md) [modulo](../sockets/Integer.md#modulo) : Method
- [Integer](../sockets/Integer.md) [multiply](../sockets/Integer.md#multiply) : Method
- [Integer](../sockets/Integer.md) [multiply_add](../sockets/Integer.md#multiply_add) : Method
- [Integer](../sockets/Integer.md) [pingpong](../sockets/Integer.md#pingpong) : Method
- [Integer](../sockets/Integer.md) [pow](../sockets/Integer.md#pow) : Method
- [Integer](../sockets/Integer.md) [radians](../sockets/Integer.md#radians) : Method
- [Integer](../sockets/Integer.md) [round](../sockets/Integer.md#round) : Method
- [Integer](../sockets/Integer.md) [sign](../sockets/Integer.md#sign) : Method
- [Integer](../sockets/Integer.md) [sin](../sockets/Integer.md#sin) : Method
- [Integer](../sockets/Integer.md) [sinh](../sockets/Integer.md#sinh) : Method
- [Integer](../sockets/Integer.md) [smooth_max](../sockets/Integer.md#smooth_max) : Method
- [Integer](../sockets/Integer.md) [smooth_min](../sockets/Integer.md#smooth_min) : Method
- [Integer](../sockets/Integer.md) [snap](../sockets/Integer.md#snap) : Method
- [Integer](../sockets/Integer.md) [sqrt](../sockets/Integer.md#sqrt) : Method
- [Integer](../sockets/Integer.md) [subtract](../sockets/Integer.md#subtract) : Method
- [Integer](../sockets/Integer.md) [tan](../sockets/Integer.md#tan) : Method
- [Integer](../sockets/Integer.md) [tanh](../sockets/Integer.md#tanh) : Method
- [Integer](../sockets/Integer.md) [trunc](../sockets/Integer.md#trunc) : Method
- [Integer](../sockets/Integer.md) [wrap](../sockets/Integer.md#wrap) : Method
- [functions](../sockets/functions.md) [abs](../sockets/functions.md#abs) : Function
- [functions](../sockets/functions.md) [add](../sockets/functions.md#add) : Function
- [functions](../sockets/functions.md) [arccos](../sockets/functions.md#arccos) : Function
- [functions](../sockets/functions.md) [arcsin](../sockets/functions.md#arcsin) : Function
- [functions](../sockets/functions.md) [arctan](../sockets/functions.md#arctan) : Function
- [functions](../sockets/functions.md) [arctan2](../sockets/functions.md#arctan2) : Function
- [functions](../sockets/functions.md) [ceil](../sockets/functions.md#ceil) : Function
- [functions](../sockets/functions.md) [compare](../sockets/functions.md#compare) : Function
- [functions](../sockets/functions.md) [cos](../sockets/functions.md#cos) : Function
- [functions](../sockets/functions.md) [cosh](../sockets/functions.md#cosh) : Function
- [functions](../sockets/functions.md) [degrees](../sockets/functions.md#degrees) : Function
- [functions](../sockets/functions.md) [divide](../sockets/functions.md#divide) : Function
- [functions](../sockets/functions.md) [exp](../sockets/functions.md#exp) : Function
- [functions](../sockets/functions.md) [floor](../sockets/functions.md#floor) : Function
- [functions](../sockets/functions.md) [fract](../sockets/functions.md#fract) : Function
- [functions](../sockets/functions.md) [greater_than](../sockets/functions.md#greater_than) : Function
- [functions](../sockets/functions.md) [inverse_sqrt](../sockets/functions.md#inverse_sqrt) : Function
- [functions](../sockets/functions.md) [less_than](../sockets/functions.md#less_than) : Function
- [functions](../sockets/functions.md) [log](../sockets/functions.md#log) : Function
- [functions](../sockets/functions.md) [max](../sockets/functions.md#max) : Function
- [functions](../sockets/functions.md) [min](../sockets/functions.md#min) : Function
- [functions](../sockets/functions.md) [modulo](../sockets/functions.md#modulo) : Function
- [functions](../sockets/functions.md) [multiply](../sockets/functions.md#multiply) : Function
- [functions](../sockets/functions.md) [multiply_add](../sockets/functions.md#multiply_add) : Function
- [functions](../sockets/functions.md) [pingpong](../sockets/functions.md#pingpong) : Function
- [functions](../sockets/functions.md) [pow](../sockets/functions.md#pow) : Function
- [functions](../sockets/functions.md) [radians](../sockets/functions.md#radians) : Function
- [functions](../sockets/functions.md) [round](../sockets/functions.md#round) : Function
- [functions](../sockets/functions.md) [sign](../sockets/functions.md#sign) : Function
- [functions](../sockets/functions.md) [sin](../sockets/functions.md#sin) : Function
- [functions](../sockets/functions.md) [sinh](../sockets/functions.md#sinh) : Function
- [functions](../sockets/functions.md) [smooth_max](../sockets/functions.md#smooth_max) : Function
- [functions](../sockets/functions.md) [smooth_min](../sockets/functions.md#smooth_min) : Function
- [functions](../sockets/functions.md) [snap](../sockets/functions.md#snap) : Function
- [functions](../sockets/functions.md) [sqrt](../sockets/functions.md#sqrt) : Function
- [functions](../sockets/functions.md) [subtract](../sockets/functions.md#subtract) : Function
- [functions](../sockets/functions.md) [tan](../sockets/functions.md#tan) : Function
- [functions](../sockets/functions.md) [tanh](../sockets/functions.md#tanh) : Function
- [functions](../sockets/functions.md) [trunc](../sockets/functions.md#trunc) : Function
- [functions](../sockets/functions.md) [wrap](../sockets/functions.md#wrap) : Function


