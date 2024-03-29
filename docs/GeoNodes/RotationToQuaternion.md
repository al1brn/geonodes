# Node RotationToQuaternion

- Node name : 'Rotation to Quaternion'
- bl_idname : [FunctionNodeRotationToQuaternion](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotationToQuaternion.html)


``` python
RotationToQuaternion(rotation=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- rotation : None

## Implementation

- [ROTATION](/docs/GeoNodes/socket_ROTATION.md) : [rotation_to_quaternion](/docs/GeoNodes/socket_ROTATION.md#rotation_to_quaternion)
- [VECTOR](/docs/GeoNodes/socket_VECTOR.md) : [rotation_to_quaternion](/docs/GeoNodes/socket_VECTOR.md#rotation_to_quaternion)

## Init

``` python
def __init__(self, rotation=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'FunctionNodeRotationToQuaternion', node_label=node_label, node_color=node_color, **kwargs)

    self.rotation        = rotation
```
