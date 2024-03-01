# Node ValueToString

- Node name : 'Value to String'
- bl_idname : [FunctionNodeValueToString](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
ValueToString(value=None, decimals=None, node_label=None, node_color=None)
```
##### Arguments

- value : None
- decimals : None

## Implementation

- [Float](/docs/GeoNodes/Float.md) : [value_to_string](/docs/GeoNodes/Float.md#value_to_string)
- [Int](/docs/GeoNodes/Int.md) : [value_to_string](/docs/GeoNodes/Int.md#value_to_string)

## Init

``` python
def __init__(self, value=None, decimals=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'FunctionNodeValueToString', node_label=node_label, node_color=node_color)

    self.value           = value
    self.decimals        = decimals
```
