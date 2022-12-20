# class {class_name}

## abs {#abs}

> def abs(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## absolute {#absolute}

> def absolute(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## add {#add}

> def add(value0=None, value1=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value0: Float
- value1: Float
- clamp (bool): False

### Returns:

  socket 'value'

## align_euler_to_vector {#align_euler_to_vector}

> def align_euler_to_vector(rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO'):

Node [Align Euler to Vector](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- rotation: Vector
- factor: Float
- vector: Vector
- axis (str): 'X' in [X, Y, Z]
- pivot_axis (str): 'AUTO' in [AUTO, X, Y, Z]

### Returns:

  socket 'rotation'

## arccos {#arccos}

> def arccos(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## arccosine {#arccosine}

> def arccosine(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## arcsin {#arcsin}

> def arcsin(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## arcsine {#arcsine}

> def arcsine(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## arctan {#arctan}

> def arctan(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## arctan2 {#arctan2}

> def arctan2(value0=None, value1=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value0: Float
- value1: Float
- clamp (bool): False

### Returns:

  socket 'value'

## arctangent {#arctangent}

> def arctangent(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## b_and {#b_and}

> def b_and(boolean0=None, boolean1=None):

Node [Boolean Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- boolean0: Boolean
- boolean1: Boolean

### Returns:

  socket 'boolean'

## b_not {#b_not}

> def b_not(boolean0=None):

Node [Boolean Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- boolean0: Boolean

### Returns:

  socket 'boolean'

## b_or {#b_or}

> def b_or(boolean0=None, boolean1=None):

Node [Boolean Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- boolean0: Boolean
- boolean1: Boolean

### Returns:

  socket 'boolean'

## clamp {#clamp}

> def clamp(value=None, min=None, max=None, clamp_type='MINMAX'):

Node [Clamp](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- min: Float
- max: Float
- clamp_type (str): 'MINMAX' in [MINMAX, RANGE]

### Returns:

  socket 'result'

## clamp_min_max {#clamp_min_max}

> def clamp_min_max(value=None, min=None, max=None):

Node [Clamp](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- min: Float
- max: Float

### Returns:

  socket 'result'

## clamp_range {#clamp_range}

> def clamp_range(value=None, min=None, max=None):

Node [Clamp](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- min: Float
- max: Float

### Returns:

  socket 'result'

## color_add {#color_add}

> def color_add(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## color_burn {#color_burn}

> def color_burn(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## color_color {#color_color}

> def color_color(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## color_darken {#color_darken}

> def color_darken(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## color_difference {#color_difference}

> def color_difference(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## color_divide {#color_divide}

> def color_divide(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## color_dodge {#color_dodge}

> def color_dodge(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## color_hue {#color_hue}

> def color_hue(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## color_lighten {#color_lighten}

> def color_lighten(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## color_linear_light {#color_linear_light}

> def color_linear_light(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## color_mix {#color_mix}

> def color_mix(factor=None, a=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- blend_type (str): 'MIX' in [MIX, DARKEN, MULTIPLY, BURN, LIGHTEN,... , SATURATION, COLOR, VALUE]
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## color_multiply {#color_multiply}

> def color_multiply(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## color_overlay {#color_overlay}

> def color_overlay(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## color_ramp {#color_ramp}

> def color_ramp(fac=None):

Node [ColorRamp](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- fac: Float

### Returns:

- node with sockets ['color', 'alpha']

## color_saturation {#color_saturation}

> def color_saturation(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## color_screen {#color_screen}

> def color_screen(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## color_soft_light {#color_soft_light}

> def color_soft_light(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## color_subtract {#color_subtract}

> def color_subtract(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## color_value {#color_value}

> def color_value(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## combine_hsl {#combine_hsl}

> def combine_hsl(hue=None, saturation=None, lightness=None, alpha=None):

Node [Combine Color](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- hue: Float
- saturation: Float
- lightness: Float
- alpha: Float

### Returns:

  socket 'color'

## combine_hsv {#combine_hsv}

> def combine_hsv(hue=None, saturation=None, value=None, alpha=None):

Node [Combine Color](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- hue: Float
- saturation: Float
- value: Float
- alpha: Float

### Returns:

  socket 'color'

## combine_rgb {#combine_rgb}

> def combine_rgb(red=None, green=None, blue=None, alpha=None):

Node [Combine Color](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- red: Float
- green: Float
- blue: Float
- alpha: Float

### Returns:

  socket 'color'

## compare {#compare}

> def compare(a=None, b=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN'):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- a: ['Float', 'Integer', 'Vector', 'Color', 'String']
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float
- angle: Float
- epsilon: Float
- data_type (str): 'FLOAT' in [FLOAT, INT, VECTOR, STRING, RGBA]
- mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
- operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

### Returns:

  socket 'result'

## cos {#cos}

> def cos(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## cosh {#cosh}

> def cosh(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## cosine {#cosine}

> def cosine(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## div {#div}

> def div(value0=None, value1=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value0: Float
- value1: Float
- clamp (bool): False

### Returns:

  socket 'value'

## divide {#divide}

> def divide(value0=None, value1=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value0: Float
- value1: Float
- clamp (bool): False

### Returns:

  socket 'value'

## exp {#exp}

> def exp(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## exponent {#exponent}

> def exponent(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## float_mix {#float_mix}

> def float_mix(factor=None, a=None, b=None, clamp_factor=True):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True

### Returns:

  socket 'result'

## fraction {#fraction}

> def fraction(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## geometry_to_instance {#geometry_to_instance}

> def geometry_to_instance(*geometry):

Node [Geometry to Instance](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- geometry: <m>Geometry

### Returns:

  socket 'instances' of class Instances

## imply {#imply}

> def imply(boolean0=None, boolean1=None):

Node [Boolean Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- boolean0: Boolean
- boolean1: Boolean

### Returns:

  socket 'boolean'

## inverse_sqrt {#inverse_sqrt}

> def inverse_sqrt(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## join_geometry {#join_geometry}

> def join_geometry(*geometry):

Node [Join Geometry](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- geometry: <m>Geometry

### Returns:

  socket 'geometry'

## join_strings {#join_strings}

> def join_strings(*strings, delimiter=None):

Node [Join Strings](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- strings: <m>String
- delimiter: String

### Returns:

  socket 'string'

## log {#log}

> def log(value=None, base=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- base: Float
- clamp (bool): False

### Returns:

  socket 'value'

## logarithm {#logarithm}

> def logarithm(value=None, base=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- base: Float
- clamp (bool): False

### Returns:

  socket 'value'

## math {#math}

> def math(value0=None, value1=None, value2=None, operation='ADD', clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value0: Float
- value1: Float
- value2: Float
- operation (str): 'ADD' in [ADD, SUBTRACT, MULTIPLY, DIVIDE,... , TANH, RADIANS, DEGREES]
- clamp (bool): False

### Returns:

  socket 'value'

## math_ceil {#math_ceil}

> def math_ceil(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## math_compare {#math_compare}

> def math_compare(value0=None, value1=None, epsilon=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value0: Float
- value1: Float
- epsilon: Float
- clamp (bool): False

### Returns:

  socket 'value'

## math_floor {#math_floor}

> def math_floor(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## math_greater_than {#math_greater_than}

> def math_greater_than(value=None, threshold=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- threshold: Float
- clamp (bool): False

### Returns:

  socket 'value'

## math_less_than {#math_less_than}

> def math_less_than(value=None, threshold=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- threshold: Float
- clamp (bool): False

### Returns:

  socket 'value'

## math_round {#math_round}

> def math_round(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## math_trun {#math_trun}

> def math_trun(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## math_truncate {#math_truncate}

> def math_truncate(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## max {#max}

> def max(value0=None, value1=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value0: Float
- value1: Float
- clamp (bool): False

### Returns:

  socket 'value'

## maximum {#maximum}

> def maximum(value0=None, value1=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value0: Float
- value1: Float
- clamp (bool): False

### Returns:

  socket 'value'

## min {#min}

> def min(value0=None, value1=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value0: Float
- value1: Float
- clamp (bool): False

### Returns:

  socket 'value'

## minimum {#minimum}

> def minimum(value0=None, value1=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value0: Float
- value1: Float
- clamp (bool): False

### Returns:

  socket 'value'

## modulo {#modulo}

> def modulo(value0=None, value1=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value0: Float
- value1: Float
- clamp (bool): False

### Returns:

  socket 'value'

## mul {#mul}

> def mul(value0=None, value1=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value0: Float
- value1: Float
- clamp (bool): False

### Returns:

  socket 'value'

## mul_add {#mul_add}

> def mul_add(value=None, multiplier=None, addend=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- multiplier: Float
- addend: Float
- clamp (bool): False

### Returns:

  socket 'value'

## multiply {#multiply}

> def multiply(value0=None, value1=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value0: Float
- value1: Float
- clamp (bool): False

### Returns:

  socket 'value'

## multiply_add {#multiply_add}

> def multiply_add(value=None, multiplier=None, addend=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- multiplier: Float
- addend: Float
- clamp (bool): False

### Returns:

  socket 'value'

## nand {#nand}

> def nand(boolean0=None, boolean1=None):

Node [Boolean Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- boolean0: Boolean
- boolean1: Boolean

### Returns:

  socket 'boolean'

## nimply {#nimply}

> def nimply(boolean0=None, boolean1=None):

Node [Boolean Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- boolean0: Boolean
- boolean1: Boolean

### Returns:

  socket 'boolean'

## nor {#nor}

> def nor(boolean0=None, boolean1=None):

Node [Boolean Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- boolean0: Boolean
- boolean1: Boolean

### Returns:

  socket 'boolean'

## ping_pong {#ping_pong}

> def ping_pong(value=None, scale=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- scale: Float
- clamp (bool): False

### Returns:

  socket 'value'

## power {#power}

> def power(base=None, exponent=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- base: Float
- exponent: Float
- clamp (bool): False

### Returns:

  socket 'value'

## random_boolean {#random_boolean}

> def random_boolean(probability=None, ID=None, seed=None):

Node [Random Value](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- probability: Float
- ID: Integer
- seed: Integer

### Returns:

  socket 'value'

## random_float {#random_float}

> def random_float(min=None, max=None, ID=None, seed=None):

Node [Random Value](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

### Returns:

  socket 'value'

## random_integer {#random_integer}

> def random_integer(min=None, max=None, ID=None, seed=None):

Node [Random Value](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

### Returns:

  socket 'value'

## random_vector {#random_vector}

> def random_vector(min=None, max=None, ID=None, seed=None):

Node [Random Value](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

### Returns:

  socket 'value'

## replace_string {#replace_string}

> def replace_string(string=None, find=None, replace=None):

Node [Replace String](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- string: String
- find: String
- replace: String

### Returns:

  socket 'string'

## rgb_curves {#rgb_curves}

> def rgb_curves(fac=None, color=None):

Node [RGB Curves](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- fac: Float
- color: Color

### Returns:

- node with sockets ['color']

## rotate_axis_angle {#rotate_axis_angle}

> def rotate_axis_angle(rotation=None, axis=None, angle=None, space='OBJECT'):

Node [Rotate Euler](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- rotation: Vector
- axis: Vector
- angle: Float
- space (str): 'OBJECT' in [OBJECT, LOCAL]

### Returns:

  socket 'rotation'

## rotate_euler {#rotate_euler}

> def rotate_euler(rotation=None, rotate_by=None, space='OBJECT'):

Node [Rotate Euler](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- rotation: Vector
- rotate_by: Vector
- space (str): 'OBJECT' in [OBJECT, LOCAL]

### Returns:

  socket 'rotation'

## separate_hsl {#separate_hsl}

> def separate_hsl(color=None):

Node [Separate Color](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- color: Color

### Returns:

- tuple ('red', 'green', 'blue', 'alpha')

## separate_hsv {#separate_hsv}

> def separate_hsv(color=None):

Node [Separate Color](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- color: Color

### Returns:

- tuple ('red', 'green', 'blue', 'alpha')

## separate_rgb {#separate_rgb}

> def separate_rgb(color=None):

Node [Separate Color](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- color: Color

### Returns:

- tuple ('red', 'green', 'blue', 'alpha')

## sign {#sign}

> def sign(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## sin {#sin}

> def sin(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## sine {#sine}

> def sine(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## sinh {#sinh}

> def sinh(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## slice_string {#slice_string}

> def slice_string(string=None, position=None, length=None):

Node [Slice String](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- string: String
- position: Integer
- length: Integer

### Returns:

  socket 'string'

## smooth_maximum {#smooth_maximum}

> def smooth_maximum(value0=None, value1=None, distance=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value0: Float
- value1: Float
- distance: Float
- clamp (bool): False

### Returns:

  socket 'value'

## smooth_minimum {#smooth_minimum}

> def smooth_minimum(value0=None, value1=None, distance=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value0: Float
- value1: Float
- distance: Float
- clamp (bool): False

### Returns:

  socket 'value'

## snap {#snap}

> def snap(value=None, increment=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- increment: Float
- clamp (bool): False

### Returns:

  socket 'value'

## sqrt {#sqrt}

> def sqrt(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## string_length {#string_length}

> def string_length(string=None):

Node [String Length](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- string: String

### Returns:

  socket 'length'

## string_to_curves {#string_to_curves}

> def string_to_curves(string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT'):

Node [String to Curves](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- string: String
- size: Float
- character_spacing: Float
- word_spacing: Float
- line_spacing: Float
- text_box_width: Float
- text_box_height: Float
- align_x (str): 'LEFT' in [LEFT, CENTER, RIGHT, JUSTIFY, FLUSH]
- align_y (str): 'TOP_BASELINE' in [TOP_BASELINE, TOP, MIDDLE, BOTTOM_BASELINE, BOTTOM]
- overflow (str): 'OVERFLOW' in [OVERFLOW, SCALE_TO_FIT, TRUNCATE]
- pivot_mode (str): 'BOTTOM_LEFT' in [MIDPOINT, TOP_LEFT, TOP_CENTER,... , BOTTOM_LEFT, BOTTOM_CENTER, BOTTOM_RIGHT]

### Returns:

- tuple ('curve_instances', 'line', 'pivot_point')

## sub {#sub}

> def sub(value0=None, value1=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value0: Float
- value1: Float
- clamp (bool): False

### Returns:

  socket 'value'

## subtract {#subtract}

> def subtract(value0=None, value1=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value0: Float
- value1: Float
- clamp (bool): False

### Returns:

  socket 'value'

## switch {#switch}

> def switch(switch=None, false=None, true=None, input_type='GEOMETRY'):

Node [Switch](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- input_type (str): 'GEOMETRY' in [FLOAT, INT, BOOLEAN, VECTOR, STRING,... , COLLECTION, TEXTURE, MATERIAL]

### Returns:

  socket 'output'

## switch_boolean {#switch_boolean}

> def switch_boolean(switch=None, false=None, true=None):

Node [Switch](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

## switch_collection {#switch_collection}

> def switch_collection(switch=None, false=None, true=None):

Node [Switch](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

## switch_color {#switch_color}

> def switch_color(switch=None, false=None, true=None):

Node [Switch](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

## switch_float {#switch_float}

> def switch_float(switch=None, false=None, true=None):

Node [Switch](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

## switch_geometry {#switch_geometry}

> def switch_geometry(switch=None, false=None, true=None):

Node [Switch](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

## switch_image {#switch_image}

> def switch_image(switch=None, false=None, true=None):

Node [Switch](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

## switch_integer {#switch_integer}

> def switch_integer(switch=None, false=None, true=None):

Node [Switch](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

## switch_material {#switch_material}

> def switch_material(switch=None, false=None, true=None):

Node [Switch](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

## switch_object {#switch_object}

> def switch_object(switch=None, false=None, true=None):

Node [Switch](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

## switch_string {#switch_string}

> def switch_string(switch=None, false=None, true=None):

Node [Switch](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

## switch_texture {#switch_texture}

> def switch_texture(switch=None, false=None, true=None):

Node [Switch](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

## switch_vector {#switch_vector}

> def switch_vector(switch=None, false=None, true=None):

Node [Switch](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

## tan {#tan}

> def tan(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## tangent {#tangent}

> def tangent(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## tanh {#tanh}

> def tanh(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## to_degrees {#to_degrees}

> def to_degrees(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## to_radians {#to_radians}

> def to_radians(value=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- clamp (bool): False

### Returns:

  socket 'value'

## value_to_string {#value_to_string}

> def value_to_string(value=None, decimals=None):

Node [Value to String](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- decimals: Integer

### Returns:

  socket 'string'

## vector_mix {#vector_mix}

> def vector_mix(factor=None, a=None, b=None, clamp_factor=True, factor_mode='UNIFORM'):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- factor_mode (str): 'UNIFORM' in [UNIFORM, NON_UNIFORM]

### Returns:

  socket 'result'

## wrap {#wrap}

> def wrap(value=None, max=None, min=None, clamp=False):

Node [Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- value: Float
- max: Float
- min: Float
- clamp (bool): False

### Returns:

  socket 'value'

## xnor {#xnor}

> def xnor(boolean0=None, boolean1=None):

Node [Boolean Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- boolean0: Boolean
- boolean1: Boolean

### Returns:

  socket 'boolean'

## xor {#xor}

> def xor(boolean0=None, boolean1=None):

Node [Boolean Math](node.blender_ref) ( [api](node.blender_python_ref) )

    ### Args:
- boolean0: Boolean
- boolean1: Boolean

### Returns:

  socket 'boolean'

