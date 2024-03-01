# Node Compare

- Node name : 'Compare'
- bl_idname : FunctionNodeCompare


``` python
Compare(a=None, b=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', node_label=None, node_color=None)
```
##### Arguments

- a : None
- b : None
- epsilon : None
- data_type : FLOAT
- mode : ELEMENT
- operation : GREATER_THAN

## Implementation

- [Col](/docs/GeoNodes/Col.md) : [brighter](/docs/GeoNodes/Col.md#brighter) [darker](/docs/GeoNodes/Col.md#darker) [equal](/docs/GeoNodes/Col.md#equal) [not_equal](/docs/GeoNodes/Col.md#not_equal)
- [Float](/docs/GeoNodes/Float.md) : [equal](/docs/GeoNodes/Float.md#equal) [greater_equal](/docs/GeoNodes/Float.md#greater_equal) [greater_than](/docs/GeoNodes/Float.md#greater_than) [less_equal](/docs/GeoNodes/Float.md#less_equal) [less_than](/docs/GeoNodes/Float.md#less_than) [not_equal](/docs/GeoNodes/Float.md#not_equal)
- [Int](/docs/GeoNodes/Int.md) : [equal](/docs/GeoNodes/Int.md#equal) [greater_equal](/docs/GeoNodes/Int.md#greater_equal) [greater_than](/docs/GeoNodes/Int.md#greater_than) [less_equal](/docs/GeoNodes/Int.md#less_equal) [less_than](/docs/GeoNodes/Int.md#less_than) [not_equal](/docs/GeoNodes/Int.md#not_equal)
- [Str](/docs/GeoNodes/Str.md) : [equal](/docs/GeoNodes/Str.md#equal) [not_equal](/docs/GeoNodes/Str.md#not_equal)
- [Vect](/docs/GeoNodes/Vect.md) : [equal](/docs/GeoNodes/Vect.md#equal) [greater_equal](/docs/GeoNodes/Vect.md#greater_equal) [greater_than](/docs/GeoNodes/Vect.md#greater_than) [less_equal](/docs/GeoNodes/Vect.md#less_equal) [less_than](/docs/GeoNodes/Vect.md#less_than) [not_equal](/docs/GeoNodes/Vect.md#not_equal)

## Init

``` python
def __init__(self, a=None, b=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', node_label=None, node_color=None):

    StackedNode.__init__(self, 'FunctionNodeCompare', node_label=node_label, node_color=node_color)

    self.data_type       = data_type
    self.mode            = mode
    self.operation       = operation
    self.a               = a
    self.b               = b
    self.epsilon         = epsilon
```
