# gnmath



## Content

- **A** : [abs](gnmath.md#abs) :black_small_square: [add](gnmath.md#add) :black_small_square: [arccosine](gnmath.md#arccosine) :black_small_square: [arcsine](gnmath.md#arcsine) :black_small_square: [arctan2](gnmath.md#arctan2) :black_small_square: [arctangent](gnmath.md#arctangent)
- **B** : [band](gnmath.md#band) :black_small_square: [bnot](gnmath.md#bnot) :black_small_square: [bor](gnmath.md#bor)
- **C** : [ceil](gnmath.md#ceil) :black_small_square: [compare](gnmath.md#compare) :black_small_square: [cos](gnmath.md#cos) :black_small_square: [cosh](gnmath.md#cosh) :black_small_square: [cross](gnmath.md#cross)
- **D** : [degrees](gnmath.md#degrees) :black_small_square: [distance](gnmath.md#distance) :black_small_square: [divide](gnmath.md#divide) :black_small_square: [divide_ceil](gnmath.md#divide_ceil) :black_small_square: [divide_floor](gnmath.md#divide_floor) :black_small_square: [divide_round](gnmath.md#divide_round) :black_small_square: [dot](gnmath.md#dot)
- **E** : [exp](gnmath.md#exp)
- **F** : [faceforward](gnmath.md#faceforward) :black_small_square: [floor](gnmath.md#floor) :black_small_square: [floored_modulo](gnmath.md#floored_modulo) :black_small_square: [fract](gnmath.md#fract)
- **G** : [gcd](gnmath.md#gcd)
- **I** : [iabs](gnmath.md#iabs) :black_small_square: [iadd](gnmath.md#iadd) :black_small_square: [idivide](gnmath.md#idivide) :black_small_square: [ifloored_modulo](gnmath.md#ifloored_modulo) :black_small_square: [imax](gnmath.md#imax) :black_small_square: [imin](gnmath.md#imin) :black_small_square: [imodulo](gnmath.md#imodulo) :black_small_square: [imply](gnmath.md#imply) :black_small_square: [imultiply](gnmath.md#imultiply) :black_small_square: [imultiply_add](gnmath.md#imultiply_add) :black_small_square: [inverse_sqrt](gnmath.md#inverse_sqrt) :black_small_square: [ipower](gnmath.md#ipower) :black_small_square: [isign](gnmath.md#isign) :black_small_square: [isubtract](gnmath.md#isubtract)
- **L** : [lcm](gnmath.md#lcm) :black_small_square: [length](gnmath.md#length) :black_small_square: [log](gnmath.md#log)
- **M** : [max](gnmath.md#max) :black_small_square: [mgreater_than](gnmath.md#mgreater_than) :black_small_square: [min](gnmath.md#min) :black_small_square: [mless_than](gnmath.md#mless_than) :black_small_square: [modulo](gnmath.md#modulo) :black_small_square: [multiply](gnmath.md#multiply) :black_small_square: [multiply_add](gnmath.md#multiply_add)
- **N** : [negate](gnmath.md#negate) :black_small_square: [nimply](gnmath.md#nimply) :black_small_square: [nor](gnmath.md#nor) :black_small_square: [normalize](gnmath.md#normalize) :black_small_square: [not_and](gnmath.md#not_and)
- **P** : [pingpong](gnmath.md#pingpong) :black_small_square: [power](gnmath.md#power) :black_small_square: [project](gnmath.md#project)
- **R** : [radians](gnmath.md#radians) :black_small_square: [reflect](gnmath.md#reflect) :black_small_square: [refract](gnmath.md#refract) :black_small_square: [round](gnmath.md#round)
- **S** : [scale](gnmath.md#scale) :black_small_square: [sign](gnmath.md#sign) :black_small_square: [sin](gnmath.md#sin) :black_small_square: [sinh](gnmath.md#sinh) :black_small_square: [smooth_max](gnmath.md#smooth_max) :black_small_square: [smooth_min](gnmath.md#smooth_min) :black_small_square: [snap](gnmath.md#snap) :black_small_square: [sqrt](gnmath.md#sqrt) :black_small_square: [subtract](gnmath.md#subtract)
- **T** : [tan](gnmath.md#tan) :black_small_square: [tanh](gnmath.md#tanh) :black_small_square: [trunc](gnmath.md#trunc)
- **V** : [vabs](gnmath.md#vabs) :black_small_square: [vadd](gnmath.md#vadd) :black_small_square: [vceil](gnmath.md#vceil) :black_small_square: [vcos](gnmath.md#vcos) :black_small_square: [vdivide](gnmath.md#vdivide) :black_small_square: [vfloor](gnmath.md#vfloor) :black_small_square: [vfraction](gnmath.md#vfraction) :black_small_square: [vmax](gnmath.md#vmax) :black_small_square: [vmin](gnmath.md#vmin) :black_small_square: [vmodulo](gnmath.md#vmodulo) :black_small_square: [vmultiply](gnmath.md#vmultiply) :black_small_square: [vmultiply_add](gnmath.md#vmultiply_add) :black_small_square: [vsin](gnmath.md#vsin) :black_small_square: [vsnap](gnmath.md#vsnap) :black_small_square: [vsubtract](gnmath.md#vsubtract) :black_small_square: [vtan](gnmath.md#vtan) :black_small_square: [vwrap](gnmath.md#vwrap)
- **W** : [wrap](gnmath.md#wrap)
- **X** : [xnor](gnmath.md#xnor) :black_small_square: [xor](gnmath.md#xor)

## Functions



----------
### abs()

> function

``` python
abs(value=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'ABSOLUTE'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### add()

> function

``` python
add(value=None, value_1=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'ADD'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **value_1** (_Float_ = None) : socket 'Value' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### arccosine()

> function

``` python
arccosine(value=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'ARCCOSINE'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### arcsine()

> function

``` python
arcsine(value=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'ARCSINE'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### arctan2()

> function

``` python
arctan2(value=None, value_1=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'ARCTAN2'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **value_1** (_Float_ = None) : socket 'Value' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### arctangent()

> function

``` python
arctangent(value=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'ARCTANGENT'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### band()

> function

``` python
band(boolean=None, boolean_1=None)
```

> Function [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

Information
-----------
- Parameter 'operation' : 'AND'

#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean)
- **boolean_1** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### bnot()

> function

``` python
bnot(boolean=None)
```

> Function [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

Information
-----------
- Parameter 'operation' : 'NOT'

#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### bor()

> function

``` python
bor(boolean=None, boolean_1=None)
```

> Function [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

Information
-----------
- Parameter 'operation' : 'OR'

#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean)
- **boolean_1** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### ceil()

> function

``` python
ceil(value=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'CEIL'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### compare()

> function

``` python
compare(value=None, value_1=None, epsilon=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'COMPARE'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **value_1** (_Float_ = None) : socket 'Value' (id: Value_001)
- **epsilon** (_Float_ = None) : socket 'Epsilon' (id: Value_002)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### cos()

> function

``` python
cos(value=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'COSINE'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### cosh()

> function

``` python
cosh(value=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'COSH'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### cross()

> function

``` python
cross(vector=None, vector_1=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'CROSS_PRODUCT'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **vector_1** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### degrees()

> function

``` python
degrees(radians=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'DEGREES'

#### Arguments:
- **radians** (_Float_ = None) : socket 'Radians' (id: Value)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### distance()

> function

``` python
distance(vector=None, vector_1=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'DISTANCE'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **vector_1** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### divide()

> function

``` python
divide(value=None, value_1=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'DIVIDE'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **value_1** (_Float_ = None) : socket 'Value' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### divide_ceil()

> function

``` python
divide_ceil(value=None, value_1=None)
```

> Function [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

Information
-----------
- Parameter 'operation' : 'DIVIDE_CEIL'

#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value)
- **value_1** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### divide_floor()

> function

``` python
divide_floor(value=None, value_1=None)
```

> Function [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

Information
-----------
- Parameter 'operation' : 'DIVIDE_FLOOR'

#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value)
- **value_1** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### divide_round()

> function

``` python
divide_round(value=None, value_1=None)
```

> Function [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

Information
-----------
- Parameter 'operation' : 'DIVIDE_ROUND'

#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value)
- **value_1** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### dot()

> function

``` python
dot(vector=None, vector_1=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'DOT_PRODUCT'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **vector_1** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### exp()

> function

``` python
exp(value=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'EXPONENT'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### faceforward()

> function

``` python
faceforward(vector=None, incident=None, reference=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'FACEFORWARD'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **incident** (_Vector_ = None) : socket 'Incident' (id: Vector_001)
- **reference** (_Vector_ = None) : socket 'Reference' (id: Vector_002)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### floor()

> function

``` python
floor(value=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'FLOOR'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### floored_modulo()

> function

``` python
floored_modulo(value=None, value_1=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'FLOORED_MODULO'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **value_1** (_Float_ = None) : socket 'Value' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### fract()

> function

``` python
fract(value=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'FRACT'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### gcd()

> function

``` python
gcd(value=None, value_1=None)
```

> Function [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

Information
-----------
- Parameter 'operation' : 'GCD'

#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value)
- **value_1** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### iabs()

> function

``` python
iabs(value=None)
```

> Function [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

Information
-----------
- Parameter 'operation' : 'ABSOLUTE'

#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### iadd()

> function

``` python
iadd(value=None, value_1=None)
```

> Function [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

Information
-----------
- Parameter 'operation' : 'ADD'

#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value)
- **value_1** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### idivide()

> function

``` python
idivide(value=None, value_1=None)
```

> Function [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

Information
-----------
- Parameter 'operation' : 'DIVIDE'

#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value)
- **value_1** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### ifloored_modulo()

> function

``` python
ifloored_modulo(value=None, value_1=None)
```

> Function [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

Information
-----------
- Parameter 'operation' : 'FLOORED_MODULO'

#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value)
- **value_1** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### imax()

> function

``` python
imax(value=None, value_1=None)
```

> Function [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

Information
-----------
- Parameter 'operation' : 'MAXIMUM'

#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value)
- **value_1** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### imin()

> function

``` python
imin(value=None, value_1=None)
```

> Function [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

Information
-----------
- Parameter 'operation' : 'MINIMUM'

#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value)
- **value_1** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### imodulo()

> function

``` python
imodulo(value=None, value_1=None)
```

> Function [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

Information
-----------
- Parameter 'operation' : 'MODULO'

#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value)
- **value_1** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### imply()

> function

``` python
imply(boolean=None, boolean_1=None)
```

> Function [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

Information
-----------
- Parameter 'operation' : 'IMPLY'

#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean)
- **boolean_1** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### imultiply()

> function

``` python
imultiply(value=None, value_1=None)
```

> Function [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

Information
-----------
- Parameter 'operation' : 'MULTIPLY'

#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value)
- **value_1** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### imultiply_add()

> function

``` python
imultiply_add(value=None, multiplier=None, addend=None)
```

> Function [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

Information
-----------
- Parameter 'operation' : 'MULTIPLY_ADD'

#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value)
- **multiplier** (_Integer_ = None) : socket 'Multiplier' (id: Value_001)
- **addend** (_Integer_ = None) : socket 'Addend' (id: Value_002)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### inverse_sqrt()

> function

``` python
inverse_sqrt(value=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'INVERSE_SQRT'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### ipower()

> function

``` python
ipower(base=None, exponent=None)
```

> Function [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

Information
-----------
- Parameter 'operation' : 'POWER'

#### Arguments:
- **base** (_Integer_ = None) : socket 'Base' (id: Value)
- **exponent** (_Integer_ = None) : socket 'Exponent' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### isign()

> function

``` python
isign(value=None)
```

> Function [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

Information
-----------
- Parameter 'operation' : 'SIGN'

#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### isubtract()

> function

``` python
isubtract(value=None, value_1=None)
```

> Function [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

Information
-----------
- Parameter 'operation' : 'SUBTRACT'

#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value)
- **value_1** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### lcm()

> function

``` python
lcm(value=None, value_1=None)
```

> Function [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

Information
-----------
- Parameter 'operation' : 'LCM'

#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value)
- **value_1** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### length()

> function

``` python
length(vector=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'LENGTH'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### log()

> function

``` python
log(value=None, base=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'LOGARITHM'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **base** (_Float_ = None) : socket 'Base' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### max()

> function

``` python
max(value=None, value_1=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'MAXIMUM'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **value_1** (_Float_ = None) : socket 'Value' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### mgreater_than()

> function

``` python
mgreater_than(value=None, threshold=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'GREATER_THAN'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **threshold** (_Float_ = None) : socket 'Threshold' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### min()

> function

``` python
min(value=None, value_1=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'MINIMUM'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **value_1** (_Float_ = None) : socket 'Value' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### mless_than()

> function

``` python
mless_than(value=None, threshold=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'LESS_THAN'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **threshold** (_Float_ = None) : socket 'Threshold' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### modulo()

> function

``` python
modulo(value=None, value_1=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'MODULO'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **value_1** (_Float_ = None) : socket 'Value' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### multiply()

> function

``` python
multiply(value=None, value_1=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'MULTIPLY'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **value_1** (_Float_ = None) : socket 'Value' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### multiply_add()

> function

``` python
multiply_add(value=None, multiplier=None, addend=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'MULTIPLY_ADD'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **multiplier** (_Float_ = None) : socket 'Multiplier' (id: Value_001)
- **addend** (_Float_ = None) : socket 'Addend' (id: Value_002)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### negate()

> function

``` python
negate(value=None)
```

> Function [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

Information
-----------
- Parameter 'operation' : 'NEGATE'

#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### nimply()

> function

``` python
nimply(boolean=None, boolean_1=None)
```

> Function [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

Information
-----------
- Parameter 'operation' : 'NIMPLY'

#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean)
- **boolean_1** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### nor()

> function

``` python
nor(boolean=None, boolean_1=None)
```

> Function [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

Information
-----------
- Parameter 'operation' : 'NOR'

#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean)
- **boolean_1** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### normalize()

> function

``` python
normalize(vector=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'NORMALIZE'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### not_and()

> function

``` python
not_and(boolean=None, boolean_1=None)
```

> Function [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

Information
-----------
- Parameter 'operation' : 'NAND'

#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean)
- **boolean_1** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### pingpong()

> function

``` python
pingpong(value=None, scale=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'PINGPONG'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **scale** (_Float_ = None) : socket 'Scale' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### power()

> function

``` python
power(base=None, exponent=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'POWER'

#### Arguments:
- **base** (_Float_ = None) : socket 'Base' (id: Value)
- **exponent** (_Float_ = None) : socket 'Exponent' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### project()

> function

``` python
project(vector=None, vector_1=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'PROJECT'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **vector_1** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### radians()

> function

``` python
radians(degrees=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'RADIANS'

#### Arguments:
- **degrees** (_Float_ = None) : socket 'Degrees' (id: Value)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### reflect()

> function

``` python
reflect(vector=None, vector_1=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'REFLECT'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **vector_1** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### refract()

> function

``` python
refract(vector=None, vector_1=None, ior=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'REFRACT'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **vector_1** (_Vector_ = None) : socket 'Vector' (id: Vector_001)
- **ior** (_Float_ = None) : socket 'IOR' (id: Scale)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### round()

> function

``` python
round(value=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'ROUND'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### scale()

> function

``` python
scale(vector=None, scale=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'SCALE'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### sign()

> function

``` python
sign(value=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'SIGN'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### sin()

> function

``` python
sin(value=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'SINE'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### sinh()

> function

``` python
sinh(value=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'SINH'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### smooth_max()

> function

``` python
smooth_max(value=None, value_1=None, distance=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'SMOOTH_MAX'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **value_1** (_Float_ = None) : socket 'Value' (id: Value_001)
- **distance** (_Float_ = None) : socket 'Distance' (id: Value_002)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### smooth_min()

> function

``` python
smooth_min(value=None, value_1=None, distance=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'SMOOTH_MIN'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **value_1** (_Float_ = None) : socket 'Value' (id: Value_001)
- **distance** (_Float_ = None) : socket 'Distance' (id: Value_002)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### snap()

> function

``` python
snap(value=None, increment=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'SNAP'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **increment** (_Float_ = None) : socket 'Increment' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### sqrt()

> function

``` python
sqrt(value=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'SQRT'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### subtract()

> function

``` python
subtract(value=None, value_1=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'SUBTRACT'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **value_1** (_Float_ = None) : socket 'Value' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### tan()

> function

``` python
tan(value=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'TANGENT'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### tanh()

> function

``` python
tanh(value=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'TANH'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### trunc()

> function

``` python
trunc(value=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'TRUNC'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vabs()

> function

``` python
vabs(vector=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'ABSOLUTE'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vadd()

> function

``` python
vadd(vector=None, vector_1=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'ADD'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **vector_1** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vceil()

> function

``` python
vceil(vector=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'CEIL'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vcos()

> function

``` python
vcos(vector=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'COSINE'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vdivide()

> function

``` python
vdivide(vector=None, vector_1=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'DIVIDE'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **vector_1** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vfloor()

> function

``` python
vfloor(vector=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'FLOOR'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vfraction()

> function

``` python
vfraction(vector=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'FRACTION'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vmax()

> function

``` python
vmax(vector=None, vector_1=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'MAXIMUM'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **vector_1** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vmin()

> function

``` python
vmin(vector=None, vector_1=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'MINIMUM'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **vector_1** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vmodulo()

> function

``` python
vmodulo(vector=None, vector_1=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'MODULO'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **vector_1** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vmultiply()

> function

``` python
vmultiply(vector=None, vector_1=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'MULTIPLY'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **vector_1** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vmultiply_add()

> function

``` python
vmultiply_add(vector=None, multiplier=None, addend=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'MULTIPLY_ADD'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **multiplier** (_Vector_ = None) : socket 'Multiplier' (id: Vector_001)
- **addend** (_Vector_ = None) : socket 'Addend' (id: Vector_002)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vsin()

> function

``` python
vsin(vector=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'SINE'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vsnap()

> function

``` python
vsnap(vector=None, increment=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'SNAP'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **increment** (_Vector_ = None) : socket 'Increment' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vsubtract()

> function

``` python
vsubtract(vector=None, vector_1=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'SUBTRACT'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **vector_1** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vtan()

> function

``` python
vtan(vector=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'TANGENT'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### vwrap()

> function

``` python
vwrap(vector=None, max=None, min=None)
```

> Function [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

Information
-----------
- Parameter 'operation' : 'WRAP'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **max** (_Vector_ = None) : socket 'Max' (id: Vector_001)
- **min** (_Vector_ = None) : socket 'Min' (id: Vector_002)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### wrap()

> function

``` python
wrap(value=None, max=None, min=None, use_clamp=False)
```

> Function [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

Information
-----------
- Parameter 'operation' : 'WRAP'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **max** (_Float_ = None) : socket 'Max' (id: Value_001)
- **min** (_Float_ = None) : socket 'Min' (id: Value_002)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### xnor()

> function

``` python
xnor(boolean=None, boolean_1=None)
```

> Function [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

Information
-----------
- Parameter 'operation' : 'XNOR'

#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean)
- **boolean_1** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

----------
### xor()

> function

``` python
xor(boolean=None, boolean_1=None)
```

> Function [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

Information
-----------
- Parameter 'operation' : 'XOR'

#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean)
- **boolean_1** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [Functions](gnmath.md#functions)</sub>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [gnmath](gnmath.md#gnmath) :black_small_square: [Content](gnmath.md#content) :black_small_square: [gnmath](gnmath.md#gnmath)</sub>