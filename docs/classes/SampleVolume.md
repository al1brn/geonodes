# class SampleVolume (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : SampleVolume
 - bl_idname : GeometryNodeSampleVolume

Node parameters
 - grid_type : 'FLOAT'
 - interpolation_mode : 'TRILINEAR'

Input sockets
 - volume : Geometry
 - grid : Vect
 - grid_1 : Float
 - grid_2 : Bool
 - grid_3 : Int
 - position : Vect

Output sockets
 - value : Vect
 - value_1 : Float
 - value_2 : Bool
 - value_3 : Int

### Header

``` python
def SampleVolume(self, volume=None, grid=None, position=None, grid_type='FLOAT', interpolation_mode='TRILINEAR', node_label=None, node_color=None):
```

## Implementations

o functions : [sample_volume](#sample_volume)
o Float : [sample_volume](#sample_volume) 
o Int : [sample_volume](#sample_volume) 

