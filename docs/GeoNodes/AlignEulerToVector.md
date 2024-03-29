# Node AlignEulerToVector

- Node name : 'Align Euler to Vector'
- bl_idname : [FunctionNodeAlignEulerToVector](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html)


``` python
AlignEulerToVector(rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- rotation : None
- factor : None
- vector : None
- axis : 'X'
- pivot_axis : 'AUTO'

## Implementation

- [ROTATION](/docs/GeoNodes/socket_ROTATION.md) : [align_euler_to_vector](/docs/GeoNodes/socket_ROTATION.md#align_euler_to_vector)
- [VECTOR](/docs/GeoNodes/socket_VECTOR.md) : [align_euler_to_vector](/docs/GeoNodes/socket_VECTOR.md#align_euler_to_vector)

## Init

``` python
def __init__(self, rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'FunctionNodeAlignEulerToVector', node_label=node_label, node_color=node_color, **kwargs)

    self.axis            = axis
    self.pivot_axis      = pivot_axis
    self.rotation        = rotation
    self.factor          = factor
    self.vector          = vector
```
