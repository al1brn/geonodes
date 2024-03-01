# Node SetCurveRadius

- Node name : 'Set Curve Radius'
- bl_idname : GeometryNodeSetCurveRadius


``` python
SetCurveRadius(curve=None, selection=None, radius=None, node_label=None, node_color=None)
```
##### Arguments

- curve : None
- selection : None
- radius : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [radius](/docs/GeoNodes/Geometry.md#radius) [set_curve_radius](/docs/GeoNodes/Geometry.md#set_curve_radius)

## Init

``` python
def __init__(self, curve=None, selection=None, radius=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeSetCurveRadius', node_label=node_label, node_color=node_color)

    self.curve           = curve
    self.selection       = selection
    self.radius          = radius
```
