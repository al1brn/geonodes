# Socket VECTOR


### Methods

- [abs](#abs)
- [add](#add)
- [align_euler_to_vector](#align_euler_to_vector)
- [axis_angle_to_rotation](#axis_angle_to_rotation)
- [blur_attribute](#blur_attribute)
- [ceil](#ceil)
- [cos](#cos)
- [cross](#cross)
- [distance](#distance)
- [divide](#divide)
- [dot](#dot)
- [equal](#equal)
- [euler_to_rotation](#euler_to_rotation)
- [faceforward](#faceforward)
- [floor](#floor)
- [frac](#frac)
- [greater_equal](#greater_equal)
- [greater_than](#greater_than)
- [index_switch](#index_switch)
- [invert_rotation](#invert_rotation)
- [length](#length)
- [less_equal](#less_equal)
- [less_than](#less_than)
- [map_range](#map_range)
- [max](#max)
- [min](#min)
- [mix](#mix)
- [mod](#mod)
- [multiply](#multiply)
- [multiply_add](#multiply_add)
- [normalize](#normalize)
- [not_equal](#not_equal)
- [pack_uv_islands](#pack_uv_islands)
- [project](#project)
- [reflect](#reflect)
- [refract](#refract)
- [rotate_euler](#rotate_euler)
- [rotate_euler_axis_angle](#rotate_euler_axis_angle)
- [rotate_euler_euler](#rotate_euler_euler)
- [rotate_vector](#rotate_vector)
- [rotation_to_axis_angle](#rotation_to_axis_angle)
- [rotation_to_euler](#rotation_to_euler)
- [rotation_to_quaternion](#rotation_to_quaternion)
- [scale](#scale)
- [separate_xyz](#separate_xyz)
- [sin](#sin)
- [snap](#snap)
- [subtract](#subtract)
- [switch](#switch)
- [tan](#tan)
- [vector_curves](#vector_curves)
- [vector_rotate](#vector_rotate)
- [wrap](#wrap)

## Methods

### abs


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def abs(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, operation='ABSOLUTE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### add


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def add(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='ADD', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### align_euler_to_vector


- node : [AlignEulerToVector](/docs/GeoNodes/AlignEulerToVector.md)
- self : rotation
- jump : No
- return : rotation

##### Arguments

- factor : None
- vector : None
- axis : 'X' in ('X', 'Y', 'Z')
- pivot_axis : 'AUTO' in ('AUTO', 'X', 'Y', 'Z')
- node_label : None
- node_color : None

#### Source code

``` python
def align_euler_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO', node_label=None, node_color=None, **kwargs):
    node = self.tree.AlignEulerToVector(rotation=self, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis, node_label=node_label, node_color=node_color, **kwargs)
    return node.rotation
```
### axis_angle_to_rotation


- node : [AxisAngleToRotation](/docs/GeoNodes/AxisAngleToRotation.md)
- self : axis
- jump : No
- return : rotation

##### Arguments

- angle : None
- node_label : None
- node_color : None

#### Source code

``` python
def axis_angle_to_rotation(self, angle=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.AxisAngleToRotation(axis=self, angle=angle, node_label=node_label, node_color=node_color, **kwargs)
    return node.rotation
```
### blur_attribute


- node : [BlurAttribute](/docs/GeoNodes/BlurAttribute.md)
- self : value
- jump : No
- return : value

##### Arguments

- iterations : None
- weight : None
- node_label : None
- node_color : None

#### Source code

``` python
def blur_attribute(self, iterations=None, weight=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.BlurAttribute(value=self, iterations=iterations, weight=weight, data_type='FLOAT_VECTOR', node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### ceil


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def ceil(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, operation='CEIL', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### cos


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def cos(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, operation='COSINE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### cross


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def cross(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='CROSS_PRODUCT', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### distance


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def distance(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='DISTANCE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### divide


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def divide(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='DIVIDE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### dot


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def dot(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='DOT_PRODUCT', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### equal


- node : [Compare](/docs/GeoNodes/Compare.md)
- self : a
- jump : No
- return : result

##### Arguments

- b : None
- epsilon : None
- mode : 'ELEMENT' in ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION')
- node_label : None
- node_color : None

#### Source code

``` python
def equal(self, b=None, epsilon=None, mode='ELEMENT', node_label=None, node_color=None, **kwargs):
    node = self.tree.Compare(a=self, b=b, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='EQUAL', node_label=node_label, node_color=node_color, **kwargs)
    return node.result
```
### euler_to_rotation


- node : [EulerToRotation](/docs/GeoNodes/EulerToRotation.md)
- self : euler
- jump : No
- return : rotation

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def euler_to_rotation(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.EulerToRotation(euler=self, node_label=node_label, node_color=node_color, **kwargs)
    return node.rotation
```
### faceforward


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- node_label : None
- node_color : None

#### Source code

``` python
def faceforward(self, vector=None, vector_1=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, vector_2=vector_1, operation='FACEFORWARD', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### floor


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def floor(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, operation='FLOOR', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### frac


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def frac(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, operation='FRACTION', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### greater_equal


- node : [Compare](/docs/GeoNodes/Compare.md)
- self : a
- jump : No
- return : result

##### Arguments

- b : None
- mode : 'ELEMENT' in ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION')
- node_label : None
- node_color : None

#### Source code

``` python
def greater_equal(self, b=None, mode='ELEMENT', node_label=None, node_color=None, **kwargs):
    node = self.tree.Compare(a=self, b=b, data_type='VECTOR', mode=mode, operation='GREATER_EQUAL', node_label=node_label, node_color=node_color, **kwargs)
    return node.result
```
### greater_than


- node : [Compare](/docs/GeoNodes/Compare.md)
- self : a
- jump : No
- return : result

##### Arguments

- b : None
- mode : 'ELEMENT' in ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION')
- node_label : None
- node_color : None

#### Source code

``` python
def greater_than(self, b=None, mode='ELEMENT', node_label=None, node_color=None, **kwargs):
    node = self.tree.Compare(a=self, b=b, data_type='VECTOR', mode=mode, operation='GREATER_THAN', node_label=node_label, node_color=node_color, **kwargs)
    return node.result
```
### index_switch


- node : [IndexSwitch](/docs/GeoNodes/IndexSwitch.md)
- self : ARG0
- jump : No
- return : output

##### Arguments

- *args : 'ARG_NO_VALUE'
- index : None
- node_label : None
- node_color : None

#### Source code

``` python
def index_switch(self, *args, index=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.IndexSwitch(self, *args, index=index, data_type='VECTOR', node_label=node_label, node_color=node_color, **kwargs)
    return node.output
```
### invert_rotation


- node : [InvertRotation](/docs/GeoNodes/InvertRotation.md)
- self : rotation
- jump : rotation
- return : self

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def invert_rotation(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.InvertRotation(rotation=self, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.rotation)
    return self
```
### length


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def length(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, operation='LENGTH', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### less_equal


- node : [Compare](/docs/GeoNodes/Compare.md)
- self : a
- jump : No
- return : result

##### Arguments

- b : None
- mode : 'ELEMENT' in ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION')
- node_label : None
- node_color : None

#### Source code

``` python
def less_equal(self, b=None, mode='ELEMENT', node_label=None, node_color=None, **kwargs):
    node = self.tree.Compare(a=self, b=b, data_type='VECTOR', mode=mode, operation='LESS_EQUAL', node_label=node_label, node_color=node_color, **kwargs)
    return node.result
```
### less_than


- node : [Compare](/docs/GeoNodes/Compare.md)
- self : a
- jump : No
- return : result

##### Arguments

- b : None
- mode : 'ELEMENT' in ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION')
- node_label : None
- node_color : None

#### Source code

``` python
def less_than(self, b=None, mode='ELEMENT', node_label=None, node_color=None, **kwargs):
    node = self.tree.Compare(a=self, b=b, data_type='VECTOR', mode=mode, operation='LESS_THAN', node_label=node_label, node_color=node_color, **kwargs)
    return node.result
```
### map_range


- node : [MapRange](/docs/GeoNodes/MapRange.md)
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


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def max(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='MAXIMUM', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### min


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def min(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='MINIMUM', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### mix


- node : [Mix](/docs/GeoNodes/Mix.md)
- self : a
- jump : result
- return : self

##### Arguments

- factor : None
- b : None
- clamp_factor : True
- clamp_result : False
- factor_mode : 'UNIFORM' in ('UNIFORM', 'NON_UNIFORM')
- node_label : None
- node_color : None

#### Source code

``` python
def mix(self, factor=None, b=None, clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='VECTOR', factor_mode=factor_mode, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.result)
    return self
```
### mod


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def mod(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='MODULO', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### multiply


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def multiply(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='MULTIPLY', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### multiply_add


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- node_label : None
- node_color : None

#### Source code

``` python
def multiply_add(self, vector=None, vector_1=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, vector_2=vector_1, operation='MULTIPLY_ADD', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### normalize


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def normalize(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, operation='NORMALIZE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### not_equal


- node : [Compare](/docs/GeoNodes/Compare.md)
- self : a
- jump : No
- return : result

##### Arguments

- b : None
- epsilon : None
- mode : 'ELEMENT' in ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION')
- node_label : None
- node_color : None

#### Source code

``` python
def not_equal(self, b=None, epsilon=None, mode='ELEMENT', node_label=None, node_color=None, **kwargs):
    node = self.tree.Compare(a=self, b=b, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='NOT_EQUAL', node_label=node_label, node_color=node_color, **kwargs)
    return node.result
```
### pack_uv_islands


- node : [PackUVIslands](/docs/GeoNodes/PackUVIslands.md)
- self : uv
- jump : uv
- return : self

##### Arguments

- margin : None
- rotate : None
- selection : None
- node_label : None
- node_color : None

#### Source code

``` python
def pack_uv_islands(self, margin=None, rotate=None, selection=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.PackUVIslands(uv=self, margin=margin, rotate=rotate, selection=self._get_selection(selection), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.uv)
    return self
```
### project


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def project(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='PROJECT', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### reflect


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def reflect(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='REFLECT', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### refract


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- scale : None
- node_label : None
- node_color : None

#### Source code

``` python
def refract(self, vector=None, scale=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, scale=scale, operation='REFRACT', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### rotate_euler


- node : [RotateEuler](/docs/GeoNodes/RotateEuler.md)
- self : rotation
- jump : rotation
- return : self

##### Arguments

- rotate_by : None
- axis : None
- angle : None
- rotation_type : 'EULER' in ('AXIS_ANGLE', 'EULER')
- space : 'OBJECT' in ('OBJECT', 'LOCAL')
- node_label : None
- node_color : None

#### Source code

``` python
def rotate_euler(self, rotate_by=None, axis=None, angle=None, rotation_type='EULER', space='OBJECT', node_label=None, node_color=None, **kwargs):
    node = self.tree.RotateEuler(rotation=self, rotate_by=rotate_by, axis=axis, angle=angle, rotation_type=rotation_type, space=space, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.rotation)
    return self
```
### rotate_euler_axis_angle


- node : [RotateEuler](/docs/GeoNodes/RotateEuler.md)
- self : rotation
- jump : rotation
- return : self

##### Arguments

- rotate_by : None
- axis : None
- angle : None
- rotation_type : 'EULER' in ('AXIS_ANGLE', 'EULER')
- space : 'OBJECT' in ('OBJECT', 'LOCAL')
- node_label : None
- node_color : None

#### Source code

``` python
def rotate_euler_axis_angle(self, rotate_by=None, axis=None, angle=None, rotation_type='EULER', space='OBJECT', node_label=None, node_color=None, **kwargs):
    node = self.tree.RotateEuler(rotation=self, rotate_by=rotate_by, axis=axis, angle=angle, rotation_type=rotation_type, space=space, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.rotation)
    return self
```
### rotate_euler_euler


- node : [RotateEuler](/docs/GeoNodes/RotateEuler.md)
- self : rotation
- jump : rotation
- return : self

##### Arguments

- rotate_by : None
- axis : None
- angle : None
- rotation_type : 'EULER' in ('AXIS_ANGLE', 'EULER')
- space : 'OBJECT' in ('OBJECT', 'LOCAL')
- node_label : None
- node_color : None

#### Source code

``` python
def rotate_euler_euler(self, rotate_by=None, axis=None, angle=None, rotation_type='EULER', space='OBJECT', node_label=None, node_color=None, **kwargs):
    node = self.tree.RotateEuler(rotation=self, rotate_by=rotate_by, axis=axis, angle=angle, rotation_type=rotation_type, space=space, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.rotation)
    return self
```
### rotate_vector


- node : [RotateVector](/docs/GeoNodes/RotateVector.md)
- self : vector
- jump : vector
- return : self

##### Arguments

- rotation : None
- node_label : None
- node_color : None

#### Source code

``` python
def rotate_vector(self, rotation=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.RotateVector(vector=self, rotation=rotation, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.vector)
    return self
```
### rotation_to_axis_angle


- node : [RotationToAxisAngle](/docs/GeoNodes/RotationToAxisAngle.md)
- self : rotation
- jump : No
- return : node

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def rotation_to_axis_angle(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.RotationToAxisAngle(rotation=self, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### rotation_to_euler


- node : [RotationToEuler](/docs/GeoNodes/RotationToEuler.md)
- self : rotation
- jump : No
- return : node

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def rotation_to_euler(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.RotationToEuler(rotation=self, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### rotation_to_quaternion


- node : [RotationToQuaternion](/docs/GeoNodes/RotationToQuaternion.md)
- self : rotation
- jump : No
- return : node

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def rotation_to_quaternion(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.RotationToQuaternion(rotation=self, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### scale


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- scale : None
- node_label : None
- node_color : None

#### Source code

``` python
def scale(self, scale=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, scale=scale, operation='SCALE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### separate_xyz


- node : [SeparateXYZ](/docs/GeoNodes/SeparateXYZ.md)
- self : vector
- jump : No
- return : node

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def separate_xyz(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.SeparateXYZ(vector=self, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sin


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def sin(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, operation='SINE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### snap


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def snap(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='SNAP', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### subtract


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def subtract(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='SUBTRACT', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### switch


- node : [Switch](/docs/GeoNodes/Switch.md)
- self : false
- jump : No
- return : output

##### Arguments

- switch : None
- true : None
- node_label : None
- node_color : None

#### Source code

``` python
def switch(self, switch=None, true=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.Switch(switch=switch, false=self, true=true, input_type='VECTOR', node_label=node_label, node_color=node_color, **kwargs)
    return node.output
```
### tan


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def tan(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, operation='TANGENT', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vector_curves


- node : [VectorCurves](/docs/GeoNodes/VectorCurves.md)
- self : vector
- jump : vector
- return : self

##### Arguments

- fac : None
- mapping : None
- node_label : None
- node_color : None

#### Source code

``` python
def vector_curves(self, fac=None, mapping=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorCurves(fac=fac, vector=self, mapping=mapping, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.vector)
    return self
```
### vector_rotate


- node : [VectorRotate](/docs/GeoNodes/VectorRotate.md)
- self : vector
- jump : No
- return : vector

##### Arguments

- center : None
- axis : None
- angle : None
- rotation : None
- invert : False
- rotation_type : 'AXIS_ANGLE' in ('AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ')
- node_label : None
- node_color : None

#### Source code

``` python
def vector_rotate(self, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE', node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorRotate(vector=self, center=center, axis=axis, angle=angle, rotation=rotation, invert=invert, rotation_type=rotation_type, node_label=node_label, node_color=node_color, **kwargs)
    return node.vector
```
### wrap


- node : [VectorMath](/docs/GeoNodes/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- node_label : None
- node_color : None

#### Source code

``` python
def wrap(self, vector=None, vector_1=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, vector_2=vector_1, operation='WRAP', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
