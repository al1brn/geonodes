# Node Clamp

- Node name : 'Clamp'
- bl_idname : [ShaderNodeClamp](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)


``` python
Clamp(value=None, min=None, max=None, clamp_type='MINMAX', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- value : None
- min : None
- max : None
- clamp_type : 'MINMAX'

## Implementation

- [VALUE](/docs/Shader/socket_VALUE.md) : [clamp](/docs/Shader/socket_VALUE.md#clamp)

## Init

``` python
def __init__(self, value=None, min=None, max=None, clamp_type='MINMAX', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeClamp', node_label=node_label, node_color=node_color, **kwargs)

    self.clamp_type      = clamp_type
    self.value           = value
    self.min             = min
    self.max             = max
```
