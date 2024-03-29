# Socket VALUE


### Methods

- [abs](#abs)
- [add](#add)
- [arccos](#arccos)
- [arcsin](#arcsin)
- [arctan](#arctan)
- [arctan2](#arctan2)
- [ceil](#ceil)
- [color_ramp](#color_ramp)
- [compare](#compare)
- [cos](#cos)
- [cosh](#cosh)
- [degrees](#degrees)
- [divide](#divide)
- [exp](#exp)
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


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def abs(self, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='ABSOLUTE', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### add


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def add(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='ADD', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### arccos


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def arccos(self, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='ARCCOSINE', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### arcsin


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def arcsin(self, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='ARCSINE', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### arctan


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def arctan(self, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='ARCTANGENT', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### arctan2


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def arctan2(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='ARCTAN2', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### ceil


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def ceil(self, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='CEIL', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### color_ramp


- node : [ColorRamp](/docs/Compositor/ColorRamp.md)
- self : fac
- jump : No
- return : value

##### Arguments

- color_ramp : None
- tag_need_exec : None
- node_label : None
- node_color : None

#### Source code

``` python
def color_ramp(self, color_ramp=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.ColorRamp(fac=self, color_ramp=color_ramp, tag_need_exec=tag_need_exec, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### compare


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- value_1 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def compare(self, value=None, value_1=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, value_2=value_1, operation='COMPARE', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### cos


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def cos(self, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='COSINE', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### cosh


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def cosh(self, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='COSH', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### degrees


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def degrees(self, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='DEGREES', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### divide


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def divide(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='DIVIDE', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### exp


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def exp(self, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='EXPONENT', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### floor


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def floor(self, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='FLOOR', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### floored_modulo


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def floored_modulo(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='FLOORED_MODULO', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### fract


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def fract(self, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='FRACT', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### greater_than


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def greater_than(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='GREATER_THAN', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### inverse_sqrt


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def inverse_sqrt(self, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='INVERSE_SQRT', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### less_than


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def less_than(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='LESS_THAN', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### log


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def log(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='LOGARITHM', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### map_range


- node : [MapRange](/docs/Compositor/MapRange.md)
- self : value
- jump : No
- return : result

##### Arguments

- from_min : None
- from_max : None
- to_min : None
- to_max : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.result
```
### max


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def max(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='MAXIMUM', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### min


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def min(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='MINIMUM', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### mix


- node : [Mix](/docs/Compositor/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- fac : None
- image : None
- image_1 : None
- tag_need_exec : None
- use_alpha : False
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def mix(self, fac=None, image=None, image_1=None, tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(fac=fac, image=image, image_1=image_1, blend_type='MIX', tag_need_exec=tag_need_exec, use_alpha=use_alpha, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mod


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def mod(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='MODULO', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### multiply


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def multiply(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='MULTIPLY', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### multiply_add


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- value_1 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def multiply_add(self, value=None, value_1=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, value_2=value_1, operation='MULTIPLY_ADD', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### pingpong


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def pingpong(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='PINGPONG', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### power


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def power(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='POWER', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### radians


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def radians(self, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='RADIANS', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### round


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def round(self, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='ROUND', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sign


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def sign(self, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='SIGN', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sin


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def sin(self, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='SINE', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sinh


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def sinh(self, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='SINH', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### smooth_max


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- value_1 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def smooth_max(self, value=None, value_1=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, value_2=value_1, operation='SMOOTH_MAX', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### smooth_min


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- value_1 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def smooth_min(self, value=None, value_1=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, value_2=value_1, operation='SMOOTH_MIN', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### snap


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def snap(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='SNAP', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sqrt


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def sqrt(self, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='SQRT', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### subtract


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def subtract(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, operation='SUBTRACT', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### tan


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def tan(self, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='TANGENT', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### tanh


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def tanh(self, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='TANH', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### trunc


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def trunc(self, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, operation='TRUNC', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### wrap


- node : [Math](/docs/Compositor/Math.md)
- self : value
- jump : No
- return : value

##### Arguments

- value : None
- value_1 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def wrap(self, value=None, value_1=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Math(value=self, value_1=value, value_2=value_1, operation='WRAP', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
