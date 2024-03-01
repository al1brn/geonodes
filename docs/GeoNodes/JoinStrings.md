# Node JoinStrings

- Node name : 'Join Strings'
- bl_idname : [GeometryNodeStringJoin](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
JoinStrings(*args, delimiter=None, strings=None, node_label=None, node_color=None)
```
##### Arguments

- *args : 'ARG_NO_VALUE'
- delimiter : None
- strings : None

## Implementation

- [Str](/docs/GeoNodes/Str.md) : [join_strings](/docs/GeoNodes/Str.md#join_strings)
- Functions : [join_strings](/docs/GeoNodes/GeoNodes.md#join_strings)

## Init

``` python
def __init__(self, *args, delimiter=None, strings=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeStringJoin', node_label=node_label, node_color=node_color)

    self._set_multi_input(*args)
    self.delimiter       = delimiter
    self.strings         = strings
```
