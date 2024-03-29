# Node AxisAngleToRotation

- Node name : 'Axis Angle to Rotation'
- bl_idname : [FunctionNodeAxisAngleToRotation](https://docs.blender.org/api/current/bpy.types.FunctionNodeAxisAngleToRotation.html)


``` python
AxisAngleToRotation(axis=None, angle=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- axis : None
- angle : None

## Implementation

- [VECTOR](/docs/GeoNodes/socket_VECTOR.md) : [axis_angle_to_rotation](/docs/GeoNodes/socket_VECTOR.md#axis_angle_to_rotation)

## Init

``` python
def __init__(self, axis=None, angle=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'FunctionNodeAxisAngleToRotation', node_label=node_label, node_color=node_color, **kwargs)

    self.axis            = axis
    self.angle           = angle
```
