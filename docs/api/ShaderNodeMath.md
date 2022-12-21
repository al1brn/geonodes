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

 - [math](A.md#math)
  ```python
  def math(value0=None, value1=None, value2=None, operation='ADD', clamp=False)
  ```

 - [add](A.md#add)
  ```python
  def add(value0=None, value1=None, clamp=False)
  ```

 - [subtract](A.md#subtract)
  ```python
  def subtract(value0=None, value1=None, clamp=False)
  ```

 - [sub](A.md#sub)
  ```python
  def sub(value0=None, value1=None, clamp=False)
  ```

 - [multiply](A.md#multiply)
  ```python
  def multiply(value0=None, value1=None, clamp=False)
  ```

 - [mul](A.md#mul)
  ```python
  def mul(value0=None, value1=None, clamp=False)
  ```

 - [divide](A.md#divide)
  ```python
  def divide(value0=None, value1=None, clamp=False)
  ```

 - [div](A.md#div)
  ```python
  def div(value0=None, value1=None, clamp=False)
  ```

 - [multiply_add](A.md#multiply_add)
  ```python
  def multiply_add(value=None, multiplier=None, addend=None, clamp=False)
  ```

 - [mul_add](A.md#mul_add)
  ```python
  def mul_add(value=None, multiplier=None, addend=None, clamp=False)
  ```

 - [power](A.md#power)
  ```python
  def power(base=None, exponent=None, clamp=False)
  ```

 - [logarithm](A.md#logarithm)
  ```python
  def logarithm(value=None, base=None, clamp=False)
  ```

 - [log](A.md#log)
  ```python
  def log(value=None, base=None, clamp=False)
  ```

 - [sqrt](A.md#sqrt)
  ```python
  def sqrt(value=None, clamp=False)
  ```

 - [inverse_sqrt](A.md#inverse_sqrt)
  ```python
  def inverse_sqrt(value=None, clamp=False)
  ```

 - [absolute](A.md#absolute)
  ```python
  def absolute(value=None, clamp=False)
  ```

 - [abs](A.md#abs)
  ```python
  def abs(value=None, clamp=False)
  ```

 - [exponent](A.md#exponent)
  ```python
  def exponent(value=None, clamp=False)
  ```

 - [exp](A.md#exp)
  ```python
  def exp(value=None, clamp=False)
  ```

 - [minimum](A.md#minimum)
  ```python
  def minimum(value0=None, value1=None, clamp=False)
  ```

 - [min](A.md#min)
  ```python
  def min(value0=None, value1=None, clamp=False)
  ```

 - [maximum](A.md#maximum)
  ```python
  def maximum(value0=None, value1=None, clamp=False)
  ```

 - [max](A.md#max)
  ```python
  def max(value0=None, value1=None, clamp=False)
  ```

 - [math_less_than](A.md#math_less_than)
  ```python
  def math_less_than(value=None, threshold=None, clamp=False)
  ```

 - [math_greater_than](A.md#math_greater_than)
  ```python
  def math_greater_than(value=None, threshold=None, clamp=False)
  ```

 - [sign](A.md#sign)
  ```python
  def sign(value=None, clamp=False)
  ```

 - [math_compare](A.md#math_compare)
  ```python
  def math_compare(value0=None, value1=None, epsilon=None, clamp=False)
  ```

 - [smooth_minimum](A.md#smooth_minimum)
  ```python
  def smooth_minimum(value0=None, value1=None, distance=None, clamp=False)
  ```

 - [smooth_maximum](A.md#smooth_maximum)
  ```python
  def smooth_maximum(value0=None, value1=None, distance=None, clamp=False)
  ```

 - [math_round](A.md#math_round)
  ```python
  def math_round(value=None, clamp=False)
  ```

 - [math_floor](A.md#math_floor)
  ```python
  def math_floor(value=None, clamp=False)
  ```

 - [math_ceil](A.md#math_ceil)
  ```python
  def math_ceil(value=None, clamp=False)
  ```

 - [math_truncate](A.md#math_truncate)
  ```python
  def math_truncate(value=None, clamp=False)
  ```

 - [math_trun](A.md#math_trun)
  ```python
  def math_trun(value=None, clamp=False)
  ```

 - [fraction](A.md#fraction)
  ```python
  def fraction(value=None, clamp=False)
  ```

 - [modulo](A.md#modulo)
  ```python
  def modulo(value0=None, value1=None, clamp=False)
  ```

 - [wrap](A.md#wrap)
  ```python
  def wrap(value=None, max=None, min=None, clamp=False)
  ```

 - [snap](A.md#snap)
  ```python
  def snap(value=None, increment=None, clamp=False)
  ```

 - [ping_pong](A.md#ping_pong)
  ```python
  def ping_pong(value=None, scale=None, clamp=False)
  ```

 - [sine](A.md#sine)
  ```python
  def sine(value=None, clamp=False)
  ```

 - [sin](A.md#sin)
  ```python
  def sin(value=None, clamp=False)
  ```

 - [cosine](A.md#cosine)
  ```python
  def cosine(value=None, clamp=False)
  ```

 - [cos](A.md#cos)
  ```python
  def cos(value=None, clamp=False)
  ```

 - [tangent](A.md#tangent)
  ```python
  def tangent(value=None, clamp=False)
  ```

 - [tan](A.md#tan)
  ```python
  def tan(value=None, clamp=False)
  ```

 - [arcsine](A.md#arcsine)
  ```python
  def arcsine(value=None, clamp=False)
  ```

 - [arcsin](A.md#arcsin)
  ```python
  def arcsin(value=None, clamp=False)
  ```

 - [arccosine](A.md#arccosine)
  ```python
  def arccosine(value=None, clamp=False)
  ```

 - [arccos](A.md#arccos)
  ```python
  def arccos(value=None, clamp=False)
  ```

 - [arctangent](A.md#arctangent)
  ```python
  def arctangent(value=None, clamp=False)
  ```

 - [arctan](A.md#arctan)
  ```python
  def arctan(value=None, clamp=False)
  ```

 - [arctan2](A.md#arctan2)
  ```python
  def arctan2(value0=None, value1=None, clamp=False)
  ```

 - [sinh](A.md#sinh)
  ```python
  def sinh(value=None, clamp=False)
  ```

 - [cosh](A.md#cosh)
  ```python
  def cosh(value=None, clamp=False)
  ```

 - [tanh](A.md#tanh)
  ```python
  def tanh(value=None, clamp=False)
  ```

 - [to_radians](A.md#to_radians)
  ```python
  def to_radians(value=None, clamp=False)
  ```

 - [to_degrees](A.md#to_degrees)
  ```python
  def to_degrees(value=None, clamp=False)
  ```

#### [Float](Float.md)

 - [add](Float.md#add)
  ```python
  def add(self, value)
  ```

 - [subtract](Float.md#subtract)
  ```python
  def add(self, value)
  ```

 - [sub](Float.md#sub)
  ```python
  def add(self, value)
  ```

 - [multiply](Float.md#multiply)
  ```python
  def multiply(self, value)
  ```

 - [mul](Float.md#mul)
  ```python
  def multiply(self, value)
  ```

 - [divide](Float.md#divide)
  ```python
  def multiply(self, value)
  ```

 - [div](Float.md#div)
  ```python
  def multiply(self, value)
  ```

 - [multiply_add](Float.md#multiply_add)
  ```python
  def multiply_add(self, multiplier=None, addend=None, clamp=False)
  ```

 - [mul_add](Float.md#mul_add)
  ```python
  def mul_add(self, multiplier=None, addend=None, clamp=False)
  ```

 - [power](Float.md#power)
  ```python
  def power(self, exponent=None, clamp=False)
  ```

 - [pow](Float.md#pow)
  ```python
  def pow(self, exponent=None, clamp=False)
  ```

 - [logarithm](Float.md#logarithm)
  ```python
  def logarithm(self, base=None, clamp=False)
  ```

 - [log](Float.md#log)
  ```python
  def log(self, base=None, clamp=False)
  ```

 - [sqrt](Float.md#sqrt)
  ```python
  def sqrt(self, clamp=False)
  ```

 - [inverse_sqrt](Float.md#inverse_sqrt)
  ```python
  def inverse_sqrt(self, clamp=False)
  ```

 - [absolute](Float.md#absolute)
  ```python
  def absolute(self, clamp=False)
  ```

 - [abs](Float.md#abs)
  ```python
  def abs(self, clamp=False)
  ```

 - [exponent](Float.md#exponent)
  ```python
  def exponent(self, clamp=False)
  ```

 - [exp](Float.md#exp)
  ```python
  def exp(self, clamp=False)
  ```

 - [minimum](Float.md#minimum)
  ```python
  def minimum(self, value=None, clamp=False)
  ```

 - [min](Float.md#min)
  ```python
  def min(self, value=None, clamp=False)
  ```

 - [maximum](Float.md#maximum)
  ```python
  def maximum(self, value=None, clamp=False)
  ```

 - [max](Float.md#max)
  ```python
  def max(self, value=None, clamp=False)
  ```

 - [math_less_than](Float.md#math_less_than)
  ```python
  def math_less_than(self, threshold=None, clamp=False)
  ```

 - [math_greater_than](Float.md#math_greater_than)
  ```python
  def math_greater_than(self, threshold=None, clamp=False)
  ```

 - [sign](Float.md#sign)
  ```python
  def sign(self, clamp=False)
  ```

 - [math_compare](Float.md#math_compare)
  ```python
  def math_compare(self, value=None, epsilon=None, clamp=False)
  ```

 - [smooth_minimum](Float.md#smooth_minimum)
  ```python
  def smooth_minimum(self, value=None, distance=None, clamp=False)
  ```

 - [smooth_maximum](Float.md#smooth_maximum)
  ```python
  def smooth_maximum(self, value=None, distance=None, clamp=False)
  ```

 - [math_round](Float.md#math_round)
  ```python
  def math_round(self, clamp=False)
  ```

 - [math_floor](Float.md#math_floor)
  ```python
  def math_floor(self, clamp=False)
  ```

 - [math_ceil](Float.md#math_ceil)
  ```python
  def math_ceil(self, clamp=False)
  ```

 - [math_truncate](Float.md#math_truncate)
  ```python
  def math_truncate(self, clamp=False)
  ```

 - [math_trunc](Float.md#math_trunc)
  ```python
  def math_trunc(self, clamp=False)
  ```

 - [fraction](Float.md#fraction)
  ```python
  def fraction(self, clamp=False)
  ```

 - [fact](Float.md#fact)
  ```python
  def fact(self, clamp=False)
  ```

 - [modulo](Float.md#modulo)
  ```python
  def modulo(self, value=None, clamp=False)
  ```

 - [wrap](Float.md#wrap)
  ```python
  def wrap(self, max=None, min=None, clamp=False)
  ```

 - [snap](Float.md#snap)
  ```python
  def snap(self, increment=None, clamp=False)
  ```

 - [ping_pong](Float.md#ping_pong)
  ```python
  def ping_pong(self, scale=None, clamp=False)
  ```

 - [sine](Float.md#sine)
  ```python
  def sine(self, value=None, clamp=False)
  ```

 - [sin](Float.md#sin)
  ```python
  def sin(self, value=None, clamp=False)
  ```

 - [cosine](Float.md#cosine)
  ```python
  def cosine(self, value=None, clamp=False)
  ```

 - [cos](Float.md#cos)
  ```python
  def cos(self, value=None, clamp=False)
  ```

 - [tangent](Float.md#tangent)
  ```python
  def tangent(self, value=None, clamp=False)
  ```

 - [tan](Float.md#tan)
  ```python
  def tan(self, value=None, clamp=False)
  ```

 - [arcsine](Float.md#arcsine)
  ```python
  def arcsine(self, value=None, clamp=False)
  ```

 - [arcsin](Float.md#arcsin)
  ```python
  def arcsin(self, value=None, clamp=False)
  ```

 - [arccosine](Float.md#arccosine)
  ```python
  def arccosine(self, value=None, clamp=False)
  ```

 - [arccos](Float.md#arccos)
  ```python
  def arccos(self, value=None, clamp=False)
  ```

 - [arctangent](Float.md#arctangent)
  ```python
  def arctangent(self, value=None, clamp=False)
  ```

 - [arctan](Float.md#arctan)
  ```python
  def arctan(self, value=None, clamp=False)
  ```

 - [arctan2](Float.md#arctan2)
  ```python
  def arctan2(self, value1=None, clamp=False)
  ```

 - [sinh](Float.md#sinh)
  ```python
  def sinh(self, value=None, clamp=False)
  ```

 - [cosh](Float.md#cosh)
  ```python
  def cosh(self, value=None, clamp=False)
  ```

 - [tanh](Float.md#tanh)
  ```python
  def tanh(self, value=None, clamp=False)
  ```

 - [to_radians](Float.md#to_radians)
  ```python
  def to_radians(self, clamp=False)
  ```

 - [to_degrees](Float.md#to_degrees)
  ```python
  def to_degrees(self, clamp=False)
  ```

#### [Integer](Integer.md)

 - [add](Integer.md#add)
  ```python
  def add(self, value)
  ```

 - [subtract](Integer.md#subtract)
  ```python
  def add(self, value)
  ```

 - [sub](Integer.md#sub)
  ```python
  def add(self, value)
  ```

 - [multiply](Integer.md#multiply)
  ```python
  def multiply(self, value)
  ```

 - [mul](Integer.md#mul)
  ```python
  def multiply(self, value)
  ```

 - [divide](Integer.md#divide)
  ```python
  def multiply(self, value)
  ```

 - [div](Integer.md#div)
  ```python
  def multiply(self, value)
  ```

 - [multiply_add](Integer.md#multiply_add)
  ```python
  def multiply_add(self, multiplier=None, addend=None, clamp=False)
  ```

 - [mul_add](Integer.md#mul_add)
  ```python
  def mul_add(self, multiplier=None, addend=None, clamp=False)
  ```

 - [power](Integer.md#power)
  ```python
  def power(self, exponent=None, clamp=False)
  ```

 - [pow](Integer.md#pow)
  ```python
  def pow(self, exponent=None, clamp=False)
  ```

 - [logarithm](Integer.md#logarithm)
  ```python
  def logarithm(self, base=None, clamp=False)
  ```

 - [log](Integer.md#log)
  ```python
  def log(self, base=None, clamp=False)
  ```

 - [sqrt](Integer.md#sqrt)
  ```python
  def sqrt(self, clamp=False)
  ```

 - [inverse_sqrt](Integer.md#inverse_sqrt)
  ```python
  def inverse_sqrt(self, clamp=False)
  ```

 - [absolute](Integer.md#absolute)
  ```python
  def absolute(self, clamp=False)
  ```

 - [abs](Integer.md#abs)
  ```python
  def abs(self, clamp=False)
  ```

 - [exponent](Integer.md#exponent)
  ```python
  def exponent(self, clamp=False)
  ```

 - [exp](Integer.md#exp)
  ```python
  def exp(self, clamp=False)
  ```

 - [minimum](Integer.md#minimum)
  ```python
  def minimum(self, value=None, clamp=False)
  ```

 - [min](Integer.md#min)
  ```python
  def min(self, value=None, clamp=False)
  ```

 - [maximum](Integer.md#maximum)
  ```python
  def maximum(self, value=None, clamp=False)
  ```

 - [max](Integer.md#max)
  ```python
  def max(self, value=None, clamp=False)
  ```

 - [math_less_than](Integer.md#math_less_than)
  ```python
  def math_less_than(self, threshold=None, clamp=False)
  ```

 - [math_greater_than](Integer.md#math_greater_than)
  ```python
  def math_greater_than(self, threshold=None, clamp=False)
  ```

 - [sign](Integer.md#sign)
  ```python
  def sign(self, clamp=False)
  ```

 - [math_compare](Integer.md#math_compare)
  ```python
  def math_compare(self, value=None, epsilon=None, clamp=False)
  ```

 - [smooth_minimum](Integer.md#smooth_minimum)
  ```python
  def smooth_minimum(self, value=None, distance=None, clamp=False)
  ```

 - [smooth_maximum](Integer.md#smooth_maximum)
  ```python
  def smooth_maximum(self, value=None, distance=None, clamp=False)
  ```

 - [math_round](Integer.md#math_round)
  ```python
  def math_round(self, clamp=False)
  ```

 - [math_floor](Integer.md#math_floor)
  ```python
  def math_floor(self, clamp=False)
  ```

 - [math_ceil](Integer.md#math_ceil)
  ```python
  def math_ceil(self, clamp=False)
  ```

 - [math_truncate](Integer.md#math_truncate)
  ```python
  def math_truncate(self, clamp=False)
  ```

 - [math_trunc](Integer.md#math_trunc)
  ```python
  def math_trunc(self, clamp=False)
  ```

 - [fraction](Integer.md#fraction)
  ```python
  def fraction(self, clamp=False)
  ```

 - [fact](Integer.md#fact)
  ```python
  def fact(self, clamp=False)
  ```

 - [modulo](Integer.md#modulo)
  ```python
  def modulo(self, value=None, clamp=False)
  ```

 - [wrap](Integer.md#wrap)
  ```python
  def wrap(self, max=None, min=None, clamp=False)
  ```

 - [snap](Integer.md#snap)
  ```python
  def snap(self, increment=None, clamp=False)
  ```

 - [ping_pong](Integer.md#ping_pong)
  ```python
  def ping_pong(self, scale=None, clamp=False)
  ```

 - [sine](Integer.md#sine)
  ```python
  def sine(self, value=None, clamp=False)
  ```

 - [sin](Integer.md#sin)
  ```python
  def sin(self, value=None, clamp=False)
  ```

 - [cosine](Integer.md#cosine)
  ```python
  def cosine(self, value=None, clamp=False)
  ```

 - [cos](Integer.md#cos)
  ```python
  def cos(self, value=None, clamp=False)
  ```

 - [tangent](Integer.md#tangent)
  ```python
  def tangent(self, value=None, clamp=False)
  ```

 - [tan](Integer.md#tan)
  ```python
  def tan(self, value=None, clamp=False)
  ```

 - [arcsine](Integer.md#arcsine)
  ```python
  def arcsine(self, value=None, clamp=False)
  ```

 - [arcsin](Integer.md#arcsin)
  ```python
  def arcsin(self, value=None, clamp=False)
  ```

 - [arccosine](Integer.md#arccosine)
  ```python
  def arccosine(self, value=None, clamp=False)
  ```

 - [arccos](Integer.md#arccos)
  ```python
  def arccos(self, value=None, clamp=False)
  ```

 - [arctangent](Integer.md#arctangent)
  ```python
  def arctangent(self, value=None, clamp=False)
  ```

 - [arctan](Integer.md#arctan)
  ```python
  def arctan(self, value=None, clamp=False)
  ```

 - [arctan2](Integer.md#arctan2)
  ```python
  def arctan2(self, value1=None, clamp=False)
  ```

 - [sinh](Integer.md#sinh)
  ```python
  def sinh(self, value=None, clamp=False)
  ```

 - [cosh](Integer.md#cosh)
  ```python
  def cosh(self, value=None, clamp=False)
  ```

 - [tanh](Integer.md#tanh)
  ```python
  def tanh(self, value=None, clamp=False)
  ```

 - [to_radians](Integer.md#to_radians)
  ```python
  def to_radians(self, clamp=False)
  ```

 - [to_degrees](Integer.md#to_degrees)
  ```python
  def to_degrees(self, clamp=False)
  ```

