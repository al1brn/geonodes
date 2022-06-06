
# Class String

> Inherits from: ***dsock.String***


[Index](/docs/index.md)

## Properties



- [**length**](#length) : [StringLength](../nodes/StringLength.md) length (Integer)



## Methods



- [**average**](#average) : [Compare](../nodes/Compare.md) result (Boolean)
- [**direction**](#direction) : [Compare](../nodes/Compare.md) result (Boolean)
- [**dot_product**](#dot_product) : [Compare](../nodes/Compare.md) result (Boolean)
- [**element**](#element) : [Compare](../nodes/Compare.md) result (Boolean)
- [**join**](#join) : [JoinStrings](../nodes/JoinStrings.md) string (String)
- [**length**](#length) : [Compare](../nodes/Compare.md) result (Boolean)
- [**replace**](#replace) : [ReplaceString](../nodes/ReplaceString.md) string (String)
- [**slice**](#slice) : [SliceString](../nodes/SliceString.md) string (String)
- [**switch**](#switch) : [Switch](../nodes/Switch.md) output (String)
- [**to_curves**](#to_curves) : [StringToCurves](../nodes/StringToCurves.md) Sockets      [curve_instances (Geometry), remainder (String), line (Integer), pivot_point (Vector)]



## Methods reference


### average

> Node: [Compare](../nodes/{self.node_name}.md)


[Top](#class-string) [Index](/docs/index.md)

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



#### Node creation


```python
node = nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='AVERAGE')
```


#### Returns

    Boolean

### direction

> Node: [Compare](../nodes/{self.node_name}.md)


[Top](#class-string) [Index](/docs/index.md)

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



#### Node creation


```python
node = nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='DIRECTION')
```


#### Returns

    Boolean

### dot_product

> Node: [Compare](../nodes/{self.node_name}.md)


[Top](#class-string) [Index](/docs/index.md)

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



#### Node creation


```python
node = nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='DOT_PRODUCT')
```


#### Returns

    Boolean

### element

> Node: [Compare](../nodes/{self.node_name}.md)


[Top](#class-string) [Index](/docs/index.md)

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



#### Node creation


```python
node = nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='ELEMENT')
```


#### Returns

    Boolean

### join

> Node: [JoinStrings](../nodes/{self.node_name}.md)


[Top](#class-string) [Index](/docs/index.md)

```python
v = string.join(strings_1, strings_2, strings_3, delimiter)
```


#### Arguments


##### Sockets arguments



- strings : *String (self)
- delimiter : String



#### Node creation


```python
node = nodes.JoinStrings(self, *strings, delimiter=delimiter)
```


#### Returns

    String

### length

> Node: [Compare](../nodes/{self.node_name}.md)


[Top](#class-string) [Index](/docs/index.md)

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



#### Node creation


```python
node = nodes.Compare(a=self, b=b, data_type='STRING', mode='ELEMENT', operation='LENGTH')
```


#### Returns

    Boolean

### replace

> Node: [ReplaceString](../nodes/{self.node_name}.md)


[Top](#class-string) [Index](/docs/index.md)

```python
v = string.replace(find, replace)
```


#### Arguments


##### Sockets arguments



- string : String (self)
- find : String
- replace : String



#### Node creation


```python
node = nodes.ReplaceString(string=self, find=find, replace=replace)
```


#### Returns

    String

### slice

> Node: [SliceString](../nodes/{self.node_name}.md)


[Top](#class-string) [Index](/docs/index.md)

```python
v = string.slice(position, length)
```


#### Arguments


##### Sockets arguments



- string : String (self)
- position : Integer
- length : Integer



#### Node creation


```python
node = nodes.SliceString(string=self, position=position, length=length)
```


#### Returns

    String

### switch

> Node: [Switch](../nodes/{self.node_name}.md)


[Top](#class-string) [Index](/docs/index.md)

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



#### Node creation


```python
node = nodes.Switch(false=self, switch0=switch0, true=true, input_type='STRING')
```


#### Returns

    String

### to_curves

> Node: [StringToCurves](../nodes/{self.node_name}.md)


[Top](#class-string) [Index](/docs/index.md)

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



#### Node creation


```python
node = nodes.StringToCurves(string=self, size=size, character_spacing=character_spacing, word_spacing=word_spacing, line_spacing=line_spacing, text_box_width=text_box_width, text_box_height=text_box_height, align_x=align_x, align_y=align_y, overflow=overflow, pivot_mode=pivot_mode)
```


#### Returns

    Sockets [curve_instances (Geometry), remainder (String), line (Integer), pivot_point (Vector)]
