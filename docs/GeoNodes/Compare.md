# Node Compare

- Node name : 'Compare'
- bl_idname : [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)


``` python
Compare(a=None, b=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- a : None
- b : None
- epsilon : None
- data_type : 'FLOAT'
- mode : 'ELEMENT'
- operation : 'GREATER_THAN'

## Implementation

- [INT](/docs/GeoNodes/socket_INT.md) : [equal](/docs/GeoNodes/socket_INT.md#equal) [greater_equal](/docs/GeoNodes/socket_INT.md#greater_equal) [greater_than](/docs/GeoNodes/socket_INT.md#greater_than) [less_equal](/docs/GeoNodes/socket_INT.md#less_equal) [less_than](/docs/GeoNodes/socket_INT.md#less_than) [not_equal](/docs/GeoNodes/socket_INT.md#not_equal)
- [RGBA](/docs/GeoNodes/socket_RGBA.md) : [brighter](/docs/GeoNodes/socket_RGBA.md#brighter) [darker](/docs/GeoNodes/socket_RGBA.md#darker) [equal](/docs/GeoNodes/socket_RGBA.md#equal) [not_equal](/docs/GeoNodes/socket_RGBA.md#not_equal)
- [STRING](/docs/GeoNodes/socket_STRING.md) : [equal](/docs/GeoNodes/socket_STRING.md#equal) [not_equal](/docs/GeoNodes/socket_STRING.md#not_equal)
- [VALUE](/docs/GeoNodes/socket_VALUE.md) : [equal](/docs/GeoNodes/socket_VALUE.md#equal) [greater_equal](/docs/GeoNodes/socket_VALUE.md#greater_equal) [greater_than](/docs/GeoNodes/socket_VALUE.md#greater_than) [less_equal](/docs/GeoNodes/socket_VALUE.md#less_equal) [less_than](/docs/GeoNodes/socket_VALUE.md#less_than) [not_equal](/docs/GeoNodes/socket_VALUE.md#not_equal)
- [VECTOR](/docs/GeoNodes/socket_VECTOR.md) : [equal](/docs/GeoNodes/socket_VECTOR.md#equal) [greater_equal](/docs/GeoNodes/socket_VECTOR.md#greater_equal) [greater_than](/docs/GeoNodes/socket_VECTOR.md#greater_than) [less_equal](/docs/GeoNodes/socket_VECTOR.md#less_equal) [less_than](/docs/GeoNodes/socket_VECTOR.md#less_than) [not_equal](/docs/GeoNodes/socket_VECTOR.md#not_equal)

## Init

``` python
def __init__(self, a=None, b=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'FunctionNodeCompare', node_label=node_label, node_color=node_color, **kwargs)

    self.data_type       = data_type
    self.mode            = mode
    self.operation       = operation
    self.a               = a
    self.b               = b
    self.epsilon         = epsilon
```
