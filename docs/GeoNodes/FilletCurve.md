# Node FilletCurve

- Node name : 'Fillet Curve'
- bl_idname : [Fillet Curve](https://docs.blender.org/api/current/bpy.types.Fillet Curve.html)


``` python
FilletCurve(curve=None, radius=None, limit_radius=None, count=None, mode='BEZIER', node_label=None, node_color=None)
```
##### Arguments

- curve : None
- radius : None
- limit_radius : None
- count : None
- mode : 'BEZIER'

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [fillet_curve](/docs/GeoNodes/Geometry.md#fillet_curve) [fillet_curve_bezier](/docs/GeoNodes/Geometry.md#fillet_curve_bezier) [fillet_curve_poly](/docs/GeoNodes/Geometry.md#fillet_curve_poly)

## Init

``` python
def __init__(self, curve=None, radius=None, limit_radius=None, count=None, mode='BEZIER', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeFilletCurve', node_label=node_label, node_color=node_color)

    self.mode            = mode
    self.curve           = curve
    self.radius          = radius
    self.limit_radius    = limit_radius
    self.count           = count
```
