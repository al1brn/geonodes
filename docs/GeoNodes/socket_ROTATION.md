# Socket ROTATION


### Methods

- [abs](#abs)
- [add](#add)
- [align_euler_to_vector](#align_euler_to_vector)
- [ceil](#ceil)
- [cos](#cos)
- [cross](#cross)
- [distance](#distance)
- [divide](#divide)
- [dot](#dot)
- [faceforward](#faceforward)
- [floor](#floor)
- [frac](#frac)
- [index_switch](#index_switch)
- [invert_rotation](#invert_rotation)
- [length](#length)
- [max](#max)
- [min](#min)
- [mix](#mix)
- [mod](#mod)
- [multiply](#multiply)
- [multiply_add](#multiply_add)
- [normalize](#normalize)
- [project](#project)
- [reflect](#reflect)
- [refract](#refract)
- [rotate_euler](#rotate_euler)
- [rotate_euler_axis_angle](#rotate_euler_axis_angle)
- [rotate_euler_euler](#rotate_euler_euler)
- [rotate_rotation](#rotate_rotation)
- [rotation_to_axis_angle](#rotation_to_axis_angle)
- [rotation_to_euler](#rotation_to_euler)
- [rotation_to_quaternion](#rotation_to_quaternion)
- [scale](#scale)
- [sin](#sin)
- [snap](#snap)
- [subtract](#subtract)
- [switch](#switch)
- [tan](#tan)
- [vector_curves](#vector_curves)
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
    node = self.tree.IndexSwitch(self, *args, index=index, data_type='ROTATION', node_label=node_label, node_color=node_color, **kwargs)
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
- node_label : None
- node_color : None

#### Source code

``` python
def mix(self, factor=None, b=None, clamp_factor=True, clamp_result=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.Mix(factor=factor, a=self, b=b, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='ROTATION', factor_mode='UNIFORM', node_label=node_label, node_color=node_color, **kwargs)
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
### rotate_rotation


- node : [RotateRotation](/docs/GeoNodes/RotateRotation.md)
- self : rotation
- jump : rotation
- return : self

##### Arguments

- rotate_by : None
- rotation_space : 'GLOBAL' in ('GLOBAL', 'LOCAL')
- node_label : None
- node_color : None

#### Source code

``` python
def rotate_rotation(self, rotate_by=None, rotation_space='GLOBAL', node_label=None, node_color=None, **kwargs):
    node = self.tree.RotateRotation(rotation=self, rotate_by=rotate_by, rotation_space=rotation_space, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.rotation)
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
    node = self.tree.Switch(switch=switch, false=self, true=true, input_type='ROTATION', node_label=node_label, node_color=node_color, **kwargs)
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
