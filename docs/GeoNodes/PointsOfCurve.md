# Node PointsOfCurve

- Node name : 'Points of Curve'
- bl_idname : [GeometryNodePointsOfCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsOfCurve.html)


``` python
PointsOfCurve(curve_index=None, weights=None, sort_index=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- curve_index : None
- weights : None
- sort_index : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [points_of_curve](/docs/GeoNodes/socket_GEOMETRY.md#points_of_curve)

## Init

``` python
def __init__(self, curve_index=None, weights=None, sort_index=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodePointsOfCurve', node_label=node_label, node_color=node_color, **kwargs)

    self.curve_index     = curve_index
    self.weights         = weights
    self.sort_index      = sort_index
```
