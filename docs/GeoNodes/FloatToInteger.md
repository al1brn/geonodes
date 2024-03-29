# Node FloatToInteger

- Node name : 'Float to Integer'
- bl_idname : [FunctionNodeFloatToInt](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)


``` python
FloatToInteger(float=None, rounding_mode='ROUND', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- float : None
- rounding_mode : 'ROUND'

## Implementation

- [VALUE](/docs/GeoNodes/socket_VALUE.md) : [ceiling](/docs/GeoNodes/socket_VALUE.md#ceiling) [float_to_integer](/docs/GeoNodes/socket_VALUE.md#float_to_integer) [float_to_integer_ceiling](/docs/GeoNodes/socket_VALUE.md#float_to_integer_ceiling) [float_to_integer_floor](/docs/GeoNodes/socket_VALUE.md#float_to_integer_floor) [float_to_integer_round](/docs/GeoNodes/socket_VALUE.md#float_to_integer_round) [float_to_integer_truncate](/docs/GeoNodes/socket_VALUE.md#float_to_integer_truncate) [floor](/docs/GeoNodes/socket_VALUE.md#floor) [round](/docs/GeoNodes/socket_VALUE.md#round) [truncate](/docs/GeoNodes/socket_VALUE.md#truncate)

## Init

``` python
def __init__(self, float=None, rounding_mode='ROUND', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'FunctionNodeFloatToInt', node_label=node_label, node_color=node_color, **kwargs)

    self.rounding_mode   = rounding_mode
    self.float           = float
```
