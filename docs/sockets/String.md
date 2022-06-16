
# Data socket String

> Inherits from dsock.String
  
<sub>go to [index](/docs/index.md)</sub>



## Properties

- [length](#length) : length (Integer)

## Methods

- [average](#average) : result (Boolean)
- [direction](#direction) : result (Boolean)
- [dot_product](#dot_product) : result (Boolean)
- [element](#element) : result (Boolean)
- [join](#join) : string (String)
- [length](#length) : result (Boolean)
- [replace](#replace) : string (String)
- [slice](#slice) : string (String)
- [switch](#switch) : output (String)
- [to_curves](#to_curves) : Sockets      [curve_instances (Geometry), remainder (String), line (Integer), pivot_point (Vector)]

## length

> Node: [StringLength](/docs/nodes/StringLength.md)
  
<sub>go to: [top](#data-socket-string) [index](/docs/index.md)
blender ref [FunctionNodeStringLength](https://docs.blender.org/api/current/bpy.types.FunctionNodeStringLength.html)
node ref [String Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/string_length.html) </sub>
                          
```python
v = string.length
```

### Arguments

## Sockets
- string : String (self)## Fixed parameters
- label:f"{self.node_chain_label}.length"

### Node creation

```python
from geondes import nodes
nodes.StringLength(string=self, label=f"{self.node_chain_label}.length")
```

### Returns

Integer


## switch

> Node: [Switch](/docs/nodes/Switch.md)
  
<sub>go to: [top](#data-socket-string) [index](/docs/index.md)
blender ref [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
node ref [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) </sub>
                          
```python
v = string.switch(switch, true, node_label = None, node_color = None)
```

### Arguments

## Sockets
- false : String (self)
- switch : Boolean
- true : String## Parameters
- node_label : None
- node_color : None## Fixed parameters
- input_type : 'STRING'

### Node creation

```python
from geondes import nodes
nodes.Switch(false=self, switch=switch, true=true, input_type='STRING', label=node_label, node_color=node_color)
```

### Returns

String


## element

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-string) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>
                          
```python
v = string.element(b, node_label = None, node_color = None)
```

### Arguments

## Sockets
- a : String (self)
- b : String## Parameters
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'STRING'
- mode : 'ELEMENT'
- operation : 'ELEMENT'

### Node creation

```python
from geondes import nodes
nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='ELEMENT', label=node_label, node_color=node_color)
```

### Returns

Boolean


## length

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-string) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>
                          
```python
v = string.length(b, node_label = None, node_color = None)
```

### Arguments

## Sockets
- a : String (self)
- b : String## Parameters
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'STRING'
- mode : 'ELEMENT'
- operation : 'LENGTH'

### Node creation

```python
from geondes import nodes
nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='LENGTH', label=node_label, node_color=node_color)
```

### Returns

Boolean


## average

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-string) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>
                          
```python
v = string.average(b, node_label = None, node_color = None)
```

### Arguments

## Sockets
- a : String (self)
- b : String## Parameters
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'STRING'
- mode : 'ELEMENT'
- operation : 'AVERAGE'

### Node creation

```python
from geondes import nodes
nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='AVERAGE', label=node_label, node_color=node_color)
```

### Returns

Boolean


## dot_product

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-string) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>
                          
```python
v = string.dot_product(b, node_label = None, node_color = None)
```

### Arguments

## Sockets
- a : String (self)
- b : String## Parameters
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'STRING'
- mode : 'ELEMENT'
- operation : 'DOT_PRODUCT'

### Node creation

```python
from geondes import nodes
nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='DOT_PRODUCT', label=node_label, node_color=node_color)
```

### Returns

Boolean


## direction

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-string) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>
                          
```python
v = string.direction(b, node_label = None, node_color = None)
```

### Arguments

## Sockets
- a : String (self)
- b : String## Parameters
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'STRING'
- mode : 'ELEMENT'
- operation : 'DIRECTION'

### Node creation

```python
from geondes import nodes
nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='DIRECTION', label=node_label, node_color=node_color)
```

### Returns

Boolean


## join

> Node: [JoinStrings](/docs/nodes/JoinStrings.md)
  
<sub>go to: [top](#data-socket-string) [index](/docs/index.md)
blender ref [GeometryNodeStringJoin](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringJoin.html)
node ref [Join Strings](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/join_strings.html) </sub>
                          
```python
v = string.join(strings_1, strings_2, strings_3, delimiter, node_label = None, node_color = None)
```

### Arguments

## Sockets
- strings : *String (self)
- delimiter : String## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.JoinStrings(self, *strings, delimiter=delimiter, label=node_label, node_color=node_color)
```

### Returns

String


## replace

> Node: [ReplaceString](/docs/nodes/ReplaceString.md)
  
<sub>go to: [top](#data-socket-string) [index](/docs/index.md)
blender ref [FunctionNodeReplaceString](https://docs.blender.org/api/current/bpy.types.FunctionNodeReplaceString.html)
node ref [Replace String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/replace_string.html) </sub>
                          
```python
v = string.replace(find, replace, node_label = None, node_color = None)
```

### Arguments

## Sockets
- string : String (self)
- find : String
- replace : String## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.ReplaceString(string=self, find=find, replace=replace, label=node_label, node_color=node_color)
```

### Returns

String


## slice

> Node: [SliceString](/docs/nodes/SliceString.md)
  
<sub>go to: [top](#data-socket-string) [index](/docs/index.md)
blender ref [FunctionNodeSliceString](https://docs.blender.org/api/current/bpy.types.FunctionNodeSliceString.html)
node ref [Slice String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/slice_string.html) </sub>
                          
```python
v = string.slice(position, length, node_label = None, node_color = None)
```

### Arguments

## Sockets
- string : String (self)
- position : Integer
- length : Integer## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.SliceString(string=self, position=position, length=length, label=node_label, node_color=node_color)
```

### Returns

String


## to_curves

> Node: [StringToCurves](/docs/nodes/StringToCurves.md)
  
<sub>go to: [top](#data-socket-string) [index](/docs/index.md)
blender ref [GeometryNodeStringToCurves](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringToCurves.html)
node ref [String to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/string_to_curves.html) </sub>
                          
```python
v = string.to_curves(size, character_spacing, word_spacing, line_spacing, text_box_width, text_box_height, align_x, align_y, overflow, pivot_mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- string : String (self)
- size : Float
- character_spacing : Float
- word_spacing : Float
- line_spacing : Float
- text_box_width : Float
- text_box_height : Float## Parameters
- align_x : 'LEFT' in [LEFT, CENTER, RIGHT, JUSTIFY, FLUSH]
- align_y : 'TOP_BASELINE' in [TOP_BASELINE, TOP, MIDDLE, BOTTOM_BASELINE, BOTTOM]
- overflow : 'OVERFLOW' in [OVERFLOW, SCALE_TO_FIT, TRUNCATE]
- pivot_mode : 'BOTTOM_LEFT' in [MIDPOINT, TOP_LEFT, TOP_CENTER,... , BOTTOM_LEFT, BOTTOM_CENTER, BOTTOM_RIGHT]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.StringToCurves(string=self, size=size, character_spacing=character_spacing, word_spacing=word_spacing, line_spacing=line_spacing, text_box_width=text_box_width, text_box_height=text_box_height, align_x=align_x, align_y=align_y, overflow=overflow, pivot_mode=pivot_mode, label=node_label, node_color=node_color)
```

### Returns

Sockets [curve_instances (Geometry), remainder (String), line (Integer), pivot_point (Vector)]

