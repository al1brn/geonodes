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

o functions : [sample_index](/docs/GeoNodes_classes/sample_index.md)
o Float : [sample_index](/docs/GeoNodes_classes/sample_index.md) 
o Int : [sample_index](/docs/GeoNodes_classes/sample_index.md) 
o Geometry : [sample_index_float](/docs/GeoNodes_classes/sample_index_float.md) [sample_index_int](/docs/GeoNodes_classes/sample_index_int.md) [sample_index_vector](/docs/GeoNodes_classes/sample_index_vector.md) [sample_index_color](/docs/GeoNodes_classes/sample_index_color.md) [sample_index_boolean](/docs/GeoNodes_classes/sample_index_boolean.md) [sample_index_quaternion](/docs/GeoNodes_classes/sample_index_quaternion.md) 
o Domain : [sample_index_float](/docs/GeoNodes_classes/sample_index_float.md) [sample_index_int](/docs/GeoNodes_classes/sample_index_int.md) [sample_index_vector](/docs/GeoNodes_classes/sample_index_vector.md) [sample_index_color](/docs/GeoNodes_classes/sample_index_color.md) [sample_index_boolean](/docs/GeoNodes_classes/sample_index_boolean.md) [sample_index_quaternion](/docs/GeoNodes_classes/sample_index_quaternion.md) 
