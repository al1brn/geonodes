# Node MixShader

- Node name : 'Mix Shader'
- bl_idname : [Mix Shader](https://docs.blender.org/api/current/bpy.types.Mix Shader.html)


``` python
MixShader(fac=None, shader=None, shader_1=None, node_label=None, node_color=None)
```
##### Arguments

- fac : None
- shader : None
- shader_1 : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, fac=None, shader=None, shader_1=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeMixShader', node_label=node_label, node_color=node_color)

    self.fac             = fac
    self.shader          = shader
    self.shader_1        = shader_1
```
