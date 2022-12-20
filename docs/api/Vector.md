# class {class_name}

## Combine *classmethod* {#Combine}

> def Combine(cls, x=None, y=None, z=None):

Node [Combine XYZ](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- x: Float
- y: Float
- z: Float

### Returns:

  socket 'vector'

## Vector *classmethod* {#Vector}

> def Vector(cls, vector=[0.0, 0.0, 0.0]):

Node [Vector](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector (list): [0.0, 0.0, 0.0]

### Returns:

  socket 'vector'

## abs {#abs}

> def abs(self):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'vector'

## absolute {#absolute}

> def absolute(self):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'vector'

## add {#add}

> def add(self, vector=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: Vector

### Returns:

  socket 'vector'

## align_euler_to_vector {#align_euler_to_vector}

> def align_euler_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO'):

Node [Align Euler to Vector](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: Float
- vector: Vector
- axis (str): 'X' in [X, Y, Z]
- pivot_axis (str): 'AUTO' in [AUTO, X, Y, Z]

### Returns:

- node with sockets ['rotation']

## average_equal {#average_equal}

> def average_equal(self, b=None, epsilon=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

## average_greater_equal {#average_greater_equal}

> def average_greater_equal(self, b=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## average_greater_than {#average_greater_than}

> def average_greater_than(self, b=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## average_less_equal {#average_less_equal}

> def average_less_equal(self, b=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## average_less_than {#average_less_than}

> def average_less_than(self, b=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## average_not_equal {#average_not_equal}

> def average_not_equal(self, b=None, epsilon=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

## ceil {#ceil}

> def ceil(self):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'vector'

## compare {#compare}

> def compare(self, b=None, c=None, angle=None, epsilon=None, mode='ELEMENT', operation='GREATER_THAN'):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float
- angle: Float
- epsilon: Float
- mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
- operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

### Returns:

  socket 'result'

## cos {#cos}

> def cos(self):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'vector'

## cosine {#cosine}

> def cosine(self):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'vector'

## cross {#cross}

> def cross(self, vector=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: Vector

### Returns:

  socket 'vector'

## cross_product {#cross_product}

> def cross_product(self, vector=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: Vector

### Returns:

  socket 'vector'

## curves {#curves}

> def curves(self, fac=None):

Node [Vector Curves](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- fac: Float

### Returns:

  socket 'vector'

## direction_equal {#direction_equal}

> def direction_equal(self, b=None, angle=None, epsilon=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float
- epsilon: Float

### Returns:

  socket 'result'

## direction_greater_equal {#direction_greater_equal}

> def direction_greater_equal(self, b=None, angle=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float

### Returns:

  socket 'result'

## direction_greater_than {#direction_greater_than}

> def direction_greater_than(self, b=None, angle=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float

### Returns:

  socket 'result'

## direction_less_equal {#direction_less_equal}

> def direction_less_equal(self, b=None, angle=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float

### Returns:

  socket 'result'

## direction_less_than {#direction_less_than}

> def direction_less_than(self, b=None, angle=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float

### Returns:

  socket 'result'

## direction_not_equal {#direction_not_equal}

> def direction_not_equal(self, b=None, angle=None, epsilon=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float
- epsilon: Float

### Returns:

  socket 'result'

## distance {#distance}

> def distance(self, vector=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: Vector

### Returns:

  socket 'value'

## div {#div}

> def div(self, vector=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: Vector

### Returns:

  socket 'vector'

## divide {#divide}

> def divide(self, vector=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: Vector

### Returns:

  socket 'vector'

## dot {#dot}

> def dot(self, vector=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: Vector

### Returns:

  socket 'value'

## dot_product {#dot_product}

> def dot_product(self, vector=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: Vector

### Returns:

  socket 'value'

## dot_product_equal {#dot_product_equal}

> def dot_product_equal(self, b=None, c=None, epsilon=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float
- epsilon: Float

### Returns:

  socket 'result'

## dot_product_greater_equal {#dot_product_greater_equal}

> def dot_product_greater_equal(self, b=None, c=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float

### Returns:

  socket 'result'

## dot_product_greater_than {#dot_product_greater_than}

> def dot_product_greater_than(self, b=None, c=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float

### Returns:

  socket 'result'

## dot_product_less_equal {#dot_product_less_equal}

> def dot_product_less_equal(self, b=None, c=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float

### Returns:

  socket 'result'

## dot_product_less_than {#dot_product_less_than}

> def dot_product_less_than(self, b=None, c=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float

### Returns:

  socket 'result'

## dot_product_not_equal {#dot_product_not_equal}

> def dot_product_not_equal(self, b=None, c=None, epsilon=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float
- epsilon: Float

### Returns:

  socket 'result'

## elements_equal {#elements_equal}

> def elements_equal(self, b=None, epsilon=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

## elements_greater_equal {#elements_greater_equal}

> def elements_greater_equal(self, b=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## elements_greater_than {#elements_greater_than}

> def elements_greater_than(self, b=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## elements_less_equal {#elements_less_equal}

> def elements_less_equal(self, b=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## elements_less_than {#elements_less_than}

> def elements_less_than(self, b=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## elements_not_equal {#elements_not_equal}

> def elements_not_equal(self, b=None, epsilon=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

## face_forward {#face_forward}

> def face_forward(self, incident=None, reference=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- incident: Vector
- reference: Vector

### Returns:

  socket 'vector'

## floor {#floor}

> def floor(self):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'vector'

## fract {#fract}

> def fract(self):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'vector'

## fraction {#fraction}

> def fraction(self):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'vector'

## length *property* {#length}

> def length(self):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'value'

## length_equal {#length_equal}

> def length_equal(self, b=None, epsilon=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

## length_greater_equal {#length_greater_equal}

> def length_greater_equal(self, b=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## length_greater_than {#length_greater_than}

> def length_greater_than(self, b=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## length_less_equal {#length_less_equal}

> def length_less_equal(self, b=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## length_less_than {#length_less_than}

> def length_less_than(self, b=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## length_not_equal {#length_not_equal}

> def length_not_equal(self, b=None, epsilon=None):

Node [Compare](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

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

  socket 'vector'

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

  socket 'vector'

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

  socket 'vector'

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

  socket 'vector'

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

  socket 'vector'

## max {#max}

> def max(self, vector=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: Vector

### Returns:

  socket 'vector'

## maximum {#maximum}

> def maximum(self, vector=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: Vector

### Returns:

  socket 'vector'

## min {#min}

> def min(self, vector=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: Vector

### Returns:

  socket 'vector'

## minimum {#minimum}

> def minimum(self, vector=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: Vector

### Returns:

  socket 'vector'

## mix {#mix}

> def mix(self, factor=None, vector=None, clamp_factor=True, factor_mode='UNIFORM'):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: ['Float', 'Vector']
- vector: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- factor_mode (str): 'UNIFORM' in [UNIFORM, NON_UNIFORM]

### Returns:

  socket 'result'

## mix_non_uniform {#mix_non_uniform}

> def mix_non_uniform(self, factor=None, vector=None, clamp_factor=True):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- factor: ['Float', 'Vector']
- vector: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True

### Returns:

  socket 'result'

## mix_uniform {#mix_uniform}

> def mix_uniform(self, vector=None, clamp_factor=True):

Node [Mix](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True

### Returns:

  socket 'result'

## modulo {#modulo}

> def modulo(self, vector=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: Vector

### Returns:

  socket 'vector'

## mul {#mul}

> def mul(self, vector=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: Vector

### Returns:

  socket 'vector'

## mul_add {#mul_add}

> def mul_add(self, multiplier=None, addend=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- multiplier: Vector
- addend: Vector

### Returns:

  socket 'vector'

## multiply {#multiply}

> def multiply(self, vector=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: Vector

### Returns:

  socket 'vector'

## multiply_add {#multiply_add}

> def multiply_add(self, multiplier=None, addend=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- multiplier: Vector
- addend: Vector

### Returns:

  socket 'vector'

## normalize {#normalize}

> def normalize(self):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'vector'

## project {#project}

> def project(self, vector=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: Vector

### Returns:

  socket 'vector'

## reflect {#reflect}

> def reflect(self, vector=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: Vector

### Returns:

  socket 'vector'

## refract {#refract}

> def refract(self, vector=None, ior=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: Vector
- ior: Float

### Returns:

  socket 'vector'

## rotate_axis_angle {#rotate_axis_angle}

> def rotate_axis_angle(self, center=None, axis=None, angle=None, invert=False):

Node [Vector Rotate](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- center: Vector
- axis: Vector
- angle: Float
- invert (bool): False

### Returns:

  socket 'vector'

## rotate_euler {#rotate_euler}

> def rotate_euler(self, center=None, rotation=None, invert=False):

Node [Vector Rotate](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- center: Vector
- rotation: Vector
- invert (bool): False

### Returns:

  socket 'vector'

## rotate_x {#rotate_x}

> def rotate_x(self, center=None, angle=None, invert=False):

Node [Vector Rotate](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- center: Vector
- angle: Float
- invert (bool): False

### Returns:

  socket 'vector'

## rotate_y {#rotate_y}

> def rotate_y(self, center=None, angle=None, invert=False):

Node [Vector Rotate](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- center: Vector
- angle: Float
- invert (bool): False

### Returns:

  socket 'vector'

## rotate_z {#rotate_z}

> def rotate_z(self, center=None, angle=None, invert=False):

Node [Vector Rotate](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- center: Vector
- angle: Float
- invert (bool): False

### Returns:

  socket 'vector'

## scale {#scale}

> def scale(self, scale=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- scale: Float

### Returns:

  socket 'vector'

## separate *property* {#separate}

> def separate(self):

Node [Separate XYZ](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

- node with sockets ['x', 'y', 'z']

## sin {#sin}

> def sin(self):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'vector'

## sine {#sine}

> def sine(self):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'vector'

## snap {#snap}

> def snap(self, increment=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- increment: Vector

### Returns:

  socket 'vector'

## sub {#sub}

> def sub(self, vector=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: Vector

### Returns:

  socket 'vector'

## subtract {#subtract}

> def subtract(self, vector=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vector: Vector

### Returns:

  socket 'vector'

## switch {#switch}

> def switch(self, switch=None, true=None):

Node [Switch](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- switch: ['Boolean', 'Boolean']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

## tan {#tan}

> def tan(self):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'vector'

## tangent {#tangent}

> def tangent(self):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'vector'

## wrap {#wrap}

> def wrap(self, max=None, min=None):

Node [Vector Math](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- max: Vector
- min: Vector

### Returns:

  socket 'vector'

