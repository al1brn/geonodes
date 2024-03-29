# Node SetSplineType

- Node name : 'Set Spline Type'
- bl_idname : [GeometryNodeCurveSplineType](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html)


``` python
SetSplineType(curve=None, selection=None, spline_type='POLY', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- curve : None
- selection : None
- spline_type : 'POLY'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [set_spline_type](/docs/GeoNodes/socket_GEOMETRY.md#set_spline_type) [spline_type](/docs/GeoNodes/socket_GEOMETRY.md#spline_type)

## Init

``` python
def __init__(self, curve=None, selection=None, spline_type='POLY', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeCurveSplineType', node_label=node_label, node_color=node_color, **kwargs)

    self.spline_type     = spline_type
    self.curve           = curve
    self.selection       = selection
```
