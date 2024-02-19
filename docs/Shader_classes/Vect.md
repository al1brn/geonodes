# class Vect (Socket)

<sub>go to [index](/docs/index.md)</sub>

Socket
 - Type : VECTOR
 - bl_idname : NodeSocketVector

Methods
 - [abs](#abs) : VectorMath, vector=self, operation='ABSOLUTE'
 - [add](#add) : VectorMath, vector=self, operation='ADD'
 - [bevel](#bevel) : Bevel, normal=self
 - [bump](#bump) : Bump, normal=self
 - [ceil](#ceil) : VectorMath, vector=self, operation='CEIL'
 - [cos](#cos) : VectorMath, vector=self, operation='COSINE'
 - [cross](#cross) : VectorMath, vector=self, operation='CROSS_PRODUCT'
 - [displacement](#displacement) : Displacement, normal=self
 - [distance](#distance) : VectorMath, vector=self, operation='DISTANCE'
 - [divide](#divide) : VectorMath, vector=self, operation='DIVIDE'
 - [dot](#dot) : VectorMath, vector=self, operation='DOT_PRODUCT'
 - [environment_texture](#environment_texture) : EnvironmentTexture, vector=self, return socket
 - [faceforward](#faceforward) : VectorMath, vector=self, operation='FACEFORWARD'
 - [floor](#floor) : VectorMath, vector=self, operation='FLOOR'
 - [frac](#frac) : VectorMath, vector=self, operation='FRACTION'
 - [gradient_texture](#gradient_texture) : GradientTexture, vector=self, return node
 - [image_texture](#image_texture) : ImageTexture, vector=self, return node
 - [length](#length) : VectorMath, vector=self, operation='LENGTH'
 - [mapping](#mapping) : Mapping, vector=self
 - [max](#max) : VectorMath, vector=self, operation='MAXIMUM'
 - [min](#min) : VectorMath, vector=self, operation='MINIMUM'
 - [mix](#mix) : Mix, a=self, data_type='VECTOR'
 - [mod](#mod) : VectorMath, vector=self, operation='MODULO'
 - [multiply](#multiply) : VectorMath, vector=self, operation='MULTIPLY'
 - [multiply_add](#multiply_add) : VectorMath, vector=self, operation='MULTIPLY_ADD'
 - [normal](#normal) : Normal, normal=self
 - [normalize](#normalize) : VectorMath, vector=self, operation='NORMALIZE'
 - [point_density](#point_density) : PointDensity, vector=self, return node
 - [project](#project) : VectorMath, vector=self, operation='PROJECT'
 - [reflect](#reflect) : VectorMath, vector=self, operation='REFLECT'
 - [refract](#refract) : VectorMath, vector=self, operation='REFRACT'
 - [scale](#scale) : VectorMath, vector=self, operation='SCALE'
 - [separate_xyz](#separate_xyz) : SeparateXYZ, vector=self, return node
 - [sin](#sin) : VectorMath, vector=self, operation='SINE'
 - [sky_texture](#sky_texture) : SkyTexture, vector=self, return socket
 - [snap](#snap) : VectorMath, vector=self, operation='SNAP'
 - [subtract](#subtract) : VectorMath, vector=self, operation='SUBTRACT'
 - [tan](#tan) : VectorMath, vector=self, operation='TANGENT'
 - [vector_curves](#vector_curves) : VectorCurves, vector=self
 - [vector_math](#vector_math) : VectorMath, vector=self
 - [vector_rotate](#vector_rotate) : VectorRotate, vector=self
 - [vector_transform](#vector_transform) : VectorTransform, vector=self
 - [white_noise_texture](#white_noise_texture) : WhiteNoiseTexture, vector=self
 - [wrap](#wrap) : VectorMath, vector=self, operation='WRAP'
 - [xyz](#xyz) : SeparateXYZ, Shortcut for Vect.separate_xyz

## Methods

### abs

> VectorMath, vector=self, operation='ABSOLUTE'

``` python
def abs(self, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - operation : 'ABSOLUTE'
 - node_label : node_label
 - node_color : node_color

### add

> VectorMath, vector=self, operation='ADD'

``` python
def add(self, vector=None, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
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

### bevel

> Bevel, normal=self

``` python
def bevel(self, radius=None, samples=4, node_label=None, node_color=None):
```
Node
 - class_name : [Bevel](/docs/Shader_classes/Bevel.md)
 - bl_idname : ShaderNodeBevel

Arguments
 - radius : None
 - samples : 4
 - node_label : None
 - node_color : None

Node initialization
 - radius : radius
 - normal : self
 - samples : samples
 - node_label : node_label
 - node_color : node_color

### bump

> Bump, normal=self

``` python
def bump(self, strength=None, distance=None, height=None, invert=False, node_label=None, node_color=None):
```
Node
 - class_name : [Bump](/docs/Shader_classes/Bump.md)
 - bl_idname : ShaderNodeBump

Arguments
 - strength : None
 - distance : None
 - height : None
 - invert : False
 - node_label : None
 - node_color : None

Node initialization
 - strength : strength
 - distance : distance
 - height : height
 - normal : self
 - invert : invert
 - node_label : node_label
 - node_color : node_color

### ceil

> VectorMath, vector=self, operation='CEIL'

``` python
def ceil(self, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - operation : 'CEIL'
 - node_label : node_label
 - node_color : node_color

### cos

> VectorMath, vector=self, operation='COSINE'

``` python
def cos(self, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - operation : 'COSINE'
 - node_label : node_label
 - node_color : node_color

### cross

> VectorMath, vector=self, operation='CROSS_PRODUCT'

``` python
def cross(self, vector=None, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
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

### displacement

> Displacement, normal=self

``` python
def displacement(self, height=None, midlevel=None, scale=None, space='OBJECT', node_label=None, node_color=None):
```
Node
 - class_name : [Displacement](/docs/Shader_classes/Displacement.md)
 - bl_idname : ShaderNodeDisplacement

Arguments
 - height : None
 - midlevel : None
 - scale : None
 - space : 'OBJECT'
 - node_label : None
 - node_color : None

Node initialization
 - height : height
 - midlevel : midlevel
 - scale : scale
 - normal : self
 - space : space
 - node_label : node_label
 - node_color : node_color

### distance

> VectorMath, vector=self, operation='DISTANCE'

``` python
def distance(self, vector=None, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
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

### divide

> VectorMath, vector=self, operation='DIVIDE'

``` python
def divide(self, vector=None, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
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

### dot

> VectorMath, vector=self, operation='DOT_PRODUCT'

``` python
def dot(self, vector=None, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
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

### environment_texture

> EnvironmentTexture, vector=self, return socket

``` python
def environment_texture(self, color_mapping=None, image=None, image_user=None, interpolation='Linear', projection='EQUIRECTANGULAR', texture_mapping=None, node_label=None, node_color=None):
```
Node
 - class_name : [EnvironmentTexture](/docs/Shader_classes/EnvironmentTexture.md)
 - bl_idname : ShaderNodeTexEnvironment

Arguments
 - color_mapping
 - image : None
 - image_user
 - interpolation : 'Linear'
 - projection : 'EQUIRECTANGULAR'
 - texture_mapping
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - color_mapping : color_mapping
 - image : image
 - image_user : image_user
 - interpolation : interpolation
 - projection : projection
 - texture_mapping : texture_mapping
 - node_label : node_label
 - node_color : node_color

### faceforward

> VectorMath, vector=self, operation='FACEFORWARD'

``` python
def faceforward(self, vector=None, vector_1=None, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
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

### floor

> VectorMath, vector=self, operation='FLOOR'

``` python
def floor(self, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - operation : 'FLOOR'
 - node_label : node_label
 - node_color : node_color

### frac

> VectorMath, vector=self, operation='FRACTION'

``` python
def frac(self, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - operation : 'FRACTION'
 - node_label : node_label
 - node_color : node_color

### gradient_texture

> GradientTexture, vector=self, return node

``` python
def gradient_texture(self, color_mapping=None, gradient_type='LINEAR', texture_mapping=None, node_label=None, node_color=None):
```
Node
 - class_name : [GradientTexture](/docs/Shader_classes/GradientTexture.md)
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

### image_texture

> ImageTexture, vector=self, return node

``` python
def image_texture(self, color_mapping=None, extension='REPEAT', image=None, image_user=None, interpolation='Linear', projection='FLAT', projection_blend=0.0, texture_mapping=None, node_label=None, node_color=None):
```
Node
 - class_name : [ImageTexture](/docs/Shader_classes/ImageTexture.md)
 - bl_idname : ShaderNodeTexImage

Arguments
 - color_mapping
 - extension : 'REPEAT'
 - image : None
 - image_user
 - interpolation : 'Linear'
 - projection : 'FLAT'
 - projection_blend : 0.0
 - texture_mapping
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - color_mapping : color_mapping
 - extension : extension
 - image : image
 - image_user : image_user
 - interpolation : interpolation
 - projection : projection
 - projection_blend : projection_blend
 - texture_mapping : texture_mapping
 - node_label : node_label
 - node_color : node_color

### length

> VectorMath, vector=self, operation='LENGTH'

``` python
def length(self, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - operation : 'LENGTH'
 - node_label : node_label
 - node_color : node_color

### mapping

> Mapping, vector=self

``` python
def mapping(self, location=None, rotation=None, scale=None, vector_type='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [Mapping](/docs/Shader_classes/Mapping.md)
 - bl_idname : ShaderNodeMapping

Arguments
 - location : None
 - rotation : None
 - scale : None
 - vector_type : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - location : location
 - rotation : rotation
 - scale : scale
 - vector_type : vector_type
 - node_label : node_label
 - node_color : node_color

### max

> VectorMath, vector=self, operation='MAXIMUM'

``` python
def max(self, vector=None, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
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

### min

> VectorMath, vector=self, operation='MINIMUM'

``` python
def min(self, vector=None, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
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

### mix

> Mix, a=self, data_type='VECTOR'

``` python
def mix(self, factor=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False, factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/Shader_classes/Mix.md)
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

### mod

> VectorMath, vector=self, operation='MODULO'

``` python
def mod(self, vector=None, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
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

### multiply

> VectorMath, vector=self, operation='MULTIPLY'

``` python
def multiply(self, vector=None, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
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

### multiply_add

> VectorMath, vector=self, operation='MULTIPLY_ADD'

``` python
def multiply_add(self, vector=None, vector_1=None, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
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

### normal

> Normal, normal=self

``` python
def normal(self, node_label=None, node_color=None):
```
Node
 - class_name : [Normal](/docs/Shader_classes/Normal.md)
 - bl_idname : ShaderNodeNormal

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - normal : self
 - node_label : node_label
 - node_color : node_color

### normalize

> VectorMath, vector=self, operation='NORMALIZE'

``` python
def normalize(self, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - operation : 'NORMALIZE'
 - node_label : node_label
 - node_color : node_color

### point_density

> PointDensity, vector=self, return node

``` python
def point_density(self, cache_point_density=None, calc_point_density=None, calc_point_density_minmax=None, interpolation='Linear', object=None, particle_color_source='PARTICLE_AGE', particle_system=None, point_source='PARTICLE_SYSTEM',
radius=0.30000001192092896, resolution=100, space='OBJECT', vertex_attribute_name='', vertex_color_source='VERTEX_COLOR', node_label=None, node_color=None):
```
Node
 - class_name : [PointDensity](/docs/Shader_classes/PointDensity.md)
 - bl_idname : ShaderNodeTexPointDensity

Arguments
 - cache_point_density
 - calc_point_density
 - calc_point_density_minmax
 - interpolation : 'Linear'
 - object : None
 - particle_color_source : 'PARTICLE_AGE'
 - particle_system : None
 - point_source : 'PARTICLE_SYSTEM'
 - radius : 0.30000001192092896
 - resolution : 100
 - space : 'OBJECT'
 - vertex_attribute_name : ''
 - vertex_color_source : 'VERTEX_COLOR'
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - cache_point_density : cache_point_density
 - calc_point_density : calc_point_density
 - calc_point_density_minmax : calc_point_density_minmax
 - interpolation : interpolation
 - object : object
 - particle_color_source : particle_color_source
 - particle_system : particle_system
 - point_source : point_source
 - radius : radius
 - resolution : resolution
 - space : space
 - vertex_attribute_name : vertex_attribute_name
 - vertex_color_source : vertex_color_source
 - node_label : node_label
 - node_color : node_color

### project

> VectorMath, vector=self, operation='PROJECT'

``` python
def project(self, vector=None, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
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

### reflect

> VectorMath, vector=self, operation='REFLECT'

``` python
def reflect(self, vector=None, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
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

### refract

> VectorMath, vector=self, operation='REFRACT'

``` python
def refract(self, vector=None, scale=None, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
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

### scale

> VectorMath, vector=self, operation='SCALE'

``` python
def scale(self, scale=None, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
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

### separate_xyz

> SeparateXYZ, vector=self, return node

``` python
def separate_xyz(self, node_label=None, node_color=None):
```
Node
 - class_name : [SeparateXYZ](/docs/Shader_classes/SeparateXYZ.md)
 - bl_idname : ShaderNodeSeparateXYZ

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - node_label : node_label
 - node_color : node_color

### sin

> VectorMath, vector=self, operation='SINE'

``` python
def sin(self, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - operation : 'SINE'
 - node_label : node_label
 - node_color : node_color

### sky_texture

> SkyTexture, vector=self, return socket

``` python
def sky_texture(self, air_density=1.0, altitude=0.0, color_mapping=None, dust_density=1.0, ground_albedo=0.30000001192092896, ozone_density=1.0, sky_type='NISHITA', sun_direction=(0.0, 0.0, 1.0), sun_disc=True, sun_elevation=0.2617993950843811,
sun_intensity=1.0, sun_rotation=0.0, sun_size=0.009512044489383698, texture_mapping=None, turbidity=2.200000047683716, node_label=None, node_color=None):
```
Node
 - class_name : [SkyTexture](/docs/Shader_classes/SkyTexture.md)
 - bl_idname : ShaderNodeTexSky

Arguments
 - air_density : 1.0
 - altitude : 0.0
 - color_mapping
 - dust_density : 1.0
 - ground_albedo : 0.30000001192092896
 - ozone_density : 1.0
 - sky_type : 'NISHITA'
 - sun_direction : (0.0, 0.0, 1.0)
 - sun_disc : True
 - sun_elevation : 0.2617993950843811
 - sun_intensity : 1.0
 - sun_rotation : 0.0
 - sun_size : 0.009512044489383698
 - texture_mapping
 - turbidity : 2.200000047683716
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - air_density : air_density
 - altitude : altitude
 - color_mapping : color_mapping
 - dust_density : dust_density
 - ground_albedo : ground_albedo
 - ozone_density : ozone_density
 - sky_type : sky_type
 - sun_direction : sun_direction
 - sun_disc : sun_disc
 - sun_elevation : sun_elevation
 - sun_intensity : sun_intensity
 - sun_rotation : sun_rotation
 - sun_size : sun_size
 - texture_mapping : texture_mapping
 - turbidity : turbidity
 - node_label : node_label
 - node_color : node_color

### snap

> VectorMath, vector=self, operation='SNAP'

``` python
def snap(self, vector=None, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
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

### subtract

> VectorMath, vector=self, operation='SUBTRACT'

``` python
def subtract(self, vector=None, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
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

### tan

> VectorMath, vector=self, operation='TANGENT'

``` python
def tan(self, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
 - bl_idname : ShaderNodeVectorMath

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - operation : 'TANGENT'
 - node_label : node_label
 - node_color : node_color

### vector_curves

> VectorCurves, vector=self

``` python
def vector_curves(self, fac=None, mapping=None, node_label=None, node_color=None):
```
Node
 - class_name : [VectorCurves](/docs/Shader_classes/VectorCurves.md)
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

### vector_math

> VectorMath, vector=self

``` python
def vector_math(self, vector=None, vector_1=None, scale=None, operation='ADD', node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
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

### vector_rotate

> VectorRotate, vector=self

``` python
def vector_rotate(self, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE', node_label=None, node_color=None):
```
Node
 - class_name : [VectorRotate](/docs/Shader_classes/VectorRotate.md)
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

### vector_transform

> VectorTransform, vector=self

``` python
def vector_transform(self, convert_from='WORLD', convert_to='OBJECT', vector_type='VECTOR', node_label=None, node_color=None):
```
Node
 - class_name : [VectorTransform](/docs/Shader_classes/VectorTransform.md)
 - bl_idname : ShaderNodeVectorTransform

Arguments
 - convert_from : 'WORLD'
 - convert_to : 'OBJECT'
 - vector_type : 'VECTOR'
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - convert_from : convert_from
 - convert_to : convert_to
 - vector_type : vector_type
 - node_label : node_label
 - node_color : node_color

### white_noise_texture

> WhiteNoiseTexture, vector=self

``` python
def white_noise_texture(self, w=None, noise_dimensions='3D', node_label=None, node_color=None):
```
Node
 - class_name : [WhiteNoiseTexture](/docs/Shader_classes/WhiteNoiseTexture.md)
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

### wrap

> VectorMath, vector=self, operation='WRAP'

``` python
def wrap(self, vector=None, vector_1=None, node_label=None, node_color=None):
```
Node
 - class_name : [VectorMath](/docs/Shader_classes/VectorMath.md)
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

### xyz

> SeparateXYZ, Shortcut for Vect.separate_xyz

``` python
def xyz(self, node_label=None, node_color=None):
```
Node
 - class_name : [SeparateXYZ](/docs/Shader_classes/SeparateXYZ.md)
 - bl_idname : ShaderNodeSeparateXYZ

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - vector : self
 - node_label : node_label
 - node_color : node_color
