
# Class Color

> Inherits from: ***dsock.Color***

## Constructors



- [Combine](#combine) : image (Color)



## Properties



- [separate](#separate) : Sockets      [r (Float), g (Float), b (Float)]



## Methods



- [add](#add) : color (Color)
- [brighter](#brighter) : result (Boolean)
- [burn](#burn) : color (Color)
- [capture_attribute](#capture_attribute) : Sockets      [geometry (Geometry), attribute (Color)]
- [darken](#darken) : color (Color)
- [darker](#darker) : result (Boolean)
- [difference](#difference) : color (Color)
- [divide](#divide) : color (Color)
- [dodge](#dodge) : color (Color)
- [equal](#equal) : result (Boolean)
- [field_at_index](#field_at_index) : value (Color)
- [hue](#hue) : color (Color)
- [lighten](#lighten) : color (Color)
- [linear_light](#linear_light) : color (Color)
- [mix](#mix) : color (Color)
- [mix](#mix) : color (Color)
- [mix_color](#mix_color) : color (Color)
- [multiply](#multiply) : color (Color)
- [not_equal](#not_equal) : result (Boolean)
- [overlay](#overlay) : color (Color)
- [raycast](#raycast) : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Color)]
- [saturation](#saturation) : color (Color)
- [screen](#screen) : color (Color)
- [soft_light](#soft_light) : color (Color)
- [subtract](#subtract) : color (Color)
- [transfer_attribute](#transfer_attribute) : attribute (Color)
- [value](#value) : color (Color)



## Stacked methods



- [curves](#curves) : Color



## Methods


### Combine

> Node: [CombineRgb](../nodes/{self.node_name}.md)

```python
v = Color.Combine(r, g, b)
```


#### Arguments


##### Sockets arguments



- r : Float
- g : Float
- b : Float



#### Returns

    Color

### add

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = color.add(color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color (self)
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'ADD'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### brighter

> Node: [Compare](../nodes/{self.node_name}.md)

```python
v = color.brighter(b)
```


#### Arguments


##### Sockets arguments



- a : Color (self)
- b : Color



##### Fixed parameters



- data_type : 'RGBA'
- mode : 'ELEMENT'
- operation : 'BRIGHTER'



#### Returns

    Boolean

### burn

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = color.burn(color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color (self)
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'BURN'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### capture_attribute

> Node: [CaptureAttribute](../nodes/{self.node_name}.md)

```python
v = color.capture_attribute(geometry, domain)
```


#### Arguments


##### Sockets arguments



- value : Color (self)
- geometry : Geometry



##### Fixed parameters



- data_type : 'FLOAT_COLOR'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]



#### Returns

    Sockets [geometry (Geometry), attribute (Color)]

### curves

> Node: [RgbCurves](../nodes/{self.node_name}.md)

```python
color.curves(fac)
```


#### Arguments


##### Sockets arguments



- color : Color (self)
- fac : Float



#### Returns

    self

### darken

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = color.darken(color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color (self)
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'DARKEN'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### darker

> Node: [Compare](../nodes/{self.node_name}.md)

```python
v = color.darker(b)
```


#### Arguments


##### Sockets arguments



- a : Color (self)
- b : Color



##### Fixed parameters



- data_type : 'RGBA'
- mode : 'ELEMENT'
- operation : 'DARKER'



#### Returns

    Boolean

### difference

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = color.difference(color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color (self)
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'DIFFERENCE'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### divide

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = color.divide(color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color (self)
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'DIVIDE'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### dodge

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = color.dodge(color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color (self)
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'DODGE'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### equal

> Node: [Compare](../nodes/{self.node_name}.md)

```python
v = color.equal(b, epsilon)
```


#### Arguments


##### Sockets arguments



- a : Color (self)
- b : Color
- epsilon : Float



##### Fixed parameters



- data_type : 'RGBA'
- mode : 'ELEMENT'
- operation : 'EQUAL'



#### Returns

    Boolean

### field_at_index

> Node: [FieldAtIndex](../nodes/{self.node_name}.md)

```python
v = color.field_at_index(index, domain)
```


#### Arguments


##### Sockets arguments



- value : Color (self)
- index : Integer



##### Fixed parameters



- data_type : 'FLOAT_COLOR'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]



#### Returns

    Color

### hue

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = color.hue(color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color (self)
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'HUE'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### lighten

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = color.lighten(color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color (self)
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'LIGHTEN'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### linear_light

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = color.linear_light(color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color (self)
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'LINEAR_LIGHT'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### mix

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = color.mix(color2, fac, blend_type, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color (self)
- color2 : Color
- fac : Float



##### Parameters arguments



- blend_type : 'MIX' in [MIX, DARKEN, MULTIPLY, BURN, LIGHTEN,... , SATURATION, COLOR, VALUE]
- use_alpha : False



#### Returns

    Color

### mix_color

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = color.mix_color(color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color (self)
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'COLOR'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### multiply

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = color.multiply(color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color (self)
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'MULTIPLY'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### not_equal

> Node: [Compare](../nodes/{self.node_name}.md)

```python
v = color.not_equal(b, epsilon)
```


#### Arguments


##### Sockets arguments



- a : Color (self)
- b : Color
- epsilon : Float



##### Fixed parameters



- data_type : 'RGBA'
- mode : 'ELEMENT'
- operation : 'NOT_EQUAL'



#### Returns

    Boolean

### overlay

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = color.overlay(color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color (self)
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'OVERLAY'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### raycast

> Node: [Raycast](../nodes/{self.node_name}.md)

```python
v = color.raycast(target_geometry, source_position, ray_direction, ray_length, mapping)
```


#### Arguments


##### Sockets arguments



- attribute : Color (self)
- target_geometry : Geometry
- source_position : Vector
- ray_direction : Vector
- ray_length : Float



##### Fixed parameters



- data_type : 'FLOAT_COLOR'



##### Parameters arguments



- mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST]



#### Returns

    Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Color)]

### saturation

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = color.saturation(color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color (self)
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'SATURATION'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### screen

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = color.screen(color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color (self)
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'SCREEN'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### separate

> Node: [SeparateRgb](../nodes/{self.node_name}.md)

```python
v = color.separate
```


#### Arguments


##### Sockets arguments



- image : Color (self)



##### Fixed parameters



- label:f"{self.node_chain_label}.separate"



#### Returns

    Sockets [r (Float), g (Float), b (Float)]

### soft_light

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = color.soft_light(color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color (self)
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'SOFT_LIGHT'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### subtract

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = color.subtract(color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color (self)
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'SUBTRACT'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### transfer_attribute

> Node: [TransferAttribute](../nodes/{self.node_name}.md)

```python
v = color.transfer_attribute(source, source_position, index, domain, mapping)
```


#### Arguments


##### Sockets arguments



- attribute : Color (self)
- source : Geometry
- source_position : Vector
- index : Integer



##### Fixed parameters



- data_type : 'FLOAT_COLOR'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]



#### Returns

    Color

### value

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = color.value(color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color (self)
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'VALUE'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color
