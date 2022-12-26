# Class String

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

 String DataSocket
String supports python slicing:
    
```python
s = String("ABCDEFGHIJK")

a = s[3]   # Returns String("A")
a = s[:3]  # Returns String("ABC")
a = s[3:6] # Returns String("DEF")

i = Integer(6)
j = Integer(9)

a = s[i:j] # Returns String("GHI")
```




### Constructor

```python
String(self, value = "Text", label = None)
```

## Content

**Properties**

[length](#length)

***Inherited***

[bl_idname](DataSocket.md#bl_idname) | [bnode](DataSocket.md#bnode) | [is_multi_input](DataSocket.md#is_multi_input) | [is_output](DataSocket.md#is_output) | [is_plugged](DataSocket.md#is_plugged) | [links](DataSocket.md#links) | [name](DataSocket.md#name) | [node_chain_label](DataSocket.md#node_chain_label) | [socket_index](DataSocket.md#socket_index)

**Class and static methods**

[Input](#Input) | [LineBreak](#LineBreak) | [String](#String) | [Tab](#Tab) | [Value](#Value)

***Inherited***

[get_bl_idname](DataSocket.md#get_bl_idname) | [get_class_name](DataSocket.md#get_class_name) | [gives_bsocket](DataSocket.md#gives_bsocket) | [is_socket](DataSocket.md#is_socket) | [is_vector](DataSocket.md#is_vector) | [python_type_to_socket](DataSocket.md#python_type_to_socket) | [value_data_type](DataSocket.md#value_data_type)

**Methods**

[equal](#equal) | [join](#join) | [join_strings](#join_strings) | [not_equal](#not_equal) | [replace](#replace) | [slice](#slice) | [string_join](#string_join) | [switch](#switch) | [to_curves](#to_curves)

***Inherited***

[connected_sockets](DataSocket.md#connected_sockets) | [get_blender_socket](DataSocket.md#get_blender_socket) | [init_domains](DataSocket.md#init_domains) | [init_socket](DataSocket.md#init_socket) | [plug](DataSocket.md#plug) | [reroute](DataSocket.md#reroute) | [reset_properties](DataSocket.md#reset_properties) | [stack](DataSocket.md#stack) | [to_output](DataSocket.md#to_output)

## Properties

### length



> Node: [String Length](FunctionNodeStringLength.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/string_length.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeStringLength.html)

#### Returns:
- socket `length`






<sub>Go to [top](#class-String) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Class and static methods

### Input

```python
@classmethod
def Input(cls, value = "Text", name = "String", description = "")
```

 Create a String input socket in the Group Input Node

#### Args:
- value: The default value
- name: The socket name
- description: User tip
    
#### Returns:
- Float: The Float data socket



<sub>Go to [top](#class-String) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### LineBreak

```python
@staticmethod
def LineBreak()
```



> Node: [Special Characters](FunctionNodeInputSpecialCharacters.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/special_characters.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputSpecialCharacters.html)

#### Returns:
- socket `line_break`






<sub>Go to [top](#class-String) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### String

```python
@classmethod
def String(cls, string='')
```



> Node: [String](FunctionNodeInputString.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/string.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputString.html)

#### Args:
- string (str): ''

#### Returns:
- socket `string`






<sub>Go to [top](#class-String) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Tab

```python
@staticmethod
def Tab()
```



> Node: [Special Characters](FunctionNodeInputSpecialCharacters.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/special_characters.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputSpecialCharacters.html)

#### Returns:
- socket `tab`






<sub>Go to [top](#class-String) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Value

```python
@staticmethod
def Value(value = None, decimals = None)
```

 String constructor : initialize a String from a numeric value

#### Args:
- value: Value to convert
- decimals: Number of decimals
    
```python
s = String.Value(Float(12.34), decimal=2)




<sub>Go to [top](#class-String) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### equal

```python
def equal(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-String) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### join

```python
def join(self, *strings)
```



> Node: [Join Strings](GeometryNodeStringJoin.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/join_strings.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringJoin.html)

#### Args:
- strings: <m>String

#### Returns:
- socket `string`






<sub>Go to [top](#class-String) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### join_strings

```python
def join_strings(self, *strings, delimiter = None)
```

 Join strings with a delimiter

#### Args:
- strings (str, String): List of strings to join
- delimiter (str, String): Delimiter between the strings
    
#### Returns:
- String: strings joined with the delimiter
    
> Note: Here, the `self` String is used as the first String to join.
  In the method `join`, `self` acts as the delimiter.
  
**Example**

```python
s0 = String("Demo")
s1 = String("ABC")
s2 = String("BCD")
delimiter = String(", ")

s = s0.join_strings(s1, s2, "EFG", delimiter=delimiter)

# Is equivalent to the more *pythonic*:
    
s = delimiter.join(s0, s1, s2, "EFG")    
```




<sub>Go to [top](#class-String) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### not_equal

```python
def not_equal(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-String) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### replace

```python
def replace(self, find=None, replace=None)
```



> Node: [Replace String](FunctionNodeReplaceString.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/replace_string.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeReplaceString.html)

#### Args:
- find: String
- replace: String

#### Returns:
- socket `string`






<sub>Go to [top](#class-String) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### slice

```python
def slice(self, position=None, length=None)
```



> Node: [Slice String](FunctionNodeSliceString.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/slice_string.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSliceString.html)

#### Args:
- position: Integer
- length: Integer

#### Returns:
- socket `string`






<sub>Go to [top](#class-String) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### string_join

```python
def string_join(*strings, delimiter=None)
```



> Node: [Join Strings](GeometryNodeStringJoin.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/join_strings.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringJoin.html)

#### Args:
- strings: <m>String
- delimiter: String

#### Returns:
- socket `string`






<sub>Go to [top](#class-String) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch

```python
def switch(self, switch=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: String

#### Returns:
- socket `output`






<sub>Go to [top](#class-String) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_curves

```python
def to_curves(self, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT')
```



> Node: [String to Curves](GeometryNodeStringToCurves.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/string_to_curves.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringToCurves.html)

#### Args:
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

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeStringToCurves.webp)

#### Returns:
- tuple ('`curve_instances`', '`line`', '`pivot_point`')






<sub>Go to [top](#class-String) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

