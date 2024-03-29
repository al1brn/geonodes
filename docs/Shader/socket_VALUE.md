# Socket VALUE


### Methods

- [abs](#abs)
- [add](#add)
- [arccos](#arccos)
- [arcsin](#arcsin)
- [arctan](#arctan)
- [arctan2](#arctan2)
- [ceil](#ceil)
- [clamp](#clamp)
- [color_ramp](#color_ramp)
- [compare](#compare)
- [cos](#cos)
- [cosh](#cosh)
- [degrees](#degrees)
- [divide](#divide)
- [exp](#exp)
- [float_curve](#float_curve)
- [floor](#floor)
- [floored_modulo](#floored_modulo)
- [fract](#fract)
- [greater_than](#greater_than)
- [inverse_sqrt](#inverse_sqrt)
- [less_than](#less_than)
- [log](#log)
- [map_range](#map_range)
- [max](#max)
- [min](#min)
- [mix](#mix)
- [mod](#mod)
- [multiply](#multiply)
- [multiply_add](#multiply_add)
- [pingpong](#pingpong)
- [power](#power)
- [radians](#radians)
- [round](#round)
- [sign](#sign)
- [sin](#sin)
- [sinh](#sinh)
- [smooth_max](#smooth_max)
- [smooth_min](#smooth_min)
- [snap](#snap)
- [sqrt](#sqrt)
- [subtract](#subtract)
- [tan](#tan)
- [tanh](#tanh)
- [trunc](#trunc)
- [wrap](#wrap)

## Methods

### abs


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def abs(self, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='ABSOLUTE', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### add


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def add(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='ADD', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### arccos


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def arccos(self, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='ARCCOSINE', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### arcsin


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def arcsin(self, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='ARCSINE', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### arctan


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def arctan(self, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='ARCTANGENT', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### arctan2


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def arctan2(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='ARCTAN2', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### ceil


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def ceil(self, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='CEIL', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### clamp


- node : [Clamp](/docs/Shader/Clamp.md)
- self : value
- jump : No
- return : result

##### Arguments

- min : None
- max : None
- clamp_type : 'MINMAX' in ('MINMAX', 'RANGE')
- node_label : None
- node_color : None

#### Source code

``` python
def clamp(self, min=None, max=None, clamp_type='MINMAX', node_label=None, node_color=None, **kwargs):
    node = self.tree.Clamp(value=self, min=min, max=max, clamp_type=clamp_type, node_label=node_label, node_color=node_color, **kwargs)
    return node.result
```
### color_ramp


- node : [ColorRamp](/docs/Shader/ColorRamp.md)
- self : fac
- jump : No
- return : value

##### Arguments

- color_ramp : None
- node_label : None
- node_color : None

#### Source code

``` python
def color_ramp(self, color_ramp=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.ColorRamp(fac=self, color_ramp=color_ramp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### compare


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- value_1 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def compare(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, value_2=value_1, operation='COMPARE', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### cos


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def cos(self, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='COSINE', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### cosh


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def cosh(self, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='COSH', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### degrees


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def degrees(self, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='DEGREES', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### divide


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def divide(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='DIVIDE', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### exp


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def exp(self, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='EXPONENT', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### float_curve


- node : [FloatCurve](/docs/Shader/FloatCurve.md)
- self : value
- jump : value
- return : self

##### Arguments

- factor : None
- mapping : None
- node_label : None
- node_color : None

#### Source code

``` python
def float_curve(self, factor=None, mapping=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.FloatCurve(factor=factor, value=self, mapping=mapping, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.value)
    return self
```
### floor


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def floor(self, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='FLOOR', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### floored_modulo


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def floored_modulo(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='FLOORED_MODULO', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### fract


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def fract(self, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='FRACT', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### greater_than


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def greater_than(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='GREATER_THAN', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### inverse_sqrt


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def inverse_sqrt(self, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='INVERSE_SQRT', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### less_than


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def less_than(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='LESS_THAN', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### log


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def log(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='LOGARITHM', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### map_range


- node : [MapRange](/docs/Shader/MapRange.md)
- self : value
- jump : No
- return : result

##### Arguments

- from_min : None
- from_max : None
- to_min : None
- to_max : None
- vector : None
- steps : None
- clamp : True
- data_type : 'FLOAT' in ('FLOAT', 'FLOAT_VECTOR')
- interpolation_type : 'LINEAR' in ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP')
- node_label : None
- node_color : None

#### Source code

``` python
def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, vector=None, steps=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR', node_label=None, node_color=None, **kwargs):
    node = self.tree.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, vector=vector, steps=steps, clamp=clamp, data_type=data_type, interpolation_type=interpolation_type, node_label=node_label, node_color=node_color, **kwargs)
    return node.result
```
### max


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def max(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='MAXIMUM', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### min


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def min(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='MINIMUM', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### mix


- node : [Mix](/docs/Shader/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- clamp_factor : True
- clamp_result : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix(self, factor=None, b=None, clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='FLOAT', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mod


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def mod(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='MODULO', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### multiply


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def multiply(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='MULTIPLY', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### multiply_add


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- value_1 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def multiply_add(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, value_2=value_1, operation='MULTIPLY_ADD', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### pingpong


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def pingpong(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='PINGPONG', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### power


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def power(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='POWER', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### radians


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def radians(self, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='RADIANS', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### round


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def round(self, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='ROUND', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sign


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def sign(self, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='SIGN', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sin


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def sin(self, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='SINE', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sinh


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def sinh(self, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='SINH', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### smooth_max


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- value_1 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def smooth_max(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, value_2=value_1, operation='SMOOTH_MAX', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### smooth_min


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- value_1 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def smooth_min(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, value_2=value_1, operation='SMOOTH_MIN', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### snap


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def snap(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='SNAP', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sqrt


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def sqrt(self, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='SQRT', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### subtract


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def subtract(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='SUBTRACT', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### tan


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def tan(self, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='TANGENT', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### tanh


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def tanh(self, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='TANH', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### trunc


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def trunc(self, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='TRUNC', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### wrap


- node : [Math](/docs/Shader/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- value_1 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def wrap(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, value_2=value_1, operation='WRAP', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
