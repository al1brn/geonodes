# Tree Compositor (CompositorNodeTree)


### Socket classes

- [CUSTOM](/docs/Compositor/socket_CUSTOM.md)
- [RGBA](/docs/Compositor/socket_RGBA.md)
- [VALUE](/docs/Compositor/socket_VALUE.md)
- [VECTOR](/docs/Compositor/socket_VECTOR.md)

### Node classes

- A : [AlphaOver](/docs/Compositor/AlphaOver.md) [AntiAliasing](/docs/Compositor/AntiAliasing.md) [AlphaConvert](/docs/Compositor/AlphaConvert.md)
- B : [BilateralBlur](/docs/Compositor/BilateralBlur.md) [Blur](/docs/Compositor/Blur.md) [BokehBlur](/docs/Compositor/BokehBlur.md) [BokehImage](/docs/Compositor/BokehImage.md) [BoxMask](/docs/Compositor/BoxMask.md) [BrightnessContrast](/docs/Compositor/BrightnessContrast.md)
- C : [ChannelKey](/docs/Compositor/ChannelKey.md) [ChromaKey](/docs/Compositor/ChromaKey.md) [ColorBalance](/docs/Compositor/ColorBalance.md) [ColorCorrection](/docs/Compositor/ColorCorrection.md) [ColorKey](/docs/Compositor/ColorKey.md) [ColorSpill](/docs/Compositor/ColorSpill.md) [CombineColor](/docs/Compositor/CombineColor.md) [CombineXYZ](/docs/Compositor/CombineXYZ.md) [Composite](/docs/Compositor/Composite.md) [ConvertColorspace](/docs/Compositor/ConvertColorspace.md) [CornerPin](/docs/Compositor/CornerPin.md) [Crop](/docs/Compositor/Crop.md) [ColorRamp](/docs/Compositor/ColorRamp.md)
- D : [DirectionalBlur](/docs/Compositor/DirectionalBlur.md) [Defocus](/docs/Compositor/Defocus.md) [Denoise](/docs/Compositor/Denoise.md) [Despeckle](/docs/Compositor/Despeckle.md) [DifferenceKey](/docs/Compositor/DifferenceKey.md) [DilateErode](/docs/Compositor/DilateErode.md) [Displace](/docs/Compositor/Displace.md) [DistanceKey](/docs/Compositor/DistanceKey.md) [DoubleEdgeMask](/docs/Compositor/DoubleEdgeMask.md)
- E : [EllipseMask](/docs/Compositor/EllipseMask.md) [Exposure](/docs/Compositor/Exposure.md)
- F : [Filter](/docs/Compositor/Filter.md) [Flip](/docs/Compositor/Flip.md) [FileOutput](/docs/Compositor/FileOutput.md) [Frame](/docs/Compositor/Frame.md)
- G : [Gamma](/docs/Compositor/Gamma.md) [Glare](/docs/Compositor/Glare.md) [Group](/docs/Compositor/Group.md) [GroupInput](/docs/Compositor/GroupInput.md) [GroupOutput](/docs/Compositor/GroupOutput.md)
- H : [HueCorrect](/docs/Compositor/HueCorrect.md) [HueSaturationValue](/docs/Compositor/HueSaturationValue.md)
- I : [IDMask](/docs/Compositor/IDMask.md) [Image](/docs/Compositor/Image.md) [Inpaint](/docs/Compositor/Inpaint.md) [InvertColor](/docs/Compositor/InvertColor.md)
- K : [Keying](/docs/Compositor/Keying.md) [KeyingScreen](/docs/Compositor/KeyingScreen.md) [Kuwahara](/docs/Compositor/Kuwahara.md)
- L : [LensDistortion](/docs/Compositor/LensDistortion.md) [Levels](/docs/Compositor/Levels.md) [LuminanceKey](/docs/Compositor/LuminanceKey.md)
- M : [MapRange](/docs/Compositor/MapRange.md) [MapUV](/docs/Compositor/MapUV.md) [MapValue](/docs/Compositor/MapValue.md) [Mask](/docs/Compositor/Mask.md) [Math](/docs/Compositor/Math.md) [Mix](/docs/Compositor/Mix.md) [MovieClip](/docs/Compositor/MovieClip.md) [MovieDistortion](/docs/Compositor/MovieDistortion.md)
- N : [Normal](/docs/Compositor/Normal.md) [Normalize](/docs/Compositor/Normalize.md)
- P : [Pixelate](/docs/Compositor/Pixelate.md) [PlaneTrackDeform](/docs/Compositor/PlaneTrackDeform.md) [Posterize](/docs/Compositor/Posterize.md)
- R : [RGBCurves](/docs/Compositor/RGBCurves.md) [RGB](/docs/Compositor/RGB.md) [RGBToBW](/docs/Compositor/RGBToBW.md) [RenderLayers](/docs/Compositor/RenderLayers.md) [Rotate](/docs/Compositor/Rotate.md) [Reroute](/docs/Compositor/Reroute.md)
- S : [Scale](/docs/Compositor/Scale.md) [SceneTime](/docs/Compositor/SceneTime.md) [SeparateColor](/docs/Compositor/SeparateColor.md) [SeparateXYZ](/docs/Compositor/SeparateXYZ.md) [SetAlpha](/docs/Compositor/SetAlpha.md) [Split](/docs/Compositor/Split.md) [Stabilize2D](/docs/Compositor/Stabilize2D.md) [SunBeams](/docs/Compositor/SunBeams.md) [Switch](/docs/Compositor/Switch.md) [SwitchView](/docs/Compositor/SwitchView.md)
- T : [Texture](/docs/Compositor/Texture.md) [TimeCurve](/docs/Compositor/TimeCurve.md) [Tonemap](/docs/Compositor/Tonemap.md) [TrackPosition](/docs/Compositor/TrackPosition.md) [Transform](/docs/Compositor/Transform.md) [Translate](/docs/Compositor/Translate.md)
- V : [VectorCurves](/docs/Compositor/VectorCurves.md) [Value](/docs/Compositor/Value.md) [VectorBlur](/docs/Compositor/VectorBlur.md) [Viewer](/docs/Compositor/Viewer.md)
- Z : [ZCombine](/docs/Compositor/ZCombine.md)

