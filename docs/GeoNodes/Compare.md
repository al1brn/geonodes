# Node Compare

- Node name : 'Compare'
- bl_idname : [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)


``` python
Compare(a=None, b=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', node_label=None, node_color=None)
```
##### Arguments

- a : None
- b : None
- epsilon : None
- data_type : 'FLOAT'
- mode : 'ELEMENT'
- operation : 'GREATER_THAN'

## Implementation

- [INT](/docs/GeoNodes/INT.md) : [equal](/docs/GeoNodes/INT.md#equal) [equal](/docs/GeoNodes/INT.md#equal) [greater_equal](/docs/GeoNodes/INT.md#greater_equal) [greater_equal](/docs/GeoNodes/INT.md#greater_equal) [greater_than](/docs/GeoNodes/INT.md#greater_than) [greater_than](/docs/GeoNodes/INT.md#greater_than) [less_equal](/docs/GeoNodes/INT.md#less_equal) [less_equal](/docs/GeoNodes/INT.md#less_equal) [less_than](/docs/GeoNodes/INT.md#less_than) [less_than](/docs/GeoNodes/INT.md#less_than) [not_equal](/docs/GeoNodes/INT.md#not_equal) [not_equal](/docs/GeoNodes/INT.md#not_equal)
- [RGBA](/docs/GeoNodes/RGBA.md) : [brighter](/docs/GeoNodes/RGBA.md#brighter) [brighter](/docs/GeoNodes/RGBA.md#brighter) [darker](/docs/GeoNodes/RGBA.md#darker) [darker](/docs/GeoNodes/RGBA.md#darker) [equal](/docs/GeoNodes/RGBA.md#equal) [equal](/docs/GeoNodes/RGBA.md#equal) [not_equal](/docs/GeoNodes/RGBA.md#not_equal) [not_equal](/docs/GeoNodes/RGBA.md#not_equal)
- [STRING](/docs/GeoNodes/STRING.md) : [equal](/docs/GeoNodes/STRING.md#equal) [equal](/docs/GeoNodes/STRING.md#equal) [not_equal](/docs/GeoNodes/STRING.md#not_equal) [not_equal](/docs/GeoNodes/STRING.md#not_equal)
- [VALUE](/docs/GeoNodes/VALUE.md) : [equal](/docs/GeoNodes/VALUE.md#equal) [equal](/docs/GeoNodes/VALUE.md#equal) [greater_equal](/docs/GeoNodes/VALUE.md#greater_equal) [greater_equal](/docs/GeoNodes/VALUE.md#greater_equal) [greater_than](/docs/GeoNodes/VALUE.md#greater_than) [greater_than](/docs/GeoNodes/VALUE.md#greater_than) [less_equal](/docs/GeoNodes/VALUE.md#less_equal) [less_equal](/docs/GeoNodes/VALUE.md#less_equal) [less_than](/docs/GeoNodes/VALUE.md#less_than) [less_than](/docs/GeoNodes/VALUE.md#less_than) [not_equal](/docs/GeoNodes/VALUE.md#not_equal) [not_equal](/docs/GeoNodes/VALUE.md#not_equal)
- [VECTOR](/docs/GeoNodes/VECTOR.md) : [equal](/docs/GeoNodes/VECTOR.md#equal) [equal](/docs/GeoNodes/VECTOR.md#equal) [greater_equal](/docs/GeoNodes/VECTOR.md#greater_equal) [greater_equal](/docs/GeoNodes/VECTOR.md#greater_equal) [greater_than](/docs/GeoNodes/VECTOR.md#greater_than) [greater_than](/docs/GeoNodes/VECTOR.md#greater_than) [less_equal](/docs/GeoNodes/VECTOR.md#less_equal) [less_equal](/docs/GeoNodes/VECTOR.md#less_equal) [less_than](/docs/GeoNodes/VECTOR.md#less_than) [less_than](/docs/GeoNodes/VECTOR.md#less_than) [not_equal](/docs/GeoNodes/VECTOR.md#not_equal) [not_equal](/docs/GeoNodes/VECTOR.md#not_equal)

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
