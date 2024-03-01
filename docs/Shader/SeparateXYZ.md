# Node SeparateXYZ

- Node name : 'Separate XYZ'
- bl_idname : [ShaderNodeSeparateXYZ](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html)


``` python
SeparateXYZ(vector=None, node_label=None, node_color=None)
```
##### Arguments

- vector : None

## Implementation

- [Vect](/docs/Shader/Vect.md) : [separate_xyz](/docs/Shader/Vect.md#separate_xyz)

## Init

``` python
def __init__(self, vector=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeSeparateXYZ', node_label=node_label, node_color=node_color)

    self.vector          = vector
```
