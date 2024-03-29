# Node SliceString

- Node name : 'Slice String'
- bl_idname : [FunctionNodeSliceString](https://docs.blender.org/api/current/bpy.types.FunctionNodeSliceString.html)


``` python
SliceString(string=None, position=None, length=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- string : None
- position : None
- length : None

## Implementation

- [STRING](/docs/GeoNodes/socket_STRING.md) : [slice_string](/docs/GeoNodes/socket_STRING.md#slice_string)

## Init

``` python
def __init__(self, string=None, position=None, length=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'FunctionNodeSliceString', node_label=node_label, node_color=node_color, **kwargs)

    self.string          = string
    self.position        = position
    self.length          = length
```
