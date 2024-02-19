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

o functions : [compare](/docs/GeoNodes_classes/compare.md)
o Float : [less_than](/docs/GeoNodes_classes/less_than.md) [less_equal](/docs/GeoNodes_classes/less_equal.md) [greater_than](/docs/GeoNodes_classes/greater_than.md) [greater_equal](/docs/GeoNodes_classes/greater_equal.md) [equal](/docs/GeoNodes_classes/equal.md) [not_equal](/docs/GeoNodes_classes/not_equal.md) 
o Int : [less_than](/docs/GeoNodes_classes/less_than.md) [less_equal](/docs/GeoNodes_classes/less_equal.md) [greater_than](/docs/GeoNodes_classes/greater_than.md) [greater_equal](/docs/GeoNodes_classes/greater_equal.md) [equal](/docs/GeoNodes_classes/equal.md) [not_equal](/docs/GeoNodes_classes/not_equal.md) 
o Vect : [less_than](/docs/GeoNodes_classes/less_than.md) [less_equal](/docs/GeoNodes_classes/less_equal.md) [greater_than](/docs/GeoNodes_classes/greater_than.md) [greater_equal](/docs/GeoNodes_classes/greater_equal.md) [equal](/docs/GeoNodes_classes/equal.md) [not_equal](/docs/GeoNodes_classes/not_equal.md) 
o Str : [equal](/docs/GeoNodes_classes/equal.md) [not_equal](/docs/GeoNodes_classes/not_equal.md) 
o Col : [equal](/docs/GeoNodes_classes/equal.md) [not_equal](/docs/GeoNodes_classes/not_equal.md) [brighter](/docs/GeoNodes_classes/brighter.md) [darker](/docs/GeoNodes_classes/darker.md) 
