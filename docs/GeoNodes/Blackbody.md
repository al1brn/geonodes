# Node Blackbody

- Node name : 'Blackbody'
- bl_idname : [ShaderNodeBlackbody](https://docs.blender.org/api/current/bpy.types.ShaderNodeBlackbody.html)


``` python
Blackbody(temperature=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- temperature : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, temperature=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeBlackbody', node_label=node_label, node_color=node_color, **kwargs)

    self.temperature     = temperature
```
