# Node SpecialCharacters

- Node name : 'Special Characters'
- bl_idname : [FunctionNodeInputSpecialCharacters](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputSpecialCharacters.html)


``` python
SpecialCharacters(node_label=None, node_color=None, **kwargs)
```
## Implementation

- [STRING](/docs/GeoNodes/socket_STRING.md) : [line_break](/docs/GeoNodes/socket_STRING.md#line_break) [special_characters](/docs/GeoNodes/socket_STRING.md#special_characters) [tab](/docs/GeoNodes/socket_STRING.md#tab)

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'FunctionNodeInputSpecialCharacters', node_label=node_label, node_color=node_color, **kwargs)
```
