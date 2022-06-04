
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


- [Float](aaa). [abs](bbb) : Method
- [Float](aaa). [add](bbb) : Method
- [Float](aaa). [arccos](bbb) : Method
- [Float](aaa). [arcsin](bbb) : Method
- [Float](aaa). [arctan](bbb) : Method
- [Float](aaa). [arctan2](bbb) : Method
- [Float](aaa). [ceil](bbb) : Method
- [Float](aaa). [compare](bbb) : Method
- [Float](aaa). [cos](bbb) : Method
- [Float](aaa). [cosh](bbb) : Method
- [Float](aaa). [degrees](bbb) : Method
- [Float](aaa). [divide](bbb) : Method
- [Float](aaa). [exp](bbb) : Method
- [Float](aaa). [floor](bbb) : Method
- [Float](aaa). [fract](bbb) : Method
- [Float](aaa). [greater_than](bbb) : Method
- [Float](aaa). [inverse_sqrt](bbb) : Method
- [Float](aaa). [less_than](bbb) : Method
- [Float](aaa). [log](bbb) : Method
- [Float](aaa). [max](bbb) : Method
- [Float](aaa). [min](bbb) : Method
- [Float](aaa). [modulo](bbb) : Method
- [Float](aaa). [multiply](bbb) : Method
- [Float](aaa). [multiply_add](bbb) : Method
- [Float](aaa). [pingpong](bbb) : Method
- [Float](aaa). [pow](bbb) : Method
- [Float](aaa). [radians](bbb) : Method
- [Float](aaa). [round](bbb) : Method
- [Float](aaa). [sign](bbb) : Method
- [Float](aaa). [sin](bbb) : Method
- [Float](aaa). [sinh](bbb) : Method
- [Float](aaa). [smooth_max](bbb) : Method
- [Float](aaa). [smooth_min](bbb) : Method
- [Float](aaa). [snap](bbb) : Method
- [Float](aaa). [sqrt](bbb) : Method
- [Float](aaa). [subtract](bbb) : Method
- [Float](aaa). [tan](bbb) : Method
- [Float](aaa). [tanh](bbb) : Method
- [Float](aaa). [trunc](bbb) : Method
- [Float](aaa). [wrap](bbb) : Method
- [Integer](aaa). [abs](bbb) : Method
- [Integer](aaa). [add](bbb) : Method
- [Integer](aaa). [arccos](bbb) : Method
- [Integer](aaa). [arcsin](bbb) : Method
- [Integer](aaa). [arctan](bbb) : Method
- [Integer](aaa). [arctan2](bbb) : Method
- [Integer](aaa). [ceil](bbb) : Method
- [Integer](aaa). [compare](bbb) : Method
- [Integer](aaa). [cos](bbb) : Method
- [Integer](aaa). [cosh](bbb) : Method
- [Integer](aaa). [degrees](bbb) : Method
- [Integer](aaa). [divide](bbb) : Method
- [Integer](aaa). [exp](bbb) : Method
- [Integer](aaa). [floor](bbb) : Method
- [Integer](aaa). [fract](bbb) : Method
- [Integer](aaa). [greater_than](bbb) : Method
- [Integer](aaa). [inverse_sqrt](bbb) : Method
- [Integer](aaa). [less_than](bbb) : Method
- [Integer](aaa). [log](bbb) : Method
- [Integer](aaa). [max](bbb) : Method
- [Integer](aaa). [min](bbb) : Method
- [Integer](aaa). [modulo](bbb) : Method
- [Integer](aaa). [multiply](bbb) : Method
- [Integer](aaa). [multiply_add](bbb) : Method
- [Integer](aaa). [pingpong](bbb) : Method
- [Integer](aaa). [pow](bbb) : Method
- [Integer](aaa). [radians](bbb) : Method
- [Integer](aaa). [round](bbb) : Method
- [Integer](aaa). [sign](bbb) : Method
- [Integer](aaa). [sin](bbb) : Method
- [Integer](aaa). [sinh](bbb) : Method
- [Integer](aaa). [smooth_max](bbb) : Method
- [Integer](aaa). [smooth_min](bbb) : Method
- [Integer](aaa). [snap](bbb) : Method
- [Integer](aaa). [sqrt](bbb) : Method
- [Integer](aaa). [subtract](bbb) : Method
- [Integer](aaa). [tan](bbb) : Method
- [Integer](aaa). [tanh](bbb) : Method
- [Integer](aaa). [trunc](bbb) : Method
- [Integer](aaa). [wrap](bbb) : Method
- [functions](aaa). [abs](bbb) : Function
- [functions](aaa). [add](bbb) : Function
- [functions](aaa). [arccos](bbb) : Function
- [functions](aaa). [arcsin](bbb) : Function
- [functions](aaa). [arctan](bbb) : Function
- [functions](aaa). [arctan2](bbb) : Function
- [functions](aaa). [ceil](bbb) : Function
- [functions](aaa). [compare](bbb) : Function
- [functions](aaa). [cos](bbb) : Function
- [functions](aaa). [cosh](bbb) : Function
- [functions](aaa). [degrees](bbb) : Function
- [functions](aaa). [divide](bbb) : Function
- [functions](aaa). [exp](bbb) : Function
- [functions](aaa). [floor](bbb) : Function
- [functions](aaa). [fract](bbb) : Function
- [functions](aaa). [greater_than](bbb) : Function
- [functions](aaa). [inverse_sqrt](bbb) : Function
- [functions](aaa). [less_than](bbb) : Function
- [functions](aaa). [log](bbb) : Function
- [functions](aaa). [max](bbb) : Function
- [functions](aaa). [min](bbb) : Function
- [functions](aaa). [modulo](bbb) : Function
- [functions](aaa). [multiply](bbb) : Function
- [functions](aaa). [multiply_add](bbb) : Function
- [functions](aaa). [pingpong](bbb) : Function
- [functions](aaa). [pow](bbb) : Function
- [functions](aaa). [radians](bbb) : Function
- [functions](aaa). [round](bbb) : Function
- [functions](aaa). [sign](bbb) : Function
- [functions](aaa). [sin](bbb) : Function
- [functions](aaa). [sinh](bbb) : Function
- [functions](aaa). [smooth_max](bbb) : Function
- [functions](aaa). [smooth_min](bbb) : Function
- [functions](aaa). [snap](bbb) : Function
- [functions](aaa). [sqrt](bbb) : Function
- [functions](aaa). [subtract](bbb) : Function
- [functions](aaa). [tan](bbb) : Function
- [functions](aaa). [tanh](bbb) : Function
- [functions](aaa). [trunc](bbb) : Function
- [functions](aaa). [wrap](bbb) : Function


