# Node RotationToAxisAngle

- Node name : 'Rotation to Axis Angle'
- bl_idname : [FunctionNodeRotationToAxisAngle](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotationToAxisAngle.html)


``` python
RotationToAxisAngle(rotation=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- rotation : None

## Implementation

- [ROTATION](/docs/GeoNodes/socket_ROTATION.md) : [rotation_to_axis_angle](/docs/GeoNodes/socket_ROTATION.md#rotation_to_axis_angle)
- [VECTOR](/docs/GeoNodes/socket_VECTOR.md) : [rotation_to_axis_angle](/docs/GeoNodes/socket_VECTOR.md#rotation_to_axis_angle)

## Init

``` python
def __init__(self, rotation=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'FunctionNodeRotationToAxisAngle', node_label=node_label, node_color=node_color, **kwargs)

    self.rotation        = rotation
```
