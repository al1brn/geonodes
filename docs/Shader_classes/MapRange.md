# class MapRange (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : MapRange
 - bl_idname : ShaderNodeMapRange

Node parameters
 - clamp : True
 - data_type : 'FLOAT'
 - interpolation_type : 'LINEAR'

Input sockets
 - value : Float
 - from_min : Float
 - from_max : Float
 - to_min : Float
 - to_max : Float
 - steps : Float
 - vector : Vect
 - from_min_1 : Vect
 - from_max_1 : Vect
 - to_min_1 : Vect
 - to_max_1 : Vect
 - steps_1 : Vect

Output sockets
 - result : Float
 - vector : Vect

### Header

``` python
def MapRange(self, value=None, from_min=None, from_max=None, to_min=None, to_max=None, vector=None, steps=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR', node_label=None, node_color=None):
```

## Implementations

o Float : [map_range](/docs/Shader_classes/Float.md#map_range) 

