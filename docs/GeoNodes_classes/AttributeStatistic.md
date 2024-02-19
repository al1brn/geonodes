# class AttributeStatistic (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : AttributeStatistic
 - bl_idname : GeometryNodeAttributeStatistic

Node parameters
 - data_type : 'FLOAT'
 - domain : 'POINT'

Input sockets
 - geometry : Geometry
 - selection : Bool
 - attribute : Float
 - attribute_1 : Vect

Output sockets
 - mean : Float
 - median : Float
 - sum : Float
 - min : Float
 - max : Float
 - range : Float
 - standard_deviation : Float
 - variance : Float
 - mean_1 : Vect
 - median_1 : Vect
 - sum_1 : Vect
 - min_1 : Vect
 - max_1 : Vect
 - range_1 : Vect
 - standard_deviation_1 : Vect
 - variance_1 : Vect

### Header

``` python
def AttributeStatistic(self, geometry=None, attribute=None, selection=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):
```

## Implementations

o Float : [attribute_statistic](/docs/GeoNodes_classes/Float.md#attribute_statistic) 
o Int : [attribute_statistic](/docs/GeoNodes_classes/Int.md#attribute_statistic) 

