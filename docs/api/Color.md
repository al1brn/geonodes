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

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def Color(cls):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputColor.html) )

<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'color'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## HSL <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def HSL(cls, hue=None, saturation=None, lightness=None, alpha=None):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- hue: Float
<sub>Go to [top](#class-Color)</sub>

- saturation: Float
<sub>Go to [top](#class-Color)</sub>

- lightness: Float
<sub>Go to [top](#class-Color)</sub>

- alpha: Float
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'color'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## HSV <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def HSV(cls, hue=None, saturation=None, value=None, alpha=None):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- hue: Float
<sub>Go to [top](#class-Color)</sub>

- saturation: Float
<sub>Go to [top](#class-Color)</sub>

- value: Float
<sub>Go to [top](#class-Color)</sub>

- alpha: Float
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'color'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## RGB <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def RGB(cls, red=None, green=None, blue=None, alpha=None):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- red: Float
<sub>Go to [top](#class-Color)</sub>

- green: Float
<sub>Go to [top](#class-Color)</sub>

- blue: Float
<sub>Go to [top](#class-Color)</sub>

- alpha: Float
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'color'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## alpha <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def alpha(self):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

<sub>Go to [top](#class-Color)</sub>

Node implemented as property.

<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'alpha'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## blue <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def blue(self):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

<sub>Go to [top](#class-Color)</sub>

Node implemented as property.

<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'blue'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## brighter

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def brighter(self, b=None):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## compare

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def compare(self, b=None, epsilon=None, operation='GREATER_THAN'):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Color)</sub>

- epsilon: Float
<sub>Go to [top](#class-Color)</sub>

- operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## darker

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def darker(self, b=None):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## equal

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def equal(self, b=None, epsilon=None):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Color)</sub>

- epsilon: Float
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## equal

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def equal(self, b=None, epsilon=None):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Color)</sub>

- epsilon: Float
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## green <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def green(self):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

<sub>Go to [top](#class-Color)</sub>

Node implemented as property.

<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'green'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## hsl <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def hsl(self):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

<sub>Go to [top](#class-Color)</sub>

Node implemented as property.

<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

- tuple ('red', 'green', 'blue', 'alpha')
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## hsv <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def hsv(self):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

<sub>Go to [top](#class-Color)</sub>

Node implemented as property.

<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

- tuple ('red', 'green', 'blue', 'alpha')
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## hue <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def hue(self):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

<sub>Go to [top](#class-Color)</sub>

Node implemented as property.

<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'red'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## lightness <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def lightness(self):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

<sub>Go to [top](#class-Color)</sub>

Node implemented as property.

<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'blue'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## mix

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def mix(self, factor=None, color=None, blend_type='MIX', clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- factor: ['Float', 'Vector']
<sub>Go to [top](#class-Color)</sub>

- color: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Color)</sub>

- blend_type (str): 'MIX' in [MIX, DARKEN, MULTIPLY, BURN, LIGHTEN,... , SATURATION, COLOR, VALUE]
<sub>Go to [top](#class-Color)</sub>

- clamp_factor (bool): True
<sub>Go to [top](#class-Color)</sub>

- clamp_result (bool): False
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## mix_add

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def mix_add(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- factor: ['Float', 'Vector']
<sub>Go to [top](#class-Color)</sub>

- color: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Color)</sub>

- clamp_factor (bool): True
<sub>Go to [top](#class-Color)</sub>

- clamp_result (bool): False
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## mix_burn

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def mix_burn(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- factor: ['Float', 'Vector']
<sub>Go to [top](#class-Color)</sub>

- color: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Color)</sub>

- clamp_factor (bool): True
<sub>Go to [top](#class-Color)</sub>

- clamp_result (bool): False
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## mix_color

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def mix_color(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- factor: ['Float', 'Vector']
<sub>Go to [top](#class-Color)</sub>

- color: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Color)</sub>

- clamp_factor (bool): True
<sub>Go to [top](#class-Color)</sub>

- clamp_result (bool): False
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## mix_darken

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def mix_darken(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- factor: ['Float', 'Vector']
<sub>Go to [top](#class-Color)</sub>

- color: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Color)</sub>

- clamp_factor (bool): True
<sub>Go to [top](#class-Color)</sub>

- clamp_result (bool): False
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## mix_difference

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def mix_difference(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- factor: ['Float', 'Vector']
<sub>Go to [top](#class-Color)</sub>

- color: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Color)</sub>

- clamp_factor (bool): True
<sub>Go to [top](#class-Color)</sub>

- clamp_result (bool): False
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## mix_divide

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def mix_divide(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- factor: ['Float', 'Vector']
<sub>Go to [top](#class-Color)</sub>

- color: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Color)</sub>

- clamp_factor (bool): True
<sub>Go to [top](#class-Color)</sub>

- clamp_result (bool): False
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## mix_dodge

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def mix_dodge(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- factor: ['Float', 'Vector']
<sub>Go to [top](#class-Color)</sub>

- color: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Color)</sub>

- clamp_factor (bool): True
<sub>Go to [top](#class-Color)</sub>

- clamp_result (bool): False
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## mix_hue

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def mix_hue(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- factor: ['Float', 'Vector']
<sub>Go to [top](#class-Color)</sub>

- color: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Color)</sub>

- clamp_factor (bool): True
<sub>Go to [top](#class-Color)</sub>

- clamp_result (bool): False
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## mix_lighten

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def mix_lighten(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- factor: ['Float', 'Vector']
<sub>Go to [top](#class-Color)</sub>

- color: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Color)</sub>

- clamp_factor (bool): True
<sub>Go to [top](#class-Color)</sub>

- clamp_result (bool): False
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## mix_linear_light

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def mix_linear_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- factor: ['Float', 'Vector']
<sub>Go to [top](#class-Color)</sub>

- color: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Color)</sub>

- clamp_factor (bool): True
<sub>Go to [top](#class-Color)</sub>

- clamp_result (bool): False
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## mix_multiply

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def mix_multiply(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- factor: ['Float', 'Vector']
<sub>Go to [top](#class-Color)</sub>

- color: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Color)</sub>

- clamp_factor (bool): True
<sub>Go to [top](#class-Color)</sub>

- clamp_result (bool): False
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## mix_overlay

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def mix_overlay(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- factor: ['Float', 'Vector']
<sub>Go to [top](#class-Color)</sub>

- color: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Color)</sub>

- clamp_factor (bool): True
<sub>Go to [top](#class-Color)</sub>

- clamp_result (bool): False
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## mix_saturation

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def mix_saturation(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- factor: ['Float', 'Vector']
<sub>Go to [top](#class-Color)</sub>

- color: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Color)</sub>

- clamp_factor (bool): True
<sub>Go to [top](#class-Color)</sub>

- clamp_result (bool): False
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## mix_screen

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def mix_screen(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- factor: ['Float', 'Vector']
<sub>Go to [top](#class-Color)</sub>

- color: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Color)</sub>

- clamp_factor (bool): True
<sub>Go to [top](#class-Color)</sub>

- clamp_result (bool): False
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## mix_soft_light

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def mix_soft_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- factor: ['Float', 'Vector']
<sub>Go to [top](#class-Color)</sub>

- color: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Color)</sub>

- clamp_factor (bool): True
<sub>Go to [top](#class-Color)</sub>

- clamp_result (bool): False
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## mix_subtract

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def mix_subtract(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- factor: ['Float', 'Vector']
<sub>Go to [top](#class-Color)</sub>

- color: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Color)</sub>

- clamp_factor (bool): True
<sub>Go to [top](#class-Color)</sub>

- clamp_result (bool): False
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## mix_value

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def mix_value(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- factor: ['Float', 'Vector']
<sub>Go to [top](#class-Color)</sub>

- color: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Color)</sub>

- clamp_factor (bool): True
<sub>Go to [top](#class-Color)</sub>

- clamp_result (bool): False
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'result'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## red <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def red(self):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

<sub>Go to [top](#class-Color)</sub>

Node implemented as property.

<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'red'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## rgb <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def rgb(self):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

<sub>Go to [top](#class-Color)</sub>

Node implemented as property.

<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

- tuple ('red', 'green', 'blue', 'alpha')
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## rgb_curves <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def rgb_curves(self, fac=None):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [RGB Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/rgb_curves.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBCurve.html) )

<sub>Go to [top](#class-Color)</sub>

Node implemented as property.

<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

- node with sockets ['color']
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## saturation <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def saturation(self):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

<sub>Go to [top](#class-Color)</sub>

Node implemented as property.

<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'green'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## switch

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def switch(self, switch=None, true=None):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

<sub>Go to [top](#class-Color)</sub>

### Args:
<sub>Go to [top](#class-Color)</sub>

- switch: ['Boolean', 'Boolean']
<sub>Go to [top](#class-Color)</sub>

- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'output'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

## value <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Color)</sub>

```python
<sub>Go to [top](#class-Color)</sub>

def value(self):

<sub>Go to [top](#class-Color)</sub>

```
<sub>Go to [top](#class-Color)</sub>

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

<sub>Go to [top](#class-Color)</sub>

Node implemented as property.

<sub>Go to [top](#class-Color)</sub>

### Returns:

<sub>Go to [top](#class-Color)</sub>

  socket 'blue'<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>


<sub>Go to [top](#class-Color)</sub>

