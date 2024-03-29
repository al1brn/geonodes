# Node RotateRotation

- Node name : 'Rotate Rotation'
- bl_idname : [FunctionNodeRotateRotation](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateRotation.html)


``` python
RotateRotation(rotation=None, rotate_by=None, rotation_space='GLOBAL', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- rotation : None
- rotate_by : None
- rotation_space : 'GLOBAL'

## Implementation

- [ROTATION](/docs/GeoNodes/socket_ROTATION.md) : [rotate_rotation](/docs/GeoNodes/socket_ROTATION.md#rotate_rotation)

## Init

``` python
def __init__(self, rotation=None, rotate_by=None, rotation_space='GLOBAL', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'FunctionNodeRotateRotation', node_label=node_label, node_color=node_color, **kwargs)

    self.rotation_space  = rotation_space
    self.rotation        = rotation
    self.rotate_by       = rotate_by
```
