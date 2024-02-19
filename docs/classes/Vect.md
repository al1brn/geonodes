# class Vect (Socket)

<sub>go to [index](/docs/index.md)</sub>

Socket
 - Type : VECTOR
 - bl_idname : NodeSocketVector

Methods
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
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - operation : 'ABSOLUTE'
 - node_label : node_label
 - node_color : node_color

``` python
def abs(self, node_label=None, node_color=None):
```
### add

VectorMath, vector=self, operation='ADD'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - vector : None
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - vector_1 : vector
 - operation : 'ADD'
 - node_label : node_label
 - node_color : node_color

``` python
def add(self, vector=None, node_label=None, node_color=None):
```
### align_euler_to_vector

AlignEulerToVector, rotation=self

Node
 - class_name : [AlignEulerToVector](/docs/classes/AlignEulerToVector.md)
 - bl_idname : FunctionNodeAlignEulerToVector

Arguments
 - factor : None
 - vector : None
 - axis : 'X'
 - pivot_axis : 'AUTO'
 - node_label : None
 - node_color : None

Node initialization
 - rotation : self
 - factor : factor
 - vector : vector
 - axis : axis
 - pivot_axis : pivot_axis
 - node_label : node_label
 - node_color : node_color

``` python
def align_euler_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO', node_label=None, node_color=None):
```
### ceil

VectorMath, vector=self, operation='CEIL'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - operation : 'CEIL'
 - node_label : node_label
 - node_color : node_color

``` python
def ceil(self, node_label=None, node_color=None):
```
### cos

VectorMath, vector=self, operation='COSINE'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - operation : 'COSINE'
 - node_label : node_label
 - node_color : node_color

``` python
def cos(self, node_label=None, node_color=None):
```
### cross

VectorMath, vector=self, operation='CROSS_PRODUCT'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - vector : None
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - vector_1 : vector
 - operation : 'CROSS_PRODUCT'
 - node_label : node_label
 - node_color : node_color

``` python
def cross(self, vector=None, node_label=None, node_color=None):
```
### cube

Cube, size=self

Node
 - class_name : [Cube](/docs/classes/Cube.md)
 - bl_idname : GeometryNodeMeshCube

Arguments
 - vertices_x : None
 - vertices_y : None
 - vertices_z : None
 - node_label : None
 - node_color : None

Node initialization
 - size : self
 - vertices_x : vertices_x
 - vertices_y : vertices_y
 - vertices_z : vertices_z
 - node_label : node_label
 - node_color : node_color

``` python
def cube(self, vertices_x=None, vertices_y=None, vertices_z=None, node_label=None, node_color=None):
```
### distance

VectorMath, vector=self, operation='DISTANCE'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - vector : None
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - vector_1 : vector
 - operation : 'DISTANCE'
 - node_label : node_label
 - node_color : node_color

``` python
def distance(self, vector=None, node_label=None, node_color=None):
```
### divide

VectorMath, vector=self, operation='DIVIDE'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - vector : None
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - vector_1 : vector
 - operation : 'DIVIDE'
 - node_label : node_label
 - node_color : node_color

``` python
def divide(self, vector=None, node_label=None, node_color=None):
```
### dot

VectorMath, vector=self, operation='DOT_PRODUCT'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - vector : None
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - vector_1 : vector
 - operation : 'DOT_PRODUCT'
 - node_label : node_label
 - node_color : node_color

``` python
def dot(self, vector=None, node_label=None, node_color=None):
```
### equal

Compare, a=self, data_type='VECTOR', operation='EQUAL'

Node
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

Arguments
 - b : None
 - epsilon : None
 - mode : 'ELEMENT'
 - node_label : None
 - node_color : None

Node initialization
 - a : self
 - b : b
 - epsilon : epsilon
 - data_type : 'VECTOR'
 - mode : mode
 - operation : 'EQUAL'
 - node_label : node_label
 - node_color : node_color

``` python
def equal(self, b=None, epsilon=None, mode='ELEMENT', node_label=None, node_color=None):
```
### euler_to_rotation

EulerToRotation, euler=self, return socket

Node
 - class_name : [EulerToRotation](/docs/classes/EulerToRotation.md)
 - bl_idname : FunctionNodeEulerToRotation

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - euler : self
 - node_label : node_label
 - node_color : node_color

``` python
def euler_to_rotation(self, node_label=None, node_color=None):
```
### faceforward

