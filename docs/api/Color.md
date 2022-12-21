# class Color

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

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
- [Input](#Input-classmethod)
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

## Color <sub>*classmethod*</sub>

```python
def Color(cls):

```
> Node: [Color](FunctionNodeInputColor.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/color.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputColor.html)

#### Returns:
- socket `color`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## HSL <sub>*classmethod*</sub>

```python
def HSL(cls, hue=None, saturation=None, lightness=None, alpha=None):

```
> Node: [Combine Color](FunctionNodeCombineColor.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)

#### Args:
- hue: Float
- saturation: Float
- lightness: Float
- alpha: Float

#### Returns:
- socket `color`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## HSV <sub>*classmethod*</sub>

```python
def HSV(cls, hue=None, saturation=None, value=None, alpha=None):

```
> Node: [Combine Color](FunctionNodeCombineColor.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)

#### Args:
- hue: Float
- saturation: Float
- value: Float
- alpha: Float

#### Returns:
- socket `color`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Input <sub>*classmethod*</sub>

```python
def Input(cls, value=None, name="CLASS_METHOD", min_value=None, max_value=None, description=""):

```
Used to create an input socket in the Group Input node.
Even if homonyms are accepted, it is recommended to avoid to create to input sockets with the same name.

#### Args:
- value: Initial value. Not changed if the group input socket already exists
- name: Input socket name. Avoid homonyms!
- min_value: minimum value
- max_value: maxium value
- description: user help

#### Returns:
- Color

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## RGB <sub>*classmethod*</sub>

```python
def RGB(cls, red=None, green=None, blue=None, alpha=None):

```
> Node: [Combine Color](FunctionNodeCombineColor.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)

#### Args:
- red: Float
- green: Float
- blue: Float
- alpha: Float

#### Returns:
- socket `color`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## alpha <sub>*property*</sub>

```python
def alpha(self):

```
> Node: [Separate Color](FunctionNodeSeparateColor.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

#### Returns:
- socket `alpha`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## blue <sub>*property*</sub>

```python
def blue(self):

```
> Node: [Separate Color](FunctionNodeSeparateColor.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

#### Returns:
- socket `blue`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## brighter

```python
def brighter(self, b=None):

```
> Node: [Compare](FunctionNodeCompare.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## compare

```python
def compare(self, b=None, epsilon=None, operation='GREATER_THAN'):

```
> Node: [Compare](FunctionNodeCompare.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float
- operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## darker

```python
def darker(self, b=None):

```
> Node: [Compare](FunctionNodeCompare.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## equal

```python
def equal(self, b=None, epsilon=None):

```
> Node: [Compare](FunctionNodeCompare.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## equal

```python
def equal(self, b=None, epsilon=None):

```
> Node: [Compare](FunctionNodeCompare.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## green <sub>*property*</sub>

```python
def green(self):

```
> Node: [Separate Color](FunctionNodeSeparateColor.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

#### Returns:
- socket `green`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## hsl <sub>*property*</sub>

```python
def hsl(self):

```
> Node: [Separate Color](FunctionNodeSeparateColor.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

#### Returns:
- tuple ('`red`', '`green`', '`blue`', '`alpha`')
  [Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeSeparateColor.webp)

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## hsv <sub>*property*</sub>

```python
def hsv(self):

```
> Node: [Separate Color](FunctionNodeSeparateColor.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

#### Returns:
- tuple ('`red`', '`green`', '`blue`', '`alpha`')
  [Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeSeparateColor.webp)

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## hue <sub>*property*</sub>

```python
def hue(self):

```
> Node: [Separate Color](FunctionNodeSeparateColor.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

#### Returns:
- socket `red`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## lightness <sub>*property*</sub>

```python
def lightness(self):

```
> Node: [Separate Color](FunctionNodeSeparateColor.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

#### Returns:
- socket `blue`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## mix

```python
def mix(self, factor=None, color=None, blend_type='MIX', clamp_factor=True, clamp_result=False):

```
> Node: [Mix](ShaderNodeMix.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- blend_type (str): 'MIX' in [MIX, DARKEN, MULTIPLY, BURN, LIGHTEN,... , SATURATION, COLOR, VALUE]
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## mix_add

```python
def mix_add(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
> Node: [Mix](ShaderNodeMix.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## mix_burn

```python
def mix_burn(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
> Node: [Mix](ShaderNodeMix.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## mix_color

```python
def mix_color(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
> Node: [Mix](ShaderNodeMix.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## mix_darken

```python
def mix_darken(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
> Node: [Mix](ShaderNodeMix.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## mix_difference

```python
def mix_difference(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
> Node: [Mix](ShaderNodeMix.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## mix_divide

```python
def mix_divide(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
> Node: [Mix](ShaderNodeMix.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## mix_dodge

```python
def mix_dodge(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
> Node: [Mix](ShaderNodeMix.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## mix_hue

```python
def mix_hue(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
> Node: [Mix](ShaderNodeMix.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## mix_lighten

```python
def mix_lighten(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
> Node: [Mix](ShaderNodeMix.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## mix_linear_light

```python
def mix_linear_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
> Node: [Mix](ShaderNodeMix.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## mix_multiply

```python
def mix_multiply(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
> Node: [Mix](ShaderNodeMix.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## mix_overlay

```python
def mix_overlay(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
> Node: [Mix](ShaderNodeMix.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## mix_saturation

```python
def mix_saturation(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
> Node: [Mix](ShaderNodeMix.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## mix_screen

```python
def mix_screen(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
> Node: [Mix](ShaderNodeMix.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## mix_soft_light

```python
def mix_soft_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
> Node: [Mix](ShaderNodeMix.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## mix_subtract

```python
def mix_subtract(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
> Node: [Mix](ShaderNodeMix.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## mix_value

```python
def mix_value(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

```
> Node: [Mix](ShaderNodeMix.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## red <sub>*property*</sub>

```python
def red(self):

```
> Node: [Separate Color](FunctionNodeSeparateColor.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

#### Returns:
- socket `red`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## rgb <sub>*property*</sub>

```python
def rgb(self):

```
> Node: [Separate Color](FunctionNodeSeparateColor.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

#### Returns:
- tuple ('`red`', '`green`', '`blue`', '`alpha`')
  [Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeSeparateColor.webp)

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## rgb_curves <sub>*property*</sub>

```python
def rgb_curves(self, fac=None):

```
> Node: [RGB Curves](ShaderNodeRGBCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/rgb_curves.html) - [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBCurve.html)

#### Returns:
- node with sockets ['color']

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## saturation <sub>*property*</sub>

```python
def saturation(self):

```
> Node: [Separate Color](FunctionNodeSeparateColor.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

#### Returns:
- socket `green`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## switch

```python
def switch(self, switch=None, true=None):

```
> Node: [Switch](GeometryNodeSwitch.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: Color

#### Returns:
- socket `output`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## value <sub>*property*</sub>

```python
def value(self):

```
> Node: [Separate Color](FunctionNodeSeparateColor.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

#### Returns:
- socket `blue`

<sub>Go to [top](#class-Color) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

