# Node RotateVector

- Node name : 'Rotate Vector'
- bl_idname : [FunctionNodeRotateVector](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateVector.html)


``` python
RotateVector(vector=None, rotation=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vector : None
- rotation : None

## Implementation

- [VECTOR](/docs/GeoNodes/socket_VECTOR.md) : [rotate_vector](/docs/GeoNodes/socket_VECTOR.md#rotate_vector)

## Init

``` python
def __init__(self, vector=None, rotation=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'FunctionNodeRotateVector', node_label=node_label, node_color=node_color, **kwargs)

    self.vector          = vector
    self.rotation        = rotation
```
