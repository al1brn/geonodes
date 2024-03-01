# Node RotationToQuaternion

- Node name : 'Rotation to Quaternion'
- bl_idname : [Rotation to Quaternion](https://docs.blender.org/api/current/bpy.types.Rotation to Quaternion.html)


``` python
RotationToQuaternion(rotation=None, node_label=None, node_color=None)
```
##### Arguments

- rotation : None

## Implementation

- [Rot](/docs/GeoNodes/Rot.md) : [rotation_to_quaternion](/docs/GeoNodes/Rot.md#rotation_to_quaternion)
- [Vect](/docs/GeoNodes/Vect.md) : [rotation_to_quaternion](/docs/GeoNodes/Vect.md#rotation_to_quaternion)

## Init

``` python
def __init__(self, rotation=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'FunctionNodeRotationToQuaternion', node_label=node_label, node_color=node_color)

    self.rotation        = rotation
```
