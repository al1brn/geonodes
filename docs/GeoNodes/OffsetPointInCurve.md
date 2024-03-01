# Node OffsetPointInCurve

- Node name : 'Offset Point in Curve'
- bl_idname : GeometryNodeOffsetPointInCurve


``` python
OffsetPointInCurve(point_index=None, offset=None, node_label=None, node_color=None)
```
##### Arguments

- point_index : None
- offset : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [offset_point_in_curve](/docs/GeoNodes/Geometry.md#offset_point_in_curve)

## Init

``` python
def __init__(self, point_index=None, offset=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeOffsetPointInCurve', node_label=node_label, node_color=node_color)

    self.point_index     = point_index
    self.offset          = offset
```
