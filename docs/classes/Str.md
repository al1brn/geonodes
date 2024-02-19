# class Str (Socket)

<sub>go to [index](/docs/index.md)</sub>

Socket
------
 - Type : STRING
 - bl_idname : NodeSocketString

Methods
-------
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
----
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

### join_strings

JoinStrings, delimiter=self

Node
----
 - class_name : [JoinStrings](/docs/classes/JoinStrings.md)
 - bl_idname : GeometryNodeStringJoin

### named_attribute

NamedAttribute, name=self, return node

Node
----
 - class_name : [NamedAttribute](/docs/classes/NamedAttribute.md)
 - bl_idname : GeometryNodeInputNamedAttribute

### not_equal

Compare, a=self, data_type='STRING', operation='NOT_EQUAL'

Node
----
 - class_name : [Compare](/docs/classes/Compare.md)
 - bl_idname : FunctionNodeCompare

### replace_string

ReplaceString, string=self

Node
----
 - class_name : [ReplaceString](/docs/classes/ReplaceString.md)
 - bl_idname : FunctionNodeReplaceString

### slice_string

SliceString, string=self

Node
----
 - class_name : [SliceString](/docs/classes/SliceString.md)
 - bl_idname : FunctionNodeSliceString

### string_length

StringLength, string=self, return socket

Node
----
 - class_name : [StringLength](/docs/classes/StringLength.md)
 - bl_idname : FunctionNodeStringLength

### switch

Switch, false=self, input_type='STRING'

Node
----
 - class_name : [Switch](/docs/classes/Switch.md)
 - bl_idname : GeometryNodeSwitch
