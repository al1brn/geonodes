# class Str (Socket)

<sub>go to [index](/docs/index.md)</sub>

Socket
 - Type : STRING
 - bl_idname : NodeSocketString

Methods
 - [equal](#equal) : Compare, a=self, data_type='STRING', operation='EQUAL'
 - [join_strings](#join_strings) : JoinStrings, delimiter=self
 - [named_attribute](#named_attribute) : NamedAttribute, name=self, return node
 - [not_equal](#not_equal) : Compare, a=self, data_type='STRING', operation='NOT_EQUAL'
 - [replace_string](#replace_string) : ReplaceString, string=self
 - [slice_string](#slice_string) : SliceString, string=self
 - [string_length](#string_length) : StringLength, string=self, return socket
 - [switch](#switch) : Switch, false=self, input_type='STRING'

## Methods

### equal

Compare, a=self, data_type='STRING', operation='EQUAL'

Node
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

Arguments
 - b : None
 - mode : 'ELEMENT'
 - node_label : None
 - node_color : None

Node initialization
 - a : self
 - b : b
 - data_type : 'STRING'
 - mode : mode
 - operation : 'EQUAL'
 - node_label : node_label
 - node_color : node_color

``` python
def equal(self, b=None, mode='ELEMENT', node_label=None, node_color=None):
```
### join_strings

JoinStrings, delimiter=self

Node
 - class_name : [JoinStrings](/docs/classes/JoinStrings.md)
 - bl_idname : GeometryNodeStringJoin

Arguments
 - *args : 
 - strings : None
 - node_label : None
 - node_color : None

Node initialization
 - *args : 
 - delimiter : self
 - strings : strings
 - node_label : node_label
 - node_color : node_color

``` python
def join_strings(self, *args, strings=None, node_label=None, node_color=None):
```
### named_attribute

NamedAttribute, name=self, return node

Node
 - class_name : [NamedAttribute](/docs/classes/NamedAttribute.md)
 - bl_idname : GeometryNodeInputNamedAttribute

Arguments
 - data_type : 'FLOAT'
 - node_label : None
 - node_color : None

Node initialization
 - name : self
 - data_type : data_type
 - node_label : node_label
 - node_color : node_color

``` python
def named_attribute(self, data_type='FLOAT', node_label=None, node_color=None):
```
### not_equal

Compare, a=self, data_type='STRING', operation='NOT_EQUAL'

Node
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

Arguments
 - b : None
 - mode : 'ELEMENT'
 - node_label : None
 - node_color : None

Node initialization
 - a : self
 - b : b
 - data_type : 'STRING'
 - mode : mode
 - operation : 'NOT_EQUAL'
 - node_label : node_label
 - node_color : node_color

``` python
def not_equal(self, b=None, mode='ELEMENT', node_label=None, node_color=None):
```
### replace_string

ReplaceString, string=self

Node
 - class_name : [ReplaceString](/docs/classes/ReplaceString.md)
 - bl_idname : FunctionNodeReplaceString

Arguments
 - find : None
 - replace : None
 - node_label : None
 - node_color : None

Node initialization
 - string : self
 - find : find
 - replace : replace
 - node_label : node_label
 - node_color : node_color

``` python
def replace_string(self, find=None, replace=None, node_label=None, node_color=None):
```
### slice_string

SliceString, string=self

Node
 - class_name : [SliceString](/docs/classes/SliceString.md)
 - bl_idname : FunctionNodeSliceString

Arguments
 - position : None
 - length : None
 - node_label : None
 - node_color : None

Node initialization
 - string : self
 - position : position
 - length : length
 - node_label : node_label
 - node_color : node_color

``` python
def slice_string(self, position=None, length=None, node_label=None, node_color=None):
```
### string_length

StringLength, string=self, return socket

Node
 - class_name : [StringLength](/docs/classes/StringLength.md)
 - bl_idname : FunctionNodeStringLength

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - string : self
 - node_label : node_label
 - node_color : node_color

``` python
def string_length(self, node_label=None, node_color=None):
```
### switch

Switch, false=self, input_type='STRING'

Node
 - class_name : [Switch](/docs/classes/Switch.md)
 - bl_idname : GeometryNodeSwitch

Arguments
 - switch : None
 - true : None
 - node_label : None
 - node_color : None

Node initialization
 - switch : switch
 - false : self
 - true : true
 - input_type : 'STRING'
 - node_label : node_label
 - node_color : node_color

``` python
def switch(self, switch=None, true=None, node_label=None, node_color=None):
```