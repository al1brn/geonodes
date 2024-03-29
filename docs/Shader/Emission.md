# Node Emission

- Node name : 'Emission'
- bl_idname : [ShaderNodeEmission](https://docs.blender.org/api/current/bpy.types.ShaderNodeEmission.html)


``` python
Emission(color=None, strength=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- color : None
- strength : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, strength=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeEmission', node_label=node_label, node_color=node_color, **kwargs)

    self.color           = color
    self.strength        = strength
```
