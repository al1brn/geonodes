# Node RotationToEuler

- Node name : 'Rotation to Euler'
- bl_idname : [FunctionNodeRotationToEuler](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotationToEuler.html)


``` python
RotationToEuler(rotation=None, node_label=None, node_color=None)
```
##### Arguments

- rotation : None

## Implementation

- [ROTATION](/docs/GeoNodes/ROTATION.md) : [rotation_to_euler](/docs/GeoNodes/socket_ROTATION.md#rotation_to_euler) [rotation_to_euler](/docs/GeoNodes/socket_ROTATION.md#rotation_to_euler)
- [VECTOR](/docs/GeoNodes/VECTOR.md) : [rotation_to_euler](/docs/GeoNodes/socket_VECTOR.md#rotation_to_euler) [rotation_to_euler](/docs/GeoNodes/socket_VECTOR.md#rotation_to_euler)

## Init

``` python
def __init__(self, rotation=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'FunctionNodeRotationToEuler', node_label=node_label, node_color=node_color)

    self.rotation        = rotation
```
