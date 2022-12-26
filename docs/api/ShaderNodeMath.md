# Node *Math*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
- geonodes name: `Math`
- bl_idname: `ShaderNodeMath`

```python
from geonodes import nodes

node = nodes.Math(value0=None, value1=None, value2=None, operation='ADD', use_clamp=False)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeMath.webp)

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

| Class or method name | Definition |
|----------------------|------------|
| **[Float](Float.md)** |
| [multiply_add](Float.md#multiply_add) | `def multiply_add(self, multiplier=None, addend=None, clamp=False):` |
| [mul_add](Float.md#mul_add) | `def mul_add(self, multiplier=None, addend=None, clamp=False):` |
| [power](Float.md#power) | `def power(self, exponent=None, clamp=False):` |
| [pow](Float.md#pow) | `def pow(self, exponent=None, clamp=False):` |
| [logarithm](Float.md#logarithm) | `def logarithm(self, base=None, clamp=False):` |
| [log](Float.md#log) | `def log(self, base=None, clamp=False):` |
| [sqrt](Float.md#sqrt) | `def sqrt(self, clamp=False):` |
| [inverse_sqrt](Float.md#inverse_sqrt) | `def inverse_sqrt(self, clamp=False):` |
| [absolute](Float.md#absolute) | `def absolute(self, clamp=False):` |
| [abs](Float.md#abs) | `def abs(self, clamp=False):` |
| [exponent](Float.md#exponent) | `def exponent(self, clamp=False):` |
| [exp](Float.md#exp) | `def exp(self, clamp=False):` |
| [minimum](Float.md#minimum) | `def minimum(self, value=None, clamp=False):` |
| [min](Float.md#min) | `def min(self, value=None, clamp=False):` |
| [maximum](Float.md#maximum) | `def maximum(self, value=None, clamp=False):` |
| [max](Float.md#max) | `def max(self, value=None, clamp=False):` |
| [math_less_than](Float.md#math_less_than) | `def math_less_than(self, threshold=None, clamp=False):` |
| [math_greater_than](Float.md#math_greater_than) | `def math_greater_than(self, threshold=None, clamp=False):` |
| [sign](Float.md#sign) | `def sign(self, clamp=False):` |
| [math_compare](Float.md#math_compare) | `def math_compare(self, value=None, epsilon=None, clamp=False):` |
| [smooth_minimum](Float.md#smooth_minimum) | `def smooth_minimum(self, value=None, distance=None, clamp=False):` |
| [smooth_maximum](Float.md#smooth_maximum) | `def smooth_maximum(self, value=None, distance=None, clamp=False):` |
| [math_round](Float.md#math_round) | `def math_round(self, clamp=False):` |
| [math_floor](Float.md#math_floor) | `def math_floor(self, clamp=False):` |
| [math_ceil](Float.md#math_ceil) | `def math_ceil(self, clamp=False):` |
| [math_truncate](Float.md#math_truncate) | `def math_truncate(self, clamp=False):` |
| [math_trunc](Float.md#math_trunc) | `def math_trunc(self, clamp=False):` |
| [fraction](Float.md#fraction) | `def fraction(self, clamp=False):` |
| [fact](Float.md#fact) | `def fact(self, clamp=False):` |
| [modulo](Float.md#modulo) | `def modulo(self, value=None, clamp=False):` |
| [wrap](Float.md#wrap) | `def wrap(self, max=None, min=None, clamp=False):` |
| [snap](Float.md#snap) | `def snap(self, increment=None, clamp=False):` |
| [ping_pong](Float.md#ping_pong) | `def ping_pong(self, scale=None, clamp=False):` |
| [sine](Float.md#sine) | `def sine(self, value=None, clamp=False):` |
| [sin](Float.md#sin) | `def sin(self, value=None, clamp=False):` |
| [cosine](Float.md#cosine) | `def cosine(self, value=None, clamp=False):` |
| [cos](Float.md#cos) | `def cos(self, value=None, clamp=False):` |
| [tangent](Float.md#tangent) | `def tangent(self, value=None, clamp=False):` |
| [tan](Float.md#tan) | `def tan(self, value=None, clamp=False):` |
| [arcsine](Float.md#arcsine) | `def arcsine(self, value=None, clamp=False):` |
| [arcsin](Float.md#arcsin) | `def arcsin(self, value=None, clamp=False):` |
| [arccosine](Float.md#arccosine) | `def arccosine(self, value=None, clamp=False):` |
| [arccos](Float.md#arccos) | `def arccos(self, value=None, clamp=False):` |
| [arctangent](Float.md#arctangent) | `def arctangent(self, value=None, clamp=False):` |
| [arctan](Float.md#arctan) | `def arctan(self, value=None, clamp=False):` |
| [arctan2](Float.md#arctan2) | `def arctan2(self, value1=None, clamp=False):` |
| [sinh](Float.md#sinh) | `def sinh(self, value=None, clamp=False):` |
| [cosh](Float.md#cosh) | `def cosh(self, value=None, clamp=False):` |
| [tanh](Float.md#tanh) | `def tanh(self, value=None, clamp=False):` |
| [to_radians](Float.md#to_radians) | `def to_radians(self, clamp=False):` |
| [to_degrees](Float.md#to_degrees) | `def to_degrees(self, clamp=False):` |
| **[Integer](Integer.md)** |
| [multiply_add](Integer.md#multiply_add) | `def multiply_add(self, multiplier=None, addend=None, clamp=False):` |
| [mul_add](Integer.md#mul_add) | `def mul_add(self, multiplier=None, addend=None, clamp=False):` |
| [power](Integer.md#power) | `def power(self, exponent=None, clamp=False):` |
| [pow](Integer.md#pow) | `def pow(self, exponent=None, clamp=False):` |
| [logarithm](Integer.md#logarithm) | `def logarithm(self, base=None, clamp=False):` |
| [log](Integer.md#log) | `def log(self, base=None, clamp=False):` |
| [sqrt](Integer.md#sqrt) | `def sqrt(self, clamp=False):` |
| [inverse_sqrt](Integer.md#inverse_sqrt) | `def inverse_sqrt(self, clamp=False):` |
| [absolute](Integer.md#absolute) | `def absolute(self, clamp=False):` |
| [abs](Integer.md#abs) | `def abs(self, clamp=False):` |
| [exponent](Integer.md#exponent) | `def exponent(self, clamp=False):` |
| [exp](Integer.md#exp) | `def exp(self, clamp=False):` |
| [minimum](Integer.md#minimum) | `def minimum(self, value=None, clamp=False):` |
| [min](Integer.md#min) | `def min(self, value=None, clamp=False):` |
| [maximum](Integer.md#maximum) | `def maximum(self, value=None, clamp=False):` |
| [max](Integer.md#max) | `def max(self, value=None, clamp=False):` |
| [math_less_than](Integer.md#math_less_than) | `def math_less_than(self, threshold=None, clamp=False):` |
| [math_greater_than](Integer.md#math_greater_than) | `def math_greater_than(self, threshold=None, clamp=False):` |
| [sign](Integer.md#sign) | `def sign(self, clamp=False):` |
| [math_compare](Integer.md#math_compare) | `def math_compare(self, value=None, epsilon=None, clamp=False):` |
| [smooth_minimum](Integer.md#smooth_minimum) | `def smooth_minimum(self, value=None, distance=None, clamp=False):` |
| [smooth_maximum](Integer.md#smooth_maximum) | `def smooth_maximum(self, value=None, distance=None, clamp=False):` |
| [math_round](Integer.md#math_round) | `def math_round(self, clamp=False):` |
| [math_floor](Integer.md#math_floor) | `def math_floor(self, clamp=False):` |
| [math_ceil](Integer.md#math_ceil) | `def math_ceil(self, clamp=False):` |
| [math_truncate](Integer.md#math_truncate) | `def math_truncate(self, clamp=False):` |
| [math_trunc](Integer.md#math_trunc) | `def math_trunc(self, clamp=False):` |
| [fraction](Integer.md#fraction) | `def fraction(self, clamp=False):` |
| [fact](Integer.md#fact) | `def fact(self, clamp=False):` |
| [modulo](Integer.md#modulo) | `def modulo(self, value=None, clamp=False):` |
| [wrap](Integer.md#wrap) | `def wrap(self, max=None, min=None, clamp=False):` |
| [snap](Integer.md#snap) | `def snap(self, increment=None, clamp=False):` |
| [ping_pong](Integer.md#ping_pong) | `def ping_pong(self, scale=None, clamp=False):` |
| [sine](Integer.md#sine) | `def sine(self, value=None, clamp=False):` |
| [sin](Integer.md#sin) | `def sin(self, value=None, clamp=False):` |
| [cosine](Integer.md#cosine) | `def cosine(self, value=None, clamp=False):` |
| [cos](Integer.md#cos) | `def cos(self, value=None, clamp=False):` |
| [tangent](Integer.md#tangent) | `def tangent(self, value=None, clamp=False):` |
| [tan](Integer.md#tan) | `def tan(self, value=None, clamp=False):` |
| [arcsine](Integer.md#arcsine) | `def arcsine(self, value=None, clamp=False):` |
| [arcsin](Integer.md#arcsin) | `def arcsin(self, value=None, clamp=False):` |
| [arccosine](Integer.md#arccosine) | `def arccosine(self, value=None, clamp=False):` |
| [arccos](Integer.md#arccos) | `def arccos(self, value=None, clamp=False):` |
| [arctangent](Integer.md#arctangent) | `def arctangent(self, value=None, clamp=False):` |
| [arctan](Integer.md#arctan) | `def arctan(self, value=None, clamp=False):` |
| [arctan2](Integer.md#arctan2) | `def arctan2(self, value1=None, clamp=False):` |
| [sinh](Integer.md#sinh) | `def sinh(self, value=None, clamp=False):` |
| [cosh](Integer.md#cosh) | `def cosh(self, value=None, clamp=False):` |
| [tanh](Integer.md#tanh) | `def tanh(self, value=None, clamp=False):` |
| [to_radians](Integer.md#to_radians) | `def to_radians(self, clamp=False):` |
| [to_degrees](Integer.md#to_degrees) | `def to_degrees(self, clamp=False):` |
| Global functions |
| [math](functions.md#math) | `def math(value0=None, value1=None, value2=None, operation='ADD', clamp=False):` |
| [multiply_add](functions.md#multiply_add) | `def multiply_add(value=None, multiplier=None, addend=None, clamp=False):` |
| [mul_add](functions.md#mul_add) | `def mul_add(value=None, multiplier=None, addend=None, clamp=False):` |
| [power](functions.md#power) | `def power(base=None, exponent=None, clamp=False):` |
| [logarithm](functions.md#logarithm) | `def logarithm(value=None, base=None, clamp=False):` |
| [log](functions.md#log) | `def log(value=None, base=None, clamp=False):` |
| [sqrt](functions.md#sqrt) | `def sqrt(value=None, clamp=False):` |
| [inverse_sqrt](functions.md#inverse_sqrt) | `def inverse_sqrt(value=None, clamp=False):` |
| [absolute](functions.md#absolute) | `def absolute(value=None, clamp=False):` |
| [abs](functions.md#abs) | `def abs(value=None, clamp=False):` |
| [exponent](functions.md#exponent) | `def exponent(value=None, clamp=False):` |
| [exp](functions.md#exp) | `def exp(value=None, clamp=False):` |
| [minimum](functions.md#minimum) | `def minimum(value0=None, value1=None, clamp=False):` |
| [min](functions.md#min) | `def min(value0=None, value1=None, clamp=False):` |
| [maximum](functions.md#maximum) | `def maximum(value0=None, value1=None, clamp=False):` |
| [max](functions.md#max) | `def max(value0=None, value1=None, clamp=False):` |
| [math_less_than](functions.md#math_less_than) | `def math_less_than(value=None, threshold=None, clamp=False):` |
| [math_greater_than](functions.md#math_greater_than) | `def math_greater_than(value=None, threshold=None, clamp=False):` |
| [sign](functions.md#sign) | `def sign(value=None, clamp=False):` |
| [math_compare](functions.md#math_compare) | `def math_compare(value0=None, value1=None, epsilon=None, clamp=False):` |
| [smooth_minimum](functions.md#smooth_minimum) | `def smooth_minimum(value0=None, value1=None, distance=None, clamp=False):` |
| [smooth_maximum](functions.md#smooth_maximum) | `def smooth_maximum(value0=None, value1=None, distance=None, clamp=False):` |
| [math_round](functions.md#math_round) | `def math_round(value=None, clamp=False):` |
| [math_floor](functions.md#math_floor) | `def math_floor(value=None, clamp=False):` |
| [math_ceil](functions.md#math_ceil) | `def math_ceil(value=None, clamp=False):` |
| [math_truncate](functions.md#math_truncate) | `def math_truncate(value=None, clamp=False):` |
| [math_trun](functions.md#math_trun) | `def math_trun(value=None, clamp=False):` |
| [fraction](functions.md#fraction) | `def fraction(value=None, clamp=False):` |
| [modulo](functions.md#modulo) | `def modulo(value0=None, value1=None, clamp=False):` |
| [wrap](functions.md#wrap) | `def wrap(value=None, max=None, min=None, clamp=False):` |
| [snap](functions.md#snap) | `def snap(value=None, increment=None, clamp=False):` |
| [ping_pong](functions.md#ping_pong) | `def ping_pong(value=None, scale=None, clamp=False):` |
| [sine](functions.md#sine) | `def sine(value=None, clamp=False):` |
| [sin](functions.md#sin) | `def sin(value=None, clamp=False):` |
| [cosine](functions.md#cosine) | `def cosine(value=None, clamp=False):` |
| [cos](functions.md#cos) | `def cos(value=None, clamp=False):` |
| [tangent](functions.md#tangent) | `def tangent(value=None, clamp=False):` |
| [tan](functions.md#tan) | `def tan(value=None, clamp=False):` |
| [arcsine](functions.md#arcsine) | `def arcsine(value=None, clamp=False):` |
| [arcsin](functions.md#arcsin) | `def arcsin(value=None, clamp=False):` |
| [arccosine](functions.md#arccosine) | `def arccosine(value=None, clamp=False):` |
| [arccos](functions.md#arccos) | `def arccos(value=None, clamp=False):` |
| [arctangent](functions.md#arctangent) | `def arctangent(value=None, clamp=False):` |
| [arctan](functions.md#arctan) | `def arctan(value=None, clamp=False):` |
| [arctan2](functions.md#arctan2) | `def arctan2(value0=None, value1=None, clamp=False):` |
| [sinh](functions.md#sinh) | `def sinh(value=None, clamp=False):` |
| [cosh](functions.md#cosh) | `def cosh(value=None, clamp=False):` |
| [tanh](functions.md#tanh) | `def tanh(value=None, clamp=False):` |
| [to_radians](functions.md#to_radians) | `def to_radians(value=None, clamp=False):` |
| [to_degrees](functions.md#to_degrees) | `def to_degrees(value=None, clamp=False):` |

<sub>Go to [top](#node-Math) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

