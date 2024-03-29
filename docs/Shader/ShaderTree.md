# Tree Shader (ShaderNodeTree)


### Socket classes

- [CUSTOM](/docs/Shader/socket_CUSTOM.md)
- [RGBA](/docs/Shader/socket_RGBA.md)
- [ROTATION](/docs/Shader/socket_ROTATION.md)
- [SHADER](/docs/Shader/socket_SHADER.md)
- [STRING](/docs/Shader/socket_STRING.md)
- [VALUE](/docs/Shader/socket_VALUE.md)
- [VECTOR](/docs/Shader/socket_VECTOR.md)

### Node classes

- A : [AddShader](/docs/Shader/AddShader.md) [AmbientOcclusion](/docs/Shader/AmbientOcclusion.md) [Attribute](/docs/Shader/Attribute.md)
- B : [Background](/docs/Shader/Background.md) [Bevel](/docs/Shader/Bevel.md) [Blackbody](/docs/Shader/Blackbody.md) [BrightnessContrast](/docs/Shader/BrightnessContrast.md) [Bump](/docs/Shader/Bump.md) [BrickTexture](/docs/Shader/BrickTexture.md)
- C : [CameraData](/docs/Shader/CameraData.md) [Clamp](/docs/Shader/Clamp.md) [CombineColor](/docs/Shader/CombineColor.md) [CombineXYZ](/docs/Shader/CombineXYZ.md) [CurvesInfo](/docs/Shader/CurvesInfo.md) [CheckerTexture](/docs/Shader/CheckerTexture.md) [ColorRamp](/docs/Shader/ColorRamp.md) [ColorAttribute](/docs/Shader/ColorAttribute.md)
- D : [DiffuseBSDF](/docs/Shader/DiffuseBSDF.md) [Displacement](/docs/Shader/Displacement.md)
- E : [Emission](/docs/Shader/Emission.md) [EnvironmentTexture](/docs/Shader/EnvironmentTexture.md)
- F : [Frame](/docs/Shader/Frame.md) [FloatCurve](/docs/Shader/FloatCurve.md) [Fresnel](/docs/Shader/Fresnel.md)
- G : [GroupInput](/docs/Shader/GroupInput.md) [GroupOutput](/docs/Shader/GroupOutput.md) [GlossyBSDF](/docs/Shader/GlossyBSDF.md) [GlassBSDF](/docs/Shader/GlassBSDF.md) [Gamma](/docs/Shader/Gamma.md) [Group](/docs/Shader/Group.md) [Geometry](/docs/Shader/Geometry.md) [GradientTexture](/docs/Shader/GradientTexture.md)
- H : [HairBSDF](/docs/Shader/HairBSDF.md) [Holdout](/docs/Shader/Holdout.md) [HueSaturationValue](/docs/Shader/HueSaturationValue.md)
- I : [InvertColor](/docs/Shader/InvertColor.md) [IESTexture](/docs/Shader/IESTexture.md) [ImageTexture](/docs/Shader/ImageTexture.md)
- L : [LayerWeight](/docs/Shader/LayerWeight.md) [LightFalloff](/docs/Shader/LightFalloff.md) [LightPath](/docs/Shader/LightPath.md) [LightOutput](/docs/Shader/LightOutput.md) [LineStyleOutput](/docs/Shader/LineStyleOutput.md)
- M : [MapRange](/docs/Shader/MapRange.md) [Mapping](/docs/Shader/Mapping.md) [Math](/docs/Shader/Math.md) [Mix](/docs/Shader/Mix.md) [MixShader](/docs/Shader/MixShader.md) [MaterialOutput](/docs/Shader/MaterialOutput.md) [MagicTexture](/docs/Shader/MagicTexture.md)
- N : [Normal](/docs/Shader/Normal.md) [NormalMap](/docs/Shader/NormalMap.md) [NoiseTexture](/docs/Shader/NoiseTexture.md)
- O : [ObjectInfo](/docs/Shader/ObjectInfo.md)
- P : [PrincipledHairBSDF](/docs/Shader/PrincipledHairBSDF.md) [PrincipledBSDF](/docs/Shader/PrincipledBSDF.md) [ParticleInfo](/docs/Shader/ParticleInfo.md) [PointInfo](/docs/Shader/PointInfo.md) [PointDensity](/docs/Shader/PointDensity.md) [PrincipledVolume](/docs/Shader/PrincipledVolume.md)
- R : [RenderLayers](/docs/Shader/RenderLayers.md) [Reroute](/docs/Shader/Reroute.md) [RefractionBSDF](/docs/Shader/RefractionBSDF.md) [RGB](/docs/Shader/RGB.md) [RGBCurves](/docs/Shader/RGBCurves.md) [RGBToBW](/docs/Shader/RGBToBW.md)
- S : [SheenBSDF](/docs/Shader/SheenBSDF.md) [SpecularBSDF](/docs/Shader/SpecularBSDF.md) [Shadernodeoutputaov](/docs/Shader/Shadernodeoutputaov.md) [Script](/docs/Shader/Script.md) [SeparateColor](/docs/Shader/SeparateColor.md) [SeparateXYZ](/docs/Shader/SeparateXYZ.md) [ShaderToRGB](/docs/Shader/ShaderToRGB.md) [SubsurfaceScattering](/docs/Shader/SubsurfaceScattering.md) [SkyTexture](/docs/Shader/SkyTexture.md)
- T : [ToonBSDF](/docs/Shader/ToonBSDF.md) [TranslucentBSDF](/docs/Shader/TranslucentBSDF.md) [TransparentBSDF](/docs/Shader/TransparentBSDF.md) [Tangent](/docs/Shader/Tangent.md) [TextureCoordinate](/docs/Shader/TextureCoordinate.md)
- U : [UVAlongStroke](/docs/Shader/UVAlongStroke.md) [UVMap](/docs/Shader/UVMap.md)
- V : [VoronoiTexture](/docs/Shader/VoronoiTexture.md) [Value](/docs/Shader/Value.md) [VectorCurves](/docs/Shader/VectorCurves.md) [VectorDisplacement](/docs/Shader/VectorDisplacement.md) [VectorMath](/docs/Shader/VectorMath.md) [VectorRotate](/docs/Shader/VectorRotate.md) [VectorTransform](/docs/Shader/VectorTransform.md) [VolumeAbsorption](/docs/Shader/VolumeAbsorption.md) [VolumeInfo](/docs/Shader/VolumeInfo.md) [VolumeScatter](/docs/Shader/VolumeScatter.md)
- W : [WorldOutput](/docs/Shader/WorldOutput.md) [WaveTexture](/docs/Shader/WaveTexture.md) [WhiteNoiseTexture](/docs/Shader/WhiteNoiseTexture.md) [Wavelength](/docs/Shader/Wavelength.md) [Wireframe](/docs/Shader/Wireframe.md)

