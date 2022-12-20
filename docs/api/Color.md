# class Color

## Properties

- [alpha](#alpha-property)
- [blue](#blue-property)
- [green](#green-property)
- [hsl](#hsl-property)
- [hsv](#hsv-property)
- [hue](#hue-property)
- [lightness](#lightness-property)
- [red](#red-property)
- [rgb](#rgb-property)
- [rgb_curves](#rgb_curves-property)
- [saturation](#saturation-property)
- [value](#value-property)

## Class methods

- [Color](#Color-classmethod)
- [HSL](#HSL-classmethod)
- [HSV](#HSV-classmethod)
- [RGB](#RGB-classmethod)


## Methods

- [brighter](#brighter)
- [compare](#compare)
- [darker](#darker)
- [equal](#equal)
- [equal](#equal)
- [mix](#mix)
- [mix_add](#mix_add)
- [mix_burn](#mix_burn)
- [mix_color](#mix_color)
- [mix_darken](#mix_darken)
- [mix_difference](#mix_difference)
- [mix_divide](#mix_divide)
- [mix_dodge](#mix_dodge)
- [mix_hue](#mix_hue)
- [mix_lighten](#mix_lighten)
- [mix_linear_light](#mix_linear_light)
- [mix_multiply](#mix_multiply)
- [mix_overlay](#mix_overlay)
- [mix_saturation](#mix_saturation)
- [mix_screen](#mix_screen)
- [mix_soft_light](#mix_soft_light)
- [mix_subtract](#mix_subtract)
- [mix_value](#mix_value)
- [switch](#switch)

## Color <span style="color:blue">*classmethod*</span>

```python
def Color(cls):

```
Node [Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputColor.html) )

### Returns:

  socket 'color'

<sub>Go to [top](#class-Color)</sub>

## HSL <span style="color:blue">*classmethod*</span>

```python
def HSL(cls, hue=None, saturation=None, lightness=None, alpha=None):

```
Node [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html) )

### Args:
- hue: Float
- saturation: Float
- lightness: Float
- alpha: Float

### Returns:

  socket 'color'

<sub>Go to [top](#class-Color)</sub>

## HSV <span style="color:blue">*classmethod*</span>

```python
def HSV(cls, hue=None, saturation=None, value=None, alpha=None):

```
Node [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html) )

### Args:
- hue: Float
- saturation: Float
- value: Float
- alpha: Float

### Returns:

  socket 'color'

<sub>Go to [top](#class-Color)</sub>

## RGB <span style="color:blue">*classmethod*</span>

```python
def RGB(cls, red=None, green=None, blue=None, alpha=None):

```
Node [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html) )

### Args:
- red: Float
- green: Float
- blue: Float
- alpha: Float

### Returns:

  socket 'color'

<sub>Go to [top](#class-Color)</sub>

## alpha <span style="color:blue">*property*</span>

```python
def alpha(self):

```
Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

  socket 'alpha'

<sub>Go to [top](#class-Color)</sub>

## blue <span style="color:blue">*property*</span>

```python
def blue(self):

```
Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

  socket 'blue'

<sub>Go to [top](#class-Color)</sub>

## brighter

```python
def brighter(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## compare

```python
def compare(self, b=None, epsilon=None, operation='GREATER_THAN'):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float
- operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## darker

```python
def darker(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## equal

```python
def equal(self, b=None, epsilon=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## equal

```python
def equal(self, b=None, epsilon=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## green <span style="color:blue">*property*</span>

```python
def green(self):

```
Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

  socket 'green'

<sub>Go to [top](#class-Color)</sub>

## hsl <span style="color:blue">*property*</span>

```python
def hsl(self):

```
Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

- tuple ('red', 'green', 'blue', 'alpha')

<sub>Go to [top](#class-Color)</sub>

## hsv <span style="color:blue">*property*</span>

```python
def hsv(self):

```
Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

- tuple ('red', 'green', 'blue', 'alpha')

<sub>Go to [top](#class-Color)</sub>

## hue <span style="color:blue">*property*</span>

```python
def hue(self):

```
Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

  socket 'red'

<sub>Go to [top](#class-Color)</sub>

## lightness <span style="color:blue">*property*</span>

```python
def lightness(self):

```
Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

  socket 'blue'

<sub>Go to [top](#class-Color)</sub>

## mix

```python
def mix(self, factor=None, color=None, blend_type='MIX', clamp_factor=True, clamp_result=False):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- blend_type (str): 'MIX' in [MIX, DARKEN, MULTIPLY, BURN, LIGHTEN,... , SATURATION, COLOR, VALUE]
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## mix_add

```python
def mix_add(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## mix_burn

```python
def mix_burn(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## mix_color

```python
def mix_color(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## mix_darken

```python
def mix_darken(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## mix_difference

```python
def mix_difference(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## mix_divide

```python
def mix_divide(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## mix_dodge

```python
def mix_dodge(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## mix_hue

```python
def mix_hue(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## mix_lighten

```python
def mix_lighten(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## mix_linear_light

```python
def mix_linear_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## mix_multiply

```python
def mix_multiply(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## mix_overlay

```python
def mix_overlay(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## mix_saturation

```python
def mix_saturation(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## mix_screen

```python
def mix_screen(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## mix_soft_light

```python
def mix_soft_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## mix_subtract

```python
def mix_subtract(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## mix_value

```python
def mix_value(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

<sub>Go to [top](#class-Color)</sub>

## red <span style="color:blue">*property*</span>

```python
def red(self):

```
Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

  socket 'red'

<sub>Go to [top](#class-Color)</sub>

## rgb <span style="color:blue">*property*</span>

```python
def rgb(self):

```
Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

- tuple ('red', 'green', 'blue', 'alpha')

<sub>Go to [top](#class-Color)</sub>

## rgb_curves <span style="color:blue">*property*</span>

```python
def rgb_curves(self, fac=None):

```
Node [RGB Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/rgb_curves.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBCurve.html) )

Node implemented as property.

### Returns:

- node with sockets ['color']

<sub>Go to [top](#class-Color)</sub>

## saturation <span style="color:blue">*property*</span>

```python
def saturation(self):

```
Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

  socket 'green'

<sub>Go to [top](#class-Color)</sub>

## switch

```python
def switch(self, switch=None, true=None):

```
Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

### Args:
- switch: ['Boolean', 'Boolean']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

<sub>Go to [top](#class-Color)</sub>

## value <span style="color:blue">*property*</span>

```python
def value(self):

```
Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

  socket 'blue'

<sub>Go to [top](#class-Color)</sub>

