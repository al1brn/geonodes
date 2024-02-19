# class SampleUVSurface (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : SampleUVSurface
 - bl_idname : GeometryNodeSampleUVSurface

Node parameters
 - data_type : 'FLOAT'

Input sockets
 - mesh : Geometry
 - value : Float
 - value_1 : Int
 - value_2 : Vect
 - value_3 : Col
 - value_4 : Bool
 - value_5 : Rot
 - source_uv_map : Vect
 - sample_uv : Vect

Output sockets
 - value : Float
 - value_1 : Int
 - value_2 : Vect
 - value_3 : Col
 - value_4 : Bool
 - value_5 : Rot
 - is_valid : Bool

### Header

``` python
def SampleUVSurface(self, mesh=None, value=None, source_uv_map=None, sample_uv=None, data_type='FLOAT', node_label=None, node_color=None):
```

## Implementations

o Float : [sample_uv_surface](/docs/GeoNodes_classes/Float.md#sample_uv_surface)
o Int : [sample_uv_surface](/docs/GeoNodes_classes/Int.md#sample_uv_surface)

