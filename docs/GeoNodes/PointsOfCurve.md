# Node PointsOfCurve

- Node name : 'Points of Curve'
- bl_idname : [Points of Curve](https://docs.blender.org/api/current/bpy.types.Points of Curve.html)


``` python
PointsOfCurve(curve_index=None, weights=None, sort_index=None, node_label=None, node_color=None)
```
##### Arguments

- curve_index : None
- weights : None
- sort_index : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [points_of_curve](/docs/GeoNodes/Geometry.md#points_of_curve)

## Init

``` python
def __init__(self, curve_index=None, weights=None, sort_index=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodePointsOfCurve', node_label=node_label, node_color=node_color)

    self.curve_index     = curve_index
    self.weights         = weights
    self.sort_index      = sort_index
```
