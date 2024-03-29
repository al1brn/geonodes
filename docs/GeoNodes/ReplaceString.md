# Node ReplaceString

- Node name : 'Replace String'
- bl_idname : [FunctionNodeReplaceString](https://docs.blender.org/api/current/bpy.types.FunctionNodeReplaceString.html)


``` python
ReplaceString(string=None, find=None, replace=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- string : None
- find : None
- replace : None

## Implementation

- [STRING](/docs/GeoNodes/socket_STRING.md) : [replace_string](/docs/GeoNodes/socket_STRING.md#replace_string)

## Init

``` python
def __init__(self, string=None, find=None, replace=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'FunctionNodeReplaceString', node_label=node_label, node_color=node_color, **kwargs)

    self.string          = string
    self.find            = find
    self.replace         = replace
```
