# class Compare (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : Compare
 - bl_idname : FunctionNodeCompare

Node parameters
 - data_type : 'FLOAT'
 - mode : 'ELEMENT'
 - operation : 'GREATER_THAN'

Input sockets
 - a : Float
 - b : Float
 - a_1 : Int
 - b_1 : Int
 - a_2 : Vect
 - b_2 : Vect
 - a_3 : Col
 - b_3 : Col
 - a_4 : Str
 - b_4 : Str
 - c : Float
 - angle : Float
 - epsilon : Float

Output sockets
 - result : Bool

### Header

``` python
def Compare(self, a=None, b=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', node_label=None, node_color=None):
```

## Implementations

o functions : [compare](/docs/GeoNodes_classes/GLOBAL.md#compare)
o Float : [less_than](/docs/GeoNodes_classes/Float.md#less_than) [less_equal](/docs/GeoNodes_classes/Float.md#less_equal) [greater_than](/docs/GeoNodes_classes/Float.md#greater_than) [greater_equal](/docs/GeoNodes_classes/Float.md#greater_equal) [equal](/docs/GeoNodes_classes/Float.md#equal) [not_equal](/docs/GeoNodes_classes/Float.md#not_equal)

o Int : [less_than](/docs/GeoNodes_classes/Int.md#less_than) [less_equal](/docs/GeoNodes_classes/Int.md#less_equal) [greater_than](/docs/GeoNodes_classes/Int.md#greater_than) [greater_equal](/docs/GeoNodes_classes/Int.md#greater_equal) [equal](/docs/GeoNodes_classes/Int.md#equal) [not_equal](/docs/GeoNodes_classes/Int.md#not_equal)

o Vect : [less_than](/docs/GeoNodes_classes/Vect.md#less_than) [less_equal](/docs/GeoNodes_classes/Vect.md#less_equal) [greater_than](/docs/GeoNodes_classes/Vect.md#greater_than) [greater_equal](/docs/GeoNodes_classes/Vect.md#greater_equal) [equal](/docs/GeoNodes_classes/Vect.md#equal) [not_equal](/docs/GeoNodes_classes/Vect.md#not_equal)

o Str : [equal](/docs/GeoNodes_classes/Str.md#equal) [not_equal](/docs/GeoNodes_classes/Str.md#not_equal)

o Col : [equal](/docs/GeoNodes_classes/Col.md#equal) [not_equal](/docs/GeoNodes_classes/Col.md#not_equal) [brighter](/docs/GeoNodes_classes/Col.md#brighter) [darker](/docs/GeoNodes_classes/Col.md#darker)


