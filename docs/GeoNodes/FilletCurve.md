# Node FilletCurve

- Node name : 'Fillet Curve'
- bl_idname : [GeometryNodeFilletCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html)


``` python
FilletCurve(curve=None, radius=None, limit_radius=None, count=None, mode='BEZIER', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- curve : None
- radius : None
- limit_radius : None
- count : None
- mode : 'BEZIER'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [fillet_curve](/docs/GeoNodes/socket_GEOMETRY.md#fillet_curve) [fillet_curve_bezier](/docs/GeoNodes/socket_GEOMETRY.md#fillet_curve_bezier) [fillet_curve_poly](/docs/GeoNodes/socket_GEOMETRY.md#fillet_curve_poly)

## Init

``` python
def __init__(self, curve=None, radius=None, limit_radius=None, count=None, mode='BEZIER', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeFilletCurve', node_label=node_label, node_color=node_color, **kwargs)

    self.mode            = mode
    self.curve           = curve
    self.radius          = radius
    self.limit_radius    = limit_radius
    self.count           = count
```
