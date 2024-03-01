# Node Blackbody

- Node name : 'Blackbody'
- bl_idname : [Blackbody](https://docs.blender.org/api/current/bpy.types.Blackbody.html)


``` python
Blackbody(temperature=None, node_label=None, node_color=None)
```
##### Arguments

- temperature : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, temperature=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeBlackbody', node_label=node_label, node_color=node_color)

    self.temperature     = temperature
```
