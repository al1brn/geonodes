
# Class String

> Inherits from: ***dsock.String***

## Properties



- [length](#length) : length (Integer)



## Methods



- [average](#average) : result (Boolean)
- [direction](#direction) : result (Boolean)
- [dot_product](#dot_product) : result (Boolean)
- [element](#element) : result (Boolean)
- [join](#join) : string (String)
- [length](#length) : result (Boolean)
- [slice](#slice) : string (String)
- [switch](#switch) : output (String)
- [to_curves](#to_curves) : Sockets      [curve_instances (Geometry), remainder (String), line (Integer), pivot_point (Vector)]



## Stacked methods



- [replace](#replace) : String



## Methods


### average

> Node: [Compare](../nodes/{self.node_name}.md)

```python
v = string.average(b)
```


#### Arguments


##### Sockets arguments



- a : String (self)
- b : String



##### Fixed parameters



- data_type : 'STRING'
- mode : 'ELEMENT'
- operation : 'AVERAGE'



#### Returns

    Boolean

### direction

> Node: [Compare](../nodes/{self.node_name}.md)

```python
v = string.direction(b)
```


#### Arguments


##### Sockets arguments



- a : String (self)
- b : String



##### Fixed parameters



- data_type : 'STRING'
- mode : 'ELEMENT'
- operation : 'DIRECTION'



#### Returns

    Boolean

### dot_product

> Node: [Compare](../nodes/{self.node_name}.md)

```python
v = string.dot_product(b)
```


#### Arguments


##### Sockets arguments



- a : String (self)
- b : String



##### Fixed parameters



- data_type : 'STRING'
- mode : 'ELEMENT'
- operation : 'DOT_PRODUCT'



#### Returns

    Boolean

### element

> Node: [Compare](../nodes/{self.node_name}.md)

```python
v = string.element(b)
```


#### Arguments


##### Sockets arguments



- a : String (self)
- b : String



##### Fixed parameters



- data_type : 'STRING'
- mode : 'ELEMENT'
- operation : 'ELEMENT'



#### Returns

    Boolean

### join

> Node: [JoinStrings](../nodes/{self.node_name}.md)

```python
v = string.join(strings_1, strings_2, strings_3, delimiter)
```


#### Arguments


##### Sockets arguments



- strings : *String (self)
- delimiter : String



#### Returns

    String

### length

> Node: [Compare](../nodes/{self.node_name}.md)

```python
v = string.length(b)
```


#### Arguments


##### Sockets arguments



- a : String (self)
- b : String



##### Fixed parameters



- data_type : 'STRING'
- mode : 'ELEMENT'
- operation : 'LENGTH'



#### Returns

    Boolean

### replace

> Node: [ReplaceString](../nodes/{self.node_name}.md)

```python
string.replace(find, replace)
```


#### Arguments


##### Sockets arguments



- string : String (self)
- find : String
- replace : String



#### Returns

    self

### slice

> Node: [SliceString](../nodes/{self.node_name}.md)

```python
v = string.slice(position, length)
```


#### Arguments


##### Sockets arguments



- string : String (self)
- position : Integer
- length : Integer



#### Returns

    String

### switch

> Node: [Switch](../nodes/{self.node_name}.md)

```python
v = string.switch(switch0, true)
```


#### Arguments


##### Sockets arguments



- false : String (self)
- switch0 : Boolean
- true : String



##### Fixed parameters



- input_type : 'STRING'



#### Returns

    String

### to_curves

> Node: [StringToCurves](../nodes/{self.node_name}.md)

```python
v = string.to_curves(size, character_spacing, word_spacing, line_spacing, text_box_width, text_box_height, align_x, align_y, overflow, pivot_mode)
```


#### Arguments


##### Sockets arguments



- string : String (self)
- size : Float
- character_spacing : Float
- word_spacing : Float
- line_spacing : Float
- text_box_width : Float
- text_box_height : Float



##### Parameters arguments



- align_x : 'LEFT' in [LEFT, CENTER, RIGHT, JUSTIFY, FLUSH]
- align_y : 'TOP_BASELINE' in [TOP_BASELINE, TOP, MIDDLE, BOTTOM_BASELINE, BOTTOM]
- overflow : 'OVERFLOW' in [OVERFLOW, SCALE_TO_FIT, TRUNCATE]
- pivot_mode : 'BOTTOM_LEFT' in [MIDPOINT, TOP_LEFT, TOP_CENTER,... , BOTTOM_LEFT, BOTTOM_CENTER, BOTTOM_RIGHT]



#### Returns

    Sockets [curve_instances (Geometry), remainder (String), line (Integer), pivot_point (Vector)]
