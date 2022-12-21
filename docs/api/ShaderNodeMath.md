# Node Math

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
- geonodes name: `Math`
- bl_idname: `ShaderNodeMath`

```python
from geonodes import nodes

node = nodes.Math(value0=None, value1=None, value2=None, operation='ADD', use_clamp=False)
```

### Args:

#### Input socket arguments:

- **value0**: [Float](Float.md)
- **value1**: [Float](Float.md)
- **value2**: [Float](Float.md)

#### Node parameter arguments:

- **operation** (str): default = 'ADD' in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES')
- **use_clamp** (bool): default = False

### Output sockets:

- **value** : [Float](Float.md)

## Implementation

#### Global functions

 - [math](A.md#math) ```python nodes.Math(value0=value0, value1=value1, value2=value2, operation=operation, use_clamp=clamp````
 - [add](A.md#add) ```python nodes.Math(value0=value0, value1=value1, value2=None, operation='ADD', use_clamp=clamp````
 - [subtract](A.md#subtract) ```python nodes.Math(value0=value0, value1=value1, value2=None, operation='SUBTRACT', use_clamp=clamp````
 - [sub](A.md#sub) ```python nodes.Math(value0=value0, value1=value1, value2=None, operation='SUBTRACT', use_clamp=clamp````
 - [multiply](A.md#multiply) ```python nodes.Math(value0=value0, value1=value1, value2=None, operation='MULTIPLY', use_clamp=clamp````
 - [mul](A.md#mul) ```python nodes.Math(value0=value0, value1=value1, value2=None, operation='MULTIPLY', use_clamp=clamp````
 - [divide](A.md#divide) ```python nodes.Math(value0=value0, value1=value1, value2=None, operation='DIVIDE', use_clamp=clamp````
 - [div](A.md#div) ```python nodes.Math(value0=value0, value1=value1, value2=None, operation='DIVIDE', use_clamp=clamp````
 - [multiply_add](A.md#multiply_add) ```python nodes.Math(value0=value, value1=multiplier, value2=addend, operation='MULTIPLY_ADD', use_clamp=clamp````
 - [mul_add](A.md#mul_add) ```python nodes.Math(value0=value, value1=multiplier, value2=addend, operation='MULTIPLY_ADD', use_clamp=clamp````
 - [power](A.md#power) ```python nodes.Math(value0=base, value1=exponent, value2=None, operation='POWER', use_clamp=clamp````
 - [logarithm](A.md#logarithm) ```python nodes.Math(value0=value, value1=base, value2=None, operation='LOGARITHM', use_clamp=clamp````
 - [log](A.md#log) ```python nodes.Math(value0=value, value1=base, value2=None, operation='LOGARITHM', use_clamp=clamp````
 - [sqrt](A.md#sqrt) ```python nodes.Math(value0=value, value1=None, value2=None, operation='SQRT', use_clamp=clamp````
 - [inverse_sqrt](A.md#inverse_sqrt) ```python nodes.Math(value0=value, value1=None, value2=None, operation='INVERSE_SQRT', use_clamp=clamp````
 - [absolute](A.md#absolute) ```python nodes.Math(value0=value, value1=None, value2=None, operation='ABSOLUTE', use_clamp=clamp````
 - [abs](A.md#abs) ```python nodes.Math(value0=value, value1=None, value2=None, operation='ABSOLUTE', use_clamp=clamp````
 - [exponent](A.md#exponent) ```python nodes.Math(value0=value, value1=None, value2=None, operation='EXPONENT', use_clamp=clamp````
 - [exp](A.md#exp) ```python nodes.Math(value0=value, value1=None, value2=None, operation='EXPONENT', use_clamp=clamp````
 - [minimum](A.md#minimum) ```python nodes.Math(value0=value0, value1=value1, value2=None, operation='MINIMUM', use_clamp=clamp````
 - [min](A.md#min) ```python nodes.Math(value0=value0, value1=value1, value2=None, operation='MINIMUM', use_clamp=clamp````
 - [maximum](A.md#maximum) ```python nodes.Math(value0=value0, value1=value1, value2=None, operation='MAXIMUM', use_clamp=clamp````
 - [max](A.md#max) ```python nodes.Math(value0=value0, value1=value1, value2=None, operation='MAXIMUM', use_clamp=clamp````
 - [math_less_than](A.md#math_less_than) ```python nodes.Math(value0=value, value1=threshold, value2=None, operation='LESS_THAN', use_clamp=clamp````
 - [math_greater_than](A.md#math_greater_than) ```python nodes.Math(value0=value, value1=threshold, value2=None, operation='GREATER_THAN', use_clamp=clamp````
 - [sign](A.md#sign) ```python nodes.Math(value0=value, value1=None, value2=None, operation='SIGN', use_clamp=clamp````
 - [math_compare](A.md#math_compare) ```python nodes.Math(value0=value0, value1=value1, value2=epsilon, operation='COMPARE', use_clamp=clamp````
 - [smooth_minimum](A.md#smooth_minimum) ```python nodes.Math(value0=value0, value1=value1, value2=distance, operation='SMOOTH_MIN', use_clamp=clamp````
 - [smooth_maximum](A.md#smooth_maximum) ```python nodes.Math(value0=value0, value1=value1, value2=distance, operation='SMOOTH_MAX', use_clamp=clamp````
 - [math_round](A.md#math_round) ```python nodes.Math(value0=value, value1=None, value2=None, operation='ROUND', use_clamp=clamp````
 - [math_floor](A.md#math_floor) ```python nodes.Math(value0=value, value1=None, value2=None, operation='FLOOR', use_clamp=clamp````
 - [math_ceil](A.md#math_ceil) ```python nodes.Math(value0=value, value1=None, value2=None, operation='CEIL', use_clamp=clamp````
 - [math_truncate](A.md#math_truncate) ```python nodes.Math(value0=value, value1=None, value2=None, operation='TRUNC', use_clamp=clamp````
 - [math_trun](A.md#math_trun) ```python nodes.Math(value0=value, value1=None, value2=None, operation='TRUNC', use_clamp=clamp````
 - [fraction](A.md#fraction) ```python nodes.Math(value0=value, value1=None, value2=None, operation='FRACT', use_clamp=clamp````
 - [modulo](A.md#modulo) ```python nodes.Math(value0=value0, value1=value1, value2=None, operation='MODULO', use_clamp=clamp````
 - [wrap](A.md#wrap) ```python nodes.Math(value0=value, value1=max, value2=min, operation='WRAP', use_clamp=clamp````
 - [snap](A.md#snap) ```python nodes.Math(value0=value, value1=increment, value2=None, operation='SNAP', use_clamp=clamp````
 - [ping_pong](A.md#ping_pong) ```python nodes.Math(value0=value, value1=scale, value2=None, operation='PINGPONG', use_clamp=clamp````
 - [sine](A.md#sine) ```python nodes.Math(value0=value, value1=None, value2=None, operation='SINE', use_clamp=clamp````
 - [sin](A.md#sin) ```python nodes.Math(value0=value, value1=None, value2=None, operation='SINE', use_clamp=clamp````
 - [cosine](A.md#cosine) ```python nodes.Math(value0=value, value1=None, value2=None, operation='COSINE', use_clamp=clamp````
 - [cos](A.md#cos) ```python nodes.Math(value0=value, value1=None, value2=None, operation='COSINE', use_clamp=clamp````
 - [tangent](A.md#tangent) ```python nodes.Math(value0=value, value1=None, value2=None, operation='TANGENT', use_clamp=clamp````
 - [tan](A.md#tan) ```python nodes.Math(value0=value, value1=None, value2=None, operation='TANGENT', use_clamp=clamp````
 - [arcsine](A.md#arcsine) ```python nodes.Math(value0=value, value1=None, value2=None, operation='ARCSINE', use_clamp=clamp````
 - [arcsin](A.md#arcsin) ```python nodes.Math(value0=value, value1=None, value2=None, operation='ARCSINE', use_clamp=clamp````
 - [arccosine](A.md#arccosine) ```python nodes.Math(value0=value, value1=None, value2=None, operation='ARCCOSINE', use_clamp=clamp````
 - [arccos](A.md#arccos) ```python nodes.Math(value0=value, value1=None, value2=None, operation='ARCCOSINE', use_clamp=clamp````
 - [arctangent](A.md#arctangent) ```python nodes.Math(value0=value, value1=None, value2=None, operation='ARCTANGENT', use_clamp=clamp````
 - [arctan](A.md#arctan) ```python nodes.Math(value0=value, value1=None, value2=None, operation='ARCTANGENT', use_clamp=clamp````
 - [arctan2](A.md#arctan2) ```python nodes.Math(value0=value0, value1=value1, value2=None, operation='ARCTAN2', use_clamp=clamp````
 - [sinh](A.md#sinh) ```python nodes.Math(value0=value, value1=None, value2=None, operation='SINH', use_clamp=clamp````
 - [cosh](A.md#cosh) ```python nodes.Math(value0=value, value1=None, value2=None, operation='COSH', use_clamp=clamp````
 - [tanh](A.md#tanh) ```python nodes.Math(value0=value, value1=None, value2=None, operation='TANH', use_clamp=clamp````
 - [to_radians](A.md#to_radians) ```python nodes.Math(value0=value, value1=None, value2=None, operation='RADIANS', use_clamp=clamp````
 - [to_degrees](A.md#to_degrees) ```python nodes.Math(value0=value, value1=None, value2=None, operation='DEGREES', use_clamp=clamp````
#### [Float](Float.md)

 - [add](Float.md#add) ```python nodes.Math(value0=value0, value1=value1, value2=value2, operation=operation, use_clamp=clamp````
 - [subtract](Float.md#subtract) ```python nodes.Math(value0=value0, value1=value1, value2=value2, operation=operation, use_clamp=clamp````
 - [sub](Float.md#sub) ```python nodes.Math(value0=value0, value1=value1, value2=value2, operation=operation, use_clamp=clamp````
 - [multiply](Float.md#multiply) ```python nodes.Math(value0=value0, value1=value1, value2=value2, operation=operation, use_clamp=clamp````
 - [mul](Float.md#mul) ```python nodes.Math(value0=value0, value1=value1, value2=value2, operation=operation, use_clamp=clamp````
 - [divide](Float.md#divide) ```python nodes.Math(value0=value0, value1=value1, value2=value2, operation=operation, use_clamp=clamp````
 - [div](Float.md#div) ```python nodes.Math(value0=value0, value1=value1, value2=value2, operation=operation, use_clamp=clamp````
 - [multiply_add](Float.md#multiply_add) ```python nodes.Math(value0=self, value1=multiplier, value2=addend, operation='MULTIPLY_ADD', use_clamp=clamp````
 - [mul_add](Float.md#mul_add) ```python nodes.Math(value0=self, value1=multiplier, value2=addend, operation='MULTIPLY_ADD', use_clamp=clamp````
 - [power](Float.md#power) ```python nodes.Math(value0=self, value1=exponent, value2=None, operation='POWER', use_clamp=clamp````
 - [pow](Float.md#pow) ```python nodes.Math(value0=self, value1=exponent, value2=None, operation='POWER', use_clamp=clamp````
 - [logarithm](Float.md#logarithm) ```python nodes.Math(value0=self, value1=base, value2=None, operation='LOGARITHM', use_clamp=clamp````
 - [log](Float.md#log) ```python nodes.Math(value0=self, value1=base, value2=None, operation='LOGARITHM', use_clamp=clamp````
 - [sqrt](Float.md#sqrt) ```python nodes.Math(value0=self, value1=None, value2=None, operation='SQRT', use_clamp=clamp````
 - [inverse_sqrt](Float.md#inverse_sqrt) ```python nodes.Math(value0=self, value1=None, value2=None, operation='INVERSE_SQRT', use_clamp=clamp````
 - [absolute](Float.md#absolute) ```python nodes.Math(value0=self, value1=None, value2=None, operation='ABSOLUTE', use_clamp=clamp````
 - [abs](Float.md#abs) ```python nodes.Math(value0=self, value1=None, value2=None, operation='ABSOLUTE', use_clamp=clamp````
 - [exponent](Float.md#exponent) ```python nodes.Math(value0=self, value1=None, value2=None, operation='EXPONENT', use_clamp=clamp````
 - [exp](Float.md#exp) ```python nodes.Math(value0=self, value1=None, value2=None, operation='EXPONENT', use_clamp=clamp````
 - [minimum](Float.md#minimum) ```python nodes.Math(value0=self, value1=value, value2=None, operation='MINIMUM', use_clamp=clamp````
 - [min](Float.md#min) ```python nodes.Math(value0=self, value1=value, value2=None, operation='MINIMUM', use_clamp=clamp````
 - [maximum](Float.md#maximum) ```python nodes.Math(value0=self, value1=value, value2=None, operation='MAXIMUM', use_clamp=clamp````
 - [max](Float.md#max) ```python nodes.Math(value0=self, value1=value, value2=None, operation='MAXIMUM', use_clamp=clamp````
 - [math_less_than](Float.md#math_less_than) ```python nodes.Math(value0=self, value1=threshold, value2=None, operation='LESS_THAN', use_clamp=clamp````
 - [math_greater_than](Float.md#math_greater_than) ```python nodes.Math(value0=self, value1=threshold, value2=None, operation='GREATER_THAN', use_clamp=clamp````
 - [sign](Float.md#sign) ```python nodes.Math(value0=self, value1=None, value2=None, operation='SIGN', use_clamp=clamp````
 - [math_compare](Float.md#math_compare) ```python nodes.Math(value0=self, value1=value, value2=epsilon, operation='COMPARE', use_clamp=clamp````
 - [smooth_minimum](Float.md#smooth_minimum) ```python nodes.Math(value0=self, value1=value, value2=distance, operation='SMOOTH_MIN', use_clamp=clamp````
 - [smooth_maximum](Float.md#smooth_maximum) ```python nodes.Math(value0=self, value1=value, value2=distance, operation='SMOOTH_MAX', use_clamp=clamp````
 - [math_round](Float.md#math_round) ```python nodes.Math(value0=self, value1=None, value2=None, operation='ROUND', use_clamp=clamp````
 - [math_floor](Float.md#math_floor) ```python nodes.Math(value0=self, value1=None, value2=None, operation='FLOOR', use_clamp=clamp````
 - [math_ceil](Float.md#math_ceil) ```python nodes.Math(value0=self, value1=None, value2=None, operation='CEIL', use_clamp=clamp````
 - [math_truncate](Float.md#math_truncate) ```python nodes.Math(value0=self, value1=None, value2=None, operation='TRUNC', use_clamp=clamp````
 - [math_trunc](Float.md#math_trunc) ```python nodes.Math(value0=self, value1=None, value2=None, operation='TRUNC', use_clamp=clamp````
 - [fraction](Float.md#fraction) ```python nodes.Math(value0=self, value1=None, value2=None, operation='FRACT', use_clamp=clamp````
 - [fact](Float.md#fact) ```python nodes.Math(value0=self, value1=None, value2=None, operation='FRACT', use_clamp=clamp````
 - [modulo](Float.md#modulo) ```python nodes.Math(value0=self, value1=value, value2=None, operation='MODULO', use_clamp=clamp````
 - [wrap](Float.md#wrap) ```python nodes.Math(value0=self, value1=max, value2=min, operation='WRAP', use_clamp=clamp````
 - [snap](Float.md#snap) ```python nodes.Math(value0=self, value1=increment, value2=None, operation='SNAP', use_clamp=clamp````
 - [ping_pong](Float.md#ping_pong) ```python nodes.Math(value0=self, value1=scale, value2=None, operation='PINGPONG', use_clamp=clamp````
 - [sine](Float.md#sine) ```python nodes.Math(value0=self, value1=value, value2=None, operation='SINE', use_clamp=clamp````
 - [sin](Float.md#sin) ```python nodes.Math(value0=self, value1=value, value2=None, operation='SINE', use_clamp=clamp````
 - [cosine](Float.md#cosine) ```python nodes.Math(value0=self, value1=value, value2=None, operation='COSINE', use_clamp=clamp````
 - [cos](Float.md#cos) ```python nodes.Math(value0=self, value1=value, value2=None, operation='COSINE', use_clamp=clamp````
 - [tangent](Float.md#tangent) ```python nodes.Math(value0=self, value1=value, value2=None, operation='TANGENT', use_clamp=clamp````
 - [tan](Float.md#tan) ```python nodes.Math(value0=self, value1=value, value2=None, operation='TANGENT', use_clamp=clamp````
 - [arcsine](Float.md#arcsine) ```python nodes.Math(value0=self, value1=value, value2=None, operation='ARCSINE', use_clamp=clamp````
 - [arcsin](Float.md#arcsin) ```python nodes.Math(value0=self, value1=value, value2=None, operation='ARCSINE', use_clamp=clamp````
 - [arccosine](Float.md#arccosine) ```python nodes.Math(value0=self, value1=value, value2=None, operation='ARCCOSINE', use_clamp=clamp````
 - [arccos](Float.md#arccos) ```python nodes.Math(value0=self, value1=value, value2=None, operation='ARCCOSINE', use_clamp=clamp````
 - [arctangent](Float.md#arctangent) ```python nodes.Math(value0=self, value1=value, value2=None, operation='ARCTANGENT', use_clamp=clamp````
 - [arctan](Float.md#arctan) ```python nodes.Math(value0=self, value1=value, value2=None, operation='ARCTANGENT', use_clamp=clamp````
 - [arctan2](Float.md#arctan2) ```python nodes.Math(value0=self, value1=value1, value2=None, operation='ARCTAN2', use_clamp=clamp````
 - [sinh](Float.md#sinh) ```python nodes.Math(value0=self, value1=value, value2=None, operation='SINH', use_clamp=clamp````
 - [cosh](Float.md#cosh) ```python nodes.Math(value0=self, value1=value, value2=None, operation='COSH', use_clamp=clamp````
 - [tanh](Float.md#tanh) ```python nodes.Math(value0=self, value1=value, value2=None, operation='TANH', use_clamp=clamp````
 - [to_radians](Float.md#to_radians) ```python nodes.Math(value0=self, value1=None, value2=None, operation='RADIANS', use_clamp=clamp````
 - [to_degrees](Float.md#to_degrees) ```python nodes.Math(value0=self, value1=None, value2=None, operation='DEGREES', use_clamp=clamp````
#### [Integer](Integer.md)

 - [add](Integer.md#add) ```python nodes.Math(value0=value0, value1=value1, value2=value2, operation=operation, use_clamp=clamp````
 - [subtract](Integer.md#subtract) ```python nodes.Math(value0=value0, value1=value1, value2=value2, operation=operation, use_clamp=clamp````
 - [sub](Integer.md#sub) ```python nodes.Math(value0=value0, value1=value1, value2=value2, operation=operation, use_clamp=clamp````
 - [multiply](Integer.md#multiply) ```python nodes.Math(value0=value0, value1=value1, value2=value2, operation=operation, use_clamp=clamp````
 - [mul](Integer.md#mul) ```python nodes.Math(value0=value0, value1=value1, value2=value2, operation=operation, use_clamp=clamp````
 - [divide](Integer.md#divide) ```python nodes.Math(value0=value0, value1=value1, value2=value2, operation=operation, use_clamp=clamp````
 - [div](Integer.md#div) ```python nodes.Math(value0=value0, value1=value1, value2=value2, operation=operation, use_clamp=clamp````
 - [multiply_add](Integer.md#multiply_add) ```python nodes.Math(value0=self, value1=multiplier, value2=addend, operation='MULTIPLY_ADD', use_clamp=clamp````
 - [mul_add](Integer.md#mul_add) ```python nodes.Math(value0=self, value1=multiplier, value2=addend, operation='MULTIPLY_ADD', use_clamp=clamp````
 - [power](Integer.md#power) ```python nodes.Math(value0=self, value1=exponent, value2=None, operation='POWER', use_clamp=clamp````
 - [pow](Integer.md#pow) ```python nodes.Math(value0=self, value1=exponent, value2=None, operation='POWER', use_clamp=clamp````
 - [logarithm](Integer.md#logarithm) ```python nodes.Math(value0=self, value1=base, value2=None, operation='LOGARITHM', use_clamp=clamp````
 - [log](Integer.md#log) ```python nodes.Math(value0=self, value1=base, value2=None, operation='LOGARITHM', use_clamp=clamp````
 - [sqrt](Integer.md#sqrt) ```python nodes.Math(value0=self, value1=None, value2=None, operation='SQRT', use_clamp=clamp````
 - [inverse_sqrt](Integer.md#inverse_sqrt) ```python nodes.Math(value0=self, value1=None, value2=None, operation='INVERSE_SQRT', use_clamp=clamp````
 - [absolute](Integer.md#absolute) ```python nodes.Math(value0=self, value1=None, value2=None, operation='ABSOLUTE', use_clamp=clamp````
 - [abs](Integer.md#abs) ```python nodes.Math(value0=self, value1=None, value2=None, operation='ABSOLUTE', use_clamp=clamp````
 - [exponent](Integer.md#exponent) ```python nodes.Math(value0=self, value1=None, value2=None, operation='EXPONENT', use_clamp=clamp````
 - [exp](Integer.md#exp) ```python nodes.Math(value0=self, value1=None, value2=None, operation='EXPONENT', use_clamp=clamp````
 - [minimum](Integer.md#minimum) ```python nodes.Math(value0=self, value1=value, value2=None, operation='MINIMUM', use_clamp=clamp````
 - [min](Integer.md#min) ```python nodes.Math(value0=self, value1=value, value2=None, operation='MINIMUM', use_clamp=clamp````
 - [maximum](Integer.md#maximum) ```python nodes.Math(value0=self, value1=value, value2=None, operation='MAXIMUM', use_clamp=clamp````
 - [max](Integer.md#max) ```python nodes.Math(value0=self, value1=value, value2=None, operation='MAXIMUM', use_clamp=clamp````
 - [math_less_than](Integer.md#math_less_than) ```python nodes.Math(value0=self, value1=threshold, value2=None, operation='LESS_THAN', use_clamp=clamp````
 - [math_greater_than](Integer.md#math_greater_than) ```python nodes.Math(value0=self, value1=threshold, value2=None, operation='GREATER_THAN', use_clamp=clamp````
 - [sign](Integer.md#sign) ```python nodes.Math(value0=self, value1=None, value2=None, operation='SIGN', use_clamp=clamp````
 - [math_compare](Integer.md#math_compare) ```python nodes.Math(value0=self, value1=value, value2=epsilon, operation='COMPARE', use_clamp=clamp````
 - [smooth_minimum](Integer.md#smooth_minimum) ```python nodes.Math(value0=self, value1=value, value2=distance, operation='SMOOTH_MIN', use_clamp=clamp````
 - [smooth_maximum](Integer.md#smooth_maximum) ```python nodes.Math(value0=self, value1=value, value2=distance, operation='SMOOTH_MAX', use_clamp=clamp````
 - [math_round](Integer.md#math_round) ```python nodes.Math(value0=self, value1=None, value2=None, operation='ROUND', use_clamp=clamp````
 - [math_floor](Integer.md#math_floor) ```python nodes.Math(value0=self, value1=None, value2=None, operation='FLOOR', use_clamp=clamp````
 - [math_ceil](Integer.md#math_ceil) ```python nodes.Math(value0=self, value1=None, value2=None, operation='CEIL', use_clamp=clamp````
 - [math_truncate](Integer.md#math_truncate) ```python nodes.Math(value0=self, value1=None, value2=None, operation='TRUNC', use_clamp=clamp````
 - [math_trunc](Integer.md#math_trunc) ```python nodes.Math(value0=self, value1=None, value2=None, operation='TRUNC', use_clamp=clamp````
 - [fraction](Integer.md#fraction) ```python nodes.Math(value0=self, value1=None, value2=None, operation='FRACT', use_clamp=clamp````
 - [fact](Integer.md#fact) ```python nodes.Math(value0=self, value1=None, value2=None, operation='FRACT', use_clamp=clamp````
 - [modulo](Integer.md#modulo) ```python nodes.Math(value0=self, value1=value, value2=None, operation='MODULO', use_clamp=clamp````
 - [wrap](Integer.md#wrap) ```python nodes.Math(value0=self, value1=max, value2=min, operation='WRAP', use_clamp=clamp````
 - [snap](Integer.md#snap) ```python nodes.Math(value0=self, value1=increment, value2=None, operation='SNAP', use_clamp=clamp````
 - [ping_pong](Integer.md#ping_pong) ```python nodes.Math(value0=self, value1=scale, value2=None, operation='PINGPONG', use_clamp=clamp````
 - [sine](Integer.md#sine) ```python nodes.Math(value0=self, value1=value, value2=None, operation='SINE', use_clamp=clamp````
 - [sin](Integer.md#sin) ```python nodes.Math(value0=self, value1=value, value2=None, operation='SINE', use_clamp=clamp````
 - [cosine](Integer.md#cosine) ```python nodes.Math(value0=self, value1=value, value2=None, operation='COSINE', use_clamp=clamp````
 - [cos](Integer.md#cos) ```python nodes.Math(value0=self, value1=value, value2=None, operation='COSINE', use_clamp=clamp````
 - [tangent](Integer.md#tangent) ```python nodes.Math(value0=self, value1=value, value2=None, operation='TANGENT', use_clamp=clamp````
 - [tan](Integer.md#tan) ```python nodes.Math(value0=self, value1=value, value2=None, operation='TANGENT', use_clamp=clamp````
 - [arcsine](Integer.md#arcsine) ```python nodes.Math(value0=self, value1=value, value2=None, operation='ARCSINE', use_clamp=clamp````
 - [arcsin](Integer.md#arcsin) ```python nodes.Math(value0=self, value1=value, value2=None, operation='ARCSINE', use_clamp=clamp````
 - [arccosine](Integer.md#arccosine) ```python nodes.Math(value0=self, value1=value, value2=None, operation='ARCCOSINE', use_clamp=clamp````
 - [arccos](Integer.md#arccos) ```python nodes.Math(value0=self, value1=value, value2=None, operation='ARCCOSINE', use_clamp=clamp````
 - [arctangent](Integer.md#arctangent) ```python nodes.Math(value0=self, value1=value, value2=None, operation='ARCTANGENT', use_clamp=clamp````
 - [arctan](Integer.md#arctan) ```python nodes.Math(value0=self, value1=value, value2=None, operation='ARCTANGENT', use_clamp=clamp````
 - [arctan2](Integer.md#arctan2) ```python nodes.Math(value0=self, value1=value1, value2=None, operation='ARCTAN2', use_clamp=clamp````
 - [sinh](Integer.md#sinh) ```python nodes.Math(value0=self, value1=value, value2=None, operation='SINH', use_clamp=clamp````
 - [cosh](Integer.md#cosh) ```python nodes.Math(value0=self, value1=value, value2=None, operation='COSH', use_clamp=clamp````
 - [tanh](Integer.md#tanh) ```python nodes.Math(value0=self, value1=value, value2=None, operation='TANH', use_clamp=clamp````
 - [to_radians](Integer.md#to_radians) ```python nodes.Math(value0=self, value1=None, value2=None, operation='RADIANS', use_clamp=clamp````
 - [to_degrees](Integer.md#to_degrees) ```python nodes.Math(value0=self, value1=None, value2=None, operation='DEGREES', use_clamp=clamp````