### Functions

- A : [add](#add) [abs](#abs) [arcsin](#arcsin) [arccos](#arccos) [arctan](#arctan) [arctan2](#arctan2)
- B : [brick_texture](#brick_texture)
- C : [combine_color](#combine_color) [combine_xyz](#combine_xyz) [compare](#compare) [ceil](#ceil) [cos](#cos) [cosh](#cosh) [checker_texture](#checker_texture)
- D : [divide](#divide) [degrees](#degrees)
- E : [exp](#exp)
- F : [floor](#floor) [fract](#fract) [floored_modulo](#floored_modulo)
- G : [greater_than](#greater_than) [gradient_texture](#gradient_texture)
- H : [hsv](#hsv) [hsl](#hsl)
- I : [inverse_sqrt](#inverse_sqrt)
- L : [log](#log) [less_than](#less_than)
- M : [multiply](#multiply) [multiply_add](#multiply_add) [min](#min) [max](#max) [mod](#mod) [magic_texture](#magic_texture)
- N : [noise_texture](#noise_texture)
- P : [power](#power) [pingpong](#pingpong)
- R : [rgb](#rgb) [round](#round) [radians](#radians)
- S : [subtract](#subtract) [sqrt](#sqrt) [sign](#sign) [smooth_min](#smooth_min) [smooth_max](#smooth_max) [snap](#snap) [sin](#sin) [sinh](#sinh)
- T : [trunc](#trunc) [tan](#tan) [tanh](#tanh)
- V : [voronoi_texture](#voronoi_texture) [vadd](#vadd) [vsubtract](#vsubtract) [vmultiply](#vmultiply) [vdivide](#vdivide) [vmultiply_add](#vmultiply_add) [vcross](#vcross) [vproject](#vproject) [vreflect](#vreflect) [vrefract](#vrefract) [vfaceforward](#vfaceforward) [vdot](#vdot) [vdistance](#vdistance) [vlength](#vlength) [vscale](#vscale) [vnormalize](#vnormalize) [vabs](#vabs) [vmin](#vmin) [vmax](#vmax) [vfloor](#vfloor) [vceil](#vceil) [vfrac](#vfrac) [vmod](#vmod) [vwrap](#vwrap) [vsnap](#vsnap) [vsin](#vsin) [vcos](#vcos) [vtan](#vtan)
- W : [wrap](#wrap) [wave_texture](#wave_texture) [white_noise_texture](#white_noise_texture)
- X : [xyz](#xyz)

## Functions

### abs


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def abs(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='ABSOLUTE', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### add


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def add(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='ADD', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### arccos


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def arccos(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='ARCCOSINE', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### arcsin


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def arcsin(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='ARCSINE', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### arctan


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def arctan(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='ARCTANGENT', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### arctan2


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def arctan2(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='ARCTAN2', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### brick_texture


- node : [BrickTexture](/docs/Shader/BrickTexture.md)
- return : color

##### Arguments

- vector : None
- color1 : None
- color2 : None
- mortar : None
- scale : None
- mortar_size : None
- mortar_smooth : None
- bias : None
- brick_width : None
- row_height : None
- color_mapping : None
- offset : 0.5
- offset_frequency : 2
- squash : 1.0
- squash_frequency : 2
- texture_mapping : None
- node_label : None
- node_color : None

#### Source code

``` python
def brick_texture(self, vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, color_mapping=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2, texture_mapping=None, node_label=None, node_color=None, **kwargs):
    node = self.BrickTexture(vector=vector, color1=color1, color2=color2, mortar=mortar, scale=scale, mortar_size=mortar_size, mortar_smooth=mortar_smooth, bias=bias, brick_width=brick_width, row_height=row_height, color_mapping=color_mapping, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency, texture_mapping=texture_mapping, node_label=node_label, node_color=node_color, **kwargs)
    return node.color
```
### ceil


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def ceil(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='CEIL', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### checker_texture


- node : [CheckerTexture](/docs/Shader/CheckerTexture.md)
- return : curve

##### Arguments

- vector : None
- color1 : None
- color2 : None
- scale : None
- color_mapping : None
- texture_mapping : None
- node_label : None
- node_color : None

#### Source code

``` python
def checker_texture(self, vector=None, color1=None, color2=None, scale=None, color_mapping=None, texture_mapping=None, node_label=None, node_color=None, **kwargs):
    node = self.CheckerTexture(vector=vector, color1=color1, color2=color2, scale=scale, color_mapping=color_mapping, texture_mapping=texture_mapping, node_label=node_label, node_color=node_color, **kwargs)
    return node.curve
```
### combine_color


- node : [CombineColor](/docs/Shader/CombineColor.md)
- return : color

##### Arguments

- red : None
- green : None
- blue : None
- mode : 'RGB' in ('RGB', 'HSV', 'HSL')
- node_label : None
- node_color : None

#### Source code

``` python
def combine_color(self, red=None, green=None, blue=None, mode='RGB', node_label=None, node_color=None, **kwargs):
    node = self.CombineColor(red=red, green=green, blue=blue, mode=mode, node_label=node_label, node_color=node_color, **kwargs)
    return node.color
```
### combine_xyz


- node : [CombineXYZ](/docs/Shader/CombineXYZ.md)
- return : vector

##### Arguments

- x : None
- y : None
- z : None
- node_label : None
- node_color : None

#### Source code

``` python
def combine_xyz(self, x=None, y=None, z=None, node_label=None, node_color=None, **kwargs):
    node = self.CombineXYZ(x=x, y=y, z=z, node_label=node_label, node_color=node_color, **kwargs)
    return node.vector
```
### compare


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- value_2 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def compare(self, value=None, value_1=None, value_2=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, value_2=value_2, operation='COMPARE', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### cos


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def cos(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='COSINE', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### cosh


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def cosh(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='COSH', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### degrees


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def degrees(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='DEGREES', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### divide


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def divide(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='DIVIDE', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### exp


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def exp(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='EXPONENT', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### floor


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def floor(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='FLOOR', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### floored_modulo


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def floored_modulo(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='FLOORED_MODULO', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### fract


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def fract(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='FRACT', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### gradient_texture


- node : [GradientTexture](/docs/Shader/GradientTexture.md)
- return : color

##### Arguments

- vector : None
- color_mapping : None
- gradient_type : 'LINEAR' in ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL')
- texture_mapping : None
- node_label : None
- node_color : None

#### Source code

``` python
def gradient_texture(self, vector=None, color_mapping=None, gradient_type='LINEAR', texture_mapping=None, node_label=None, node_color=None, **kwargs):
    node = self.GradientTexture(vector=vector, color_mapping=color_mapping, gradient_type=gradient_type, texture_mapping=texture_mapping, node_label=node_label, node_color=node_color, **kwargs)
    return node.color
```
### greater_than


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def greater_than(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='GREATER_THAN', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### hsl


- node : [CombineColor](/docs/Shader/CombineColor.md)
- return : color

##### Arguments

- red : None
- green : None
- blue : None
- node_label : None
- node_color : None

#### Source code

``` python
def hsl(self, red=None, green=None, blue=None, node_label=None, node_color=None, **kwargs):
    node = self.CombineColor(red=red, green=green, blue=blue, mode='HSL', node_label=node_label, node_color=node_color, **kwargs)
    return node.color
```
### hsv


- node : [CombineColor](/docs/Shader/CombineColor.md)
- return : color

##### Arguments

- red : None
- green : None
- blue : None
- node_label : None
- node_color : None

#### Source code

``` python
def hsv(self, red=None, green=None, blue=None, node_label=None, node_color=None, **kwargs):
    node = self.CombineColor(red=red, green=green, blue=blue, mode='HSV', node_label=node_label, node_color=node_color, **kwargs)
    return node.color
```
### inverse_sqrt


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def inverse_sqrt(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='INVERSE_SQRT', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### less_than


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def less_than(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='LESS_THAN', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### log


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def log(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='LOGARITHM', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### magic_texture


- node : [MagicTexture](/docs/Shader/MagicTexture.md)
- return : color

##### Arguments

- vector : None
- scale : None
- distortion : None
- color_mapping : None
- texture_mapping : None
- turbulence_depth : 2
- node_label : None
- node_color : None

#### Source code

``` python
def magic_texture(self, vector=None, scale=None, distortion=None, color_mapping=None, texture_mapping=None, turbulence_depth=2, node_label=None, node_color=None, **kwargs):
    node = self.MagicTexture(vector=vector, scale=scale, distortion=distortion, color_mapping=color_mapping, texture_mapping=texture_mapping, turbulence_depth=turbulence_depth, node_label=node_label, node_color=node_color, **kwargs)
    return node.color
```
### max


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def max(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='MAXIMUM', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### min


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def min(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='MINIMUM', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### mod


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def mod(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='MODULO', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### multiply


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def multiply(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='MULTIPLY', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### multiply_add


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- value_2 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def multiply_add(self, value=None, value_1=None, value_2=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, value_2=value_2, operation='MULTIPLY_ADD', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### noise_texture


- node : [NoiseTexture](/docs/Shader/NoiseTexture.md)
- return : fac

##### Arguments

- vector : None
- scale : None
- detail : None
- roughness : None
- lacunarity : None
- distortion : None
- w : None
- offset : None
- gain : None
- color_mapping : None
- noise_dimensions : '3D' in ('1D', '2D', '3D', '4D')
- noise_type : 'FBM' in ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN')
- normalize : True
- texture_mapping : None
- node_label : None
- node_color : None

#### Source code

``` python
def noise_texture(self, vector=None, scale=None, detail=None, roughness=None, lacunarity=None, distortion=None, w=None, offset=None, gain=None, color_mapping=None, noise_dimensions='3D', noise_type='FBM', normalize=True, texture_mapping=None, node_label=None, node_color=None, **kwargs):
    node = self.NoiseTexture(vector=vector, scale=scale, detail=detail, roughness=roughness, lacunarity=lacunarity, distortion=distortion, w=w, offset=offset, gain=gain, color_mapping=color_mapping, noise_dimensions=noise_dimensions, noise_type=noise_type, normalize=normalize, texture_mapping=texture_mapping, node_label=node_label, node_color=node_color, **kwargs)
    return node.fac
```
### pingpong


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def pingpong(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='PINGPONG', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### power


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def power(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='POWER', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### radians


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def radians(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='RADIANS', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### rgb


- node : [CombineColor](/docs/Shader/CombineColor.md)
- return : color

##### Arguments

- red : None
- green : None
- blue : None
- node_label : None
- node_color : None

#### Source code

``` python
def rgb(self, red=None, green=None, blue=None, node_label=None, node_color=None, **kwargs):
    node = self.CombineColor(red=red, green=green, blue=blue, mode='RGB', node_label=node_label, node_color=node_color, **kwargs)
    return node.color
```
### round


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def round(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='ROUND', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sign


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def sign(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='SIGN', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sin


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def sin(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='SINE', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sinh


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def sinh(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='SINH', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### smooth_max


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- value_2 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def smooth_max(self, value=None, value_1=None, value_2=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, value_2=value_2, operation='SMOOTH_MAX', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### smooth_min


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- value_2 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def smooth_min(self, value=None, value_1=None, value_2=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, value_2=value_2, operation='SMOOTH_MIN', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### snap


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def snap(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='SNAP', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sqrt


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def sqrt(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='SQRT', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### subtract


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def subtract(self, value=None, value_1=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='SUBTRACT', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### tan


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def tan(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='TANGENT', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### tanh


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def tanh(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='TANH', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### trunc


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def trunc(self, value=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='TRUNC', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### vabs


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def vabs(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, operation='ABSOLUTE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vadd


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- node_label : None
- node_color : None

#### Source code

``` python
def vadd(self, vector=None, vector_1=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, vector_1=vector_1, operation='ADD', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vceil


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def vceil(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, operation='CEIL', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vcos


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def vcos(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, operation='COSINE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vcross


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- node_label : None
- node_color : None

#### Source code

``` python
def vcross(self, vector=None, vector_1=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, vector_1=vector_1, operation='CROSS_PRODUCT', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vdistance


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- node_label : None
- node_color : None

#### Source code

``` python
def vdistance(self, vector=None, vector_1=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, vector_1=vector_1, operation='DISTANCE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vdivide


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- node_label : None
- node_color : None

#### Source code

``` python
def vdivide(self, vector=None, vector_1=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, vector_1=vector_1, operation='DIVIDE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vdot


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- node_label : None
- node_color : None

#### Source code

``` python
def vdot(self, vector=None, vector_1=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, vector_1=vector_1, operation='DOT_PRODUCT', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vfaceforward


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- vector_2 : None
- node_label : None
- node_color : None

#### Source code

``` python
def vfaceforward(self, vector=None, vector_1=None, vector_2=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, vector_1=vector_1, vector_2=vector_2, operation='FACEFORWARD', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vfloor


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def vfloor(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, operation='FLOOR', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vfrac


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def vfrac(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, operation='FRACTION', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vlength


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def vlength(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, operation='LENGTH', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vmax


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- node_label : None
- node_color : None

#### Source code

``` python
def vmax(self, vector=None, vector_1=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, vector_1=vector_1, operation='MAXIMUM', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vmin


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- node_label : None
- node_color : None

#### Source code

``` python
def vmin(self, vector=None, vector_1=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, vector_1=vector_1, operation='MINIMUM', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vmod


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- node_label : None
- node_color : None

#### Source code

``` python
def vmod(self, vector=None, vector_1=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, vector_1=vector_1, operation='MODULO', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vmultiply


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- node_label : None
- node_color : None

#### Source code

``` python
def vmultiply(self, vector=None, vector_1=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, vector_1=vector_1, operation='MULTIPLY', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vmultiply_add


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- vector_2 : None
- node_label : None
- node_color : None

#### Source code

``` python
def vmultiply_add(self, vector=None, vector_1=None, vector_2=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, vector_1=vector_1, vector_2=vector_2, operation='MULTIPLY_ADD', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vnormalize


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def vnormalize(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, operation='NORMALIZE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### voronoi_texture


- node : [VoronoiTexture](/docs/Shader/VoronoiTexture.md)
- return : distance

##### Arguments

- vector : None
- scale : None
- detail : None
- roughness : None
- lacunarity : None
- randomness : None
- exponent : None
- smoothness : None
- w : None
- color_mapping : None
- distance : 'EUCLIDEAN' in ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI')
- feature : 'F1' in ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS')
- normalize : False
- texture_mapping : None
- voronoi_dimensions : '3D' in ('1D', '2D', '3D', '4D')
- node_label : None
- node_color : None

#### Source code

``` python
def voronoi_texture(self, vector=None, scale=None, detail=None, roughness=None, lacunarity=None, randomness=None, exponent=None, smoothness=None, w=None, color_mapping=None, distance='EUCLIDEAN', feature='F1', normalize=False, texture_mapping=None, voronoi_dimensions='3D', node_label=None, node_color=None, **kwargs):
    node = self.VoronoiTexture(vector=vector, scale=scale, detail=detail, roughness=roughness, lacunarity=lacunarity, randomness=randomness, exponent=exponent, smoothness=smoothness, w=w, color_mapping=color_mapping, distance=distance, feature=feature, normalize=normalize, texture_mapping=texture_mapping, voronoi_dimensions=voronoi_dimensions, node_label=node_label, node_color=node_color, **kwargs)
    return node.distance
```
### vproject


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- node_label : None
- node_color : None

#### Source code

``` python
def vproject(self, vector=None, vector_1=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, vector_1=vector_1, operation='PROJECT', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vreflect


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- node_label : None
- node_color : None

#### Source code

``` python
def vreflect(self, vector=None, vector_1=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, vector_1=vector_1, operation='REFLECT', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vrefract


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- scale : None
- node_label : None
- node_color : None

#### Source code

``` python
def vrefract(self, vector=None, vector_1=None, scale=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, vector_1=vector_1, scale=scale, operation='REFRACT', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vscale


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- scale : None
- node_label : None
- node_color : None

#### Source code

``` python
def vscale(self, vector=None, scale=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, scale=scale, operation='SCALE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vsin


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def vsin(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, operation='SINE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vsnap


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- node_label : None
- node_color : None

#### Source code

``` python
def vsnap(self, vector=None, vector_1=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, vector_1=vector_1, operation='SNAP', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vsubtract


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- node_label : None
- node_color : None

#### Source code

``` python
def vsubtract(self, vector=None, vector_1=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, vector_1=vector_1, operation='SUBTRACT', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vtan


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def vtan(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, operation='TANGENT', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vwrap


- node : [VectorMath](/docs/Shader/VectorMath.md)
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- vector_2 : None
- node_label : None
- node_color : None

#### Source code

``` python
def vwrap(self, vector=None, vector_1=None, vector_2=None, node_label=None, node_color=None, **kwargs):
    node = self.VectorMath(vector=vector, vector_1=vector_1, vector_2=vector_2, operation='WRAP', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### wave_texture


- node : [WaveTexture](/docs/Shader/WaveTexture.md)
- return : curve

##### Arguments

- vector : None
- scale : None
- distortion : None
- detail : None
- detail_scale : None
- detail_roughness : None
- phase_offset : None
- bands_direction : 'X' in ('X', 'Y', 'Z', 'DIAGONAL')
- color_mapping : None
- rings_direction : 'X' in ('X', 'Y', 'Z', 'SPHERICAL')
- texture_mapping : None
- wave_profile : 'SIN' in ('SIN', 'SAW', 'TRI')
- wave_type : 'BANDS' in ('BANDS', 'RINGS')
- node_label : None
- node_color : None

#### Source code

``` python
def wave_texture(self, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', color_mapping=None, rings_direction='X', texture_mapping=None, wave_profile='SIN', wave_type='BANDS', node_label=None, node_color=None, **kwargs):
    node = self.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=bands_direction, color_mapping=color_mapping, rings_direction=rings_direction, texture_mapping=texture_mapping, wave_profile=wave_profile, wave_type=wave_type, node_label=node_label, node_color=node_color, **kwargs)
    return node.curve
```
### white_noise_texture


- node : [WhiteNoiseTexture](/docs/Shader/WhiteNoiseTexture.md)
- return : value

##### Arguments

- vector : None
- w : None
- noise_dimensions : '3D' in ('1D', '2D', '3D', '4D')
- node_label : None
- node_color : None

#### Source code

``` python
def white_noise_texture(self, vector=None, w=None, noise_dimensions='3D', node_label=None, node_color=None, **kwargs):
    node = self.WhiteNoiseTexture(vector=vector, w=w, noise_dimensions=noise_dimensions, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### wrap


- node : [Math](/docs/Shader/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- value_2 : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def wrap(self, value=None, value_1=None, value_2=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, value_2=value_2, operation='WRAP', use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### xyz


- node : [CombineXYZ](/docs/Shader/CombineXYZ.md)
- return : vector

##### Arguments

- x : None
- y : None
- z : None
- node_label : None
- node_color : None

#### Source code

``` python
def xyz(self, x=None, y=None, z=None, node_label=None, node_color=None, **kwargs):
    node = self.CombineXYZ(x=x, y=y, z=z, node_label=node_label, node_color=node_color, **kwargs)
    return node.vector
```
