# Node SeparateXYZ

- Node name : 'Separate XYZ'
- bl_idname : [ShaderNodeSeparateXYZ](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html)


``` python
SeparateXYZ(vector=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vector : None

## Implementation

- [VECTOR](/docs/Shader/socket_VECTOR.md) : [separate_xyz](/docs/Shader/socket_VECTOR.md#separate_xyz)

## Init

``` python
def __init__(self, vector=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeSeparateXYZ', node_label=node_label, node_color=node_color, **kwargs)

    self.vector          = vector
```