VectorMath, vector=self, operation='FACEFORWARD'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - vector : None
 - vector_1 : None
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - vector_1 : vector
 - vector_2 : vector_1
 - operation : 'FACEFORWARD'
 - node_label : node_label
 - node_color : node_color

``` python
def faceforward(self, vector=None, vector_1=None, node_label=None, node_color=None):
```
### floor

VectorMath, vector=self, operation='FLOOR'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - operation : 'FLOOR'
 - node_label : node_label
 - node_color : node_color

``` python
def floor(self, node_label=None, node_color=None):
```
### frac

VectorMath, vector=self, operation='FRACTION'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - operation : 'FRACTION'
 - node_label : node_label
 - node_color : node_color

``` python
def frac(self, node_label=None, node_color=None):
```
### geometry_proximity

GeometryProximity, source_position=self

Node
 - class_name : [GeometryProximity](/docs/classes/GeometryProximity.md)
 - bl_idname : GeometryNodeProximity

Arguments
 - target : None
 - target_element : 'FACES'
 - node_label : None
 - node_color : None

Node initialization
 - target : target
 - source_position : self
 - target_element : target_element
 - node_label : node_label
 - node_color : node_color

``` python
def geometry_proximity(self, target=None, target_element='FACES', node_label=None, node_color=None):
```
### gradient_texture

GradientTexture, vector=self, return node

Node
 - class_name : [GradientTexture](/docs/classes/GradientTexture.md)
 - bl_idname : ShaderNodeTexGradient

Arguments
 - color_mapping
 - gradient_type : 'LINEAR'
 - texture_mapping
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - color_mapping : color_mapping
 - gradient_type : gradient_type
 - texture_mapping : texture_mapping
 - node_label : node_label
 - node_color : node_color

``` python
def gradient_texture(self, color_mapping=None, gradient_type='LINEAR', texture_mapping=None, node_label=None, node_color=None):
```
### greater_equal

Compare, a=self, data_type='VECTOR', operation='GREATER_EQUAL'

Node
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

Arguments
 - b : None
 - mode : 'ELEMENT'
 - node_label : None
 - node_color : None

Node initialization
 - a : self
 - b : b
 - data_type : 'VECTOR'
 - mode : mode
 - operation : 'GREATER_EQUAL'
 - node_label : node_label
 - node_color : node_color

``` python
def greater_equal(self, b=None, mode='ELEMENT', node_label=None, node_color=None):
```
### greater_than

Compare, a=self, data_type='VECTOR', operation='GREATER_THAN'

Node
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

Arguments
 - b : None
 - mode : 'ELEMENT'
 - node_label : None
 - node_color : None

Node initialization
 - a : self
 - b : b
 - data_type : 'VECTOR'
 - mode : mode
 - operation : 'GREATER_THAN'
 - node_label : node_label
 - node_color : node_color

``` python
def greater_than(self, b=None, mode='ELEMENT', node_label=None, node_color=None):
```
### length

VectorMath, vector=self, operation='LENGTH'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - operation : 'LENGTH'
 - node_label : node_label
 - node_color : node_color

``` python
def length(self, node_label=None, node_color=None):
```
### less_equal

Compare, a=self, data_type='VECTOR', operation='LESS_EQUAL'

Node
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

Arguments
 - b : None
 - mode : 'ELEMENT'
 - node_label : None
 - node_color : None

Node initialization
 - a : self
 - b : b
 - data_type : 'VECTOR'
 - mode : mode
 - operation : 'LESS_EQUAL'
 - node_label : node_label
 - node_color : node_color

``` python
def less_equal(self, b=None, mode='ELEMENT', node_label=None, node_color=None):
```
### less_than

Compare, a=self, data_type='VECTOR', operation='LESS_THAN'

Node
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

Arguments
 - b : None
 - mode : 'ELEMENT'
 - node_label : None
 - node_color : None

Node initialization
 - a : self
 - b : b
 - data_type : 'VECTOR'
 - mode : mode
 - operation : 'LESS_THAN'
 - node_label : node_label
 - node_color : node_color

``` python
def less_than(self, b=None, mode='ELEMENT', node_label=None, node_color=None):
```
### max

VectorMath, vector=self, operation='MAXIMUM'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - vector : None
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - vector_1 : vector
 - operation : 'MAXIMUM'
 - node_label : node_label
 - node_color : node_color

``` python
def max(self, vector=None, node_label=None, node_color=None):
```
### min

