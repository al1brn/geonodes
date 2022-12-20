# class Float

## Properties

- [color_ramp](#color_ramp-property)

## Class methods

- [Frame](#Frame-classmethod)
- [Seconds](#Seconds-classmethod)
- [Value](#Value-classmethod)


## Methods

- [abs](#abs)
- [absolute](#absolute)
- [arccos](#arccos)
- [arccosine](#arccosine)
- [arcsin](#arcsin)
- [arcsine](#arcsine)
- [arctan](#arctan)
- [arctan2](#arctan2)
- [arctangent](#arctangent)
- [ceiling](#ceiling)
- [clamp](#clamp)
- [clamp_min_max](#clamp_min_max)
- [clamp_range](#clamp_range)
- [compare](#compare)
- [cos](#cos)
- [cosh](#cosh)
- [cosine](#cosine)
- [equal](#equal)
- [exp](#exp)
- [exponent](#exponent)
- [fact](#fact)
- [float_curve](#float_curve)
- [floor](#floor)
- [fraction](#fraction)
- [greater_equal](#greater_equal)
- [greater_than](#greater_than)
- [inverse_sqrt](#inverse_sqrt)
- [less_equal](#less_equal)
- [less_than](#less_than)
- [log](#log)
- [logarithm](#logarithm)
- [map_range](#map_range)
- [map_range_linear](#map_range_linear)
- [map_range_smooth](#map_range_smooth)
- [map_range_smoother](#map_range_smoother)
- [map_range_stepped](#map_range_stepped)
- [math_ceil](#math_ceil)
- [math_compare](#math_compare)
- [math_floor](#math_floor)
- [math_greater_than](#math_greater_than)
- [math_less_than](#math_less_than)
- [math_round](#math_round)
- [math_trunc](#math_trunc)
- [math_truncate](#math_truncate)
- [max](#max)
- [maximum](#maximum)
- [min](#min)
- [minimum](#minimum)
- [mix](#mix)
- [modulo](#modulo)
- [mul_add](#mul_add)
- [multiply_add](#multiply_add)
- [not_equal](#not_equal)
- [ping_pong](#ping_pong)
- [pow](#pow)
- [power](#power)
- [round](#round)
- [sign](#sign)
- [sin](#sin)
- [sine](#sine)
- [sinh](#sinh)
- [smooth_maximum](#smooth_maximum)
- [smooth_minimum](#smooth_minimum)
- [snap](#snap)
- [sqrt](#sqrt)
- [switch](#switch)
- [tan](#tan)
- [tangent](#tangent)
- [tanh](#tanh)
- [to_degrees](#to_degrees)
- [to_integer](#to_integer)
- [to_radians](#to_radians)
- [to_string](#to_string)
- [truncate](#truncate)
- [wrap](#wrap)

## Frame *classmethod*

{#Frame}

> def Frame(cls):

Node [Scene Time](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene_time.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html) )

### Returns:

  socket 'frame'

## Seconds *classmethod*

{#Seconds}

> def Seconds(cls):

Node [Scene Time](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene_time.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html) )

### Returns:

  socket 'seconds'

## Value *classmethod*

{#Value}

> def Value(cls):

Node [Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/value.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeValue.html) )

### Returns:

  socket 'value'

## abs

{#abs}

> def abs(self, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## absolute

{#absolute}

> def absolute(self, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## arccos

{#arccos}

> def arccos(self, value=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## arccosine

{#arccosine}

> def arccosine(self, value=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## arcsin

{#arcsin}

> def arcsin(self, value=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## arcsine

{#arcsine}

> def arcsine(self, value=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## arctan

{#arctan}

> def arctan(self, value=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## arctan2

{#arctan2}

> def arctan2(self, value1=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value1: Float
- clamp (bool): False

### Returns:

  socket 'value'

## arctangent

{#arctangent}

> def arctangent(self, value=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## ceiling

{#ceiling}

> def ceiling(self):

Node [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html) )

### Returns:

  socket 'integer'

## clamp

{#clamp}

> def clamp(self, min=None, max=None, clamp_type='MINMAX'):

Node [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html) )

        ### Args:
- min: Float
- max: Float
- clamp_type (str): 'MINMAX' in [MINMAX, RANGE]

### Returns:

  socket 'result'

## clamp_min_max

{#clamp_min_max}

> def clamp_min_max(self, min=None, max=None):

Node [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html) )

        ### Args:
- min: Float
- max: Float

### Returns:

  socket 'result'

## clamp_range

{#clamp_range}

> def clamp_range(self, min=None, max=None):

Node [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html) )

        ### Args:
- min: Float
- max: Float

### Returns:

  socket 'result'

## color_ramp *property*

{#color_ramp}

> def color_ramp(self):

Node [ColorRamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/color_ramp.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html) )

Node implemented as property.

### Returns:

- node with sockets ['color', 'alpha']

## compare

{#compare}

> def compare(self, b=None, epsilon=None, operation='GREATER_THAN'):

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float
- operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

### Returns:

  socket 'result'

## cos

{#cos}

> def cos(self, value=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## cosh

{#cosh}

> def cosh(self, value=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## cosine

{#cosine}

> def cosine(self, value=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## equal

{#equal}

> def equal(self, b=None, epsilon=None):

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

## exp

{#exp}

> def exp(self, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## exponent

{#exponent}

> def exponent(self, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## fact

{#fact}

> def fact(self, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## float_curve

{#float_curve}

> def float_curve(self, factor=None):

Node [Float Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeFloatCurve.html) )

        ### Args:
- factor: Float

### Returns:

  socket 'value'

## floor

{#floor}

> def floor(self):

Node [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html) )

### Returns:

  socket 'integer'

## fraction

{#fraction}

> def fraction(self, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## greater_equal

{#greater_equal}

> def greater_equal(self, b=None):

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## greater_than

{#greater_than}

> def greater_than(self, b=None):

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## inverse_sqrt

{#inverse_sqrt}

> def inverse_sqrt(self, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## less_equal

{#less_equal}

> def less_equal(self, b=None):

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## less_than

{#less_than}

> def less_than(self, b=None):

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## log

{#log}

> def log(self, base=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- base: Float
- clamp (bool): False

### Returns:

  socket 'value'

## logarithm

{#logarithm}

> def logarithm(self, base=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- base: Float
- clamp (bool): False

### Returns:

  socket 'value'

## map_range

{#map_range}

> def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True, interpolation_type='LINEAR'):

Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html) )

        ### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- steps: ['Float', 'Vector']
- clamp (bool): True
- interpolation_type (str): 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP]

### Returns:

  socket 'result'

## map_range_linear

{#map_range_linear}

> def map_range_linear(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):

Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html) )

        ### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- clamp (bool): True

### Returns:

  socket 'result'

## map_range_smooth

{#map_range_smooth}

> def map_range_smooth(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):

Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html) )

        ### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- clamp (bool): True

### Returns:

  socket 'result'

## map_range_smoother

{#map_range_smoother}

> def map_range_smoother(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):

Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html) )

        ### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- clamp (bool): True

### Returns:

  socket 'result'

## map_range_stepped

{#map_range_stepped}

> def map_range_stepped(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True):

Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html) )

        ### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- steps: ['Float', 'Vector']
- clamp (bool): True

### Returns:

  socket 'result'

## math_ceil

{#math_ceil}

> def math_ceil(self, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## math_compare

{#math_compare}

> def math_compare(self, value=None, epsilon=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- epsilon: Float
- clamp (bool): False

### Returns:

  socket 'value'

## math_floor

{#math_floor}

> def math_floor(self, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## math_greater_than

{#math_greater_than}

> def math_greater_than(self, threshold=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- threshold: Float
- clamp (bool): False

### Returns:

  socket 'value'

## math_less_than

{#math_less_than}

> def math_less_than(self, threshold=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- threshold: Float
- clamp (bool): False

### Returns:

  socket 'value'

## math_round

{#math_round}

> def math_round(self, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## math_trunc

{#math_trunc}

> def math_trunc(self, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## math_truncate

{#math_truncate}

> def math_truncate(self, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## max

{#max}

> def max(self, value=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## maximum

{#maximum}

> def maximum(self, value=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## min

{#min}

> def min(self, value=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## minimum

{#minimum}

> def minimum(self, value=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## mix

{#mix}

> def mix(self, factor=None, value=None, clamp_factor=True):

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

        ### Args:
- factor: ['Float', 'Vector']
- value: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True

### Returns:

  socket 'result'

## modulo

{#modulo}

> def modulo(self, value=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## mul_add

{#mul_add}

> def mul_add(self, multiplier=None, addend=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- multiplier: Float
- addend: Float
- clamp (bool): False

### Returns:

  socket 'value'

## multiply_add

{#multiply_add}

> def multiply_add(self, multiplier=None, addend=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- multiplier: Float
- addend: Float
- clamp (bool): False

### Returns:

  socket 'value'

## not_equal

{#not_equal}

> def not_equal(self, b=None, epsilon=None):

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

## ping_pong

{#ping_pong}

> def ping_pong(self, scale=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- scale: Float
- clamp (bool): False

### Returns:

  socket 'value'

## pow

{#pow}

> def pow(self, exponent=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- exponent: Float
- clamp (bool): False

### Returns:

  socket 'value'

## power

{#power}

> def power(self, exponent=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- exponent: Float
- clamp (bool): False

### Returns:

  socket 'value'

## round

{#round}

> def round(self):

Node [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html) )

### Returns:

  socket 'integer'

## sign

{#sign}

> def sign(self, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## sin

{#sin}

> def sin(self, value=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## sine

{#sine}

> def sine(self, value=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## sinh

{#sinh}

> def sinh(self, value=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## smooth_maximum

{#smooth_maximum}

> def smooth_maximum(self, value=None, distance=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- distance: Float
- clamp (bool): False

### Returns:

  socket 'value'

## smooth_minimum

{#smooth_minimum}

> def smooth_minimum(self, value=None, distance=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- distance: Float
- clamp (bool): False

### Returns:

  socket 'value'

## snap

{#snap}

> def snap(self, increment=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- increment: Float
- clamp (bool): False

### Returns:

  socket 'value'

## sqrt

{#sqrt}

> def sqrt(self, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## switch

{#switch}

> def switch(self, switch=None, true=None):

Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

        ### Args:
- switch: ['Boolean', 'Boolean']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

## tan

{#tan}

> def tan(self, value=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## tangent

{#tangent}

> def tangent(self, value=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## tanh

{#tanh}

> def tanh(self, value=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## to_degrees

{#to_degrees}

> def to_degrees(self, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## to_integer

{#to_integer}

> def to_integer(self, rounding_mode='ROUND'):

Node [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html) )

        ### Args:
- rounding_mode (str): 'ROUND' in [ROUND, FLOOR, CEILING, TRUNCATE]

### Returns:

  socket 'integer'

## to_radians

{#to_radians}

> def to_radians(self, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## to_string

{#to_string}

> def to_string(self, decimals=None):

Node [Value to String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/value_to_string.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html) )

        ### Args:
- decimals: Integer

### Returns:

  socket 'string'

## truncate

{#truncate}

> def truncate(self):

Node [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html) )

### Returns:

  socket 'integer'

## wrap

{#wrap}

> def wrap(self, max=None, min=None, clamp=False):

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

        ### Args:
- max: Float
- min: Float
- clamp (bool): False

### Returns:

  socket 'value'

