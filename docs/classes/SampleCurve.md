# class SampleCurve (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : SampleCurve
 - bl_idname : GeometryNodeSampleCurve

Node parameters
 - data_type : 'FLOAT'
 - mode : 'FACTOR'
 - use_all_curves : False

Input sockets
 - curves : Geometry
 - value : Float
 - value_1 : Int
 - value_2 : Vect
 - value_3 : Col
 - value_4 : Bool
 - value_5 : Rot
 - factor : Float
 - length : Float
 - curve_index : Int

Output sockets
 - value : Float
 - value_1 : Int
 - value_2 : Vect
 - value_3 : Col
 - value_4 : Bool
 - value_5 : Rot
 - position : Vect
 - tangent : Vect
 - normal : Vect

### Header

``` python
def SampleCurve(self, curves=None, value=None, factor=None, curve_index=None, length=None, data_type='FLOAT', mode='FACTOR', use_all_curves=False, node_label=None, node_color=None):
```

## Implementations

o Float : [sample_curve](#sample_curve) 
o Int : [sample_curve](#sample_curve) 