VectorMath, vector=self, operation='MINIMUM'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - vector : None
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - vector_1 : vector
 - operation : 'MINIMUM'
 - node_label : node_label
 - node_color : node_color

``` python
def min(self, vector=None, node_label=None, node_color=None):
```
### mix

Mix, a=self, data_type='VECTOR'

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
 - data_type : 'VECTOR'
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

``` python
def mix(self, factor=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
### mod

VectorMath, vector=self, operation='MODULO'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - vector : None
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - vector_1 : vector
 - operation : 'MODULO'
 - node_label : node_label
 - node_color : node_color

``` python
def mod(self, vector=None, node_label=None, node_color=None):
```
### multiply

VectorMath, vector=self, operation='MULTIPLY'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - vector : None
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - vector_1 : vector
 - operation : 'MULTIPLY'
 - node_label : node_label
 - node_color : node_color

``` python
def multiply(self, vector=None, node_label=None, node_color=None):
```
### multiply_add

VectorMath, vector=self, operation='MULTIPLY_ADD'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - vector : None
 - vector_1 : None
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - vector_1 : vector
 - vector_2 : vector_1
 - operation : 'MULTIPLY_ADD'
 - node_label : node_label
 - node_color : node_color

``` python
def multiply_add(self, vector=None, vector_1=None, node_label=None, node_color=None):
```
### normalize

VectorMath, vector=self, operation='NORMALIZE'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - operation : 'NORMALIZE'
 - node_label : node_label
 - node_color : node_color

``` python
def normalize(self, node_label=None, node_color=None):
```
### not_equal

Compare, a=self, data_type='VECTOR', operation='NOT_EQUAL'

Node
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

Arguments
 - b : None
 - epsilon : None
 - mode : 'ELEMENT'
 - node_label : None
 - node_color : None

Node initialization
 - a : self
 - b : b
 - epsilon : epsilon
 - data_type : 'VECTOR'
 - mode : mode
 - operation : 'NOT_EQUAL'
 - node_label : node_label
 - node_color : node_color

``` python
def not_equal(self, b=None, epsilon=None, mode='ELEMENT', node_label=None, node_color=None):
```
### pack_uv_islands

PackUVIslands, uv=self

Node
 - class_name : [PackUVIslands](/docs/classes/PackUVIslands.md)
 - bl_idname : GeometryNodeUVPackIslands

Arguments
 - margin : None
 - rotate : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - uv : self
 - margin : margin
 - rotate : rotate
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

``` python
def pack_uv_islands(self, margin=None, rotate=None, selection=None, node_label=None, node_color=None):
```
### project

VectorMath, vector=self, operation='PROJECT'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - vector : None
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - vector_1 : vector
 - operation : 'PROJECT'
 - node_label : node_label
 - node_color : node_color

``` python
def project(self, vector=None, node_label=None, node_color=None):
```
### reflect

VectorMath, vector=self, operation='REFLECT'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - vector : None
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - vector_1 : vector
 - operation : 'REFLECT'
 - node_label : node_label
 - node_color : node_color

``` python
def reflect(self, vector=None, node_label=None, node_color=None):
```
### refract

VectorMath, vector=self, operation='REFRACT'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - vector : None
 - scale : None
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - vector_1 : vector
 - scale : scale
 - operation : 'REFRACT'
 - node_label : node_label
 - node_color : node_color

``` python
def refract(self, vector=None, scale=None, node_label=None, node_color=None):
```
### rotate_euler

RotateEuler, rotation=self

Node
 - class_name : [RotateEuler](/docs/classes/RotateEuler.md)
 - bl_idname : FunctionNodeRotateEuler

Arguments
 - rotate_by : None
 - space : 'OBJECT'
 - node_label : None
 - node_color : None

Node initialization
 - rotation : self
 - rotate_by : rotate_by
 - space : space
 - node_label : node_label
 - node_color : node_color

``` python
def rotate_euler(self, rotate_by=None, space='OBJECT', node_label=None, node_color=None):
```
### rotate_vector

RotateVector, vector=self

Node
 - class_name : [RotateVector](/docs/classes/RotateVector.md)
 - bl_idname : FunctionNodeRotateVector

Arguments
 - rotation : None
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - rotation : rotation
 - node_label : node_label
 - node_color : node_color

``` python
def rotate_vector(self, rotation=None, node_label=None, node_color=None):
```
### scale

VectorMath, vector=self, operation='SCALE'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - scale : None
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - scale : scale
 - operation : 'SCALE'
 - node_label : node_label
 - node_color : node_color

``` python
def scale(self, scale=None, node_label=None, node_color=None):
```
### separate_xyz

SeparateXYZ, vector=self, return node

Node
 - class_name : [SeparateXYZ](/docs/classes/SeparateXYZ.md)
 - bl_idname : ShaderNodeSeparateXYZ

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - node_label : node_label
 - node_color : node_color

``` python
def separate_xyz(self, node_label=None, node_color=None):
```
### sin

VectorMath, vector=self, operation='SINE'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - operation : 'SINE'
 - node_label : node_label
 - node_color : node_color

``` python
def sin(self, node_label=None, node_color=None):
```
### snap

VectorMath, vector=self, operation='SNAP'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - vector : None
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - vector_1 : vector
 - operation : 'SNAP'
 - node_label : node_label
 - node_color : node_color

``` python
def snap(self, vector=None, node_label=None, node_color=None):
```
### subtract

VectorMath, vector=self, operation='SUBTRACT'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - vector : None
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - vector_1 : vector
 - operation : 'SUBTRACT'
 - node_label : node_label
 - node_color : node_color

``` python
def subtract(self, vector=None, node_label=None, node_color=None):
```
### switch

Switch, false=self, input_type='VECTOR'

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
 - input_type : 'VECTOR'
 - node_label : node_label
 - node_color : node_color

``` python
def switch(self, switch=None, true=None, node_label=None, node_color=None):
```
### tan

VectorMath, vector=self, operation='TANGENT'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - operation : 'TANGENT'
 - node_label : node_label
 - node_color : node_color

``` python
def tan(self, node_label=None, node_color=None):
```
### vector_curves

VectorCurves, vector=self

Node
 - class_name : [VectorCurves](/docs/classes/VectorCurves.md)
 - bl_idname : ShaderNodeVectorCurve

Arguments
 - fac : None
 - mapping
 - node_label : None
 - node_color : None

Node initialization
 - fac : fac
 - vector : self
 - mapping : mapping
 - node_label : node_label
 - node_color : node_color

``` python
def vector_curves(self, fac=None, mapping=None, node_label=None, node_color=None):
```
### vector_math

VectorMath, vector=self

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - vector : None
 - vector_1 : None
 - scale : None
 - operation : 'ADD'
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - vector_1 : vector
 - vector_2 : vector_1
 - scale : scale
 - operation : operation
 - node_label : node_label
 - node_color : node_color

``` python
def vector_math(self, vector=None, vector_1=None, scale=None, operation='ADD', node_label=None, node_color=None):
```
### vector_rotate

VectorRotate, vector=self

Node
 - class_name : [VectorRotate](/docs/classes/VectorRotate.md)
 - bl_idname : ShaderNodeVectorRotate

Arguments
 - center : None
 - axis : None
 - angle : None
 - rotation : None
 - invert : False
 - rotation_type : 'AXIS_ANGLE'
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - center : center
 - axis : axis
 - angle : angle
 - rotation : rotation
 - invert : invert
 - rotation_type : rotation_type
 - node_label : node_label
 - node_color : node_color

``` python
def vector_rotate(self, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE', node_label=None, node_color=None):
```
### white_noise_texture

WhiteNoiseTexture, vector=self

Node
 - class_name : [WhiteNoiseTexture](/docs/classes/WhiteNoiseTexture.md)
 - bl_idname : ShaderNodeTexWhiteNoise

Arguments
 - w : None
 - noise_dimensions : '3D'
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - w : w
 - noise_dimensions : noise_dimensions
 - node_label : node_label
 - node_color : node_color

``` python
def white_noise_texture(self, w=None, noise_dimensions='3D', node_label=None, node_color=None):
```
### wrap

VectorMath, vector=self, operation='WRAP'

Node
 - class_name : [VectorMath](/docs/classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - vector : None
 - vector_1 : None
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - vector_1 : vector
 - vector_2 : vector_1
 - operation : 'WRAP'
 - node_label : node_label
 - node_color : node_color

``` python
def wrap(self, vector=None, vector_1=None, node_label=None, node_color=None):
```
### xyz

SeparateXYZ, Shortcut for Vect.separate_xyz

Node
 - class_name : [SeparateXYZ](/docs/classes/SeparateXYZ.md)
 - bl_idname : ShaderNodeSeparateXYZ

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - node_label : node_label
 - node_color : node_color

``` python
def xyz(self, node_label=None, node_color=None):
```