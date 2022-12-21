# class String

> [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)

## Properties

- [length](#length-property)

## Class methods

- [Input](#Input-classmethod)
- [String](#String-classmethod)

## Static methods

- [LineBreak](#LineBreak-staticmethod)
- [Tab](#Tab-staticmethod)

## Methods

- [equal](#equal)
- [join](#join)
- [not_equal](#not_equal)
- [replace](#replace)
- [slice](#slice)
- [switch](#switch)
- [to_curves](#to_curves)

## Input <sub>*classmethod*</sub>

```python
def Input(cls, value=None, name="CLASS_METHOD", min_value=None, max_value=None, description=""):

```
Used to create an input socket in the Group Input node.
Even if homonyms are accepted, it is recommended to avoid to create to input sockets with the same name.

### Args:
- value: Initial value. Not changed if the group input socket already exists
- name: Input socket name. Avoid homonyms!
- min_value: minimum value
- max_value: maxium value
- description: user help

### Returns:
- String

<sub>Go to [top](#class-String) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## LineBreak <sub>*staticmethod*</sub>

```python
def LineBreak():

```
Node [Special Characters](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/special_characters.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputSpecialCharacters.html) )

### Returns:
- socket `line_break`

<sub>Go to [top](#class-String) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## String <sub>*classmethod*</sub>

```python
def String(cls, string=''):

```
Node [String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/string.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputString.html) )

### Args:
- string (str): ''

### Returns:
- socket `string`

<sub>Go to [top](#class-String) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## Tab <sub>*staticmethod*</sub>

```python
def Tab():

```
Node [Special Characters](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/special_characters.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputSpecialCharacters.html) )

### Returns:
- socket `tab`

<sub>Go to [top](#class-String) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## equal

```python
def equal(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:
- socket `result`

<sub>Go to [top](#class-String) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## join

```python
def join(*strings, delimiter=None):

```
Node [Join Strings](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/join_strings.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringJoin.html) )

### Args:
- strings: <m>String
- delimiter: String

### Returns:
- socket `string`

<sub>Go to [top](#class-String) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## length <sub>*property*</sub>

```python
def length(self):

```
Node [String Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/string_length.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeStringLength.html) )

### Returns:
- socket `length`

<sub>Go to [top](#class-String) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## not_equal

```python
def not_equal(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:
- socket `result`

<sub>Go to [top](#class-String) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## replace

```python
def replace(self, find=None, replace=None):

```
Node [Replace String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/replace_string.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeReplaceString.html) )

### Args:
- find: String
- replace: String

### Returns:
- socket `string`

<sub>Go to [top](#class-String) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## slice

```python
def slice(self, position=None, length=None):

```
Node [Slice String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/slice_string.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSliceString.html) )

### Args:
- position: Integer
- length: Integer

### Returns:
- socket `string`

<sub>Go to [top](#class-String) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## switch

```python
def switch(self, switch=None, true=None):

```
Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

### Args:
- switch: Boolean
- true: String

### Returns:
- socket `output`

<sub>Go to [top](#class-String) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## to_curves

```python
def to_curves(self, string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT'):

```
Node [String to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/string_to_curves.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringToCurves.html) )

### Args:
- string: String
- size: Float
- character_spacing: Float
- word_spacing: Float
- line_spacing: Float
- text_box_width: Float
- text_box_height: Float
- align_x (str): 'LEFT' in [LEFT, CENTER, RIGHT, JUSTIFY, FLUSH]
- align_y (str): 'TOP_BASELINE' in [TOP_BASELINE, TOP, MIDDLE, BOTTOM_BASELINE, BOTTOM]
- overflow (str): 'OVERFLOW' in [OVERFLOW, SCALE_TO_FIT, TRUNCATE]
- pivot_mode (str): 'BOTTOM_LEFT' in [MIDPOINT, TOP_LEFT, TOP_CENTER,... , BOTTOM_LEFT, BOTTOM_CENTER, BOTTOM_RIGHT]

### Returns:
- tuple ('`curve_instances`', '`line`', '`pivot_point`')

<sub>Go to [top](#class-String) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>
