# Node ValueToString

- Node name : 'Value to String'
- bl_idname : [FunctionNodeValueToString](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html)


``` python
ValueToString(value=None, decimals=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- value : None
- decimals : None

## Implementation

- [INT](/docs/GeoNodes/socket_INT.md) : [value_to_string](/docs/GeoNodes/socket_INT.md#value_to_string)
- [VALUE](/docs/GeoNodes/socket_VALUE.md) : [value_to_string](/docs/GeoNodes/socket_VALUE.md#value_to_string)

## Init

``` python
def __init__(self, value=None, decimals=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'FunctionNodeValueToString', node_label=node_label, node_color=node_color, **kwargs)

    self.value           = value
    self.decimals        = decimals
```
