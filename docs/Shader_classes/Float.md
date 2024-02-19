# class Float (Socket)

<sub>go to [index](/docs/index.md)</sub>

Socket
 - Type : VALUE
 - bl_idname : NodeSocketFloat

Methods
 - [abs](#abs) : Math, value=self, operation='ABSOLUTE'
 - [add](#add) : Math, value=self, operation='ADD'
 - [arccos](#arccos) : Math, value=self, operation='ARCCOSINE'
 - [arcsin](#arcsin) : Math, value=self, operation='ARCSINE'
 - [arctan](#arctan) : Math, value=self, operation='ARCTANGENT'
 - [arctan2](#arctan2) : Math, value=self, operation='ARCTAN2'
 - [blackbody](#blackbody) : Blackbody, temperature=self, return socket
 - [ceil](#ceil) : Math, value=self, operation='CEIL'
 - [clamp](#clamp) : Clamp, value=self
 - [color_ramp](#color_ramp) : ColorRamp, fac=self
 - [compare](#compare) : Math, value=self, operation='COMPARE'
 - [cos](#cos) : Math, value=self, operation='COSINE'
 - [cosh](#cosh) : Math, value=self, operation='COSH'
 - [degrees](#degrees) : Math, value=self, operation='DEGREES'
 - [divide](#divide) : Math, value=self, operation='DIVIDE'
 - [exp](#exp) : Math, value=self, operation='EXPONENT'
 - [float_curve](#float_curve) : FloatCurve, value=self
 - [floor](#floor) : Math, value=self, operation='FLOOR'
 - [floored_modulo](#floored_modulo) : Math, value=self, operation='FLOORED_MODULO'
 - [fract](#fract) : Math, value=self, operation='FRACT'
 - [fresnel](#fresnel) : Fresnel, ior=self
 - [greater_than](#greater_than) : Math, value=self, operation='GREATER_THAN'
 - [ies_texture](#ies_texture) : IESTexture, strength=self
 - [inverse_sqrt](#inverse_sqrt) : Math, value=self, operation='INVERSE_SQRT'
 - [layer_weight](#layer_weight) : LayerWeight, blend=self
 - [less_than](#less_than) : Math, value=self, operation='LESS_THAN'
 - [light_falloff](#light_falloff) : LightFalloff, strength=self
 - [log](#log) : Math, value=self, operation='LOGARITHM'
 - [map_range](#map_range) : MapRange, value=self
 - [math](#math) : Math, value=self
 - [max](#max) : Math, value=self, operation='MAXIMUM'
 - [min](#min) : Math, value=self, operation='MINIMUM'
 - [mix](#mix) : Mix, a=self, data_type='FLOAT'
 - [mod](#mod) : Math, value=self, operation='MODULO'
 - [multiply](#multiply) : Math, value=self, operation='MULTIPLY'
 - [multiply_add](#multiply_add) : Math, value=self, operation='MULTIPLY_ADD'
 - [pingpong](#pingpong) : Math, value=self, operation='PINGPONG'
 - [power](#power) : Math, value=self, operation='POWER'
 - [radians](#radians) : Math, value=self, operation='RADIANS'
 - [round](#round) : Math, value=self, operation='ROUND'
 - [sign](#sign) : Math, value=self, operation='SIGN'
 - [sin](#sin) : Math, value=self, operation='SINE'
 - [sinh](#sinh) : Math, value=self, operation='SINH'
 - [smooth_max](#smooth_max) : Math, value=self, operation='SMOOTH_MAX'
 - [smooth_min](#smooth_min) : Math, value=self, operation='SMOOTH_MIN'
 - [snap](#snap) : Math, value=self, operation='SNAP'
 - [sqrt](#sqrt) : Math, value=self, operation='SQRT'
 - [subtract](#subtract) : Math, value=self, operation='SUBTRACT'
 - [tan](#tan) : Math, value=self, operation='TANGENT'
 - [tanh](#tanh) : Math, value=self, operation='TANH'
 - [trunc](#trunc) : Math, value=self, operation='TRUNC'
 - [wavelength](#wavelength) : Wavelength, wavelength=self, return socket
 - [wireframe](#wireframe) : Wireframe, size=self
 - [wrap](#wrap) : Math, value=self, operation='WRAP'

## Methods

### abs

> Math, value=self, operation='ABSOLUTE'

``` python
def abs(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'ABSOLUTE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### add

> Math, value=self, operation='ADD'

``` python
def add(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'ADD'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### arccos

> Math, value=self, operation='ARCCOSINE'

``` python
def arccos(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'ARCCOSINE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### arcsin

> Math, value=self, operation='ARCSINE'

``` python
def arcsin(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'ARCSINE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### arctan

> Math, value=self, operation='ARCTANGENT'

``` python
def arctan(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'ARCTANGENT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### arctan2

> Math, value=self, operation='ARCTAN2'

``` python
def arctan2(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'ARCTAN2'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### blackbody

> Blackbody, temperature=self, return socket

``` python
def blackbody(self, node_label=None, node_color=None):
```
Node
 - class_name : [Blackbody](/docs/Shader_classes/Blackbody.md)
 - bl_idname : ShaderNodeBlackbody

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - temperature : self
 - node_label : node_label
 - node_color : node_color

### ceil

> Math, value=self, operation='CEIL'

``` python
def ceil(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'CEIL'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### clamp

> Clamp, value=self

``` python
def clamp(self, min=None, max=None, clamp_type='MINMAX', node_label=None, node_color=None):
```
Node
 - class_name : [Clamp](/docs/Shader_classes/Clamp.md)
 - bl_idname : ShaderNodeClamp

Arguments
 - min : None
 - max : None
 - clamp_type : 'MINMAX'
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - min : min
 - max : max
 - clamp_type : clamp_type
 - node_label : node_label
 - node_color : node_color

### color_ramp

> ColorRamp, fac=self

``` python
def color_ramp(self, color_ramp=None, node_label=None, node_color=None):
```
Node
 - class_name : [ColorRamp](/docs/Shader_classes/ColorRamp.md)
 - bl_idname : ShaderNodeValToRGB

Arguments
 - color_ramp
 - node_label : None
 - node_color : None

Node initialization
 - fac : self
 - color_ramp : color_ramp
 - node_label : node_label
 - node_color : node_color

### compare

> Math, value=self, operation='COMPARE'

``` python
def compare(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - value_2 : value_1
 - operation : 'COMPARE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### cos

> Math, value=self, operation='COSINE'

``` python
def cos(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'COSINE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### cosh

> Math, value=self, operation='COSH'

``` python
def cosh(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'COSH'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### degrees

> Math, value=self, operation='DEGREES'

``` python
def degrees(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'DEGREES'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### divide

> Math, value=self, operation='DIVIDE'

``` python
def divide(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'DIVIDE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### exp

> Math, value=self, operation='EXPONENT'

``` python
def exp(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'EXPONENT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### float_curve

> FloatCurve, value=self

``` python
def float_curve(self, factor=None, mapping=None, node_label=None, node_color=None):
```
Node
 - class_name : [FloatCurve](/docs/Shader_classes/FloatCurve.md)
 - bl_idname : ShaderNodeFloatCurve

Arguments
 - factor : None
 - mapping
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - value : self
 - mapping : mapping
 - node_label : node_label
 - node_color : node_color

### floor

> Math, value=self, operation='FLOOR'

``` python
def floor(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'FLOOR'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### floored_modulo

> Math, value=self, operation='FLOORED_MODULO'

``` python
def floored_modulo(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'FLOORED_MODULO'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### fract

> Math, value=self, operation='FRACT'

``` python
def fract(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'FRACT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### fresnel

> Fresnel, ior=self

``` python
def fresnel(self, normal=None, node_label=None, node_color=None):
```
Node
 - class_name : [Fresnel](/docs/Shader_classes/Fresnel.md)
 - bl_idname : ShaderNodeFresnel

Arguments
 - normal : None
 - node_label : None
 - node_color : None

Node initialization
 - ior : self
 - normal : normal
 - node_label : node_label
 - node_color : node_color

### greater_than

> Math, value=self, operation='GREATER_THAN'

``` python
def greater_than(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'GREATER_THAN'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### ies_texture

> IESTexture, strength=self

``` python
def ies_texture(self, vector=None, filepath='', ies=None, mode='INTERNAL', node_label=None, node_color=None):
```
Node
 - class_name : [IESTexture](/docs/Shader_classes/IESTexture.md)
 - bl_idname : ShaderNodeTexIES

Arguments
 - vector : None
 - filepath : ''
 - ies : None
 - mode : 'INTERNAL'
 - node_label : None
 - node_color : None

Node initialization
 - vector : vector
 - strength : self
 - filepath : filepath
 - ies : ies
 - mode : mode
 - node_label : node_label
 - node_color : node_color

### inverse_sqrt

> Math, value=self, operation='INVERSE_SQRT'

``` python
def inverse_sqrt(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'INVERSE_SQRT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### layer_weight

> LayerWeight, blend=self

``` python
def layer_weight(self, normal=None, node_label=None, node_color=None):
```
Node
 - class_name : [LayerWeight](/docs/Shader_classes/LayerWeight.md)
 - bl_idname : ShaderNodeLayerWeight

Arguments
 - normal : None
 - node_label : None
 - node_color : None

Node initialization
 - blend : self
 - normal : normal
 - node_label : node_label
 - node_color : node_color

### less_than

> Math, value=self, operation='LESS_THAN'

``` python
def less_than(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'LESS_THAN'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### light_falloff

> LightFalloff, strength=self

``` python
def light_falloff(self, smooth=None, node_label=None, node_color=None):
```
Node
 - class_name : [LightFalloff](/docs/Shader_classes/LightFalloff.md)
 - bl_idname : ShaderNodeLightFalloff

Arguments
 - smooth : None
 - node_label : None
 - node_color : None

Node initialization
 - strength : self
 - smooth : smooth
 - node_label : node_label
 - node_color : node_color

### log

> Math, value=self, operation='LOGARITHM'

``` python
def log(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'LOGARITHM'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### map_range

> MapRange, value=self

``` python
def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, vector=None, steps=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR', node_label=None, node_color=None):
```
Node
 - class_name : [MapRange](/docs/Shader_classes/MapRange.md)
 - bl_idname : ShaderNodeMapRange

Arguments
 - from_min : None
 - from_max : None
 - to_min : None
 - to_max : None
 - vector : None
 - steps : None
 - clamp : True
 - data_type : 'FLOAT'
 - interpolation_type : 'LINEAR'
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - from_min : from_min
 - from_max : from_max
 - to_min : to_min
 - to_max : to_max
 - vector : vector
 - steps : steps
 - clamp : clamp
 - data_type : data_type
 - interpolation_type : interpolation_type
 - node_label : node_label
 - node_color : node_color

### math

> Math, value=self

``` python
def math(self, value=None, value_1=None, operation='ADD', use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - operation : 'ADD'
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - value_2 : value_1
 - operation : operation
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### max

> Math, value=self, operation='MAXIMUM'

``` python
def max(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'MAXIMUM'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### min

> Math, value=self, operation='MINIMUM'

``` python
def min(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'MINIMUM'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### mix

> Mix, a=self, data_type='FLOAT'

``` python
def mix(self, factor=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/Shader_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - b : None
 - blend_type : 'MIX'
 - clamp_factor : True
 - clamp_result : False
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : self
 - b : b
 - blend_type : blend_type
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : 'FLOAT'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

### mod

> Math, value=self, operation='MODULO'

``` python
def mod(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'MODULO'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### multiply

> Math, value=self, operation='MULTIPLY'

``` python
def multiply(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'MULTIPLY'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### multiply_add

> Math, value=self, operation='MULTIPLY_ADD'

``` python
def multiply_add(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - value_2 : value_1
 - operation : 'MULTIPLY_ADD'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### pingpong

> Math, value=self, operation='PINGPONG'

``` python
def pingpong(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'PINGPONG'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### power

> Math, value=self, operation='POWER'

``` python
def power(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'POWER'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### radians

> Math, value=self, operation='RADIANS'

``` python
def radians(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'RADIANS'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### round

> Math, value=self, operation='ROUND'

``` python
def round(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'ROUND'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### sign

> Math, value=self, operation='SIGN'

``` python
def sign(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'SIGN'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### sin

> Math, value=self, operation='SINE'

``` python
def sin(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'SINE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### sinh

> Math, value=self, operation='SINH'

``` python
def sinh(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'SINH'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### smooth_max

> Math, value=self, operation='SMOOTH_MAX'

``` python
def smooth_max(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - value_2 : value_1
 - operation : 'SMOOTH_MAX'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### smooth_min

> Math, value=self, operation='SMOOTH_MIN'

``` python
def smooth_min(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - value_2 : value_1
 - operation : 'SMOOTH_MIN'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### snap

> Math, value=self, operation='SNAP'

``` python
def snap(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'SNAP'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### sqrt

> Math, value=self, operation='SQRT'

``` python
def sqrt(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'SQRT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### subtract

> Math, value=self, operation='SUBTRACT'

``` python
def subtract(self, value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - operation : 'SUBTRACT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### tan

> Math, value=self, operation='TANGENT'

``` python
def tan(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'TANGENT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### tanh

> Math, value=self, operation='TANH'

``` python
def tanh(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'TANH'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### trunc

> Math, value=self, operation='TRUNC'

``` python
def trunc(self, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - operation : 'TRUNC'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

### wavelength

> Wavelength, wavelength=self, return socket

``` python
def wavelength(self, node_label=None, node_color=None):
```
Node
 - class_name : [Wavelength](/docs/Shader_classes/Wavelength.md)
 - bl_idname : ShaderNodeWavelength

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - wavelength : self
 - node_label : node_label
 - node_color : node_color

### wireframe

> Wireframe, size=self

``` python
def wireframe(self, use_pixel_size=False, node_label=None, node_color=None):
```
Node
 - class_name : [Wireframe](/docs/Shader_classes/Wireframe.md)
 - bl_idname : ShaderNodeWireframe

Arguments
 - use_pixel_size : False
 - node_label : None
 - node_color : None

Node initialization
 - size : self
 - use_pixel_size : use_pixel_size
 - node_label : node_label
 - node_color : node_color

### wrap

> Math, value=self, operation='WRAP'

``` python
def wrap(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : self
 - value_1 : value
 - value_2 : value_1
 - operation : 'WRAP'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color
