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

o functions : [compare](#compare)
o Float : [less_than](#less_than) [less_equal](#less_equal) [greater_than](#greater_than) [greater_equal](#greater_equal) [equal](#equal) [not_equal](#not_equal) 
o Int : [less_than](#less_than) [less_equal](#less_equal) [greater_than](#greater_than) [greater_equal](#greater_equal) [equal](#equal) [not_equal](#not_equal) 
o Vect : [less_than](#less_than) [less_equal](#less_equal) [greater_than](#greater_than) [greater_equal](#greater_equal) [equal](#equal) [not_equal](#not_equal) 
o Str : [equal](#equal) [not_equal](#not_equal) 
o Col : [equal](#equal) [not_equal](#not_equal) [brighter](#brighter) [darker](#darker) 

