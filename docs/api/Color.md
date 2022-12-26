# Class Color

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

 Color DataSocket

#### Args:
- value (float, triplet, DataSocket): Initial value
- label (str): Node label
    
Color exposes properties: `red`, `green` and `blue`, `hue`, `value`, 'lightness`, 'saturation` and `alpha`:
    
```python
c = Color()
c.red = .5
c.saturation = .2
```

Color supports some operators:
    
|    Operator            | Mix mode    | Method                             |
|------------------------|-------------|------------------------------------|
|         `+`            | ADD         | [mix_add](#mix_add)                |
|         `*`            | MULTIPLY    | [mix_multiply](#mix_multiply)      |
|         `-`            | DIFFERENCE  | [mix_difference](#mix_difference)  |
|         `/`            | DIVIDE      | [mix_divide](#mix_divide)          |
|         `%`            | MIX         | [mix](#mix)                        |





### Constructor

```python
Color(self, value=None, label=None)
```

## Content

**Properties**

[alpha](#alpha) | [blue](#blue) | [green](#green) | [hue](#hue) | [lightness](#lightness) | [red](#red) | [rgb_curves](#rgb_curves) | [saturation](#saturation) | [separate_HSL](#separate_HSL) | [separate_HSV](#separate_HSV) | [separate_RGB](#separate_RGB) | [value](#value)

***Inherited***

[bl_idname](DataSocket.md#bl_idname) | [bnode](DataSocket.md#bnode) | [is_multi_input](DataSocket.md#is_multi_input) | [is_output](DataSocket.md#is_output) | [is_plugged](DataSocket.md#is_plugged) | [links](DataSocket.md#links) | [name](DataSocket.md#name) | [node_chain_label](DataSocket.md#node_chain_label) | [socket_index](DataSocket.md#socket_index)

**Class and static methods**

[Color](#Color) | [HSL](#HSL) | [HSV](#HSV) | [Input](#Input) | [RGB](#RGB)

***Inherited***

[get_bl_idname](DataSocket.md#get_bl_idname) | [get_class_name](DataSocket.md#get_class_name) | [gives_bsocket](DataSocket.md#gives_bsocket) | [is_socket](DataSocket.md#is_socket) | [is_vector](DataSocket.md#is_vector) | [python_type_to_socket](DataSocket.md#python_type_to_socket) | [value_data_type](DataSocket.md#value_data_type)

**Methods**

[brighter](#brighter) | [darker](#darker) | [equal](#equal) | [get_blender_socket](#get_blender_socket) | [mix](#mix) | [mix_add](#mix_add) | [mix_burn](#mix_burn) | [mix_color](#mix_color) | [mix_darken](#mix_darken) | [mix_difference](#mix_difference) | [mix_divide](#mix_divide) | [mix_dodge](#mix_dodge) | [mix_hue](#mix_hue) | [mix_lighten](#mix_lighten) | [mix_linear_light](#mix_linear_light) | [mix_multiply](#mix_multiply) | [mix_overlay](#mix_overlay) | [mix_saturation](#mix_saturation) | [mix_screen](#mix_screen) | [mix_soft_light](#mix_soft_light) | [mix_subtract](#mix_subtract) | [mix_value](#mix_value) | [separate_color](#separate_color) | [switch](#switch)

***Inherited***

[connected_sockets](DataSocket.md#connected_sockets) | [get_blender_socket](DataSocket.md#get_blender_socket) | [init_domains](DataSocket.md#init_domains) | [init_socket](DataSocket.md#init_socket) | [plug](DataSocket.md#plug) | [reroute](DataSocket.md#reroute) | [reset_properties](DataSocket.md#reset_properties) | [stack](DataSocket.md#stack) | [to_output](DataSocket.md#to_output)

## Properties

### alpha

 Alpha compenent



<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### blue

 Blue compenent



<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### green

 Green compenent



<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### hue

 Hue compenent




<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### lightness

 Lightness compenent



<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### red

 Red compenent



<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### rgb_curves



> Node: [RGB Curves](ShaderNodeRGBCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/rgb_curves.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBCurve.html)

#### Returns:
- node with sockets ['color']






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### saturation

 Saturation compenent



<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### separate_HSL

 Separate HSL

#### Returns:
- node with sockets hue, saturation, lightness, alpha



<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### separate_HSV

 Separate HSV

#### Returns:
- node with sockets hue, saturation, value, alpha



<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### separate_RGB

 Separate RGB

#### Returns:
- node with sockets red, green, blue, alpha



<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### value

 Value compenent



<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Class and static methods

### Color

```python
@classmethod
def Color(cls)
```



> Node: [Color](FunctionNodeInputColor.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/color.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputColor.html)

#### Returns:
- socket `color`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### HSL

```python
@classmethod
def HSL(cls, hue=None, saturation=None, lightness=None, alpha=None)
```



> Node: [Combine Color](FunctionNodeCombineColor.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)

#### Args:
- hue: Float
- saturation: Float
- lightness: Float
- alpha: Float

#### Returns:
- socket `color`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### HSV

```python
@classmethod
def HSV(cls, hue=None, saturation=None, value=None, alpha=None)
```



> Node: [Combine Color](FunctionNodeCombineColor.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)

#### Args:
- hue: Float
- saturation: Float
- value: Float
- alpha: Float

#### Returns:
- socket `color`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Input

```python
@classmethod
def Input(cls, value=None, name = "Color", description = "")
```

 Create a Color input socket in the Group Input Node

#### Args:
- value: The default value
- name: The socket name
- description: User tip
    
#### Returns:
- Color: The Color data socket




<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### RGB

```python
@classmethod
def RGB(cls, red=None, green=None, blue=None, alpha=None)
```



> Node: [Combine Color](FunctionNodeCombineColor.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)

#### Args:
- red: Float
- green: Float
- blue: Float
- alpha: Float

#### Returns:
- socket `color`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### brighter

```python
def brighter(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### darker

```python
def darker(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### equal

```python
def equal(self, b=None, epsilon=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_blender_socket

```python
def get_blender_socket(self)
```

 Overrides the standard behavior of :class:DataSocket super class

If the `r`, `g`, `b` properties have been read or modified, a *Combine RGB* node is necessary
to recompose the Color.

.. blid:: ShaderNodeCombineRGB




<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix

```python
def mix(self, factor=None, color=None, blend_type='MIX', clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- blend_type (str): 'MIX' in [MIX, DARKEN, MULTIPLY, BURN, LIGHTEN,... , SATURATION, COLOR, VALUE]
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix_add

```python
def mix_add(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix_burn

```python
def mix_burn(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix_color

```python
def mix_color(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix_darken

```python
def mix_darken(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix_difference

```python
def mix_difference(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix_divide

```python
def mix_divide(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix_dodge

```python
def mix_dodge(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix_hue

```python
def mix_hue(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix_lighten

```python
def mix_lighten(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix_linear_light

```python
def mix_linear_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix_multiply

```python
def mix_multiply(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix_overlay

```python
def mix_overlay(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix_saturation

```python
def mix_saturation(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix_screen

```python
def mix_screen(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix_soft_light

```python
def mix_soft_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix_subtract

```python
def mix_subtract(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix_value

```python
def mix_value(self, factor=None, color=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### separate_color

```python
def separate_color(self, mode='RGB')
```



> Node: [Separate Color](FunctionNodeSeparateColor.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

#### Args:
- mode (str): 'RGB' in [RGB, HSV, HSL]

#### Returns:
- node with sockets ['red', 'green', 'blue', 'alpha']






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch

```python
def switch(self, switch=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: Color

#### Returns:
- socket `output`






<sub>Go to [top](#class-Color) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

