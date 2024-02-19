# Global functions

***A*** : [abs](#abs) [add](#add) [add_shader](#add_shader) [arccos](#arccos) [arcsin](#arcsin) [arctan](#arctan) [arctan2](#arctan2) [attribute](#attribute)

***B*** : [background](#background) [bevel](#bevel) [blackbody](#blackbody) [brightness_contrast](#brightness_contrast) [bump](#bump)

***C*** : [camera_data](#camera_data) [ceil](#ceil) [clamp](#clamp) [color_attribute](#color_attribute) [combine_color](#combine_color) [combine_hsl](#combine_hsl) [combine_hsv](#combine_hsv) [combine_rgb](#combine_rgb) [combine_xyz](#combine_xyz) [compare](#compare) [cos](#cos) [cosh](#cosh) [curves_info](#curves_info)

***D*** : [degrees](#degrees) [diffuse_bsdf](#diffuse_bsdf) [displacement](#displacement) [divide](#divide)

***E*** : [emission](#emission) [environment_texture](#environment_texture) [exp](#exp)

***F*** : [float_curve](#float_curve) [floor](#floor) [floored_modulo](#floored_modulo) [fract](#fract) [frame](#frame) [fresnel](#fresnel)

***G*** : [gamma](#gamma) [geometry](#geometry) [glass_bsdf](#glass_bsdf) [glossy_bsdf](#glossy_bsdf) [greater_than](#greater_than)

***H*** : [hair_bsdf](#hair_bsdf) [holdout](#holdout) [hue_saturation_value](#hue_saturation_value)

***I*** : [ies_texture](#ies_texture) [inverse_sqrt](#inverse_sqrt) [invert_color](#invert_color)

***L*** : [less_than](#less_than) [light_path](#light_path) [log](#log)

***M*** : [mapping](#mapping) [math](#math) [max](#max) [min](#min) [mix](#mix) [mix_shader](#mix_shader) [mod](#mod) [multiply](#multiply) [multiply_add](#multiply_add) [musgrave_texture](#musgrave_texture)

***N*** : [normal_map](#normal_map)

***O*** : [object_info](#object_info)

***P*** : [particle_info](#particle_info) [pingpong](#pingpong) [point_info](#point_info) [power](#power) [principled_bsdf](#principled_bsdf) [principled_hair_bsdf](#principled_hair_bsdf) [principled_volume](#principled_volume)

***R*** : [radians](#radians) [refraction_bsdf](#refraction_bsdf) [reroute](#reroute) [rgb](#rgb) [rgb_curves](#rgb_curves) [rgb_to_bw](#rgb_to_bw) [round](#round)

***S*** : [script](#script) [sheen_bsdf](#sheen_bsdf) [sign](#sign) [sin](#sin) [sinh](#sinh) [sky_texture](#sky_texture) [smooth_max](#smooth_max) [smooth_min](#smooth_min) [snap](#snap) [specular_bsdf](#specular_bsdf) [sqrt](#sqrt) [subsurface_scattering](#subsurface_scattering) [subtract](#subtract)

***T*** : [tan](#tan) [tangent](#tangent) [tanh](#tanh) [texture_coordinate](#texture_coordinate) [toon_bsdf](#toon_bsdf) [translucent_bsdf](#translucent_bsdf) [transparent_bsdf](#transparent_bsdf) [trunc](#trunc)

***U*** : [uv_along_stroke](#uv_along_stroke) [uv_map](#uv_map)

***V*** : [value](#value) [vector_curves](#vector_curves) [vector_displacement](#vector_displacement) [vector_rotate](#vector_rotate) [vector_transform](#vector_transform) [volume_absorption](#volume_absorption) [volume_info](#volume_info) [volume_scatter](#volume_scatter)

***W*** : [wavelength](#wavelength) [wireframe](#wireframe) [wrap](#wrap)

## abs

> Math, value=self, operation='ABSOLUTE'

``` python
def abs(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'ABSOLUTE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## add

> Math, value=self, operation='ADD'

``` python
def add(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'ADD'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## add_shader

> AddShader, return single output socket

``` python
def add_shader(shader=None, shader_1=None, node_label=None, node_color=None):
```
Node
 - class_name : [AddShader](/docs/Shader_classes/AddShader.md)
 - bl_idname : ShaderNodeAddShader

Arguments
 - shader : None
 - shader_1 : None
 - node_label : None
 - node_color : None

Node initialization
 - shader : shader
 - shader_1 : shader_1
 - node_label : node_label
 - node_color : node_color

## arccos

> Math, value=self, operation='ARCCOSINE'

``` python
def arccos(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'ARCCOSINE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## arcsin

> Math, value=self, operation='ARCSINE'

``` python
def arcsin(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'ARCSINE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## arctan

> Math, value=self, operation='ARCTANGENT'

``` python
def arctan(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'ARCTANGENT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## arctan2

> Math, value=self, operation='ARCTAN2'

``` python
def arctan2(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'ARCTAN2'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## attribute

> Attribute, return node

``` python
def attribute(attribute_name='', attribute_type='GEOMETRY', node_label=None, node_color=None):
```
Node
 - class_name : [Attribute](/docs/Shader_classes/Attribute.md)
 - bl_idname : ShaderNodeAttribute

Arguments
 - attribute_name : ''
 - attribute_type : 'GEOMETRY'
 - node_label : None
 - node_color : None

Node initialization
 - attribute_name : attribute_name
 - attribute_type : attribute_type
 - node_label : node_label
 - node_color : node_color

## background

> Background, return single output socket

``` python
def background(color=None, strength=None, node_label=None, node_color=None):
```
Node
 - class_name : [Background](/docs/Shader_classes/Background.md)
 - bl_idname : ShaderNodeBackground

Arguments
 - color : None
 - strength : None
 - node_label : None
 - node_color : None

Node initialization
 - color : color
 - strength : strength
 - node_label : node_label
 - node_color : node_color

## bevel

> Bevel, return single output socket

``` python
def bevel(radius=None, normal=None, samples=4, node_label=None, node_color=None):
```
Node
 - class_name : [Bevel](/docs/Shader_classes/Bevel.md)
 - bl_idname : ShaderNodeBevel

Arguments
 - radius : None
 - normal : None
 - samples : 4
 - node_label : None
 - node_color : None

Node initialization
 - radius : radius
 - normal : normal
 - samples : samples
 - node_label : node_label
 - node_color : node_color

## blackbody

> Blackbody, return single output socket

``` python
def blackbody(temperature=None, node_label=None, node_color=None):
```
Node
 - class_name : [Blackbody](/docs/Shader_classes/Blackbody.md)
 - bl_idname : ShaderNodeBlackbody

Arguments
 - temperature : None
 - node_label : None
 - node_color : None

Node initialization
 - temperature : temperature
 - node_label : node_label
 - node_color : node_color

## brightness_contrast

> BrightnessContrast, return single output socket

``` python
def brightness_contrast(color=None, bright=None, contrast=None, node_label=None, node_color=None):
```
Node
 - class_name : [BrightnessContrast](/docs/Shader_classes/BrightnessContrast.md)
 - bl_idname : ShaderNodeBrightContrast

Arguments
 - color : None
 - bright : None
 - contrast : None
 - node_label : None
 - node_color : None

Node initialization
 - color : color
 - bright : bright
 - contrast : contrast
 - node_label : node_label
 - node_color : node_color

## bump

> Bump, return single output socket

``` python
def bump(strength=None, distance=None, height=None, normal=None, invert=False, node_label=None, node_color=None):
```
Node
 - class_name : [Bump](/docs/Shader_classes/Bump.md)
 - bl_idname : ShaderNodeBump

Arguments
 - strength : None
 - distance : None
 - height : None
 - normal : None
 - invert : False
 - node_label : None
 - node_color : None

Node initialization
 - strength : strength
 - distance : distance
 - height : height
 - normal : normal
 - invert : invert
 - node_label : node_label
 - node_color : node_color

## camera_data

> CameraData, return node

``` python
def camera_data(node_label=None, node_color=None):
```
Node
 - class_name : [CameraData](/docs/Shader_classes/CameraData.md)
 - bl_idname : ShaderNodeCameraData

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## ceil

> Math, value=self, operation='CEIL'

``` python
def ceil(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'CEIL'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## clamp

> Clamp, return single output socket

``` python
def clamp(value=None, min=None, max=None, clamp_type='MINMAX', node_label=None, node_color=None):
```
Node
 - class_name : [Clamp](/docs/Shader_classes/Clamp.md)
 - bl_idname : ShaderNodeClamp

Arguments
 - value : None
 - min : None
 - max : None
 - clamp_type : 'MINMAX'
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - min : min
 - max : max
 - clamp_type : clamp_type
 - node_label : node_label
 - node_color : node_color

## color_attribute

> ColorAttribute, return node

``` python
def color_attribute(layer_name='', node_label=None, node_color=None):
```
Node
 - class_name : [ColorAttribute](/docs/Shader_classes/ColorAttribute.md)
 - bl_idname : ShaderNodeVertexColor

Arguments
 - layer_name : ''
 - node_label : None
 - node_color : None

Node initialization
 - layer_name : layer_name
 - node_label : node_label
 - node_color : node_color

## combine_color

> CombineColor, return single output socket

``` python
def combine_color(red=None, green=None, blue=None, mode='RGB', node_label=None, node_color=None):
```
Node
 - class_name : [CombineColor](/docs/Shader_classes/CombineColor.md)
 - bl_idname : ShaderNodeCombineColor

Arguments
 - red : None
 - green : None
 - blue : None
 - mode : 'RGB'
 - node_label : None
 - node_color : None

Node initialization
 - red : red
 - green : green
 - blue : blue
 - mode : mode
 - node_label : node_label
 - node_color : node_color

## combine_hsl

> CombineColor, mode='HSL'

``` python
def combine_hsl(red=None, green=None, blue=None, node_label=None, node_color=None):
```
Node
 - class_name : [CombineColor](/docs/Shader_classes/CombineColor.md)
 - bl_idname : ShaderNodeCombineColor

Arguments
 - red : None
 - green : None
 - blue : None
 - node_label : None
 - node_color : None

Node initialization
 - red : red
 - green : green
 - blue : blue
 - mode : 'HSL'
 - node_label : node_label
 - node_color : node_color

## combine_hsv

> CombineColor, mode='HSV'

``` python
def combine_hsv(red=None, green=None, blue=None, node_label=None, node_color=None):
```
Node
 - class_name : [CombineColor](/docs/Shader_classes/CombineColor.md)
 - bl_idname : ShaderNodeCombineColor

Arguments
 - red : None
 - green : None
 - blue : None
 - node_label : None
 - node_color : None

Node initialization
 - red : red
 - green : green
 - blue : blue
 - mode : 'HSV'
 - node_label : node_label
 - node_color : node_color

## combine_rgb

> CombineColor, mode='RGB'

``` python
def combine_rgb(red=None, green=None, blue=None, node_label=None, node_color=None):
```
Node
 - class_name : [CombineColor](/docs/Shader_classes/CombineColor.md)
 - bl_idname : ShaderNodeCombineColor

Arguments
 - red : None
 - green : None
 - blue : None
 - node_label : None
 - node_color : None

Node initialization
 - red : red
 - green : green
 - blue : blue
 - mode : 'RGB'
 - node_label : node_label
 - node_color : node_color

## combine_xyz

> CombineXYZ, return single output socket

``` python
def combine_xyz(x=None, y=None, z=None, node_label=None, node_color=None):
```
Node
 - class_name : [CombineXYZ](/docs/Shader_classes/CombineXYZ.md)
 - bl_idname : ShaderNodeCombineXYZ

Arguments
 - x : None
 - y : None
 - z : None
 - node_label : None
 - node_color : None

Node initialization
 - x : x
 - y : y
 - z : z
 - node_label : node_label
 - node_color : node_color

## compare

> Math, value=self, operation='COMPARE'

``` python
def compare(value=None, value_1=None, value_2=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - value_2 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - value_2 : value_2
 - operation : 'COMPARE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## cos

> Math, value=self, operation='COSINE'

``` python
def cos(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'COSINE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## cosh

> Math, value=self, operation='COSH'

``` python
def cosh(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'COSH'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## curves_info

> CurvesInfo, return node

``` python
def curves_info(node_label=None, node_color=None):
```
Node
 - class_name : [CurvesInfo](/docs/Shader_classes/CurvesInfo.md)
 - bl_idname : ShaderNodeHairInfo

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## degrees

> Math, value=self, operation='DEGREES'

``` python
def degrees(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'DEGREES'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## diffuse_bsdf

> DiffuseBSDF, return single output socket

``` python
def diffuse_bsdf(color=None, roughness=None, normal=None, node_label=None, node_color=None):
```
Node
 - class_name : [DiffuseBSDF](/docs/Shader_classes/DiffuseBSDF.md)
 - bl_idname : ShaderNodeBsdfDiffuse

Arguments
 - color : None
 - roughness : None
 - normal : None
 - node_label : None
 - node_color : None

Node initialization
 - color : color
 - roughness : roughness
 - normal : normal
 - node_label : node_label
 - node_color : node_color

## displacement

> Displacement, return single output socket

``` python
def displacement(height=None, midlevel=None, scale=None, normal=None, space='OBJECT', node_label=None, node_color=None):
```
Node
 - class_name : [Displacement](/docs/Shader_classes/Displacement.md)
 - bl_idname : ShaderNodeDisplacement

Arguments
 - height : None
 - midlevel : None
 - scale : None
 - normal : None
 - space : 'OBJECT'
 - node_label : None
 - node_color : None

Node initialization
 - height : height
 - midlevel : midlevel
 - scale : scale
 - normal : normal
 - space : space
 - node_label : node_label
 - node_color : node_color

## divide

> Math, value=self, operation='DIVIDE'

``` python
def divide(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'DIVIDE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## emission

> Emission, return single output socket

``` python
def emission(color=None, strength=None, node_label=None, node_color=None):
```
Node
 - class_name : [Emission](/docs/Shader_classes/Emission.md)
 - bl_idname : ShaderNodeEmission

Arguments
 - color : None
 - strength : None
 - node_label : None
 - node_color : None

Node initialization
 - color : color
 - strength : strength
 - node_label : node_label
 - node_color : node_color

## environment_texture

> EnvironmentTexture, return single output socket

``` python
def environment_texture(vector=None, color_mapping=None, image=None, image_user=None, interpolation='Linear', projection='EQUIRECTANGULAR', texture_mapping=None, node_label=None, node_color=None):
```
Node
 - class_name : [EnvironmentTexture](/docs/Shader_classes/EnvironmentTexture.md)
 - bl_idname : ShaderNodeTexEnvironment

Arguments
 - vector : None
 - color_mapping
 - image : None
 - image_user
 - interpolation : 'Linear'
 - projection : 'EQUIRECTANGULAR'
 - texture_mapping
 - node_label : None
 - node_color : None

Node initialization
 - vector : vector
 - color_mapping : color_mapping
 - image : image
 - image_user : image_user
 - interpolation : interpolation
 - projection : projection
 - texture_mapping : texture_mapping
 - node_label : node_label
 - node_color : node_color

## exp

> Math, value=self, operation='EXPONENT'

``` python
def exp(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'EXPONENT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## float_curve

> FloatCurve, return single output socket

``` python
def float_curve(factor=None, value=None, mapping=None, node_label=None, node_color=None):
```
Node
 - class_name : [FloatCurve](/docs/Shader_classes/FloatCurve.md)
 - bl_idname : ShaderNodeFloatCurve

Arguments
 - factor : None
 - value : None
 - mapping
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - value : value
 - mapping : mapping
 - node_label : node_label
 - node_color : node_color

## floor

> Math, value=self, operation='FLOOR'

``` python
def floor(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'FLOOR'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## floored_modulo

> Math, value=self, operation='FLOORED_MODULO'

``` python
def floored_modulo(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'FLOORED_MODULO'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## fract

> Math, value=self, operation='FRACT'

``` python
def fract(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'FRACT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## frame

> Frame, return node

``` python
def frame(label_size=20, shrink=True, text=None, node_label=None, node_color=None):
```
Node
 - class_name : [Frame](/docs/Shader_classes/Frame.md)
 - bl_idname : NodeFrame

Arguments
 - label_size : 20
 - shrink : True
 - text : None
 - node_label : None
 - node_color : None

Node initialization
 - label_size : label_size
 - shrink : shrink
 - text : text
 - node_label : node_label
 - node_color : node_color

## fresnel

> Fresnel, return single output socket

``` python
def fresnel(ior=None, normal=None, node_label=None, node_color=None):
```
Node
 - class_name : [Fresnel](/docs/Shader_classes/Fresnel.md)
 - bl_idname : ShaderNodeFresnel

Arguments
 - ior : None
 - normal : None
 - node_label : None
 - node_color : None

Node initialization
 - ior : ior
 - normal : normal
 - node_label : node_label
 - node_color : node_color

## gamma

> Gamma, return single output socket

``` python
def gamma(color=None, gamma=None, node_label=None, node_color=None):
```
Node
 - class_name : [Gamma](/docs/Shader_classes/Gamma.md)
 - bl_idname : ShaderNodeGamma

Arguments
 - color : None
 - gamma : None
 - node_label : None
 - node_color : None

Node initialization
 - color : color
 - gamma : gamma
 - node_label : node_label
 - node_color : node_color

## geometry

> Geometry, return node

``` python
def geometry(node_label=None, node_color=None):
```
Node
 - class_name : [Geometry](/docs/Shader_classes/Geometry.md)
 - bl_idname : ShaderNodeNewGeometry

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## glass_bsdf

> GlassBSDF, return single output socket

``` python
def glass_bsdf(color=None, roughness=None, ior=None, normal=None, distribution='MULTI_GGX', node_label=None, node_color=None):
```
Node
 - class_name : [GlassBSDF](/docs/Shader_classes/GlassBSDF.md)
 - bl_idname : ShaderNodeBsdfGlass

Arguments
 - color : None
 - roughness : None
 - ior : None
 - normal : None
 - distribution : 'MULTI_GGX'
 - node_label : None
 - node_color : None

Node initialization
 - color : color
 - roughness : roughness
 - ior : ior
 - normal : normal
 - distribution : distribution
 - node_label : node_label
 - node_color : node_color

## glossy_bsdf

> GlossyBSDF, return single output socket

``` python
def glossy_bsdf(color=None, roughness=None, anisotropy=None, rotation=None, normal=None, tangent=None, distribution='MULTI_GGX', node_label=None, node_color=None):
```
Node
 - class_name : [GlossyBSDF](/docs/Shader_classes/GlossyBSDF.md)
 - bl_idname : ShaderNodeBsdfAnisotropic

Arguments
 - color : None
 - roughness : None
 - anisotropy : None
 - rotation : None
 - normal : None
 - tangent : None
 - distribution : 'MULTI_GGX'
 - node_label : None
 - node_color : None

Node initialization
 - color : color
 - roughness : roughness
 - anisotropy : anisotropy
 - rotation : rotation
 - normal : normal
 - tangent : tangent
 - distribution : distribution
 - node_label : node_label
 - node_color : node_color

## greater_than

> Math, value=self, operation='GREATER_THAN'

``` python
def greater_than(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'GREATER_THAN'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## hair_bsdf

> HairBSDF, return single output socket

``` python
def hair_bsdf(color=None, offset=None, roughnessu=None, roughnessv=None, tangent=None, component='Reflection', node_label=None, node_color=None):
```
Node
 - class_name : [HairBSDF](/docs/Shader_classes/HairBSDF.md)
 - bl_idname : ShaderNodeBsdfHair

Arguments
 - color : None
 - offset : None
 - roughnessu : None
 - roughnessv : None
 - tangent : None
 - component : 'Reflection'
 - node_label : None
 - node_color : None

Node initialization
 - color : color
 - offset : offset
 - roughnessu : roughnessu
 - roughnessv : roughnessv
 - tangent : tangent
 - component : component
 - node_label : node_label
 - node_color : node_color

## holdout

> Holdout, return socket

``` python
def holdout(node_label=None, node_color=None):
```
Node
 - class_name : [Holdout](/docs/Shader_classes/Holdout.md)
 - bl_idname : ShaderNodeHoldout

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## hue_saturation_value

> HueSaturationValue, return single output socket

``` python
def hue_saturation_value(hue=None, saturation=None, value=None, fac=None, color=None, node_label=None, node_color=None):
```
Node
 - class_name : [HueSaturationValue](/docs/Shader_classes/HueSaturationValue.md)
 - bl_idname : ShaderNodeHueSaturation

Arguments
 - hue : None
 - saturation : None
 - value : None
 - fac : None
 - color : None
 - node_label : None
 - node_color : None

Node initialization
 - hue : hue
 - saturation : saturation
 - value : value
 - fac : fac
 - color : color
 - node_label : node_label
 - node_color : node_color

## ies_texture

> IESTexture, return single output socket

``` python
def ies_texture(vector=None, strength=None, filepath='', ies=None, mode='INTERNAL', node_label=None, node_color=None):
```
Node
 - class_name : [IESTexture](/docs/Shader_classes/IESTexture.md)
 - bl_idname : ShaderNodeTexIES

Arguments
 - vector : None
 - strength : None
 - filepath : ''
 - ies : None
 - mode : 'INTERNAL'
 - node_label : None
 - node_color : None

Node initialization
 - vector : vector
 - strength : strength
 - filepath : filepath
 - ies : ies
 - mode : mode
 - node_label : node_label
 - node_color : node_color

## inverse_sqrt

> Math, value=self, operation='INVERSE_SQRT'

``` python
def inverse_sqrt(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'INVERSE_SQRT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## invert_color

> InvertColor, return single output socket

``` python
def invert_color(fac=None, color=None, node_label=None, node_color=None):
```
Node
 - class_name : [InvertColor](/docs/Shader_classes/InvertColor.md)
 - bl_idname : ShaderNodeInvert

Arguments
 - fac : None
 - color : None
 - node_label : None
 - node_color : None

Node initialization
 - fac : fac
 - color : color
 - node_label : node_label
 - node_color : node_color

## less_than

> Math, value=self, operation='LESS_THAN'

``` python
def less_than(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'LESS_THAN'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## light_path

> LightPath, return node

``` python
def light_path(node_label=None, node_color=None):
```
Node
 - class_name : [LightPath](/docs/Shader_classes/LightPath.md)
 - bl_idname : ShaderNodeLightPath

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## log

> Math, value=self, operation='LOGARITHM'

``` python
def log(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'LOGARITHM'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## mapping

> Mapping, return single output socket

``` python
def mapping(vector=None, location=None, rotation=None, scale=None, vector_type='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [Mapping](/docs/Shader_classes/Mapping.md)
 - bl_idname : ShaderNodeMapping

Arguments
 - vector : None
 - location : None
 - rotation : None
 - scale : None
 - vector_type : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - vector : vector
 - location : location
 - rotation : rotation
 - scale : scale
 - vector_type : vector_type
 - node_label : node_label
 - node_color : node_color

## math

> Math, return single output socket

``` python
def math(value=None, value_1=None, value_2=None, operation='ADD', use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - value_2 : None
 - operation : 'ADD'
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - value_2 : value_2
 - operation : operation
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## max

> Math, value=self, operation='MAXIMUM'

``` python
def max(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'MAXIMUM'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## min

> Math, value=self, operation='MINIMUM'

``` python
def min(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'MINIMUM'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## mix

> Mix, return single output socket

``` python
def mix(factor=None, a=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False, data_type='FLOAT', factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/Shader_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - a : None
 - b : None
 - blend_type : 'MIX'
 - clamp_factor : True
 - clamp_result : False
 - data_type : 'FLOAT'
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : a
 - b : b
 - blend_type : blend_type
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : data_type
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

## mix_shader

> MixShader, return single output socket

``` python
def mix_shader(fac=None, shader=None, shader_1=None, node_label=None, node_color=None):
```
Node
 - class_name : [MixShader](/docs/Shader_classes/MixShader.md)
 - bl_idname : ShaderNodeMixShader

Arguments
 - fac : None
 - shader : None
 - shader_1 : None
 - node_label : None
 - node_color : None

Node initialization
 - fac : fac
 - shader : shader
 - shader_1 : shader_1
 - node_label : node_label
 - node_color : node_color

## mod

> Math, value=self, operation='MODULO'

``` python
def mod(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'MODULO'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## multiply

> Math, value=self, operation='MULTIPLY'

``` python
def multiply(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'MULTIPLY'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## multiply_add

> Math, value=self, operation='MULTIPLY_ADD'

``` python
def multiply_add(value=None, value_1=None, value_2=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - value_2 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - value_2 : value_2
 - operation : 'MULTIPLY_ADD'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## musgrave_texture

> MusgraveTexture, return single output socket

``` python
def musgrave_texture(vector=None, scale=None, detail=None, dimension=None, lacunarity=None, w=None, offset=None, gain=None, color_mapping=None, musgrave_dimensions='3D', musgrave_type='FBM', texture_mapping=None, node_label=None, node_color=None):
```
Node
 - class_name : [MusgraveTexture](/docs/Shader_classes/MusgraveTexture.md)
 - bl_idname : ShaderNodeTexMusgrave

Arguments
 - vector : None
 - scale : None
 - detail : None
 - dimension : None
 - lacunarity : None
 - w : None
 - offset : None
 - gain : None
 - color_mapping
 - musgrave_dimensions : '3D'
 - musgrave_type : 'FBM'
 - texture_mapping
 - node_label : None
 - node_color : None

Node initialization
 - vector : vector
 - scale : scale
 - detail : detail
 - dimension : dimension
 - lacunarity : lacunarity
 - w : w
 - offset : offset
 - gain : gain
 - color_mapping : color_mapping
 - musgrave_dimensions : musgrave_dimensions
 - musgrave_type : musgrave_type
 - texture_mapping : texture_mapping
 - node_label : node_label
 - node_color : node_color

## normal_map

> NormalMap, return single output socket

``` python
def normal_map(strength=None, color=None, space='TANGENT', uv_map='', node_label=None, node_color=None):
```
Node
 - class_name : [NormalMap](/docs/Shader_classes/NormalMap.md)
 - bl_idname : ShaderNodeNormalMap

Arguments
 - strength : None
 - color : None
 - space : 'TANGENT'
 - uv_map : ''
 - node_label : None
 - node_color : None

Node initialization
 - strength : strength
 - color : color
 - space : space
 - uv_map : uv_map
 - node_label : node_label
 - node_color : node_color

## object_info

> ObjectInfo, return node

``` python
def object_info(node_label=None, node_color=None):
```
Node
 - class_name : [ObjectInfo](/docs/Shader_classes/ObjectInfo.md)
 - bl_idname : ShaderNodeObjectInfo

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## particle_info

> ParticleInfo, return node

``` python
def particle_info(node_label=None, node_color=None):
```
Node
 - class_name : [ParticleInfo](/docs/Shader_classes/ParticleInfo.md)
 - bl_idname : ShaderNodeParticleInfo

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## pingpong

> Math, value=self, operation='PINGPONG'

``` python
def pingpong(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'PINGPONG'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## point_info

> PointInfo, return node

``` python
def point_info(node_label=None, node_color=None):
```
Node
 - class_name : [PointInfo](/docs/Shader_classes/PointInfo.md)
 - bl_idname : ShaderNodePointInfo

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## power

> Math, value=self, operation='POWER'

``` python
def power(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'POWER'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## principled_bsdf

> PrincipledBSDF, return single output socket

``` python
def principled_bsdf(base_color=None, metallic=None, roughness=None, ior=None, alpha=None, normal=None, subsurface_weight=None, subsurface_radius=None, subsurface_scale=None, subsurface_anisotropy=None, specular_ior_level=None, specular_tint=None,
anisotropic=None, anisotropic_rotation=None, tangent=None, transmission_weight=None, coat_weight=None, coat_roughness=None, coat_ior=None, coat_tint=None, coat_normal=None, sheen_weight=None, sheen_roughness=None, sheen_tint=None,
emission_color=None, emission_strength=None, subsurface_ior=None, distribution='MULTI_GGX', subsurface_method='RANDOM_WALK', node_label=None, node_color=None):
```
Node
 - class_name : [PrincipledBSDF](/docs/Shader_classes/PrincipledBSDF.md)
 - bl_idname : ShaderNodeBsdfPrincipled

Arguments
 - base_color : None
 - metallic : None
 - roughness : None
 - ior : None
 - alpha : None
 - normal : None
 - subsurface_weight : None
 - subsurface_radius : None
 - subsurface_scale : None
 - subsurface_anisotropy : None
 - specular_ior_level : None
 - specular_tint : None
 - anisotropic : None
 - anisotropic_rotation : None
 - tangent : None
 - transmission_weight : None
 - coat_weight : None
 - coat_roughness : None
 - coat_ior : None
 - coat_tint : None
 - coat_normal : None
 - sheen_weight : None
 - sheen_roughness : None
 - sheen_tint : None
 - emission_color : None
 - emission_strength : None
 - subsurface_ior : None
 - distribution : 'MULTI_GGX'
 - subsurface_method : 'RANDOM_WALK'
 - node_label : None
 - node_color : None

Node initialization
 - base_color : base_color
 - metallic : metallic
 - roughness : roughness
 - ior : ior
 - alpha : alpha
 - normal : normal
 - subsurface_weight : subsurface_weight
 - subsurface_radius : subsurface_radius
 - subsurface_scale : subsurface_scale
 - subsurface_anisotropy : subsurface_anisotropy
 - specular_ior_level : specular_ior_level
 - specular_tint : specular_tint
 - anisotropic : anisotropic
 - anisotropic_rotation : anisotropic_rotation
 - tangent : tangent
 - transmission_weight : transmission_weight
 - coat_weight : coat_weight
 - coat_roughness : coat_roughness
 - coat_ior : coat_ior
 - coat_tint : coat_tint
 - coat_normal : coat_normal
 - sheen_weight : sheen_weight
 - sheen_roughness : sheen_roughness
 - sheen_tint : sheen_tint
 - emission_color : emission_color
 - emission_strength : emission_strength
 - subsurface_ior : subsurface_ior
 - distribution : distribution
 - subsurface_method : subsurface_method
 - node_label : node_label
 - node_color : node_color

## principled_hair_bsdf

> PrincipledHairBSDF, return single output socket

``` python
def principled_hair_bsdf(color=None, roughness=None, radial_roughness=None, coat=None, ior=None, offset=None, random_roughness=None, random=None, aspect_ratio=None, reflection=None, transmission=None, secondary_reflection=None,
absorption_coefficient=None, melanin=None, melanin_redness=None, tint=None, random_color=None, model='CHIANG', parametrization='COLOR', node_label=None, node_color=None):
```
Node
 - class_name : [PrincipledHairBSDF](/docs/Shader_classes/PrincipledHairBSDF.md)
 - bl_idname : ShaderNodeBsdfHairPrincipled

Arguments
 - color : None
 - roughness : None
 - radial_roughness : None
 - coat : None
 - ior : None
 - offset : None
 - random_roughness : None
 - random : None
 - aspect_ratio : None
 - reflection : None
 - transmission : None
 - secondary_reflection : None
 - absorption_coefficient : None
 - melanin : None
 - melanin_redness : None
 - tint : None
 - random_color : None
 - model : 'CHIANG'
 - parametrization : 'COLOR'
 - node_label : None
 - node_color : None

Node initialization
 - color : color
 - roughness : roughness
 - radial_roughness : radial_roughness
 - coat : coat
 - ior : ior
 - offset : offset
 - random_roughness : random_roughness
 - random : random
 - aspect_ratio : aspect_ratio
 - reflection : reflection
 - transmission : transmission
 - secondary_reflection : secondary_reflection
 - absorption_coefficient : absorption_coefficient
 - melanin : melanin
 - melanin_redness : melanin_redness
 - tint : tint
 - random_color : random_color
 - model : model
 - parametrization : parametrization
 - node_label : node_label
 - node_color : node_color

## principled_volume

> PrincipledVolume, return single output socket

``` python
def principled_volume(color=None, color_attribute=None, density=None, density_attribute=None, anisotropy=None, absorption_color=None, emission_strength=None, emission_color=None, blackbody_intensity=None, blackbody_tint=None, temperature=None,
temperature_attribute=None, node_label=None, node_color=None):
```
Node
 - class_name : [PrincipledVolume](/docs/Shader_classes/PrincipledVolume.md)
 - bl_idname : ShaderNodeVolumePrincipled

Arguments
 - color : None
 - color_attribute : None
 - density : None
 - density_attribute : None
 - anisotropy : None
 - absorption_color : None
 - emission_strength : None
 - emission_color : None
 - blackbody_intensity : None
 - blackbody_tint : None
 - temperature : None
 - temperature_attribute : None
 - node_label : None
 - node_color : None

Node initialization
 - color : color
 - color_attribute : color_attribute
 - density : density
 - density_attribute : density_attribute
 - anisotropy : anisotropy
 - absorption_color : absorption_color
 - emission_strength : emission_strength
 - emission_color : emission_color
 - blackbody_intensity : blackbody_intensity
 - blackbody_tint : blackbody_tint
 - temperature : temperature
 - temperature_attribute : temperature_attribute
 - node_label : node_label
 - node_color : node_color

## radians

> Math, value=self, operation='RADIANS'

``` python
def radians(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'RADIANS'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## refraction_bsdf

> RefractionBSDF, return single output socket

``` python
def refraction_bsdf(color=None, roughness=None, ior=None, normal=None, distribution='BECKMANN', node_label=None, node_color=None):
```
Node
 - class_name : [RefractionBSDF](/docs/Shader_classes/RefractionBSDF.md)
 - bl_idname : ShaderNodeBsdfRefraction

Arguments
 - color : None
 - roughness : None
 - ior : None
 - normal : None
 - distribution : 'BECKMANN'
 - node_label : None
 - node_color : None

Node initialization
 - color : color
 - roughness : roughness
 - ior : ior
 - normal : normal
 - distribution : distribution
 - node_label : node_label
 - node_color : node_color

## reroute

> Reroute, return single output socket

``` python
def reroute(input=None, node_label=None, node_color=None):
```
Node
 - class_name : [Reroute](/docs/Shader_classes/Reroute.md)
 - bl_idname : NodeReroute

Arguments
 - input : None
 - node_label : None
 - node_color : None

Node initialization
 - input : input
 - node_label : node_label
 - node_color : node_color

## rgb

> RGB, return socket

``` python
def rgb(node_label=None, node_color=None):
```
Node
 - class_name : [RGB](/docs/Shader_classes/RGB.md)
 - bl_idname : ShaderNodeRGB

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## rgb_curves

> RGBCurves, return single output socket

``` python
def rgb_curves(fac=None, color=None, mapping=None, node_label=None, node_color=None):
```
Node
 - class_name : [RGBCurves](/docs/Shader_classes/RGBCurves.md)
 - bl_idname : ShaderNodeRGBCurve

Arguments
 - fac : None
 - color : None
 - mapping
 - node_label : None
 - node_color : None

Node initialization
 - fac : fac
 - color : color
 - mapping : mapping
 - node_label : node_label
 - node_color : node_color

## rgb_to_bw

> RGBToBW, return single output socket

``` python
def rgb_to_bw(color=None, node_label=None, node_color=None):
```
Node
 - class_name : [RGBToBW](/docs/Shader_classes/RGBToBW.md)
 - bl_idname : ShaderNodeRGBToBW

Arguments
 - color : None
 - node_label : None
 - node_color : None

Node initialization
 - color : color
 - node_label : node_label
 - node_color : node_color

## round

> Math, value=self, operation='ROUND'

``` python
def round(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'ROUND'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## script

> Script, return node

``` python
def script(bytecode='', bytecode_hash='', filepath='', mode='INTERNAL', script=None, use_auto_update=False, node_label=None, node_color=None):
```
Node
 - class_name : [Script](/docs/Shader_classes/Script.md)
 - bl_idname : ShaderNodeScript

Arguments
 - bytecode : ''
 - bytecode_hash : ''
 - filepath : ''
 - mode : 'INTERNAL'
 - script : None
 - use_auto_update : False
 - node_label : None
 - node_color : None

Node initialization
 - bytecode : bytecode
 - bytecode_hash : bytecode_hash
 - filepath : filepath
 - mode : mode
 - script : script
 - use_auto_update : use_auto_update
 - node_label : node_label
 - node_color : node_color

## sheen_bsdf

> SheenBSDF, return single output socket

``` python
def sheen_bsdf(color=None, roughness=None, normal=None, distribution='MICROFIBER', node_label=None, node_color=None):
```
Node
 - class_name : [SheenBSDF](/docs/Shader_classes/SheenBSDF.md)
 - bl_idname : ShaderNodeBsdfSheen

Arguments
 - color : None
 - roughness : None
 - normal : None
 - distribution : 'MICROFIBER'
 - node_label : None
 - node_color : None

Node initialization
 - color : color
 - roughness : roughness
 - normal : normal
 - distribution : distribution
 - node_label : node_label
 - node_color : node_color

## sign

> Math, value=self, operation='SIGN'

``` python
def sign(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'SIGN'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## sin

> Math, value=self, operation='SINE'

``` python
def sin(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'SINE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## sinh

> Math, value=self, operation='SINH'

``` python
def sinh(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'SINH'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## sky_texture

> SkyTexture, return single output socket

``` python
def sky_texture(vector=None, air_density=1.0, altitude=0.0, color_mapping=None, dust_density=1.0, ground_albedo=0.30000001192092896, ozone_density=1.0, sky_type='NISHITA', sun_direction=(0.0, 0.0, 1.0), sun_disc=True,
sun_elevation=0.2617993950843811, sun_intensity=1.0, sun_rotation=0.0, sun_size=0.009512044489383698, texture_mapping=None, turbidity=2.200000047683716, node_label=None, node_color=None):
```
Node
 - class_name : [SkyTexture](/docs/Shader_classes/SkyTexture.md)
 - bl_idname : ShaderNodeTexSky

Arguments
 - vector : None
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
 - vector : vector
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

## smooth_max

> Math, value=self, operation='SMOOTH_MAX'

``` python
def smooth_max(value=None, value_1=None, value_2=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - value_2 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - value_2 : value_2
 - operation : 'SMOOTH_MAX'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## smooth_min

> Math, value=self, operation='SMOOTH_MIN'

``` python
def smooth_min(value=None, value_1=None, value_2=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - value_2 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - value_2 : value_2
 - operation : 'SMOOTH_MIN'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## snap

> Math, value=self, operation='SNAP'

``` python
def snap(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'SNAP'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## specular_bsdf

> SpecularBSDF, return single output socket

``` python
def specular_bsdf(base_color=None, specular=None, roughness=None, emissive_color=None, transparency=None, normal=None, clear_coat=None, clear_coat_roughness=None, clear_coat_normal=None, ambient_occlusion=None, node_label=None, node_color=None):
```
Node
 - class_name : [SpecularBSDF](/docs/Shader_classes/SpecularBSDF.md)
 - bl_idname : ShaderNodeEeveeSpecular

Arguments
 - base_color : None
 - specular : None
 - roughness : None
 - emissive_color : None
 - transparency : None
 - normal : None
 - clear_coat : None
 - clear_coat_roughness : None
 - clear_coat_normal : None
 - ambient_occlusion : None
 - node_label : None
 - node_color : None

Node initialization
 - base_color : base_color
 - specular : specular
 - roughness : roughness
 - emissive_color : emissive_color
 - transparency : transparency
 - normal : normal
 - clear_coat : clear_coat
 - clear_coat_roughness : clear_coat_roughness
 - clear_coat_normal : clear_coat_normal
 - ambient_occlusion : ambient_occlusion
 - node_label : node_label
 - node_color : node_color

## sqrt

> Math, value=self, operation='SQRT'

``` python
def sqrt(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'SQRT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## subsurface_scattering

> SubsurfaceScattering, return single output socket

``` python
def subsurface_scattering(color=None, scale=None, radius=None, ior=None, anisotropy=None, normal=None, falloff='RANDOM_WALK', node_label=None, node_color=None):
```
Node
 - class_name : [SubsurfaceScattering](/docs/Shader_classes/SubsurfaceScattering.md)
 - bl_idname : ShaderNodeSubsurfaceScattering

Arguments
 - color : None
 - scale : None
 - radius : None
 - ior : None
 - anisotropy : None
 - normal : None
 - falloff : 'RANDOM_WALK'
 - node_label : None
 - node_color : None

Node initialization
 - color : color
 - scale : scale
 - radius : radius
 - ior : ior
 - anisotropy : anisotropy
 - normal : normal
 - falloff : falloff
 - node_label : node_label
 - node_color : node_color

## subtract

> Math, value=self, operation='SUBTRACT'

``` python
def subtract(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'SUBTRACT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## tan

> Math, value=self, operation='TANGENT'

``` python
def tan(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'TANGENT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## tangent

> Tangent, return socket

``` python
def tangent(axis='Z', direction_type='RADIAL', uv_map='', node_label=None, node_color=None):
```
Node
 - class_name : [Tangent](/docs/Shader_classes/Tangent.md)
 - bl_idname : ShaderNodeTangent

Arguments
 - axis : 'Z'
 - direction_type : 'RADIAL'
 - uv_map : ''
 - node_label : None
 - node_color : None

Node initialization
 - axis : axis
 - direction_type : direction_type
 - uv_map : uv_map
 - node_label : node_label
 - node_color : node_color

## tanh

> Math, value=self, operation='TANH'

``` python
def tanh(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'TANH'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## texture_coordinate

> TextureCoordinate, return node

``` python
def texture_coordinate(from_instancer=False, object=None, node_label=None, node_color=None):
```
Node
 - class_name : [TextureCoordinate](/docs/Shader_classes/TextureCoordinate.md)
 - bl_idname : ShaderNodeTexCoord

Arguments
 - from_instancer : False
 - object : None
 - node_label : None
 - node_color : None

Node initialization
 - from_instancer : from_instancer
 - object : object
 - node_label : node_label
 - node_color : node_color

## toon_bsdf

> ToonBSDF, return single output socket

``` python
def toon_bsdf(color=None, size=None, smooth=None, normal=None, component='DIFFUSE', node_label=None, node_color=None):
```
Node
 - class_name : [ToonBSDF](/docs/Shader_classes/ToonBSDF.md)
 - bl_idname : ShaderNodeBsdfToon

Arguments
 - color : None
 - size : None
 - smooth : None
 - normal : None
 - component : 'DIFFUSE'
 - node_label : None
 - node_color : None

Node initialization
 - color : color
 - size : size
 - smooth : smooth
 - normal : normal
 - component : component
 - node_label : node_label
 - node_color : node_color

## translucent_bsdf

> TranslucentBSDF, return single output socket

``` python
def translucent_bsdf(color=None, normal=None, node_label=None, node_color=None):
```
Node
 - class_name : [TranslucentBSDF](/docs/Shader_classes/TranslucentBSDF.md)
 - bl_idname : ShaderNodeBsdfTranslucent

Arguments
 - color : None
 - normal : None
 - node_label : None
 - node_color : None

Node initialization
 - color : color
 - normal : normal
 - node_label : node_label
 - node_color : node_color

## transparent_bsdf

> TransparentBSDF, return single output socket

``` python
def transparent_bsdf(color=None, node_label=None, node_color=None):
```
Node
 - class_name : [TransparentBSDF](/docs/Shader_classes/TransparentBSDF.md)
 - bl_idname : ShaderNodeBsdfTransparent

Arguments
 - color : None
 - node_label : None
 - node_color : None

Node initialization
 - color : color
 - node_label : node_label
 - node_color : node_color

## trunc

> Math, value=self, operation='TRUNC'

``` python
def trunc(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'TRUNC'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## uv_along_stroke

> UVAlongStroke, return socket

``` python
def uv_along_stroke(use_tips=False, node_label=None, node_color=None):
```
Node
 - class_name : [UVAlongStroke](/docs/Shader_classes/UVAlongStroke.md)
 - bl_idname : ShaderNodeUVAlongStroke

Arguments
 - use_tips : False
 - node_label : None
 - node_color : None

Node initialization
 - use_tips : use_tips
 - node_label : node_label
 - node_color : node_color

## uv_map

> UVMap, return socket

``` python
def uv_map(from_instancer=False, uv_map='', node_label=None, node_color=None):
```
Node
 - class_name : [UVMap](/docs/Shader_classes/UVMap.md)
 - bl_idname : ShaderNodeUVMap

Arguments
 - from_instancer : False
 - uv_map : ''
 - node_label : None
 - node_color : None

Node initialization
 - from_instancer : from_instancer
 - uv_map : uv_map
 - node_label : node_label
 - node_color : node_color

## value

> Value, return socket

``` python
def value(value, node_label=None, node_color=None):
```
Node
 - class_name : [Value](/docs/Shader_classes/Value.md)
 - bl_idname : ShaderNodeValue

## vector_curves

> VectorCurves, return single output socket

``` python
def vector_curves(fac=None, vector=None, mapping=None, node_label=None, node_color=None):
```
Node
 - class_name : [VectorCurves](/docs/Shader_classes/VectorCurves.md)
 - bl_idname : ShaderNodeVectorCurve

Arguments
 - fac : None
 - vector : None
 - mapping
 - node_label : None
 - node_color : None

Node initialization
 - fac : fac
 - vector : vector
 - mapping : mapping
 - node_label : node_label
 - node_color : node_color

## vector_displacement

> VectorDisplacement, return single output socket

``` python
def vector_displacement(vector=None, midlevel=None, scale=None, space='TANGENT', node_label=None, node_color=None):
```
Node
 - class_name : [VectorDisplacement](/docs/Shader_classes/VectorDisplacement.md)
 - bl_idname : ShaderNodeVectorDisplacement

Arguments
 - vector : None
 - midlevel : None
 - scale : None
 - space : 'TANGENT'
 - node_label : None
 - node_color : None

Node initialization
 - vector : vector
 - midlevel : midlevel
 - scale : scale
 - space : space
 - node_label : node_label
 - node_color : node_color

## vector_rotate

> VectorRotate, return single output socket

``` python
def vector_rotate(vector=None, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE', node_label=None, node_color=None):
```
Node
 - class_name : [VectorRotate](/docs/Shader_classes/VectorRotate.md)
 - bl_idname : ShaderNodeVectorRotate

Arguments
 - vector : None
 - center : None
 - axis : None
 - angle : None
 - rotation : None
 - invert : False
 - rotation_type : 'AXIS_ANGLE'
 - node_label : None
 - node_color : None

Node initialization
 - vector : vector
 - center : center
 - axis : axis
 - angle : angle
 - rotation : rotation
 - invert : invert
 - rotation_type : rotation_type
 - node_label : node_label
 - node_color : node_color

## vector_transform

> VectorTransform, return single output socket

``` python
def vector_transform(vector=None, convert_from='WORLD', convert_to='OBJECT', vector_type='VECTOR', node_label=None, node_color=None):
```
Node
 - class_name : [VectorTransform](/docs/Shader_classes/VectorTransform.md)
 - bl_idname : ShaderNodeVectorTransform

Arguments
 - vector : None
 - convert_from : 'WORLD'
 - convert_to : 'OBJECT'
 - vector_type : 'VECTOR'
 - node_label : None
 - node_color : None

Node initialization
 - vector : vector
 - convert_from : convert_from
 - convert_to : convert_to
 - vector_type : vector_type
 - node_label : node_label
 - node_color : node_color

## volume_absorption

> VolumeAbsorption, return single output socket

``` python
def volume_absorption(color=None, density=None, node_label=None, node_color=None):
```
Node
 - class_name : [VolumeAbsorption](/docs/Shader_classes/VolumeAbsorption.md)
 - bl_idname : ShaderNodeVolumeAbsorption

Arguments
 - color : None
 - density : None
 - node_label : None
 - node_color : None

Node initialization
 - color : color
 - density : density
 - node_label : node_label
 - node_color : node_color

## volume_info

> VolumeInfo, return node

``` python
def volume_info(node_label=None, node_color=None):
```
Node
 - class_name : [VolumeInfo](/docs/Shader_classes/VolumeInfo.md)
 - bl_idname : ShaderNodeVolumeInfo

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## volume_scatter

> VolumeScatter, return single output socket

``` python
def volume_scatter(color=None, density=None, anisotropy=None, node_label=None, node_color=None):
```
Node
 - class_name : [VolumeScatter](/docs/Shader_classes/VolumeScatter.md)
 - bl_idname : ShaderNodeVolumeScatter

Arguments
 - color : None
 - density : None
 - anisotropy : None
 - node_label : None
 - node_color : None

Node initialization
 - color : color
 - density : density
 - anisotropy : anisotropy
 - node_label : node_label
 - node_color : node_color

## wavelength

> Wavelength, return single output socket

``` python
def wavelength(wavelength=None, node_label=None, node_color=None):
```
Node
 - class_name : [Wavelength](/docs/Shader_classes/Wavelength.md)
 - bl_idname : ShaderNodeWavelength

Arguments
 - wavelength : None
 - node_label : None
 - node_color : None

Node initialization
 - wavelength : wavelength
 - node_label : node_label
 - node_color : node_color

## wireframe

> Wireframe, return single output socket

``` python
def wireframe(size=None, use_pixel_size=False, node_label=None, node_color=None):
```
Node
 - class_name : [Wireframe](/docs/Shader_classes/Wireframe.md)
 - bl_idname : ShaderNodeWireframe

Arguments
 - size : None
 - use_pixel_size : False
 - node_label : None
 - node_color : None

Node initialization
 - size : size
 - use_pixel_size : use_pixel_size
 - node_label : node_label
 - node_color : node_color

## wrap

> Math, value=self, operation='WRAP'

``` python
def wrap(value=None, value_1=None, value_2=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/Shader_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - value_2 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - value_2 : value_2
 - operation : 'WRAP'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color
