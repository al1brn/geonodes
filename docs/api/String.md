# class String

## Properties

- [length](#length-property)

## Class methods

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

## LineBreak <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-String)</sub>

```python
<sub>Go to [top](#class-String)</sub>

def LineBreak():

<sub>Go to [top](#class-String)</sub>

```
<sub>Go to [top](#class-String)</sub>

Node [Special Characters](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/special_characters.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputSpecialCharacters.html) )

<sub>Go to [top](#class-String)</sub>

### Returns:

<sub>Go to [top](#class-String)</sub>

  socket 'line_break'<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>

## String <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-String)</sub>

```python
<sub>Go to [top](#class-String)</sub>

def String(cls, string=''):

<sub>Go to [top](#class-String)</sub>

```
<sub>Go to [top](#class-String)</sub>

Node [String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/string.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputString.html) )

<sub>Go to [top](#class-String)</sub>

### Args:
<sub>Go to [top](#class-String)</sub>

- string (str): ''
<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>

### Returns:

<sub>Go to [top](#class-String)</sub>

  socket 'string'<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>

## Tab <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-String)</sub>

```python
<sub>Go to [top](#class-String)</sub>

def Tab():

<sub>Go to [top](#class-String)</sub>

```
<sub>Go to [top](#class-String)</sub>

Node [Special Characters](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/special_characters.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputSpecialCharacters.html) )

<sub>Go to [top](#class-String)</sub>

### Returns:

<sub>Go to [top](#class-String)</sub>

  socket 'tab'<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>

## equal

<sub>Go to [top](#class-String)</sub>

```python
<sub>Go to [top](#class-String)</sub>

def equal(self, b=None):

<sub>Go to [top](#class-String)</sub>

```
<sub>Go to [top](#class-String)</sub>

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-String)</sub>

### Args:
<sub>Go to [top](#class-String)</sub>

- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>

### Returns:

<sub>Go to [top](#class-String)</sub>

  socket 'result'<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>

## join

<sub>Go to [top](#class-String)</sub>

```python
<sub>Go to [top](#class-String)</sub>

def join(*strings, delimiter=None):

<sub>Go to [top](#class-String)</sub>

```
<sub>Go to [top](#class-String)</sub>

Node [Join Strings](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/join_strings.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringJoin.html) )

<sub>Go to [top](#class-String)</sub>

### Args:
<sub>Go to [top](#class-String)</sub>

- strings: <m>String
<sub>Go to [top](#class-String)</sub>

- delimiter: String
<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>

### Returns:

<sub>Go to [top](#class-String)</sub>

  socket 'string'<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>

## length <span style="color:blue">*property*</span>

<sub>Go to [top](#class-String)</sub>

```python
<sub>Go to [top](#class-String)</sub>

def length(self):

<sub>Go to [top](#class-String)</sub>

```
<sub>Go to [top](#class-String)</sub>

Node [String Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/string_length.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeStringLength.html) )

<sub>Go to [top](#class-String)</sub>

Node implemented as property.

<sub>Go to [top](#class-String)</sub>

### Returns:

<sub>Go to [top](#class-String)</sub>

  socket 'length'<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>

## not_equal

<sub>Go to [top](#class-String)</sub>

```python
<sub>Go to [top](#class-String)</sub>

def not_equal(self, b=None):

<sub>Go to [top](#class-String)</sub>

```
<sub>Go to [top](#class-String)</sub>

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-String)</sub>

### Args:
<sub>Go to [top](#class-String)</sub>

- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>

### Returns:

<sub>Go to [top](#class-String)</sub>

  socket 'result'<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>

## replace

<sub>Go to [top](#class-String)</sub>

```python
<sub>Go to [top](#class-String)</sub>

def replace(self, find=None, replace=None):

<sub>Go to [top](#class-String)</sub>

```
<sub>Go to [top](#class-String)</sub>

Node [Replace String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/replace_string.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeReplaceString.html) )

<sub>Go to [top](#class-String)</sub>

### Args:
<sub>Go to [top](#class-String)</sub>

- find: String
<sub>Go to [top](#class-String)</sub>

- replace: String
<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>

### Returns:

<sub>Go to [top](#class-String)</sub>

  socket 'string'<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>

## slice

<sub>Go to [top](#class-String)</sub>

```python
<sub>Go to [top](#class-String)</sub>

def slice(self, position=None, length=None):

<sub>Go to [top](#class-String)</sub>

```
<sub>Go to [top](#class-String)</sub>

Node [Slice String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/slice_string.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSliceString.html) )

<sub>Go to [top](#class-String)</sub>

### Args:
<sub>Go to [top](#class-String)</sub>

- position: Integer
<sub>Go to [top](#class-String)</sub>

- length: Integer
<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>

### Returns:

<sub>Go to [top](#class-String)</sub>

  socket 'string'<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>

## switch

<sub>Go to [top](#class-String)</sub>

```python
<sub>Go to [top](#class-String)</sub>

def switch(self, switch=None, true=None):

<sub>Go to [top](#class-String)</sub>

```
<sub>Go to [top](#class-String)</sub>

Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

<sub>Go to [top](#class-String)</sub>

### Args:
<sub>Go to [top](#class-String)</sub>

- switch: ['Boolean', 'Boolean']
<sub>Go to [top](#class-String)</sub>

- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>

### Returns:

<sub>Go to [top](#class-String)</sub>

  socket 'output'<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>

## to_curves

<sub>Go to [top](#class-String)</sub>

```python
<sub>Go to [top](#class-String)</sub>

def to_curves(self, string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT'):

<sub>Go to [top](#class-String)</sub>

```
<sub>Go to [top](#class-String)</sub>

Node [String to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/string_to_curves.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringToCurves.html) )

<sub>Go to [top](#class-String)</sub>

### Args:
<sub>Go to [top](#class-String)</sub>

- string: String
<sub>Go to [top](#class-String)</sub>

- size: Float
<sub>Go to [top](#class-String)</sub>

- character_spacing: Float
<sub>Go to [top](#class-String)</sub>

- word_spacing: Float
<sub>Go to [top](#class-String)</sub>

- line_spacing: Float
<sub>Go to [top](#class-String)</sub>

- text_box_width: Float
<sub>Go to [top](#class-String)</sub>

- text_box_height: Float
<sub>Go to [top](#class-String)</sub>

- align_x (str): 'LEFT' in [LEFT, CENTER, RIGHT, JUSTIFY, FLUSH]
<sub>Go to [top](#class-String)</sub>

- align_y (str): 'TOP_BASELINE' in [TOP_BASELINE, TOP, MIDDLE, BOTTOM_BASELINE, BOTTOM]
<sub>Go to [top](#class-String)</sub>

- overflow (str): 'OVERFLOW' in [OVERFLOW, SCALE_TO_FIT, TRUNCATE]
<sub>Go to [top](#class-String)</sub>

- pivot_mode (str): 'BOTTOM_LEFT' in [MIDPOINT, TOP_LEFT, TOP_CENTER,... , BOTTOM_LEFT, BOTTOM_CENTER, BOTTOM_RIGHT]
<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>

### Returns:

<sub>Go to [top](#class-String)</sub>

- tuple ('curve_instances', 'line', 'pivot_point')
<sub>Go to [top](#class-String)</sub>


<sub>Go to [top](#class-String)</sub>

