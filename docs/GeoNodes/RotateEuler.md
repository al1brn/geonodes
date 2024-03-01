# Node RotateEuler

- Node name : 'Rotate Euler'
- bl_idname : [Rotate Euler](https://docs.blender.org/api/current/bpy.types.Rotate Euler.html)


``` python
RotateEuler(rotation=None, rotate_by=None, space='OBJECT', node_label=None, node_color=None)
```
##### Arguments

- rotation : None
- rotate_by : None
- space : 'OBJECT'

## Implementation

- [Rot](/docs/GeoNodes/Rot.md) : [rotate_euler](/docs/GeoNodes/Rot.md#rotate_euler) [rotate_euler_axis_angle](/docs/GeoNodes/Rot.md#rotate_euler_axis_angle) [rotate_euler_euler](/docs/GeoNodes/Rot.md#rotate_euler_euler)
- [Vect](/docs/GeoNodes/Vect.md) : [rotate_euler](/docs/GeoNodes/Vect.md#rotate_euler) [rotate_euler_axis_angle](/docs/GeoNodes/Vect.md#rotate_euler_axis_angle) [rotate_euler_euler](/docs/GeoNodes/Vect.md#rotate_euler_euler)

## Init

``` python
def __init__(self, rotation=None, rotate_by=None, space='OBJECT', node_label=None, node_color=None):

    StackedNode.__init__(self, 'FunctionNodeRotateEuler', node_label=node_label, node_color=node_color)

    self.space           = space
    self.rotation        = rotation
    self.rotate_by       = rotate_by
```
