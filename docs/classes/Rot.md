# class Rot (Socket)

<sub>go to [index](/docs/index.md)</sub>

Socket
 - Type : ROTATION
 - bl_idname : NodeSocketRotation

Methods
 - [invert_rotation](#invert_rotation) : InvertRotation, rotation=self
 - [mix](#mix) : Mix, a=self, data_type='ROTATION'
 - [rotation_to_axis_angle](#rotation_to_axis_angle) : RotationToAxisAngle, rotation=self, return node
 - [rotation_to_euler](#rotation_to_euler) : RotationToEuler, rotation=self, return socket
 - [rotation_to_quaternion](#rotation_to_quaternion) : RotationToQuaternion, rotation=self, return node
 - [switch](#switch) : Switch, false=self, input_type='ROTATION'

## Methods

### invert_rotation

InvertRotation, rotation=self

Node
 - class_name : [InvertRotation](/docs/classes/InvertRotation.md)
 - bl_idname : FunctionNodeInvertRotation

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - rotation : self
 - node_label : node_label
 - node_color : node_color

``` python
def invert_rotation(self, node_label=None, node_color=None):
```
### mix

Mix, a=self, data_type='ROTATION'

Node
 - class_name : [Mix](/docs/classes/Mix.md)
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
 - data_type : 'ROTATION'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

``` python
def mix(self, factor=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
### rotation_to_axis_angle

RotationToAxisAngle, rotation=self, return node

Node
 - class_name : [RotationToAxisAngle](/docs/classes/RotationToAxisAngle.md)
 - bl_idname : FunctionNodeRotationToAxisAngle

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - rotation : self
 - node_label : node_label
 - node_color : node_color

``` python
def rotation_to_axis_angle(self, node_label=None, node_color=None):
```
### rotation_to_euler

RotationToEuler, rotation=self, return socket

Node
 - class_name : [RotationToEuler](/docs/classes/RotationToEuler.md)
 - bl_idname : FunctionNodeRotationToEuler

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - rotation : self
 - node_label : node_label
 - node_color : node_color

``` python
def rotation_to_euler(self, node_label=None, node_color=None):
```
### rotation_to_quaternion

RotationToQuaternion, rotation=self, return node

Node
 - class_name : [RotationToQuaternion](/docs/classes/RotationToQuaternion.md)
 - bl_idname : FunctionNodeRotationToQuaternion

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - rotation : self
 - node_label : node_label
 - node_color : node_color

``` python
def rotation_to_quaternion(self, node_label=None, node_color=None):
```
### switch

Switch, false=self, input_type='ROTATION'

Node
 - class_name : [Switch](/docs/classes/Switch.md)
 - bl_idname : GeometryNodeSwitch

Arguments
 - switch : None
 - true : None
 - node_label : None
 - node_color : None

Node initialization
 - switch : switch
 - false : self
 - true : true
 - input_type : 'ROTATION'
 - node_label : node_label
 - node_color : node_color

``` python
def switch(self, switch=None, true=None, node_label=None, node_color=None):
```