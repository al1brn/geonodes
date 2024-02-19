# class Vect (Socket)

<sub>go to [index](/docs/index.md)</sub>

Socket
------
 - Type : VECTOR
 - bl_idname : NodeSocketVector

Methods
-------
 - [abs](#abs) : VectorMath, vector=self, operation='ABSOLUTE'
 - [add](#add) : VectorMath, vector=self, operation='ADD'
 - [align_euler_to_vector](#align_euler_to_vector) : AlignEulerToVector, rotation=self
 - [ceil](#ceil) : VectorMath, vector=self, operation='CEIL'
 - [cos](#cos) : VectorMath, vector=self, operation='COSINE'
 - [cross](#cross) : VectorMath, vector=self, operation='CROSS_PRODUCT'
 - [cube](#cube) : Cube, size=self
 - [distance](#distance) : VectorMath, vector=self, operation='DISTANCE'
 - [divide](#divide) : VectorMath, vector=self, operation='DIVIDE'
 - [dot](#dot) : VectorMath, vector=self, operation='DOT_PRODUCT'
 - [equal](#equal) : Compare, a=self, data_type='VECTOR', operation='EQUAL'
 - [euler_to_rotation](#euler_to_rotation) : EulerToRotation, euler=self, return socket
 - [faceforward](#faceforward) : VectorMath, vector=self, operation='FACEFORWARD'
 - [floor](#floor) : VectorMath, vector=self, operation='FLOOR'
 - [frac](#frac) : VectorMath, vector=self, operation='FRACTION'
 - [geometry_proximity](#geometry_proximity) : GeometryProximity, source_position=self
 - [gradient_texture](#gradient_texture) : GradientTexture, vector=self, return node
 - [greater_equal](#greater_equal) : Compare, a=self, data_type='VECTOR', operation='GREATER_EQUAL'
 - [greater_than](#greater_than) : Compare, a=self, data_type='VECTOR', operation='GREATER_THAN'
 - [length](#length) : VectorMath, vector=self, operation='LENGTH'
 - [less_equal](#less_equal) : Compare, a=self, data_type='VECTOR', operation='LESS_EQUAL'
 - [less_than](#less_than) : Compare, a=self, data_type='VECTOR', operation='LESS_THAN'
 - [max](#max) : VectorMath, vector=self, operation='MAXIMUM'
 - [min](#min) : VectorMath, vector=self, operation='MINIMUM'
 - [mix](#mix) : Mix, a=self, data_type='VECTOR'
 - [mod](#mod) : VectorMath, vector=self, operation='MODULO'
 - [multiply](#multiply) : VectorMath, vector=self, operation='MULTIPLY'
 - [multiply_add](#multiply_add) : VectorMath, vector=self, operation='MULTIPLY_ADD'
 - [normalize](#normalize) : VectorMath, vector=self, operation='NORMALIZE'
 - [not_equal](#not_equal) : Compare, a=self, data_type='VECTOR', operation='NOT_EQUAL'
 - [pack_uv_islands](#pack_uv_islands) : PackUVIslands, uv=self
 - [project](#project) : VectorMath, vector=self, operation='PROJECT'
 - [reflect](#reflect) : VectorMath, vector=self, operation='REFLECT'
 - [refract](#refract) : VectorMath, vector=self, operation='REFRACT'
 - [rotate_euler](#rotate_euler) : RotateEuler, rotation=self
 - [rotate_vector](#rotate_vector) : RotateVector, vector=self
 - [scale](#scale) : VectorMath, vector=self, operation='SCALE'
 - [separate_xyz](#separate_xyz) : SeparateXYZ, vector=self, return node
 - [sin](#sin) : VectorMath, vector=self, operation='SINE'
 - [snap](#snap) : VectorMath, vector=self, operation='SNAP'
 - [subtract](#subtract) : VectorMath, vector=self, operation='SUBTRACT'
 - [switch](#switch) : Switch, false=self, input_type='VECTOR'
 - [tan](#tan) : VectorMath, vector=self, operation='TANGENT'
 - [vector_curves](#vector_curves) : VectorCurves, vector=self
 - [vector_math](#vector_math) : VectorMath, vector=self
 - [vector_rotate](#vector_rotate) : VectorRotate, vector=self
 - [white_noise_texture](#white_noise_texture) : WhiteNoiseTexture, vector=self
 - [wrap](#wrap) : VectorMath, vector=self, operation='WRAP'
 - [xyz](#xyz) : SeparateXYZ, Shortcut for Vect.separate_xyz

## Methods

### abs

VectorMath, vector=self, operation='ABSOLUTE'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### add

VectorMath, vector=self, operation='ADD'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### align_euler_to_vector

AlignEulerToVector, rotation=self

Node
----
 - class_name : [AlignEulerToVector](/docs/classes/AlignEulerToVector.md)
 - bl_idname : FunctionNodeAlignEulerToVector

### ceil

VectorMath, vector=self, operation='CEIL'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### cos

VectorMath, vector=self, operation='COSINE'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### cross

VectorMath, vector=self, operation='CROSS_PRODUCT'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### cube

Cube, size=self

Node
----
 - class_name : [Cube](/docs/classes/Cube.md)
 - bl_idname : GeometryNodeMeshCube

### distance

VectorMath, vector=self, operation='DISTANCE'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### divide

VectorMath, vector=self, operation='DIVIDE'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### dot

VectorMath, vector=self, operation='DOT_PRODUCT'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### equal

Compare, a=self, data_type='VECTOR', operation='EQUAL'

Node
----
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

### euler_to_rotation

EulerToRotation, euler=self, return socket

Node
----
 - class_name : [EulerToRotation](/docs/classes/EulerToRotation.md)
 - bl_idname : FunctionNodeEulerToRotation

### faceforward

VectorMath, vector=self, operation='FACEFORWARD'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### floor

VectorMath, vector=self, operation='FLOOR'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### frac

VectorMath, vector=self, operation='FRACTION'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### geometry_proximity

GeometryProximity, source_position=self

Node
----
 - class_name : [GeometryProximity](/docs/classes/GeometryProximity.md)
 - bl_idname : GeometryNodeProximity

### gradient_texture

GradientTexture, vector=self, return node

Node
----
 - class_name : [GradientTexture](/docs/classes/GradientTexture.md)
 - bl_idname : ShaderNodeTexGradient

### greater_equal

Compare, a=self, data_type='VECTOR', operation='GREATER_EQUAL'

Node
----
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

### greater_than

Compare, a=self, data_type='VECTOR', operation='GREATER_THAN'

Node
----
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

### length

VectorMath, vector=self, operation='LENGTH'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### less_equal

Compare, a=self, data_type='VECTOR', operation='LESS_EQUAL'

Node
----
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

### less_than

Compare, a=self, data_type='VECTOR', operation='LESS_THAN'

Node
----
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

### max

VectorMath, vector=self, operation='MAXIMUM'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### min

VectorMath, vector=self, operation='MINIMUM'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### mix

Mix, a=self, data_type='VECTOR'

Node
----
 - class_name : [Mix](/docs/classes/Mix.md)
 - bl_idname : ShaderNodeMix

### mod

VectorMath, vector=self, operation='MODULO'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### multiply

VectorMath, vector=self, operation='MULTIPLY'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### multiply_add

VectorMath, vector=self, operation='MULTIPLY_ADD'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### normalize

VectorMath, vector=self, operation='NORMALIZE'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### not_equal

Compare, a=self, data_type='VECTOR', operation='NOT_EQUAL'

Node
----
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

### pack_uv_islands

PackUVIslands, uv=self

Node
----
 - class_name : [PackUVIslands](/docs/classes/PackUVIslands.md)
 - bl_idname : GeometryNodeUVPackIslands

### project

VectorMath, vector=self, operation='PROJECT'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### reflect

VectorMath, vector=self, operation='REFLECT'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### refract

VectorMath, vector=self, operation='REFRACT'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### rotate_euler

RotateEuler, rotation=self

Node
----
 - class_name : [RotateEuler](/docs/classes/RotateEuler.md)
 - bl_idname : FunctionNodeRotateEuler

### rotate_vector

RotateVector, vector=self

Node
----
 - class_name : [RotateVector](/docs/classes/RotateVector.md)
 - bl_idname : FunctionNodeRotateVector

### scale

VectorMath, vector=self, operation='SCALE'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### separate_xyz

SeparateXYZ, vector=self, return node

Node
----
 - class_name : [SeparateXYZ](/docs/classes/SeparateXYZ.md)
 - bl_idname : ShaderNodeSeparateXYZ

### sin

VectorMath, vector=self, operation='SINE'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### snap

VectorMath, vector=self, operation='SNAP'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### subtract

VectorMath, vector=self, operation='SUBTRACT'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### switch

Switch, false=self, input_type='VECTOR'

Node
----
 - class_name : [Switch](/docs/classes/Switch.md)
 - bl_idname : GeometryNodeSwitch

### tan

VectorMath, vector=self, operation='TANGENT'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### vector_curves

VectorCurves, vector=self

Node
----
 - class_name : [VectorCurves](/docs/classes/VectorCurves.md)
 - bl_idname : ShaderNodeVectorCurve

### vector_math

VectorMath, vector=self

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### vector_rotate

VectorRotate, vector=self

Node
----
 - class_name : [VectorRotate](/docs/classes/VectorRotate.md)
 - bl_idname : ShaderNodeVectorRotate

### white_noise_texture

WhiteNoiseTexture, vector=self

Node
----
 - class_name : [WhiteNoiseTexture](/docs/classes/WhiteNoiseTexture.md)
 - bl_idname : ShaderNodeTexWhiteNoise

### wrap

VectorMath, vector=self, operation='WRAP'

Node
----
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

### xyz

SeparateXYZ, Shortcut for Vect.separate_xyz

Node
----
 - class_name : [SeparateXYZ](/docs/classes/SeparateXYZ.md)
 - bl_idname : ShaderNodeSeparateXYZ
