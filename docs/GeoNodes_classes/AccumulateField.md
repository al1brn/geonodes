# class AccumulateField (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : AccumulateField
 - bl_idname : GeometryNodeAccumulateField

Node parameters
 - data_type : 'FLOAT'
 - domain : 'POINT'

Input sockets
 - value : Vect
 - value_1 : Float
 - value_2 : Int
 - group_id : Int

Output sockets
 - leading : Vect
 - leading_1 : Float
 - leading_2 : Int
 - trailing : Vect
 - trailing_1 : Float
 - trailing_2 : Int
 - total : Vect
 - total_1 : Float
 - total_2 : Int

### Header

``` python
def AccumulateField(self, value=None, group_id=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):
```

## Implementations

o Float : [accumulate_field](/docs/GeoNodes_classes/accumulate_field.md) 
o Int : [accumulate_field](/docs/GeoNodes_classes/accumulate_field.md) 

