# gnmath

Created on 2024/07/26

@author: alain

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : gnmath
---------------
- Implement geometry nodes math functions

Note that this module is name gnmath rather than math to avoid collision with math standard module

classes
-------

functions
---------
'Math', 'Vector math' and 'Boolean Math' functions
When there is a collision between Math and Vector Math, the vector math function is prefixed by character 'v':
    - sin(Float)
    - vsin(vector)

Boolean math is prefixed by character 'b' when the name collides with python operator:
    - band(bool1, bool2)
    - xor(bool1, bool2)

round, ceil, floor and trunc are implemented by 'Math' node and 'Float to Integer' node.
The second one returns an Integer rather than a Float.
The implementation from 'Math' is prefixed with 'math_':
    - math_floor() -> Float
    -floor() -> Integer

updates
-------
- creation : 2024/07/23
- update : 2024/09/04

## Content

- **A** : [abs](geono-gnmat---gnmath.md#abs) :black_small_square: [acos](geono-gnmat---gnmath.md#acos) :black_small_square: [add](geono-gnmat---gnmath.md#add) :black_small_square: [asin](geono-gnmat---gnmath.md#asin) :black_small_square: [atan](geono-gnmat---gnmath.md#atan) :black_small_square: [atan2](geono-gnmat---gnmath.md#atan2)
- **B** : [band](geono-gnmat---gnmath.md#band) :black_small_square: [bnot](geono-gnmat---gnmath.md#bnot) :black_small_square: [bor](geono-gnmat---gnmath.md#bor) :black_small_square: [bsubtract](geono-gnmat---gnmath.md#bsubtract)
- **C** : [ceil](geono-gnmat---gnmath.md#ceil) :black_small_square: [compare](geono-gnmat---gnmath.md#compare) :black_small_square: [cos](geono-gnmat---gnmath.md#cos) :black_small_square: [cosh](geono-gnmat---gnmath.md#cosh) :black_small_square: [cross_product](geono-gnmat---gnmath.md#cross_product)
- **D** : [degrees](geono-gnmat---gnmath.md#degrees) :black_small_square: [distance](geono-gnmat---gnmath.md#distance) :black_small_square: [divide](geono-gnmat---gnmath.md#divide) :black_small_square: [dot_product](geono-gnmat---gnmath.md#dot_product)
- **E** : [equal](geono-gnmat---gnmath.md#equal) :black_small_square: [exp](geono-gnmat---gnmath.md#exp) :black_small_square: [exponent](geono-gnmat---gnmath.md#exponent)
- **F** : [faceforward](geono-gnmat---gnmath.md#faceforward) :black_small_square: [floor](geono-gnmat---gnmath.md#floor) :black_small_square: [floored_modulo](geono-gnmat---gnmath.md#floored_modulo) :black_small_square: [fract](geono-gnmat---gnmath.md#fract)
- **G** : [greater_than](geono-gnmat---gnmath.md#greater_than)
- **I** : [imply](geono-gnmat---gnmath.md#imply) :black_small_square: [inverse_sqrt](geono-gnmat---gnmath.md#inverse_sqrt)
- **L** : [length](geono-gnmat---gnmath.md#length) :black_small_square: [less_than](geono-gnmat---gnmath.md#less_than) :black_small_square: [ln](geono-gnmat---gnmath.md#ln) :black_small_square: [log](geono-gnmat---gnmath.md#log)
- **M** : [math_ceil](geono-gnmat---gnmath.md#math_ceil) :black_small_square: [math_floor](geono-gnmat---gnmath.md#math_floor) :black_small_square: [math_round](geono-gnmat---gnmath.md#math_round) :black_small_square: [math_trunc](geono-gnmat---gnmath.md#math_trunc) :black_small_square: [max](geono-gnmat---gnmath.md#max) :black_small_square: [min](geono-gnmat---gnmath.md#min) :black_small_square: [modulo](geono-gnmat---gnmath.md#modulo) :black_small_square: [multiply](geono-gnmat---gnmath.md#multiply) :black_small_square: [multiply_add](geono-gnmat---gnmath.md#multiply_add)
- **N** : [nand](geono-gnmat---gnmath.md#nand) :black_small_square: [nimply](geono-gnmat---gnmath.md#nimply) :black_small_square: [nor](geono-gnmat---gnmath.md#nor) :black_small_square: [normalize](geono-gnmat---gnmath.md#normalize) :black_small_square: [not_equal](geono-gnmat---gnmath.md#not_equal)
- **P** : [ping_pong](geono-gnmat---gnmath.md#ping_pong) :black_small_square: [pingpong](geono-gnmat---gnmath.md#pingpong) :black_small_square: [power](geono-gnmat---gnmath.md#power) :black_small_square: [project](geono-gnmat---gnmath.md#project)
- **R** : [radians](geono-gnmat---gnmath.md#radians) :black_small_square: [reflect](geono-gnmat---gnmath.md#reflect) :black_small_square: [refract](geono-gnmat---gnmath.md#refract) :black_small_square: [round](geono-gnmat---gnmath.md#round)
- **S** : [scale](geono-gnmat---gnmath.md#scale) :black_small_square: [sign](geono-gnmat---gnmath.md#sign) :black_small_square: [sin](geono-gnmat---gnmath.md#sin) :black_small_square: [sinh](geono-gnmat---gnmath.md#sinh) :black_small_square: [smooth_max](geono-gnmat---gnmath.md#smooth_max) :black_small_square: [smooth_min](geono-gnmat---gnmath.md#smooth_min) :black_small_square: [snap](geono-gnmat---gnmath.md#snap) :black_small_square: [sqrt](geono-gnmat---gnmath.md#sqrt) :black_small_square: [subtract](geono-gnmat---gnmath.md#subtract)
- **T** : [tan](geono-gnmat---gnmath.md#tan) :black_small_square: [tanh](geono-gnmat---gnmath.md#tanh) :black_small_square: [trunc](geono-gnmat---gnmath.md#trunc)
- **V** : [vabs](geono-gnmat---gnmath.md#vabs) :black_small_square: [vadd](geono-gnmat---gnmath.md#vadd) :black_small_square: [vceil](geono-gnmat---gnmath.md#vceil) :black_small_square: [vcos](geono-gnmat---gnmath.md#vcos) :black_small_square: [vdivide](geono-gnmat---gnmath.md#vdivide) :black_small_square: [vfloor](geono-gnmat---gnmath.md#vfloor) :black_small_square: [vfract](geono-gnmat---gnmath.md#vfract) :black_small_square: [vmax](geono-gnmat---gnmath.md#vmax) :black_small_square: [vmin](geono-gnmat---gnmath.md#vmin) :black_small_square: [vmodulo](geono-gnmat---gnmath.md#vmodulo) :black_small_square: [vmultiply](geono-gnmat---gnmath.md#vmultiply) :black_small_square: [vmultiply_add](geono-gnmat---gnmath.md#vmultiply_add) :black_small_square: [vsin](geono-gnmat---gnmath.md#vsin) :black_small_square: [vsnap](geono-gnmat---gnmath.md#vsnap) :black_small_square: [vsubtract](geono-gnmat---gnmath.md#vsubtract) :black_small_square: [vtan](geono-gnmat---gnmath.md#vtan) :black_small_square: [vwrap](geono-gnmat---gnmath.md#vwrap)
- **W** : [wrap](geono-gnmat---gnmath.md#wrap)
- **X** : [xnor](geono-gnmat---gnmath.md#xnor) :black_small_square: [xor](geono-gnmat---gnmath.md#xor)

## Functions



----------
### abs()

> function

``` python
abs(value, use_clamp=None)
```

Math ABSOLUTE.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### acos()

> function

``` python
acos(value, use_clamp=None)
```

Math ACOS.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### add()

> function

``` python
add(value, other, use_clamp=None)
```

Math ADD.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : first value
- **other** (_Float_) : second value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### asin()

> function

``` python
asin(value, use_clamp=None)
```

Math ASIN.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### atan()

> function

``` python
atan(value, use_clamp=None)
```

Math ATAN.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### atan2()

> function

``` python
atan2(value, other, use_clamp=None)
```

Math ATAN2.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **other** (_Float_) : other value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### band()

> function

``` python
band(value, other)
```

Boolean AND.

[!Node] Boolean Math


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### bnot()

> function

``` python
bnot(value)
```

Boolean NOT.

[!Node] Boolean Math


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### bor()

> function

``` python
bor(value, other)
```

Boolean OR.

[!Node] Boolean Math


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### bsubtract()

> function

``` python
bsubtract(value, other)
```

Boolean NIMPLY.

[!Node] Boolean Math


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### ceil()

> function

``` python
ceil(value, use_clamp=None)
```

Ceiling.

[!Node] Math, Float to Integer

Implements 'Math' node in ShaderNodes and 'Float to Integer' for GeoNodes.

rounding_mode in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')


Returns
- Float (ShaderNodes) or Integer (GeoNodes)

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### compare()

> function

``` python
compare(value, other, epsilon=None, use_clamp=None)
```

Math COMPARE.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : first value
- **other** (_Float_) : second value
- **epsilon** (_Float_ = None) : epsilon
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### cos()

> function

``` python
cos(value, use_clamp=None)
```

Math COS.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### cosh()

> function

``` python
cosh(value, use_clamp=None)
```

Math COSH.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### cross_product()

> function

``` python
cross_product(value, other)
```

Vector Math CROSS PRODUCT.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### degrees()

> function

``` python
degrees(value, use_clamp=None)
```

Math DEGREES.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### distance()

> function

``` python
distance(value, other)
```

Vector Math DISTANCE.

[!Node] Vector Math


Returns
- Float

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### divide()

> function

``` python
divide(value, other, use_clamp=None)
```

Math DIVIDE.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : first value
- **other** (_Float_) : second value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### dot_product()

> function

``` python
dot_product(value, other)
```

Vector Math DOT PRODUCT.

[!Node] Vector Math


Returns
- Float

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### equal()

> function

``` python
equal(value, other)
```

Boolean XNOR.

[!Node] Boolean Math


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### exp()

> function

``` python
exp(value, use_clamp=None)
```

Math EXPONENT.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### exponent()

> function

``` python
exponent(value, use_clamp=None)
```

Math EXPONENT.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### faceforward()

> function

``` python
faceforward(value, incident=None, reference=None)
```

Vector Math FACE FORWARD.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **incident** (_Vector_ = None) : incident vector
- **reference** (_Vector_ = None) : reference vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### floor()

> function

``` python
floor(value, use_clamp=None)
```

Floor.

[!Node] Math, Float to Integer

Implements 'Math' node in ShaderNodes and 'Float to Integer' for GeoNodes.

rounding_mode in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')


Returns
- Float (ShaderNodes) or Integer (GeoNodes)

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### floored_modulo()

> function

``` python
floored_modulo(value, other, use_clamp=None)
```

Math FLOORED MODULO.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **other** (_Float_) : other value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### fract()

> function

``` python
fract(value, use_clamp=None)
```

Math FRACT.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### greater_than()

> function

``` python
greater_than(value, threshold, use_clamp=None)
```

Math GREATER THAN.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : first value
- **threshold** (_Float_) : second value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### imply()

> function

``` python
imply(value, other)
```

Boolean IMPLY.

[!Node] Boolean Math


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### inverse_sqrt()

> function

``` python
inverse_sqrt(value, use_clamp=None)
```

Math INVERSE SQRT.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### length()

> function

``` python
length(value)
```

Vector Math LENGTH.

[!Node] Vector Math


Returns
- Float

#### Arguments:
- **value** (_Vector_) : vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### less_than()

> function

``` python
less_than(value, threshold, use_clamp=None)
```

Math LESS_THAN.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **threshold** (_Float_) : second value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### ln()

> function

``` python
ln(value, use_clamp=None)
```

Math neperian LOGARITHM (using base = e).

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### log()

> function

``` python
log(value, base=10, use_clamp=None)
```

Math LOGARITHM.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **base** (_Float_ = 10) : second value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### math_ceil()

> function

``` python
math_ceil(value, use_clamp=None)
```

Math CEIL.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### math_floor()

> function

``` python
math_floor(value, use_clamp=None)
```

Math FLOOR.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### math_round()

> function

``` python
math_round(value, use_clamp=None)
```

Math ROUND.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### math_trunc()

> function

``` python
math_trunc(value, use_clamp=None)
```

Math TRUNC.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### max()

> function

``` python
max(value, other, use_clamp=None)
```

Math MAXIMUM.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : first value
- **other** (_Float_) : second value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### min()

> function

``` python
min(value, other, use_clamp=None)
```

Math MINIMUM.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : first value
- **other** (_Float_) : second value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### modulo()

> function

``` python
modulo(value, other, use_clamp=None)
```

Math MODULO.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **other** (_Float_) : other value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### multiply()

> function

``` python
multiply(value, other, use_clamp=None)
```

Math MULTIPLY.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : first value
- **other** (_Float_) : second value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### multiply_add()

> function

``` python
multiply_add(value, multiplier, addend, use_clamp=None)
```

Math MULTIPLY ADD.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **multiplier** (_Float_) : multiplier value
- **addend** (_Float_) : add end value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### nand()

> function

``` python
nand(value, other)
```

Boolean NAND.

[!Node] Boolean Math


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### nimply()

> function

``` python
nimply(value, other)
```

Boolean NIMPLY.

[!Node] Boolean Math


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### nor()

> function

``` python
nor(value, other)
```

Boolean NOR.

[!Node] Boolean Math


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### normalize()

> function

``` python
normalize(value)
```

Vector Math NORMALIZE.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### not_equal()

> function

``` python
not_equal(value, other)
```

Boolean XOR.

[!Node] Boolean Math


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### ping_pong()

> function

``` python
ping_pong(value, scale=None, use_clamp=None)
```

Math PINGPONG.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **scale** (_Float_ = None) : other value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### pingpong()

> function

``` python
pingpong(value, scale=None, use_clamp=None)
```

Math PINGPONG.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **scale** (_Float_ = None) : other value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### power()

> function

``` python
power(base, exponent, use_clamp=None)
```

Math POWER.

[!Node] Math


Returns
- Float

#### Arguments:
- **base** (_Float_) : base value
- **exponent** (_Float_) : exponent value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### project()

> function

``` python
project(value, other)
```

Vector Math PROJECT.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### radians()

> function

``` python
radians(value, use_clamp=None)
```

Math RADIANS.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### reflect()

> function

``` python
reflect(value, other)
```

Vector Math REFLECT.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### refract()

> function

``` python
refract(value, other, ior=None)
```

Vector Math REFRACT.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector
- **ior** (_Float_ = None) : IOR

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### round()

> function

``` python
round(value, use_clamp=None)
```

Round.

[!Node] Math, Float to Integer

Implements 'Math' node in ShaderNodes and 'Float to Integer' for GeoNodes.

rounding_mode in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')


Returns
- Float (ShaderNodes) or Integer (GeoNodes)

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### scale()

> function

``` python
scale(value, scale)
```

Vector Math SCALE.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **scale** (_Float_) : scale factor

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### sign()

> function

``` python
sign(value)
```

Math SIGN.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### sin()

> function

``` python
sin(value, use_clamp=None)
```

Math SIN.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### sinh()

> function

``` python
sinh(value, use_clamp=None)
```

Math SINH.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### smooth_max()

> function

``` python
smooth_max(value, other, distance=None, use_clamp=None)
```

Math SMOOTH MAX.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : first value
- **other** (_Float_) : second value
- **distance** (_Float_ = None) : distance
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### smooth_min()

> function

``` python
smooth_min(value, other, distance=None, use_clamp=None)
```

Math SMOOTH_MIN.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : first value
- **other** (_Float_) : second value
- **distance** (_Float_ = None) : distance
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### snap()

> function

``` python
snap(value, increment=None, use_clamp=None)
```

Math SNAP.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **increment** (_Float_ = None) : other value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### sqrt()

> function

``` python
sqrt(value, use_clamp=None)
```

Math SQRT.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### subtract()

> function

``` python
subtract(value, other, use_clamp=None)
```

Math SUBTRACT.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : first value
- **other** (_Float_) : second value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### tan()

> function

``` python
tan(value, use_clamp=None)
```

Math TAN.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### tanh()

> function

``` python
tanh(value, use_clamp=None)
```

Math TANH.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### trunc()

> function

``` python
trunc(value, use_clamp=None)
```

Truncate.

[!Node] Math, Float to Integer

Implements 'Math' node in ShaderNodes and 'Float to Integer' for GeoNodes.

rounding_mode in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')


Returns
- Float (ShaderNodes) or Integer (GeoNodes)

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### vabs()

> function

``` python
vabs(value)
```

Vector Math ABS.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### vadd()

> function

``` python
vadd(value, other)
```

Vector Math ADD.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### vceil()

> function

``` python
vceil(value)
```

Vector Math CEIL.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### vcos()

> function

``` python
vcos(value)
```

Vector Math COS.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### vdivide()

> function

``` python
vdivide(value, other)
```

Vector Math DIVIDE.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### vfloor()

> function

``` python
vfloor(value)
```

Vector Math FLOOR.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### vfract()

> function

``` python
vfract(value)
```

Vector Math FRACT.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### vmax()

> function

``` python
vmax(value, other)
```

Vector Math MAXIMUM.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### vmin()

> function

``` python
vmin(value, other)
```

Vector Math MINIMUM.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### vmodulo()

> function

``` python
vmodulo(value, other)
```

Vector Math MODULO.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other**

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### vmultiply()

> function

``` python
vmultiply(value, other)
```

Vector Math MULTIPLY.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### vmultiply_add()

> function

``` python
vmultiply_add(value, multiplier, addend)
```

Vector Math MULTIPLY ADD.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **multiplier** (_Vector_) : other vector
- **addend** (_Vector_) : add end vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### vsin()

> function

``` python
vsin(value)
```

Vector Math SIN.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### vsnap()

> function

``` python
vsnap(value, increment)
```

Vector Math SNAP.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **increment** (_Vector_) : increment vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### vsubtract()

> function

``` python
vsubtract(value, other)
```

Vector Math SUBTRACT.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### vtan()

> function

``` python
vtan(value)
```

Vector Math TAN.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### vwrap()

> function

``` python
vwrap(value, max=None, min=None)
```

Vector Math WRAP.

[!Node] Vector Math


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **max** (_Vector_ = None) : max vector
- **min** (_Vector_ = None) : min vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### wrap()

> function

``` python
wrap(value, max=None, min=None, use_clamp=None)
```

Math WRAP.

[!Node] Math


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **max** (_Float_ = None) : max value
- **min** (_Float_ = None) : min value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### xnor()

> function

``` python
xnor(value, other)
```

Boolean XNOR.

[!Node] Boolean Math


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

----------
### xor()

> function

``` python
xor(value, other)
```

Boolean XOR.

[!Node] Boolean Math


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [Functions](geono-gnmat---gnmath.md#functions)</sub>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath) :black_small_square: [Content](geono-gnmat---gnmath.md#content) :black_small_square: [gnmath](geono-gnmat---gnmath.md#gnmath)</sub>