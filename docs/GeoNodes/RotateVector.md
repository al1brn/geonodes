# Node RotateVector

- Node name : 'Rotate Vector'
- bl_idname : [Rotate Vector](https://docs.blender.org/api/current/bpy.types.Rotate Vector.html)


``` python
RotateVector(vector=None, rotation=None, node_label=None, node_color=None)
```
##### Arguments

- vector : None
- rotation : None

## Implementation

- [Vect](/docs/GeoNodes/Vect.md) : [rotate_vector](/docs/GeoNodes/Vect.md#rotate_vector)

## Init

``` python
def __init__(self, vector=None, rotation=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'FunctionNodeRotateVector', node_label=node_label, node_color=node_color)

    self.vector          = vector
    self.rotation        = rotation
```