### Functions

- A : [add](#add) [abs](#abs) [arcsin](#arcsin) [arccos](#arccos) [arctan](#arctan) [arctan2](#arctan2)
- C : [combine_color](#combine_color) [combine_xyz](#combine_xyz) [compare](#compare) [ceil](#ceil) [cos](#cos) [cosh](#cosh)
- D : [divide](#divide) [degrees](#degrees)
- E : [exp](#exp)
- F : [floor](#floor) [fract](#fract) [floored_modulo](#floored_modulo) [frame](#frame)
- G : [greater_than](#greater_than)
- H : [hsv](#hsv) [hsl](#hsl)
- I : [inverse_sqrt](#inverse_sqrt)
- L : [log](#log) [less_than](#less_than)
- M : [multiply](#multiply) [multiply_add](#multiply_add) [min](#min) [max](#max) [mod](#mod)
- P : [power](#power) [pingpong](#pingpong)
- R : [rgb](#rgb) [round](#round) [radians](#radians)
- S : [subtract](#subtract) [sqrt](#sqrt) [sign](#sign) [smooth_min](#smooth_min) [smooth_max](#smooth_max) [snap](#snap) [sin](#sin) [sinh](#sinh) [scene_time](#scene_time) [seconds](#seconds)
- T : [trunc](#trunc) [tan](#tan) [tanh](#tanh)
- W : [wrap](#wrap)
- X : [xyz](#xyz)
- Y : [ycc](#ycc) [yuv](#yuv)

## Functions

### abs


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def abs(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='ABSOLUTE', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### add


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def add(self, value=None, value_1=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='ADD', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### arccos


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def arccos(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='ARCCOSINE', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### arcsin


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def arcsin(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='ARCSINE', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### arctan


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def arctan(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='ARCTANGENT', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### arctan2


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def arctan2(self, value=None, value_1=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='ARCTAN2', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### ceil


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def ceil(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='CEIL', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### combine_color


- node : [CombineColor](/docs/Compositor/CombineColor.md)
- return : color

##### Arguments

- red : None
- green : None
- blue : None
- alpha : None
- mode : 'RGB' in ('RGB', 'HSV', 'HSL', 'YCC', 'YUV')
- tag_need_exec : None
- ycc_mode : 'ITUBT709' in ('ITUBT601', 'ITUBT709', 'JFIF')
- node_label : None
- node_color : None

#### Source code

``` python
def combine_color(self, red=None, green=None, blue=None, alpha=None, mode='RGB', tag_need_exec=None, ycc_mode='ITUBT709', node_label=None, node_color=None, **kwargs):
    node = self.CombineColor(red=red, green=green, blue=blue, alpha=alpha, mode=mode, tag_need_exec=tag_need_exec, ycc_mode=ycc_mode, node_label=node_label, node_color=node_color, **kwargs)
    return node.color
```
### combine_xyz


- node : [CombineXYZ](/docs/Compositor/CombineXYZ.md)
- return : vector

##### Arguments

- x : None
- y : None
- z : None
- tag_need_exec : None
- node_label : None
- node_color : None

#### Source code

``` python
def combine_xyz(self, x=None, y=None, z=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs):
    node = self.CombineXYZ(x=x, y=y, z=z, tag_need_exec=tag_need_exec, node_label=node_label, node_color=node_color, **kwargs)
    return node.vector
```
### compare


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- value_2 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def compare(self, value=None, value_1=None, value_2=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, value_2=value_2, operation='COMPARE', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### cos


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def cos(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='COSINE', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### cosh


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def cosh(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='COSH', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### degrees


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def degrees(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='DEGREES', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### divide


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def divide(self, value=None, value_1=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='DIVIDE', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### exp


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def exp(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='EXPONENT', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### floor


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def floor(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='FLOOR', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### floored_modulo


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def floored_modulo(self, value=None, value_1=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='FLOORED_MODULO', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### fract


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def fract(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='FRACT', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### frame


- node : [SceneTime](/docs/Compositor/SceneTime.md)
- return : frame

##### Arguments

- tag_need_exec : None
- node_label : None
- node_color : None

#### Source code

``` python
def frame(self, tag_need_exec=None, node_label=None, node_color=None, **kwargs):
    node = self.SceneTime(tag_need_exec=tag_need_exec, node_label=node_label, node_color=node_color, **kwargs)
    return node.frame
```
### greater_than


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def greater_than(self, value=None, value_1=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='GREATER_THAN', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### hsl


- node : [CombineColor](/docs/Compositor/CombineColor.md)
- return : color

##### Arguments

- red : None
- green : None
- blue : None
- alpha : None
- tag_need_exec : None
- ycc_mode : 'ITUBT709' in ('ITUBT601', 'ITUBT709', 'JFIF')
- node_label : None
- node_color : None

#### Source code

``` python
def hsl(self, red=None, green=None, blue=None, alpha=None, tag_need_exec=None, ycc_mode='ITUBT709', node_label=None, node_color=None, **kwargs):
    node = self.CombineColor(red=red, green=green, blue=blue, alpha=alpha, mode='HSL', tag_need_exec=tag_need_exec, ycc_mode=ycc_mode, node_label=node_label, node_color=node_color, **kwargs)
    return node.color
```
### hsv


- node : [CombineColor](/docs/Compositor/CombineColor.md)
- return : color

##### Arguments

- red : None
- green : None
- blue : None
- alpha : None
- tag_need_exec : None
- ycc_mode : 'ITUBT709' in ('ITUBT601', 'ITUBT709', 'JFIF')
- node_label : None
- node_color : None

#### Source code

``` python
def hsv(self, red=None, green=None, blue=None, alpha=None, tag_need_exec=None, ycc_mode='ITUBT709', node_label=None, node_color=None, **kwargs):
    node = self.CombineColor(red=red, green=green, blue=blue, alpha=alpha, mode='HSV', tag_need_exec=tag_need_exec, ycc_mode=ycc_mode, node_label=node_label, node_color=node_color, **kwargs)
    return node.color
```
### inverse_sqrt


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def inverse_sqrt(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='INVERSE_SQRT', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### less_than


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def less_than(self, value=None, value_1=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='LESS_THAN', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### log


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def log(self, value=None, value_1=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='LOGARITHM', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### max


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def max(self, value=None, value_1=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='MAXIMUM', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### min


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def min(self, value=None, value_1=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='MINIMUM', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### mod


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def mod(self, value=None, value_1=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='MODULO', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### multiply


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def multiply(self, value=None, value_1=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='MULTIPLY', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### multiply_add


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- value_2 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def multiply_add(self, value=None, value_1=None, value_2=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, value_2=value_2, operation='MULTIPLY_ADD', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### pingpong


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def pingpong(self, value=None, value_1=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='PINGPONG', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### power


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def power(self, value=None, value_1=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='POWER', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### radians


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def radians(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='RADIANS', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### rgb


- node : [CombineColor](/docs/Compositor/CombineColor.md)
- return : color

##### Arguments

- red : None
- green : None
- blue : None
- alpha : None
- tag_need_exec : None
- ycc_mode : 'ITUBT709' in ('ITUBT601', 'ITUBT709', 'JFIF')
- node_label : None
- node_color : None

#### Source code

``` python
def rgb(self, red=None, green=None, blue=None, alpha=None, tag_need_exec=None, ycc_mode='ITUBT709', node_label=None, node_color=None, **kwargs):
    node = self.CombineColor(red=red, green=green, blue=blue, alpha=alpha, mode='RGB', tag_need_exec=tag_need_exec, ycc_mode=ycc_mode, node_label=node_label, node_color=node_color, **kwargs)
    return node.color
```
### round


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def round(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='ROUND', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### scene_time


- node : [SceneTime](/docs/Compositor/SceneTime.md)
- return : node

##### Arguments

- tag_need_exec : None
- node_label : None
- node_color : None

#### Source code

``` python
def scene_time(self, tag_need_exec=None, node_label=None, node_color=None, **kwargs):
    node = self.SceneTime(tag_need_exec=tag_need_exec, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### seconds


- node : [SceneTime](/docs/Compositor/SceneTime.md)
- return : seconds

##### Arguments

- tag_need_exec : None
- node_label : None
- node_color : None

#### Source code

``` python
def seconds(self, tag_need_exec=None, node_label=None, node_color=None, **kwargs):
    node = self.SceneTime(tag_need_exec=tag_need_exec, node_label=node_label, node_color=node_color, **kwargs)
    return node.seconds
```
### sign


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def sign(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='SIGN', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sin


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def sin(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='SINE', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sinh


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def sinh(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='SINH', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### smooth_max


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- value_2 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def smooth_max(self, value=None, value_1=None, value_2=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, value_2=value_2, operation='SMOOTH_MAX', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### smooth_min


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- value_2 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def smooth_min(self, value=None, value_1=None, value_2=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, value_2=value_2, operation='SMOOTH_MIN', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### snap


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def snap(self, value=None, value_1=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='SNAP', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sqrt


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def sqrt(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='SQRT', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### subtract


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def subtract(self, value=None, value_1=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, operation='SUBTRACT', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### tan


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def tan(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='TANGENT', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### tanh


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def tanh(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='TANH', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### trunc


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def trunc(self, value=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, operation='TRUNC', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### wrap


- node : [Math](/docs/Compositor/Math.md)
- return : value

##### Arguments

- value : None
- value_1 : None
- value_2 : None
- tag_need_exec : None
- use_clamp : False
- node_label : None
- node_color : None

#### Source code

``` python
def wrap(self, value=None, value_1=None, value_2=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):
    node = self.Math(value=value, value_1=value_1, value_2=value_2, operation='WRAP', tag_need_exec=tag_need_exec, use_clamp=use_clamp, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### xyz


- node : [CombineXYZ](/docs/Compositor/CombineXYZ.md)
- return : vector

##### Arguments

- x : None
- y : None
- z : None
- tag_need_exec : None
- node_label : None
- node_color : None

#### Source code

``` python
def xyz(self, x=None, y=None, z=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs):
    node = self.CombineXYZ(x=x, y=y, z=z, tag_need_exec=tag_need_exec, node_label=node_label, node_color=node_color, **kwargs)
    return node.vector
```
### ycc


- node : [CombineColor](/docs/Compositor/CombineColor.md)
- return : color

##### Arguments

- red : None
- green : None
- blue : None
- alpha : None
- tag_need_exec : None
- ycc_mode : 'ITUBT709' in ('ITUBT601', 'ITUBT709', 'JFIF')
- node_label : None
- node_color : None

#### Source code

``` python
def ycc(self, red=None, green=None, blue=None, alpha=None, tag_need_exec=None, ycc_mode='ITUBT709', node_label=None, node_color=None, **kwargs):
    node = self.CombineColor(red=red, green=green, blue=blue, alpha=alpha, mode='YCC', tag_need_exec=tag_need_exec, ycc_mode=ycc_mode, node_label=node_label, node_color=node_color, **kwargs)
    return node.color
```
### yuv


- node : [CombineColor](/docs/Compositor/CombineColor.md)
- return : color

##### Arguments

- red : None
- green : None
- blue : None
- alpha : None
- tag_need_exec : None
- ycc_mode : 'ITUBT709' in ('ITUBT601', 'ITUBT709', 'JFIF')
- node_label : None
- node_color : None

#### Source code

``` python
def yuv(self, red=None, green=None, blue=None, alpha=None, tag_need_exec=None, ycc_mode='ITUBT709', node_label=None, node_color=None, **kwargs):
    node = self.CombineColor(red=red, green=green, blue=blue, alpha=alpha, mode='YUV', tag_need_exec=tag_need_exec, ycc_mode=ycc_mode, node_label=node_label, node_color=node_color, **kwargs)
    return node.color
```
