# Node RotateEuler

- Node name : 'Rotate Euler'
- bl_idname : [FunctionNodeRotateEuler](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html)


``` python
RotateEuler(rotation=None, rotate_by=None, space='OBJECT', node_label=None, node_color=None)
```
##### Arguments

- rotation : None
- rotate_by : None
- space : 'OBJECT'

## Implementation

- [ROTATION](/docs/GeoNodes/socket_ROTATION.md) : [rotate_euler](/docs/GeoNodes/socket_ROTATION.md#rotate_euler) [rotate_euler_axis_angle](/docs/GeoNodes/socket_ROTATION.md#rotate_euler_axis_angle) [rotate_euler_euler](/docs/GeoNodes/socket_ROTATION.md#rotate_euler_euler)
- [VECTOR](/docs/GeoNodes/socket_VECTOR.md) : [rotate_euler](/docs/GeoNodes/socket_VECTOR.md#rotate_euler) [rotate_euler_axis_angle](/docs/GeoNodes/socket_VECTOR.md#rotate_euler_axis_angle) [rotate_euler_euler](/docs/GeoNodes/socket_VECTOR.md#rotate_euler_euler)

## Init

``` python
def __init__(self, rotation=None, rotate_by=None, space='OBJECT', node_label=None, node_color=None):

    Node.__init__(self, 'FunctionNodeRotateEuler', node_label=node_label, node_color=node_color)

    self.space           = space
    self.rotation        = rotation
    self.rotate_by       = rotate_by
```
