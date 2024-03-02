# Node RotationToQuaternion

- Node name : 'Rotation to Quaternion'
- bl_idname : [FunctionNodeRotationToQuaternion](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotationToQuaternion.html)


``` python
RotationToQuaternion(rotation=None, node_label=None, node_color=None)
```
##### Arguments

- rotation : None

## Implementation

- [ROTATION](/docs/GeoNodes/ROTATION.md) : [rotation_to_quaternion](/docs/GeoNodes/ROTATION.md#rotation_to_quaternion) [rotation_to_quaternion](/docs/GeoNodes/ROTATION.md#rotation_to_quaternion)
- [VECTOR](/docs/GeoNodes/VECTOR.md) : [rotation_to_quaternion](/docs/GeoNodes/VECTOR.md#rotation_to_quaternion) [rotation_to_quaternion](/docs/GeoNodes/VECTOR.md#rotation_to_quaternion)

## Init

``` python
def __init__(self, rotation=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'FunctionNodeRotationToQuaternion', node_label=node_label, node_color=node_color)

    self.rotation        = rotation
```
