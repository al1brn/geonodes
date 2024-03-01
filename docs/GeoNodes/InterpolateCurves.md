# Node InterpolateCurves

- Node name : 'Interpolate Curves'
- bl_idname : [Interpolate Curves](https://docs.blender.org/api/current/bpy.types.Interpolate Curves.html)


``` python
InterpolateCurves(guide_curves=None, guide_up=None, guide_group_id=None, points=None, point_up=None, point_group_id=None, max_neighbors=None, node_label=None, node_color=None)
```
##### Arguments

- guide_curves : None
- guide_up : None
- guide_group_id : None
- points : None
- point_up : None
- point_group_id : None
- max_neighbors : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [interpolate_curves](/docs/GeoNodes/Geometry.md#interpolate_curves)

## Init

``` python
def __init__(self, guide_curves=None, guide_up=None, guide_group_id=None, points=None, point_up=None, point_group_id=None, max_neighbors=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeInterpolateCurves', node_label=node_label, node_color=node_color)

    self.guide_curves    = guide_curves
    self.guide_up        = guide_up
    self.guide_group_id  = guide_group_id
    self.points          = points
    self.point_up        = point_up
    self.point_group_id  = point_group_id
    self.max_neighbors   = max_neighbors
```
