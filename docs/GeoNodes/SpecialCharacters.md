# Node SpecialCharacters

- Node name : 'Special Characters'
- bl_idname : [FunctionNodeInputSpecialCharacters](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputSpecialCharacters.html)


``` python
SpecialCharacters(node_label=None, node_color=None)
```
## Implementation

- [STRING](/docs/GeoNodes/STRING.md) : [line_break](/docs/GeoNodes/STRING.md#line_break) [line_break](/docs/GeoNodes/STRING.md#line_break) [special_characters](/docs/GeoNodes/STRING.md#special_characters) [special_characters](/docs/GeoNodes/STRING.md#special_characters) [tab](/docs/GeoNodes/STRING.md#tab) [tab](/docs/GeoNodes/STRING.md#tab)

## Init

``` python
def __init__(self, node_label=None, node_color=None):

    StackedNode.__init__(self, 'FunctionNodeInputSpecialCharacters', node_label=node_label, node_color=node_color)
```
