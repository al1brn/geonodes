# Node FillCurve

- Node name : 'Fill Curve'
- bl_idname : [GeometryNodeFillCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)


``` python
FillCurve(curve=None, mode='TRIANGLES', node_label=None, node_color=None)
```
##### Arguments

- curve : None
- mode : 'TRIANGLES'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [fill_curve](/docs/GeoNodes/socket_GEOMETRY.md#fill_curve) [fill_curve](/docs/GeoNodes/socket_GEOMETRY.md#fill_curve)

## Init

``` python
def __init__(self, curve=None, mode='TRIANGLES', node_label=None, node_color=None):

    Node.__init__(self, 'GeometryNodeFillCurve', node_label=node_label, node_color=node_color)

    self.mode            = mode
    self.curve           = curve
```