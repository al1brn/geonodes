# Node RotationToAxisAngle

- Node name : 'Rotation to Axis Angle'
- bl_idname : [Rotation to Axis Angle](https://docs.blender.org/api/current/bpy.types.Rotation to Axis Angle.html)


``` python
RotationToAxisAngle(rotation=None, node_label=None, node_color=None)
```
##### Arguments

- rotation : None

## Implementation

- [Rot](/docs/GeoNodes/Rot.md) : [rotation_to_axis_angle](/docs/GeoNodes/Rot.md#rotation_to_axis_angle)
- [Vect](/docs/GeoNodes/Vect.md) : [rotation_to_axis_angle](/docs/GeoNodes/Vect.md#rotation_to_axis_angle)

## Init

``` python
def __init__(self, rotation=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'FunctionNodeRotationToAxisAngle', node_label=node_label, node_color=node_color)

    self.rotation        = rotation
```
