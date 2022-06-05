
# Class Color

> Inherits from: ***dsock.Color***

## Constructors



- [**self.meth_name**](#combine) : [CombineRgb](../nodes/CombineRgb.md) image (Color)



## Properties



- [**self.meth_name**](#separate) : [SeparateRgb](../nodes/SeparateRgb.md) Sockets      [r (Float), g (Float), b (Float)]



## Methods



- [**self.meth_name**](#add) : [Mix](../nodes/Mix.md) color (Color)
- [**self.meth_name**](#brighter) : [Compare](../nodes/Compare.md) result (Boolean)
- [**self.meth_name**](#burn) : [Mix](../nodes/Mix.md) color (Color)
- [**self.meth_name**](#capture_attribute) : [CaptureAttribute](../nodes/CaptureAttribute.md) Sockets      [geometry (Geometry), attribute (Color)]
- [**self.meth_name**](#darken) : [Mix](../nodes/Mix.md) color (Color)
- [**self.meth_name**](#darker) : [Compare](../nodes/Compare.md) result (Boolean)
- [**self.meth_name**](#difference) : [Mix](../nodes/Mix.md) color (Color)
- [**self.meth_name**](#divide) : [Mix](../nodes/Mix.md) color (Color)
- [**self.meth_name**](#dodge) : [Mix](../nodes/Mix.md) color (Color)
- [**self.meth_name**](#equal) : [Compare](../nodes/Compare.md) result (Boolean)
- [**self.meth_name**](#field_at_index) : [FieldAtIndex](../nodes/FieldAtIndex.md) value (Color)
- [**self.meth_name**](#hue) : [Mix](../nodes/Mix.md) color (Color)
- [**self.meth_name**](#lighten) : [Mix](../nodes/Mix.md) color (Color)
- [**self.meth_name**](#linear_light) : [Mix](../nodes/Mix.md) color (Color)
- [**self.meth_name**](#mix) : [Mix](../nodes/Mix.md) color (Color)
- [**self.meth_name**](#mix) : [Mix](../nodes/Mix.md) color (Color)
- [**self.meth_name**](#mix_color) : [Mix](../nodes/Mix.md) color (Color)
- [**self.meth_name**](#multiply) : [Mix](../nodes/Mix.md) color (Color)
- [**self.meth_name**](#not_equal) : [Compare](../nodes/Compare.md) result (Boolean)
- [**self.meth_name**](#overlay) : [Mix](../nodes/Mix.md) color (Color)
- [**self.meth_name**](#raycast) : [Raycast](../nodes/Raycast.md) Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Color)]
- [**self.meth_name**](#saturation) : [Mix](../nodes/Mix.md) color (Color)
- [**self.meth_name**](#screen) : [Mix](../nodes/Mix.md) color (Color)
- [**self.meth_name**](#soft_light) : [Mix](../nodes/Mix.md) color (Color)
- [**self.meth_name**](#subtract) : [Mix](../nodes/Mix.md) color (Color)
- [**self.meth_name**](#transfer_attribute) : [TransferAttribute](../nodes/TransferAttribute.md) attribute (Color)
- [**self.meth_name**](#value) : [Mix](../nodes/Mix.md) color (Color)



## Stacked methods



- [**self.meth_name**](#curves) : [RgbCurves](../nodes/RgbCurves.md) Color



## Methods reference


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



#### Node creation


```python
node = nodes.CombineRgb(r=r, g=g, b=b)
```


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



#### Node creation


```python
node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='ADD', use_alpha=use_alpha)
```


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



#### Node creation


```python
node = nodes.Compare(a=self, b=b, data_type='RGBA', mode='ELEMENT', operation='BRIGHTER')
```


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



#### Node creation


```python
node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='BURN', use_alpha=use_alpha)
```


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



#### Node creation


```python
node = nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT_COLOR', domain=domain)
```


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



#### Node creation


```python
node = nodes.RgbCurves(color=self, fac=fac)
```


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



#### Node creation


```python
node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DARKEN', use_alpha=use_alpha)
```


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



#### Node creation


```python
node = nodes.Compare(a=self, b=b, data_type='RGBA', mode='ELEMENT', operation='DARKER')
```


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



#### Node creation


```python
node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DIFFERENCE', use_alpha=use_alpha)
```


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



#### Node creation


```python
node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DIVIDE', use_alpha=use_alpha)
```


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



#### Node creation


```python
node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DODGE', use_alpha=use_alpha)
```


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



#### Node creation


```python
node = nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='EQUAL')
```


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



#### Node creation


```python
node = nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT_COLOR', domain=domain)
```


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



#### Node creation


```python
node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='HUE', use_alpha=use_alpha)
```


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



#### Node creation


```python
node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='LIGHTEN', use_alpha=use_alpha)
```


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



#### Node creation


```python
node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='LINEAR_LIGHT', use_alpha=use_alpha)
```


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



#### Node creation


```python
node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type=blend_type, use_alpha=use_alpha)
```


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



#### Node creation


```python
node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='COLOR', use_alpha=use_alpha)
```


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



#### Node creation


```python
node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='MULTIPLY', use_alpha=use_alpha)
```


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



#### Node creation


```python
node = nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='NOT_EQUAL')
```


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



#### Node creation


```python
node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='OVERLAY', use_alpha=use_alpha)
```


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



#### Node creation


```python
node = nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_COLOR', mapping=mapping)
```


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



#### Node creation


```python
node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SATURATION', use_alpha=use_alpha)
```


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



#### Node creation


```python
node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SCREEN', use_alpha=use_alpha)
```


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



#### Node creation


```python
node = nodes.SeparateRgb(image=self, label=f"{self.node_chain_label}.separate")
```


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



#### Node creation


```python
node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SOFT_LIGHT', use_alpha=use_alpha)
```


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



#### Node creation


```python
node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SUBTRACT', use_alpha=use_alpha)
```


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



#### Node creation


```python
node = nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='FLOAT_COLOR', domain=domain, mapping=mapping)
```


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



#### Node creation


```python
node = nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='VALUE', use_alpha=use_alpha)
```


#### Returns

    Color
