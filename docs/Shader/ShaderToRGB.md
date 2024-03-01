# Node ShaderToRGB

- Node name : 'Shader to RGB'
- bl_idname : ShaderNodeShaderToRGB


``` python
ShaderToRGB(shader=None, node_label=None, node_color=None)
```
##### Arguments

- shader : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, shader=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeShaderToRGB', node_label=node_label, node_color=node_color)

    self.shader          = shader
```
