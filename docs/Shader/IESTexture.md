# Node IESTexture

- Node name : 'IES Texture'
- bl_idname : [ShaderNodeTexIES](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexIES.html)


``` python
IESTexture(vector=None, strength=None, filepath='', ies=None, mode='INTERNAL', node_label=None, node_color=None)
```
##### Arguments

- vector : None
- strength : None
- filepath : ''
- ies : None
- mode : 'INTERNAL'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, vector=None, strength=None, filepath='', ies=None, mode='INTERNAL', node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeTexIES', node_label=node_label, node_color=node_color)

    self.filepath        = filepath
    self.ies             = ies
    self.mode            = mode
    self.vector          = vector
    self.strength        = strength
```
