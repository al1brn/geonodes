# Node JoinStrings

- Node name : 'Join Strings'
- bl_idname : [GeometryNodeStringJoin](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringJoin.html)


``` python
JoinStrings(*args, delimiter=None, strings=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- *args : 'ARG_NO_VALUE'
- delimiter : None
- strings : None

## Implementation

- [STRING](/docs/GeoNodes/socket_STRING.md) : [join_strings](/docs/GeoNodes/socket_STRING.md#join_strings)
- Functions : [join_strings](/docs/GeoNodes/GeoNodesTree.md#join_strings)

## Init

``` python
def __init__(self, *args, delimiter=None, strings=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeStringJoin', node_label=node_label, node_color=node_color, **kwargs)

    self._set_multi_input(*args)
    self.delimiter       = delimiter
    self.strings         = strings
```
