# class SampleIndex (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : SampleIndex
 - bl_idname : GeometryNodeSampleIndex

Node parameters
 - clamp : False
 - data_type : 'FLOAT'
 - domain : 'POINT'

Input sockets
 - geometry : Geometry
 - value : Float
 - value_1 : Int
 - value_2 : Vect
 - value_3 : Col
 - value_4 : Bool
 - value_5 : Rot
 - index : Int

Output sockets
 - value : Float
 - value_1 : Int
 - value_2 : Vect
 - value_3 : Col
 - value_4 : Bool
 - value_5 : Rot

### Header

``` python
def SampleIndex(self, geometry=None, value=None, index=None, clamp=False, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):
```

## Implementations

o functions : [sample_index](#sample_index)
o Float : [sample_index](#sample_index) 
o Int : [sample_index](#sample_index) 
o Geometry : [sample_index_float](#sample_index_float) [sample_index_int](#sample_index_int) [sample_index_vector](#sample_index_vector) [sample_index_color](#sample_index_color) [sample_index_boolean](#sample_index_boolean) [sample_index_quaternion](#sample_index_quaternion) 
o Domain : [sample_index_float](#sample_index_float) [sample_index_int](#sample_index_int) [sample_index_vector](#sample_index_vector) [sample_index_color](#sample_index_color) [sample_index_boolean](#sample_index_boolean) [sample_index_quaternion](#sample_index_quaternion) 

