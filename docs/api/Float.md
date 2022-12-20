# class {class_name}

## Frame *classmethod* {#Frame}

> def Frame(cls):

Node [Scene Time](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'frame'

## Seconds *classmethod* {#Seconds}

> def Seconds(cls):

Node [Scene Time](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'seconds'

## Value *classmethod* {#Value}

> def Value(cls):

Node [Value](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'value'

## abs {#abs}

> def abs(self, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## absolute {#absolute}

> def absolute(self, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## arccos {#arccos}

> def arccos(self, value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## arccosine {#arccosine}

> def arccosine(self, value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## arcsin {#arcsin}

> def arcsin(self, value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## arcsine {#arcsine}

> def arcsine(self, value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## arctan {#arctan}

> def arctan(self, value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## arctan2 {#arctan2}

> def arctan2(self, value1=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value1: Float
- clamp (bool): False

### Returns:

  socket 'value'

## arctangent {#arctangent}

> def arctangent(self, value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## ceiling {#ceiling}

> def ceiling(self):

Node [Float to Integer](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'integer'

## clamp {#clamp}

> def clamp(self, min=None, max=None, clamp_type='MINMAX'):

Node [Clamp](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- min: Float
- max: Float
- clamp_type (str): 'MINMAX' in [MINMAX, RANGE]

### Returns:

  socket 'result'

## clamp_min_max {#clamp_min_max}

> def clamp_min_max(self, min=None, max=None):

Node [Clamp](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- min: Float
- max: Float

### Returns:

  socket 'result'

## clamp_range {#clamp_range}

> def clamp_range(self, min=None, max=None):

Node [Clamp](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- min: Float
- max: Float

### Returns:

  socket 'result'

## color_ramp *property* {#color_ramp}

> def color_ramp(self):

Node [ColorRamp](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

- node with sockets ['color', 'alpha']

## compare {#compare}

> def compare(self, b=None, epsilon=None, operation='GREATER_THAN'):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float
- operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

### Returns:

  socket 'result'

## cos {#cos}

> def cos(self, value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## cosh {#cosh}

> def cosh(self, value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## cosine {#cosine}

> def cosine(self, value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## equal {#equal}

> def equal(self, b=None, epsilon=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

## exp {#exp}

> def exp(self, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## exponent {#exponent}

> def exponent(self, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## fact {#fact}

> def fact(self, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## float_curve {#float_curve}

> def float_curve(self, factor=None):

Node [Float Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: Float

### Returns:

  socket 'value'

## floor {#floor}

> def floor(self):

Node [Float to Integer](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'integer'

## fraction {#fraction}

> def fraction(self, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## greater_equal {#greater_equal}

> def greater_equal(self, b=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## greater_than {#greater_than}

> def greater_than(self, b=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## inverse_sqrt {#inverse_sqrt}

> def inverse_sqrt(self, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## less_equal {#less_equal}

> def less_equal(self, b=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## less_than {#less_than}

> def less_than(self, b=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## log {#log}

> def log(self, base=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- base: Float
- clamp (bool): False

### Returns:

  socket 'value'

## logarithm {#logarithm}

> def logarithm(self, base=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- base: Float
- clamp (bool): False

### Returns:

  socket 'value'

## map_range {#map_range}

> def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True, interpolation_type='LINEAR'):

Node [Map Range](node.blender_ref) ( [api](node.blender_python_ref) )

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

## map_range_linear {#map_range_linear}

> def map_range_linear(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):

Node [Map Range](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- clamp (bool): True

### Returns:

  socket 'result'

## map_range_smooth {#map_range_smooth}

> def map_range_smooth(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):

Node [Map Range](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- clamp (bool): True

### Returns:

  socket 'result'

## map_range_smoother {#map_range_smoother}

> def map_range_smoother(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):

Node [Map Range](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- clamp (bool): True

### Returns:

  socket 'result'

## map_range_stepped {#map_range_stepped}

> def map_range_stepped(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True):

Node [Map Range](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- steps: ['Float', 'Vector']
- clamp (bool): True

### Returns:

  socket 'result'

## math_ceil {#math_ceil}

> def math_ceil(self, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## math_compare {#math_compare}

> def math_compare(self, value=None, epsilon=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- epsilon: Float
- clamp (bool): False

### Returns:

  socket 'value'

## math_floor {#math_floor}

> def math_floor(self, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## math_greater_than {#math_greater_than}

> def math_greater_than(self, threshold=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- threshold: Float
- clamp (bool): False

### Returns:

  socket 'value'

## math_less_than {#math_less_than}

> def math_less_than(self, threshold=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- threshold: Float
- clamp (bool): False

### Returns:

  socket 'value'

## math_round {#math_round}

> def math_round(self, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## math_trunc {#math_trunc}

> def math_trunc(self, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## math_truncate {#math_truncate}

> def math_truncate(self, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## max {#max}

> def max(self, value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## maximum {#maximum}

> def maximum(self, value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## min {#min}

> def min(self, value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## minimum {#minimum}

> def minimum(self, value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## mix {#mix}

> def mix(self, factor=None, value=None, clamp_factor=True):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: ['Float', 'Vector']
- value: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True

### Returns:

  socket 'result'

## modulo {#modulo}

> def modulo(self, value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## mul_add {#mul_add}

> def mul_add(self, multiplier=None, addend=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- multiplier: Float
- addend: Float
- clamp (bool): False

### Returns:

  socket 'value'

## multiply_add {#multiply_add}

> def multiply_add(self, multiplier=None, addend=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- multiplier: Float
- addend: Float
- clamp (bool): False

### Returns:

  socket 'value'

## not_equal {#not_equal}

> def not_equal(self, b=None, epsilon=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

## ping_pong {#ping_pong}

> def ping_pong(self, scale=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- scale: Float
- clamp (bool): False

### Returns:

  socket 'value'

## pow {#pow}

> def pow(self, exponent=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- exponent: Float
- clamp (bool): False

### Returns:

  socket 'value'

## power {#power}

> def power(self, exponent=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- exponent: Float
- clamp (bool): False

### Returns:

  socket 'value'

## round {#round}

> def round(self):

Node [Float to Integer](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'integer'

## sign {#sign}

> def sign(self, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## sin {#sin}

> def sin(self, value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## sine {#sine}

> def sine(self, value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## sinh {#sinh}

> def sinh(self, value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## smooth_maximum {#smooth_maximum}

> def smooth_maximum(self, value=None, distance=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- distance: Float
- clamp (bool): False

### Returns:

  socket 'value'

## smooth_minimum {#smooth_minimum}

> def smooth_minimum(self, value=None, distance=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- distance: Float
- clamp (bool): False

### Returns:

  socket 'value'

## snap {#snap}

> def snap(self, increment=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- increment: Float
- clamp (bool): False

### Returns:

  socket 'value'

## sqrt {#sqrt}

> def sqrt(self, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## switch {#switch}

> def switch(self, switch=None, true=None):

Node [Switch](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- switch: ['Boolean', 'Boolean']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

## tan {#tan}

> def tan(self, value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## tangent {#tangent}

> def tangent(self, value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## tanh {#tanh}

> def tanh(self, value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## to_degrees {#to_degrees}

> def to_degrees(self, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## to_integer {#to_integer}

> def to_integer(self, rounding_mode='ROUND'):

Node [Float to Integer](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- rounding_mode (str): 'ROUND' in [ROUND, FLOOR, CEILING, TRUNCATE]

### Returns:

  socket 'integer'

## to_radians {#to_radians}

> def to_radians(self, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- clamp (bool): False

### Returns:

  socket 'value'

## to_string {#to_string}

> def to_string(self, decimals=None):

Node [Value to String](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- decimals: Integer

### Returns:

  socket 'string'

## truncate {#truncate}

> def truncate(self):

Node [Float to Integer](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'integer'

## wrap {#wrap}

> def wrap(self, max=None, min=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- max: Float
- min: Float
- clamp (bool): False

### Returns:

  socket 'value'

