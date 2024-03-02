# Node Shadernodeoutputaov

- Node name : 'ShaderNodeOutputAOV'
- bl_idname : [ShaderNodeOutputAOV](https://docs.blender.org/api/current/bpy.types.ShaderNodeOutputAOV.html)


``` python
Shadernodeoutputaov(color=None, value=None, node_label=None, node_color=None)
```
##### Arguments

- color : None
- value : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, value=None, node_label=None, node_color=None):

    Node.__init__(self, 'ShaderNodeOutputAOV', node_label=node_label, node_color=node_color)

    self.color           = color
    self.value           = value
```