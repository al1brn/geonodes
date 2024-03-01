# Node AlignEulerToVector

- Node name : 'Align Euler to Vector'
- bl_idname : [Align Euler to Vector](https://docs.blender.org/api/current/bpy.types.Align Euler to Vector.html)


``` python
AlignEulerToVector(rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO', node_label=None, node_color=None)
```
##### Arguments

- rotation : None
- factor : None
- vector : None
- axis : 'X'
- pivot_axis : 'AUTO'

## Implementation

- [Rot](/docs/GeoNodes/Rot.md) : [align_euler_to_vector](/docs/GeoNodes/Rot.md#align_euler_to_vector)
- [Vect](/docs/GeoNodes/Vect.md) : [align_euler_to_vector](/docs/GeoNodes/Vect.md#align_euler_to_vector)

## Init

``` python
def __init__(self, rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO', node_label=None, node_color=None):

    StackedNode.__init__(self, 'FunctionNodeAlignEulerToVector', node_label=node_label, node_color=node_color)

    self.axis            = axis
    self.pivot_axis      = pivot_axis
    self.rotation        = rotation
    self.factor          = factor
    self.vector          = vector
```
