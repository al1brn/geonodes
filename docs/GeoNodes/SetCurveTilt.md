# Node SetCurveTilt

- Node name : 'Set Curve Tilt'
- bl_idname : GeometryNodeSetCurveTilt


``` python
SetCurveTilt(curve=None, selection=None, tilt=None, node_label=None, node_color=None)
```
##### Arguments

- curve : None
- selection : None
- tilt : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [set_curve_tilt](/docs/GeoNodes/Geometry.md#set_curve_tilt) [tilt](/docs/GeoNodes/Geometry.md#tilt)

## Init

``` python
def __init__(self, curve=None, selection=None, tilt=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeSetCurveTilt', node_label=node_label, node_color=node_color)

    self.curve           = curve
    self.selection       = selection
    self.tilt            = tilt
```
