# Node OffsetPointInCurve

- Node name : 'Offset Point in Curve'
- bl_idname : [GeometryNodeOffsetPointInCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetPointInCurve.html)


``` python
OffsetPointInCurve(point_index=None, offset=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- point_index : None
- offset : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [offset_point_in_curve](/docs/GeoNodes/socket_GEOMETRY.md#offset_point_in_curve)

## Init

``` python
def __init__(self, point_index=None, offset=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeOffsetPointInCurve', node_label=node_label, node_color=node_color, **kwargs)

    self.point_index     = point_index
    self.offset          = offset
```
