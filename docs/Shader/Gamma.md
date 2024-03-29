# Node Gamma

- Node name : 'Gamma'
- bl_idname : [ShaderNodeGamma](https://docs.blender.org/api/current/bpy.types.ShaderNodeGamma.html)


``` python
Gamma(color=None, gamma=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- color : None
- gamma : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, gamma=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeGamma', node_label=node_label, node_color=node_color, **kwargs)

    self.color           = color
    self.gamma           = gamma
```
