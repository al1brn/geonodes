# class Rot (Socket)

<sub>go to [index](/docs/index.md)</sub>

Socket
------
 - Type : ROTATION
 - bl_idname : NodeSocketRotation

Methods
-------
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
----
 - class_name : [InvertRotation](/docs/classes/InvertRotation.md)
 - bl_idname : FunctionNodeInvertRotation

### mix

Mix, a=self, data_type='ROTATION'

Node
----
 - class_name : [Mix](/docs/classes/Mix.md)
 - bl_idname : ShaderNodeMix

### rotation_to_axis_angle

RotationToAxisAngle, rotation=self, return node

Node
----
 - class_name : [RotationToAxisAngle](/docs/classes/RotationToAxisAngle.md)
 - bl_idname : FunctionNodeRotationToAxisAngle

### rotation_to_euler

RotationToEuler, rotation=self, return socket

Node
----
 - class_name : [RotationToEuler](/docs/classes/RotationToEuler.md)
 - bl_idname : FunctionNodeRotationToEuler

### rotation_to_quaternion

RotationToQuaternion, rotation=self, return node

Node
----
 - class_name : [RotationToQuaternion](/docs/classes/RotationToQuaternion.md)
 - bl_idname : FunctionNodeRotationToQuaternion

### switch

Switch, false=self, input_type='ROTATION'

Node
----
 - class_name : [Switch](/docs/classes/Switch.md)
 - bl_idname : GeometryNodeSwitch
