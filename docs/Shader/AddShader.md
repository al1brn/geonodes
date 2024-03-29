# Node AddShader

- Node name : 'Add Shader'
- bl_idname : [ShaderNodeAddShader](https://docs.blender.org/api/current/bpy.types.ShaderNodeAddShader.html)


``` python
AddShader(shader=None, shader_1=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- shader : None
- shader_1 : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, shader=None, shader_1=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeAddShader', node_label=node_label, node_color=node_color, **kwargs)

    self.shader          = shader
    self.shader_1        = shader_1
```
