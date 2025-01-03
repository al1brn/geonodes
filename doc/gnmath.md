# gnmath

> math library

**gnmath** libray contains the math functions for data [Booleans>, <!Float"Floats](boolean.md#boolean) and
[Vectors](vector.md#vector) using the following nodes:
- **'Boolean Math'**
- **'Math'**
- **'Vector Math'**

The name of the functions is the name of the 'operation' parameter of the node,
with some changes according the following rules:
- use python math library when it exists: [sin](gnmath.md#sin) and [cos](gnmath.md#cos) rather than 'sine' and 'cosine' for instance
- prefix with char ***'v'*** for [Vector](vector.md#vector) functions when it collides with a [Float](float.md#float) function : [vsin](gnmath.md#vsin) and [vcos](gnmath.md#vcos) for instance
- prefix with char ***'b'*** boolean reserved keywords : [band](gnmath.md#band), [bor](gnmath.md#bor) and [bnot](gnmath.md#bnot)

## Content

- **A** : [abs](gnmath.md#abs) :black_small_square: [acos](gnmath.md#acos) :black_small_square: [add](gnmath.md#add) :black_small_square: [asin](gnmath.md#asin) :black_small_square: [atan](gnmath.md#atan) :black_small_square: [atan2](gnmath.md#atan2)
- **B** : [band](gnmath.md#band) :black_small_square: [bnot](gnmath.md#bnot) :black_small_square: [bor](gnmath.md#bor) :black_small_square: [bsubtract](gnmath.md#bsubtract)
- **C** : [ceil](gnmath.md#ceil) :black_small_square: [compare](gnmath.md#compare) :black_small_square: [cos](gnmath.md#cos) :black_small_square: [cosh](gnmath.md#cosh) :black_small_square: [cross_product](gnmath.md#cross_product)
- **D** : [degrees](gnmath.md#degrees) :black_small_square: [distance](gnmath.md#distance) :black_small_square: [divide](gnmath.md#divide) :black_small_square: [dot_product](gnmath.md#dot_product)
- **E** : [equal](gnmath.md#equal) :black_small_square: [exp](gnmath.md#exp) :black_small_square: [exponent](gnmath.md#exponent)
- **F** : [faceforward](gnmath.md#faceforward) :black_small_square: [floor](gnmath.md#floor) :black_small_square: [floored_modulo](gnmath.md#floored_modulo) :black_small_square: [fract](gnmath.md#fract)
- **G** : [GCD](gnmath.md#gcd) :black_small_square: [greater_than](gnmath.md#greater_than)
- **I** : [iabs](gnmath.md#iabs) :black_small_square: [iadd](gnmath.md#iadd) :black_small_square: [idivide](gnmath.md#idivide) :black_small_square: [idivide_ceiling](gnmath.md#idivide_ceiling) :black_small_square: [idivide_floor](gnmath.md#idivide_floor) :black_small_square: [idivide_round](gnmath.md#idivide_round) :black_small_square: [ifloored_modulo](gnmath.md#ifloored_modulo) :black_small_square: [imax](gnmath.md#imax) :black_small_square: [imin](gnmath.md#imin) :black_small_square: [imodulo](gnmath.md#imodulo) :black_small_square: [imply](gnmath.md#imply) :black_small_square: [imultiply](gnmath.md#imultiply) :black_small_square: [imultiply_add](gnmath.md#imultiply_add) :black_small_square: [inegate](gnmath.md#inegate) :black_small_square: [inverse_sqrt](gnmath.md#inverse_sqrt) :black_small_square: [ipower](gnmath.md#ipower) :black_small_square: [isign](gnmath.md#isign) :black_small_square: [isubtract](gnmath.md#isubtract)
- **L** : [LCM](gnmath.md#lcm) :black_small_square: [length](gnmath.md#length) :black_small_square: [less_than](gnmath.md#less_than) :black_small_square: [ln](gnmath.md#ln) :black_small_square: [log](gnmath.md#log)
- **M** : [math_ceil](gnmath.md#math_ceil) :black_small_square: [math_floor](gnmath.md#math_floor) :black_small_square: [math_round](gnmath.md#math_round) :black_small_square: [math_trunc](gnmath.md#math_trunc) :black_small_square: [max](gnmath.md#max) :black_small_square: [min](gnmath.md#min) :black_small_square: [modulo](gnmath.md#modulo) :black_small_square: [multiply](gnmath.md#multiply) :black_small_square: [multiply_add](gnmath.md#multiply_add)
- **N** : [nand](gnmath.md#nand) :black_small_square: [nimply](gnmath.md#nimply) :black_small_square: [nor](gnmath.md#nor) :black_small_square: [normalize](gnmath.md#normalize) :black_small_square: [not_equal](gnmath.md#not_equal)
- **P** : [ping_pong](gnmath.md#ping_pong) :black_small_square: [pingpong](gnmath.md#pingpong) :black_small_square: [power](gnmath.md#power) :black_small_square: [project](gnmath.md#project)
- **R** : [radians](gnmath.md#radians) :black_small_square: [reflect](gnmath.md#reflect) :black_small_square: [refract](gnmath.md#refract) :black_small_square: [round](gnmath.md#round)
- **S** : [scale](gnmath.md#scale) :black_small_square: [sign](gnmath.md#sign) :black_small_square: [sin](gnmath.md#sin) :black_small_square: [sinh](gnmath.md#sinh) :black_small_square: [smooth_max](gnmath.md#smooth_max) :black_small_square: [smooth_min](gnmath.md#smooth_min) :black_small_square: [snap](gnmath.md#snap) :black_small_square: [sqrt](gnmath.md#sqrt) :black_small_square: [subtract](gnmath.md#subtract)
- **T** : [tan](gnmath.md#tan) :black_small_square: [tanh](gnmath.md#tanh) :black_small_square: [trunc](gnmath.md#trunc)
- **V** : [vabs](gnmath.md#vabs) :black_small_square: [vadd](gnmath.md#vadd) :black_small_square: [vceil](gnmath.md#vceil) :black_small_square: [vcos](gnmath.md#vcos) :black_small_square: [vdivide](gnmath.md#vdivide) :black_small_square: [vfloor](gnmath.md#vfloor) :black_small_square: [vfract](gnmath.md#vfract) :black_small_square: [vmax](gnmath.md#vmax) :black_small_square: [vmin](gnmath.md#vmin) :black_small_square: [vmodulo](gnmath.md#vmodulo) :black_small_square: [vmultiply](gnmath.md#vmultiply) :black_small_square: [vmultiply_add](gnmath.md#vmultiply_add) :black_small_square: [vsin](gnmath.md#vsin) :black_small_square: [vsnap](gnmath.md#vsnap) :black_small_square: [vsubtract](gnmath.md#vsubtract) :black_small_square: [vtan](gnmath.md#vtan) :black_small_square: [vwrap](gnmath.md#vwrap)
- **W** : [wrap](gnmath.md#wrap)
- **X** : [xnor](gnmath.md#xnor) :black_small_square: [xor](gnmath.md#xor)

## Functions



----------
### abs()

> function

``` python
abs(value, use_clamp=None)
```

Math ABSOLUTE.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### acos()

> function

``` python
acos(value, use_clamp=None)
```

Math ACOS.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### add()

> function

``` python
add(value, other, use_clamp=None)
```

Math ADD.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : first value
- **other** (_Float_) : second value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### asin()

> function

``` python
asin(value, use_clamp=None)
```

Math ASIN.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### atan()

> function

``` python
atan(value, use_clamp=None)
```

Math ATAN.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### atan2()

> function

``` python
atan2(value, other, use_clamp=None)
```

Math ATAN2.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **other** (_Float_) : other value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### band()

> function

``` python
band(value, other)
```

Boolean AND.

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### bnot()

> function

``` python
bnot(value)
```

Boolean NOT.

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### bor()

> function

``` python
bor(value, other)
```

Boolean OR.

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### bsubtract()

> function

``` python
bsubtract(value, other)
```

Boolean NIMPLY.

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### ceil()

> function

``` python
ceil(value, use_clamp=None)
```

Ceiling.

> Node ERROR: Node 'Math, Float to Integer' not found

Implements 'Math' node in ShaderNodes and 'Float to Integer' for GeoNodes.

rounding_mode in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')


Returns
- Float (ShaderNodes) or Integer (GeoNodes)

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### compare()

> function

``` python
compare(value, other, epsilon=None, use_clamp=None)
```

Math COMPARE.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : first value
- **other** (_Float_) : second value
- **epsilon** (_Float_ = None) : epsilon
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### cos()

> function

``` python
cos(value, use_clamp=None)
```

Math COS.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### cosh()

> function

``` python
cosh(value, use_clamp=None)
```

Math COSH.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### cross_product()

> function

``` python
cross_product(value, other)
```

Vector Math CROSS PRODUCT.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### degrees()

> function

``` python
degrees(value, use_clamp=None)
```

Math DEGREES.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### distance()

> function

``` python
distance(value, other)
```

Vector Math DISTANCE.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Float

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### divide()

> function

``` python
divide(value, other, use_clamp=None)
```

Math DIVIDE.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : first value
- **other** (_Float_) : second value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### dot_product()

> function

``` python
dot_product(value, other)
```

Vector Math DOT PRODUCT.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Float

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### equal()

> function

``` python
equal(value, other)
```

Boolean XNOR.

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### exp()

> function

``` python
exp(value, use_clamp=None)
```

Math EXPONENT.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### exponent()

> function

``` python
exponent(value, use_clamp=None)
```

Math EXPONENT.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### faceforward()

> function

``` python
faceforward(value, incident=None, reference=None)
```

Vector Math FACE FORWARD.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **incident** (_Vector_ = None) : incident vector
- **reference** (_Vector_ = None) : reference vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### floor()

> function

``` python
floor(value, use_clamp=None)
```

Floor.

> Node ERROR: Node 'Math, Float to Integer' not found

Implements 'Math' node in ShaderNodes and 'Float to Integer' for GeoNodes.

rounding_mode in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')


Returns
- Float (ShaderNodes) or Integer (GeoNodes)

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### floored_modulo()

> function

``` python
floored_modulo(value, other, use_clamp=None)
```

Math FLOORED MODULO.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **other** (_Float_) : other value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### fract()

> function

``` python
fract(value, use_clamp=None)
```

Math FRACT.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### GCD()

> function

``` python
GCD(value, other)
```

Integer Math GCD.

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)


Returns
- Integer

#### Arguments:
- **value** (_Integer_) : first value
- **other** (_Integer_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### greater_than()

> function

``` python
greater_than(value, threshold, use_clamp=None)
```

Math GREATER THAN.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : first value
- **threshold** (_Float_) : second value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### iabs()

> function

``` python
iabs(value)
```

Integer Math ABSOLUTE.

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)


Returns
- Integer

#### Arguments:
- **value** (_Integer_) : value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### iadd()

> function

``` python
iadd(value, other)
```

Integer ADD.

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)


Returns
- Integer

#### Arguments:
- **value** (_Integer_) : first value
- **other** (_Integer_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### idivide()

> function

``` python
idivide(value, other)
```

Integer Math DIVIDE.

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)


Returns
- Integer

#### Arguments:
- **value** (_Integer_) : first value
- **other** (_Integer_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### idivide_ceiling()

> function

``` python
idivide_ceiling(value, other)
```

Integer Math DIVIDE_CEIL.

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)


Returns
- Integer

#### Arguments:
- **value** (_Integer_) : first value
- **other** (_Integer_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### idivide_floor()

> function

``` python
idivide_floor(value, other)
```

Integer Math DIVIDE_FLOOR.

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)


Returns
- Integer

#### Arguments:
- **value** (_Integer_) : first value
- **other** (_Integer_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### idivide_round()

> function

``` python
idivide_round(value, other)
```

Integer Math DIVIDE_ROUND.

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)


Returns
- Integer

#### Arguments:
- **value** (_Integer_) : first value
- **other** (_Integer_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### ifloored_modulo()

> function

``` python
ifloored_modulo(value, other)
```

Integer Math FLOORED_MODULO.

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)


Returns
- Integer

#### Arguments:
- **value** (_Integer_) : first value
- **other** (_Integer_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### imax()

> function

``` python
imax(value, other)
```

Integer Math MAXIMUM.

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)


Returns
- Integer

#### Arguments:
- **value** (_Integer_) : first value
- **other** (_Integer_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### imin()

> function

``` python
imin(value, other)
```

Integer Math MINIMUM.

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)


Returns
- Integer

#### Arguments:
- **value** (_Integer_) : first value
- **other** (_Integer_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### imodulo()

> function

``` python
imodulo(value, other)
```

Integer Math MODULO.

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)


Returns
- Integer

#### Arguments:
- **value** (_Integer_) : first value
- **other** (_Integer_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### imply()

> function

``` python
imply(value, other)
```

Boolean IMPLY.

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### imultiply()

> function

``` python
imultiply(value, other)
```

Integer Math MULTIPLY.

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)


Returns
- Integer

#### Arguments:
- **value** (_Integer_) : first value
- **other** (_Integer_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### imultiply_add()

> function

``` python
imultiply_add(value, multiplier, addend)
```

Integer Math MULTIPLY ADD.

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)


Returns
- Integer

#### Arguments:
- **value** (_Integer_) : value
- **multiplier** (_Integer_) : multiplier value
- **addend** (_Integer_) : add end value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### inegate()

> function

``` python
inegate(value)
```

Integer Math NEGATE.

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)


Returns
- Integer

#### Arguments:
- **value** (_Integer_) : value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### inverse_sqrt()

> function

``` python
inverse_sqrt(value, use_clamp=None)
```

Math INVERSE SQRT.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### ipower()

> function

``` python
ipower(base, exponent)
```

Integer Math POWER.

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)


Returns
- Integer

#### Arguments:
- **base** (_Integer_) : value
- **exponent** (_Integer_) : value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### isign()

> function

``` python
isign(value)
```

Integer Math SIGN.

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)


Returns
- Integer

#### Arguments:
- **value** (_Integer_) : value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### isubtract()

> function

``` python
isubtract(value, other)
```

Integer SUBTRACT.

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)


Returns
- Integer

#### Arguments:
- **value** (_Integer_) : first value
- **other** (_Integer_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### LCM()

> function

``` python
LCM(value, other)
```

Integer Math LCM.

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)


Returns
- Integer

#### Arguments:
- **value** (_Integer_) : first value
- **other** (_Integer_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### length()

> function

``` python
length(value)
```

Vector Math LENGTH.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Float

#### Arguments:
- **value** (_Vector_) : vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### less_than()

> function

``` python
less_than(value, threshold, use_clamp=None)
```

Math LESS_THAN.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **threshold** (_Float_) : second value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### ln()

> function

``` python
ln(value, use_clamp=None)
```

Math neperian LOGARITHM (using base = e).

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### log()

> function

``` python
log(value, base=10, use_clamp=None)
```

Math LOGARITHM.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **base** (_Float_ = 10) : second value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### math_ceil()

> function

``` python
math_ceil(value, use_clamp=None)
```

Math CEIL.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### math_floor()

> function

``` python
math_floor(value, use_clamp=None)
```

Math FLOOR.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### math_round()

> function

``` python
math_round(value, use_clamp=None)
```

Math ROUND.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### math_trunc()

> function

``` python
math_trunc(value, use_clamp=None)
```

Math TRUNC.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### max()

> function

``` python
max(value, other, use_clamp=None)
```

Math MAXIMUM.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : first value
- **other** (_Float_) : second value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### min()

> function

``` python
min(value, other, use_clamp=None)
```

Math MINIMUM.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : first value
- **other** (_Float_) : second value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### modulo()

> function

``` python
modulo(value, other, use_clamp=None)
```

Math MODULO.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **other** (_Float_) : other value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### multiply()

> function

``` python
multiply(value, other, use_clamp=None)
```

Math MULTIPLY.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : first value
- **other** (_Float_) : second value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### multiply_add()

> function

``` python
multiply_add(value, multiplier, addend, use_clamp=None)
```

Math MULTIPLY ADD.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **multiplier** (_Float_) : multiplier value
- **addend** (_Float_) : add end value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### nand()

> function

``` python
nand(value, other)
```

Boolean NAND.

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### nimply()

> function

``` python
nimply(value, other)
```

Boolean NIMPLY.

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### nor()

> function

``` python
nor(value, other)
```

Boolean NOR.

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### normalize()

> function

``` python
normalize(value)
```

Vector Math NORMALIZE.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### not_equal()

> function

``` python
not_equal(value, other)
```

Boolean XOR.

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### ping_pong()

> function

``` python
ping_pong(value, scale=None, use_clamp=None)
```

Math PINGPONG.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **scale** (_Float_ = None) : other value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### pingpong()

> function

``` python
pingpong(value, scale=None, use_clamp=None)
```

Math PINGPONG.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **scale** (_Float_ = None) : other value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### power()

> function

``` python
power(base, exponent, use_clamp=None)
```

Math POWER.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **base** (_Float_) : base value
- **exponent** (_Float_) : exponent value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### project()

> function

``` python
project(value, other)
```

Vector Math PROJECT.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### radians()

> function

``` python
radians(value, use_clamp=None)
```

Math RADIANS.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### reflect()

> function

``` python
reflect(value, other)
```

Vector Math REFLECT.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### refract()

> function

``` python
refract(value, other, ior=None)
```

Vector Math REFRACT.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector
- **ior** (_Float_ = None) : IOR

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### round()

> function

``` python
round(value, use_clamp=None)
```

Round.

> Node ERROR: Node 'Math, Float to Integer' not found

Implements 'Math' node in ShaderNodes and 'Float to Integer' for GeoNodes.

rounding_mode in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')


Returns
- Float (ShaderNodes) or Integer (GeoNodes)

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### scale()

> function

``` python
scale(value, scale)
```

Vector Math SCALE.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **scale** (_Float_) : scale factor

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### sign()

> function

``` python
sign(value)
```

Math SIGN.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### sin()

> function

``` python
sin(value, use_clamp=None)
```

Math SIN.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### sinh()

> function

``` python
sinh(value, use_clamp=None)
```

Math SINH.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### smooth_max()

> function

``` python
smooth_max(value, other, distance=None, use_clamp=None)
```

Math SMOOTH MAX.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : first value
- **other** (_Float_) : second value
- **distance** (_Float_ = None) : distance
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### smooth_min()

> function

``` python
smooth_min(value, other, distance=None, use_clamp=None)
```

Math SMOOTH_MIN.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : first value
- **other** (_Float_) : second value
- **distance** (_Float_ = None) : distance
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### snap()

> function

``` python
snap(value, increment=None, use_clamp=None)
```

Math SNAP.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **increment** (_Float_ = None) : other value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### sqrt()

> function

``` python
sqrt(value, use_clamp=None)
```

Math SQRT.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### subtract()

> function

``` python
subtract(value, other, use_clamp=None)
```

Math SUBTRACT.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : first value
- **other** (_Float_) : second value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### tan()

> function

``` python
tan(value, use_clamp=None)
```

Math TAN.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### tanh()

> function

``` python
tanh(value, use_clamp=None)
```

Math TANH.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### trunc()

> function

``` python
trunc(value, use_clamp=None)
```

Truncate.

> Node ERROR: Node 'Math, Float to Integer' not found

Implements 'Math' node in ShaderNodes and 'Float to Integer' for GeoNodes.

rounding_mode in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')


Returns
- Float (ShaderNodes) or Integer (GeoNodes)

#### Arguments:
- **value** (_Float_) : value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vabs()

> function

``` python
vabs(value)
```

Vector Math ABS.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vadd()

> function

``` python
vadd(value, other)
```

Vector Math ADD.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vceil()

> function

``` python
vceil(value)
```

Vector Math CEIL.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vcos()

> function

``` python
vcos(value)
```

Vector Math COS.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vdivide()

> function

``` python
vdivide(value, other)
```

Vector Math DIVIDE.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vfloor()

> function

``` python
vfloor(value)
```

Vector Math FLOOR.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vfract()

> function

``` python
vfract(value)
```

Vector Math FRACT.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vmax()

> function

``` python
vmax(value, other)
```

Vector Math MAXIMUM.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vmin()

> function

``` python
vmin(value, other)
```

Vector Math MINIMUM.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vmodulo()

> function

``` python
vmodulo(value, other)
```

Vector Math MODULO.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other**

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vmultiply()

> function

``` python
vmultiply(value, other)
```

Vector Math MULTIPLY.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vmultiply_add()

> function

``` python
vmultiply_add(value, multiplier, addend)
```

Vector Math MULTIPLY ADD.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **multiplier** (_Vector_) : other vector
- **addend** (_Vector_) : add end vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vsin()

> function

``` python
vsin(value)
```

Vector Math SIN.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vsnap()

> function

``` python
vsnap(value, increment)
```

Vector Math SNAP.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **increment** (_Vector_) : increment vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vsubtract()

> function

``` python
vsubtract(value, other)
```

Vector Math SUBTRACT.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **other** (_Vector_) : other vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vtan()

> function

``` python
vtan(value)
```

Vector Math TAN.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vwrap()

> function

``` python
vwrap(value, max=None, min=None)
```

Vector Math WRAP.

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)


Returns
- Vector

#### Arguments:
- **value** (_Vector_) : vector
- **max** (_Vector_ = None) : max vector
- **min** (_Vector_ = None) : min vector

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### wrap()

> function

``` python
wrap(value, max=None, min=None, use_clamp=None)
```

Math WRAP.

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)


Returns
- Float

#### Arguments:
- **value** (_Float_) : value
- **max** (_Float_ = None) : max value
- **min** (_Float_ = None) : min value
- **use_clamp** (_bool_ = None) : use_clamp flag

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### xnor()

> function

``` python
xnor(value, other)
```

Boolean XNOR.

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### xor()

> function

``` python
xor(value, other)
```

Boolean XOR.

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)


Returns
- Boolean

#### Arguments:
- **value** (_Boolean_) : first value
- **other** (_Boolean_) : second value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [gnmath](gnmath.md#gnmath)</sub>