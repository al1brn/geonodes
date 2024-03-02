# Node Background

- Node name : 'Background'
- bl_idname : [ShaderNodeBackground](https://docs.blender.org/api/current/bpy.types.ShaderNodeBackground.html)


``` python
Background(color=None, strength=None, node_label=None, node_color=None)
```
##### Arguments

- color : None
- strength : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, strength=None, node_label=None, node_color=None):

    Node.__init__(self, 'ShaderNodeBackground', node_label=node_label, node_color=node_color)

    self.color           = color
    self.strength        = strength
```