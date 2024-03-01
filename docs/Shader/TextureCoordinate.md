# Node TextureCoordinate

- Node name : 'Texture Coordinate'
- bl_idname : ShaderNodeTexCoord


``` python
TextureCoordinate(from_instancer=False, object=None, node_label=None, node_color=None)
```
##### Arguments

- from_instancer : False
- object : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, from_instancer=False, object=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeTexCoord', node_label=node_label, node_color=node_color)

    self.from_instancer  = from_instancer
    self.object          = object
```
