# Node CurveToPoints

- Node name : 'Curve to Points'
- bl_idname : [GeometryNodeCurveToPoints](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html)


``` python
CurveToPoints(curve=None, count=None, length=None, mode='COUNT', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- curve : None
- count : None
- length : None
- mode : 'COUNT'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [curve_to_points](/docs/GeoNodes/socket_GEOMETRY.md#curve_to_points)

## Init

``` python
def __init__(self, curve=None, count=None, length=None, mode='COUNT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeCurveToPoints', node_label=node_label, node_color=node_color, **kwargs)

    self.mode            = mode
    self.curve           = curve
    self.count           = count
    self.length          = length
```
