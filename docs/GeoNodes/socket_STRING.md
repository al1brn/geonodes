# Socket STRING

### Properties

- [length](#length)
- [line_break](#line_break)
- [tab](#tab)

### Methods

- [equal](#equal)
- [index_switch](#index_switch)
- [join_strings](#join_strings)
- [not_equal](#not_equal)
- [replace_string](#replace_string)
- [slice_string](#slice_string)
- [special_characters](#special_characters)
- [string_to_curves](#string_to_curves)
- [switch](#switch)

## Properties

### length

> Read only property

### Get


- node : [StringLength](/docs/GeoNodes/StringLength.md)
- self : string
- jump : No
- return : length

##### Arguments

- node_color : 'ARG_NO_VALUE'

#### Source code

``` python
def length(self):
    node = self.tree.StringLength(string=self, node_color=(0.3, 0.3, 0.25))
    return node.length
```
### line_break

> Read only property

### Get


- node : [SpecialCharacters](/docs/GeoNodes/SpecialCharacters.md)
- self
- jump : No
- return : line_break

##### Arguments

- node_color : 'ARG_NO_VALUE'

#### Source code

``` python
def line_break(self):
    node = self.tree.SpecialCharacters(node_color=(0.3, 0.3, 0.25))
    return node.line_break
```
### tab

> Read only property

### Get


- node : [SpecialCharacters](/docs/GeoNodes/SpecialCharacters.md)
- self
- jump : No
- return : tab

##### Arguments

- node_color : 'ARG_NO_VALUE'

#### Source code

``` python
def tab(self):
    node = self.tree.SpecialCharacters(node_color=(0.3, 0.3, 0.25))
    return node.tab
```
## Methods

### equal


- node : [Compare](/docs/GeoNodes/Compare.md)
- self : a
- jump : No
- return : result

##### Arguments

- b : None
- mode : 'ELEMENT' in ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION')
- node_label : None
- node_color : None

#### Source code

``` python
def equal(self, b=None, mode='ELEMENT', node_label=None, node_color=None, **kwargs):
    node = self.tree.Compare(a=self, b=b, data_type='STRING', mode=mode, operation='EQUAL', node_label=node_label, node_color=node_color, **kwargs)
    return node.result
```
### index_switch


- node : [IndexSwitch](/docs/GeoNodes/IndexSwitch.md)
- self : ARG0
- jump : No
- return : output

##### Arguments

- *args : 'ARG_NO_VALUE'
- index : None
- node_label : None
- node_color : None

#### Source code

``` python
def index_switch(self, *args, index=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.IndexSwitch(self, *args, index=index, data_type='STRING', node_label=node_label, node_color=node_color, **kwargs)
    return node.output
```
### join_strings


- node : [JoinStrings](/docs/GeoNodes/JoinStrings.md)
- self : strings
- jump : string
- return : self

##### Arguments

- *args : 'ARG_NO_VALUE'
- delimiter : None
- node_label : None
- node_color : None

#### Source code

``` python
def join_strings(self, *args, delimiter=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.JoinStrings(*args, delimiter=delimiter, strings=self, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.string)
    return self
```
### not_equal


- node : [Compare](/docs/GeoNodes/Compare.md)
- self : a
- jump : No
- return : result

##### Arguments

- b : None
- mode : 'ELEMENT' in ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION')
- node_label : None
- node_color : None

#### Source code

``` python
def not_equal(self, b=None, mode='ELEMENT', node_label=None, node_color=None, **kwargs):
    node = self.tree.Compare(a=self, b=b, data_type='STRING', mode=mode, operation='NOT_EQUAL', node_label=node_label, node_color=node_color, **kwargs)
    return node.result
```
### replace_string


- node : [ReplaceString](/docs/GeoNodes/ReplaceString.md)
- self : string
- jump : string
- return : self

##### Arguments

- find : None
- replace : None
- node_label : None
- node_color : None

#### Source code

``` python
def replace_string(self, find=None, replace=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.ReplaceString(string=self, find=find, replace=replace, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.string)
    return self
```
### slice_string


- node : [SliceString](/docs/GeoNodes/SliceString.md)
- self : string
- jump : string
- return : self

##### Arguments

- position : None
- length : None
- node_label : None
- node_color : None

#### Source code

``` python
def slice_string(self, position=None, length=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SliceString(string=self, position=position, length=length, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.string)
    return self
```
### special_characters


- node : [SpecialCharacters](/docs/GeoNodes/SpecialCharacters.md)
- self
- jump : No
- return : node

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def special_characters(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.SpecialCharacters(node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### string_to_curves


- node : [StringToCurves](/docs/GeoNodes/StringToCurves.md)
- self : string
- jump : No
- return : node

##### Arguments

- size : None
- character_spacing : None
- word_spacing : None
- line_spacing : None
- text_box_width : None
- text_box_height : None
- align_x : 'LEFT' in ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH')
- align_y : 'TOP_BASELINE' in ('TOP', 'TOP_BASELINE', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM')
- font : None
- overflow : 'OVERFLOW' in ('OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE')
- pivot_mode : 'BOTTOM_LEFT' in ('MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT')
- node_label : None
- node_color : None

#### Source code

``` python
def string_to_curves(self, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', font=None, overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT', node_label=None, node_color=None, **kwargs):
    node = self.tree.StringToCurves(string=self, size=size, character_spacing=character_spacing, word_spacing=word_spacing, line_spacing=line_spacing, text_box_width=text_box_width, text_box_height=text_box_height, align_x=align_x, align_y=align_y, font=font, overflow=overflow, pivot_mode=pivot_mode, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### switch


- node : [Switch](/docs/GeoNodes/Switch.md)
- self : false
- jump : No
- return : output

##### Arguments

- switch : None
- true : None
- node_label : None
- node_color : None

#### Source code

``` python
def switch(self, switch=None, true=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.Switch(switch=switch, false=self, true=true, input_type='STRING', node_label=node_label, node_color=node_color, **kwargs)
    return node.output
```
