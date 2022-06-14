
# Data socket Color

> Inherits from dsock.Color
  
<sub>go to [index](/docs/index.md)</sub>



## Constructors

- [Combine](#combine) : image (Color)

## Properties

- [b](#b) : b (Float) = separate.b
- [g](#g) : g (Float) = separate.g
- [r](#r) : r (Float) = separate.r
- [separate](#separate) : Sockets      [r (Float), g (Float), b (Float)]

## Methods

- [add](#add) : color (Color)
- [brighter](#brighter) : result (Boolean)
- [burn](#burn) : color (Color)
- [capture_attribute](#capture_attribute) : Sockets      [geometry (Geometry), attribute (Color)]
- [curves](#curves) : color (Color)
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

## Combine

> Node: [CombineRgb](/docs/nodes/CombineRgb.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeCombineRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineRGB.html)
node ref [Combine RGB](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_rgb.html) </sub>
                          
```python
v = Color.Combine(r, g, b, node_label = None, node_color = None)
```

### Arguments

## Sockets
- r : Float
- g : Float
- b : Float## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.CombineRgb(r=r, g=g, b=b, label=node_label, node_color=node_color)
```

### Returns

Color


## separate

> Node: [SeparateRgb](/docs/nodes/SeparateRgb.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeSeparateRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateRGB.html)
node ref [Separate RGB](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_rgb.html) </sub>
                          
```python
v = color.separate
```

### Arguments

## Sockets
- image : Color (self)## Fixed parameters
- label:f"{self.node_chain_label}.separate"

### Node creation

```python
from geondes import nodes
nodes.SeparateRgb(image=self, label=f"{self.node_chain_label}.separate")
```

### Returns

Sockets [r (Float), g (Float), b (Float)]


## r

> Node: [SeparateRgb](/docs/nodes/SeparateRgb.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeSeparateRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateRGB.html)
node ref [Separate RGB](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_rgb.html) </sub>
                          
```python
v = color.r
```

### Arguments

## Sockets
- image : Color (self)## Fixed parameters
- label:f"{self.node_chain_label}.r"

### Node creation

```python
from geondes import nodes
nodes.SeparateRgb(image=self, label=f"{self.node_chain_label}.r")
```

### Returns

Sockets [r (Float), g (Float), b (Float)]


## g

> Node: [SeparateRgb](/docs/nodes/SeparateRgb.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeSeparateRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateRGB.html)
node ref [Separate RGB](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_rgb.html) </sub>
                          
```python
v = color.g
```

### Arguments

## Sockets
- image : Color (self)## Fixed parameters
- label:f"{self.node_chain_label}.g"

### Node creation

```python
from geondes import nodes
nodes.SeparateRgb(image=self, label=f"{self.node_chain_label}.g")
```

### Returns

Sockets [r (Float), g (Float), b (Float)]


## b

> Node: [SeparateRgb](/docs/nodes/SeparateRgb.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeSeparateRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateRGB.html)
node ref [Separate RGB](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_rgb.html) </sub>
                          
```python
v = color.b
```

### Arguments

## Sockets
- image : Color (self)## Fixed parameters
- label:f"{self.node_chain_label}.b"

### Node creation

```python
from geondes import nodes
nodes.SeparateRgb(image=self, label=f"{self.node_chain_label}.b")
```

### Returns

Sockets [r (Float), g (Float), b (Float)]


## transfer_attribute

> Node: [TransferAttribute](/docs/nodes/TransferAttribute.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [GeometryNodeAttributeTransfer](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeTransfer.html)
node ref [Transfer Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/transfer_attribute.html) </sub>
                          
```python
v = color.transfer_attribute(source, source_position, index, domain, mapping, node_label = None, node_color = None)
```

### Arguments

## Sockets
- attribute : Color (self)
- source : Geometry
- source_position : Vector
- index : Integer## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'FLOAT_COLOR'

### Node creation

```python
from geondes import nodes
nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='FLOAT_COLOR', domain=domain, mapping=mapping, label=node_label, node_color=node_color)
```

### Returns

Color


## capture_attribute

> Node: [CaptureAttribute](/docs/nodes/CaptureAttribute.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [GeometryNodeCaptureAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
node ref [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) </sub>
                          
```python
v = color.capture_attribute(geometry, domain, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value : Color (self)
- geometry : Geometry## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'FLOAT_COLOR'

### Node creation

```python
from geondes import nodes
nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT_COLOR', domain=domain, label=node_label, node_color=node_color)
```

### Returns

Sockets [geometry (Geometry), attribute (Color)]


## field_at_index

> Node: [FieldAtIndex](/docs/nodes/FieldAtIndex.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [GeometryNodeFieldAtIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
node ref [Field at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html) </sub>
                          
```python
v = color.field_at_index(index, domain, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value : Color (self)
- index : Integer## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'FLOAT_COLOR'

### Node creation

```python
from geondes import nodes
nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT_COLOR', domain=domain, label=node_label, node_color=node_color)
```

### Returns

Color


## raycast

> Node: [Raycast](/docs/nodes/Raycast.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [GeometryNodeRaycast](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)
node ref [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) </sub>
                          
```python
v = color.raycast(target_geometry, source_position, ray_direction, ray_length, mapping, node_label = None, node_color = None)
```

### Arguments

## Sockets
- attribute : Color (self)
- target_geometry : Geometry
- source_position : Vector
- ray_direction : Vector
- ray_length : Float## Parameters
- mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'FLOAT_COLOR'

### Node creation

```python
from geondes import nodes
nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_COLOR', mapping=mapping, label=node_label, node_color=node_color)
```

### Returns

Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Color)]


## equal

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>
                          
```python
v = color.equal(b, epsilon, node_label = None, node_color = None)
```

### Arguments

## Sockets
- a : Color (self)
- b : Color
- epsilon : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'RGBA'
- mode : 'ELEMENT'
- operation : 'EQUAL'

### Node creation

```python
from geondes import nodes
nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='EQUAL', label=node_label, node_color=node_color)
```

### Returns

Boolean


## not_equal

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>
                          
```python
v = color.not_equal(b, epsilon, node_label = None, node_color = None)
```

### Arguments

## Sockets
- a : Color (self)
- b : Color
- epsilon : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'RGBA'
- mode : 'ELEMENT'
- operation : 'NOT_EQUAL'

### Node creation

```python
from geondes import nodes
nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='NOT_EQUAL', label=node_label, node_color=node_color)
```

### Returns

Boolean


## brighter

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>
                          
```python
v = color.brighter(b, node_label = None, node_color = None)
```

### Arguments

## Sockets
- a : Color (self)
- b : Color## Parameters
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'RGBA'
- mode : 'ELEMENT'
- operation : 'BRIGHTER'

### Node creation

```python
from geondes import nodes
nodes.Compare(a=self, b=b, data_type='RGBA', mode='ELEMENT', operation='BRIGHTER', label=node_label, node_color=node_color)
```

### Returns

Boolean


## darker

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>
                          
```python
v = color.darker(b, node_label = None, node_color = None)
```

### Arguments

## Sockets
- a : Color (self)
- b : Color## Parameters
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'RGBA'
- mode : 'ELEMENT'
- operation : 'DARKER'

### Node creation

```python
from geondes import nodes
nodes.Compare(a=self, b=b, data_type='RGBA', mode='ELEMENT', operation='DARKER', label=node_label, node_color=node_color)
```

### Returns

Boolean


## mix

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>
                          
```python
v = color.mix(color2, fac, use_alpha, node_label = None, node_color = None)
```

### Arguments

## Sockets
- color1 : Color (self)
- color2 : Color
- fac : Float## Parameters
- use_alpha : False
- node_label : None
- node_color : None## Fixed parameters
- blend_type : 'MIX'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='MIX', use_alpha=use_alpha, label=node_label, node_color=node_color)
```

### Returns

Color


## darken

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>
                          
```python
v = color.darken(color2, fac, use_alpha, node_label = None, node_color = None)
```

### Arguments

## Sockets
- color1 : Color (self)
- color2 : Color
- fac : Float## Parameters
- use_alpha : False
- node_label : None
- node_color : None## Fixed parameters
- blend_type : 'DARKEN'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DARKEN', use_alpha=use_alpha, label=node_label, node_color=node_color)
```

### Returns

Color


## multiply

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>
                          
```python
v = color.multiply(color2, fac, use_alpha, node_label = None, node_color = None)
```

### Arguments

## Sockets
- color1 : Color (self)
- color2 : Color
- fac : Float## Parameters
- use_alpha : False
- node_label : None
- node_color : None## Fixed parameters
- blend_type : 'MULTIPLY'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='MULTIPLY', use_alpha=use_alpha, label=node_label, node_color=node_color)
```

### Returns

Color


## burn

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>
                          
```python
v = color.burn(color2, fac, use_alpha, node_label = None, node_color = None)
```

### Arguments

## Sockets
- color1 : Color (self)
- color2 : Color
- fac : Float## Parameters
- use_alpha : False
- node_label : None
- node_color : None## Fixed parameters
- blend_type : 'BURN'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='BURN', use_alpha=use_alpha, label=node_label, node_color=node_color)
```

### Returns

Color


## lighten

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>
                          
```python
v = color.lighten(color2, fac, use_alpha, node_label = None, node_color = None)
```

### Arguments

## Sockets
- color1 : Color (self)
- color2 : Color
- fac : Float## Parameters
- use_alpha : False
- node_label : None
- node_color : None## Fixed parameters
- blend_type : 'LIGHTEN'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='LIGHTEN', use_alpha=use_alpha, label=node_label, node_color=node_color)
```

### Returns

Color


## screen

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>
                          
```python
v = color.screen(color2, fac, use_alpha, node_label = None, node_color = None)
```

### Arguments

## Sockets
- color1 : Color (self)
- color2 : Color
- fac : Float## Parameters
- use_alpha : False
- node_label : None
- node_color : None## Fixed parameters
- blend_type : 'SCREEN'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SCREEN', use_alpha=use_alpha, label=node_label, node_color=node_color)
```

### Returns

Color


## dodge

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>
                          
```python
v = color.dodge(color2, fac, use_alpha, node_label = None, node_color = None)
```

### Arguments

## Sockets
- color1 : Color (self)
- color2 : Color
- fac : Float## Parameters
- use_alpha : False
- node_label : None
- node_color : None## Fixed parameters
- blend_type : 'DODGE'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DODGE', use_alpha=use_alpha, label=node_label, node_color=node_color)
```

### Returns

Color


## add

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>
                          
```python
v = color.add(color2, fac, use_alpha, node_label = None, node_color = None)
```

### Arguments

## Sockets
- color1 : Color (self)
- color2 : Color
- fac : Float## Parameters
- use_alpha : False
- node_label : None
- node_color : None## Fixed parameters
- blend_type : 'ADD'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='ADD', use_alpha=use_alpha, label=node_label, node_color=node_color)
```

### Returns

Color


## overlay

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>
                          
```python
v = color.overlay(color2, fac, use_alpha, node_label = None, node_color = None)
```

### Arguments

## Sockets
- color1 : Color (self)
- color2 : Color
- fac : Float## Parameters
- use_alpha : False
- node_label : None
- node_color : None## Fixed parameters
- blend_type : 'OVERLAY'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='OVERLAY', use_alpha=use_alpha, label=node_label, node_color=node_color)
```

### Returns

Color


## soft_light

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>
                          
```python
v = color.soft_light(color2, fac, use_alpha, node_label = None, node_color = None)
```

### Arguments

## Sockets
- color1 : Color (self)
- color2 : Color
- fac : Float## Parameters
- use_alpha : False
- node_label : None
- node_color : None## Fixed parameters
- blend_type : 'SOFT_LIGHT'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SOFT_LIGHT', use_alpha=use_alpha, label=node_label, node_color=node_color)
```

### Returns

Color


## linear_light

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>
                          
```python
v = color.linear_light(color2, fac, use_alpha, node_label = None, node_color = None)
```

### Arguments

## Sockets
- color1 : Color (self)
- color2 : Color
- fac : Float## Parameters
- use_alpha : False
- node_label : None
- node_color : None## Fixed parameters
- blend_type : 'LINEAR_LIGHT'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='LINEAR_LIGHT', use_alpha=use_alpha, label=node_label, node_color=node_color)
```

### Returns

Color


## difference

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>
                          
```python
v = color.difference(color2, fac, use_alpha, node_label = None, node_color = None)
```

### Arguments

## Sockets
- color1 : Color (self)
- color2 : Color
- fac : Float## Parameters
- use_alpha : False
- node_label : None
- node_color : None## Fixed parameters
- blend_type : 'DIFFERENCE'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DIFFERENCE', use_alpha=use_alpha, label=node_label, node_color=node_color)
```

### Returns

Color


## subtract

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>
                          
```python
v = color.subtract(color2, fac, use_alpha, node_label = None, node_color = None)
```

### Arguments

## Sockets
- color1 : Color (self)
- color2 : Color
- fac : Float## Parameters
- use_alpha : False
- node_label : None
- node_color : None## Fixed parameters
- blend_type : 'SUBTRACT'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SUBTRACT', use_alpha=use_alpha, label=node_label, node_color=node_color)
```

### Returns

Color


## divide

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>
                          
```python
v = color.divide(color2, fac, use_alpha, node_label = None, node_color = None)
```

### Arguments

## Sockets
- color1 : Color (self)
- color2 : Color
- fac : Float## Parameters
- use_alpha : False
- node_label : None
- node_color : None## Fixed parameters
- blend_type : 'DIVIDE'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DIVIDE', use_alpha=use_alpha, label=node_label, node_color=node_color)
```

### Returns

Color


## hue

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>
                          
```python
v = color.hue(color2, fac, use_alpha, node_label = None, node_color = None)
```

### Arguments

## Sockets
- color1 : Color (self)
- color2 : Color
- fac : Float## Parameters
- use_alpha : False
- node_label : None
- node_color : None## Fixed parameters
- blend_type : 'HUE'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='HUE', use_alpha=use_alpha, label=node_label, node_color=node_color)
```

### Returns

Color


## saturation

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>
                          
```python
v = color.saturation(color2, fac, use_alpha, node_label = None, node_color = None)
```

### Arguments

## Sockets
- color1 : Color (self)
- color2 : Color
- fac : Float## Parameters
- use_alpha : False
- node_label : None
- node_color : None## Fixed parameters
- blend_type : 'SATURATION'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SATURATION', use_alpha=use_alpha, label=node_label, node_color=node_color)
```

### Returns

Color


## mix_color

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>
                          
```python
v = color.mix_color(color2, fac, use_alpha, node_label = None, node_color = None)
```

### Arguments

## Sockets
- color1 : Color (self)
- color2 : Color
- fac : Float## Parameters
- use_alpha : False
- node_label : None
- node_color : None## Fixed parameters
- blend_type : 'COLOR'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='COLOR', use_alpha=use_alpha, label=node_label, node_color=node_color)
```

### Returns

Color


## value

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>
                          
```python
v = color.value(color2, fac, use_alpha, node_label = None, node_color = None)
```

### Arguments

## Sockets
- color1 : Color (self)
- color2 : Color
- fac : Float## Parameters
- use_alpha : False
- node_label : None
- node_color : None## Fixed parameters
- blend_type : 'VALUE'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='VALUE', use_alpha=use_alpha, label=node_label, node_color=node_color)
```

### Returns

Color


## curves

> Node: [RgbCurves](/docs/nodes/RgbCurves.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeRGBCurve](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBCurve.html)
node ref [RGB Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/rgb_curves.html) </sub>
                          
```python
v = color.curves(fac, node_label = None, node_color = None)
```

### Arguments

## Sockets
- color : Color (self)
- fac : Float## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.RgbCurves(color=self, fac=fac, label=node_label, node_color=node_color)
```

### Returns

Color


## mix

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-color) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>
                          
```python
v = color.mix(color2, fac, blend_type, use_alpha, node_label = None, node_color = None)
```

### Arguments

## Sockets
- color1 : Color (self)
- color2 : Color
- fac : Float## Parameters
- blend_type : 'MIX' in [MIX, DARKEN, MULTIPLY, BURN, LIGHTEN,... , SATURATION, COLOR, VALUE]
- use_alpha : False
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=self, color2=color2, fac=fac, blend_type=blend_type, use_alpha=use_alpha, label=node_label, node_color=node_color)
```

### Returns

Color

