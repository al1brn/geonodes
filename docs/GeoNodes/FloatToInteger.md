# Node FloatToInteger

- Node name : 'Float to Integer'
- bl_idname : [FunctionNodeFloatToInt](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)


``` python
FloatToInteger(float=None, rounding_mode='ROUND', node_label=None, node_color=None)
```
##### Arguments

- float : None
- rounding_mode : 'ROUND'

## Implementation

- [Float](/docs/GeoNodes/Float.md) : [ceiling](/docs/GeoNodes/Float.md#ceiling) [float_to_integer](/docs/GeoNodes/Float.md#float_to_integer) [float_to_integer_ceiling](/docs/GeoNodes/Float.md#float_to_integer_ceiling) [float_to_integer_floor](/docs/GeoNodes/Float.md#float_to_integer_floor) [float_to_integer_round](/docs/GeoNodes/Float.md#float_to_integer_round) [float_to_integer_truncate](/docs/GeoNodes/Float.md#float_to_integer_truncate) [floor](/docs/GeoNodes/Float.md#floor) [round](/docs/GeoNodes/Float.md#round) [truncate](/docs/GeoNodes/Float.md#truncate)

## Init

``` python
def __init__(self, float=None, rounding_mode='ROUND', node_label=None, node_color=None):

    StackedNode.__init__(self, 'FunctionNodeFloatToInt', node_label=node_label, node_color=node_color)

    self.rounding_mode   = rounding_mode
    self.float           = float
```
