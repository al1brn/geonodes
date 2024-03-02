# Node SetCurveRadius

- Node name : 'Set Curve Radius'
- bl_idname : [GeometryNodeSetCurveRadius](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html)


``` python
SetCurveRadius(curve=None, selection=None, radius=None, node_label=None, node_color=None)
```
##### Arguments

- curve : None
- selection : None
- radius : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/GEOMETRY.md) : [radius](/docs/GeoNodes/socket_GEOMETRY.md#radius) [radius](/docs/GeoNodes/socket_GEOMETRY.md#radius) [set_curve_radius](/docs/GeoNodes/socket_GEOMETRY.md#set_curve_radius) [set_curve_radius](/docs/GeoNodes/socket_GEOMETRY.md#set_curve_radius)

## Init

``` python
def __init__(self, curve=None, selection=None, radius=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeSetCurveRadius', node_label=node_label, node_color=node_color)

    self.curve           = curve
    self.selection       = selection
    self.radius          = radius
```
