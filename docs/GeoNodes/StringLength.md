# Node StringLength

- Node name : 'String Length'
- bl_idname : [FunctionNodeStringLength](https://docs.blender.org/api/current/bpy.types.FunctionNodeStringLength.html)


``` python
StringLength(string=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- string : None

## Implementation

- [STRING](/docs/GeoNodes/socket_STRING.md) : [length](/docs/GeoNodes/socket_STRING.md#length)

## Init

``` python
def __init__(self, string=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'FunctionNodeStringLength', node_label=node_label, node_color=node_color, **kwargs)

    self.string          = string
```
