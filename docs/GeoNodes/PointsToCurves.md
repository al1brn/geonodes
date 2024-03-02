# Node PointsToCurves

- Node name : 'Points to Curves'
- bl_idname : [GeometryNodePointsToCurves](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToCurves.html)


``` python
PointsToCurves(points=None, curve_group_id=None, weight=None, node_label=None, node_color=None)
```
##### Arguments

- points : None
- curve_group_id : None
- weight : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [points_to_curves](/docs/GeoNodes/socket_GEOMETRY.md#points_to_curves) [points_to_curves](/docs/GeoNodes/socket_GEOMETRY.md#points_to_curves)

## Init

``` python
def __init__(self, points=None, curve_group_id=None, weight=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodePointsToCurves', node_label=node_label, node_color=node_color)

    self.points          = points
    self.curve_group_id  = curve_group_id
    self.weight          = weight
```
