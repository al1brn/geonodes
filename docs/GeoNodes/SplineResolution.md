# Node SplineResolution

- Node name : 'Spline Resolution'
- bl_idname : [Spline Resolution](https://docs.blender.org/api/current/bpy.types.Spline Resolution.html)


``` python
SplineResolution(node_label=None, node_color=None)
```
## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [spline_resolution](/docs/GeoNodes/Geometry.md#spline_resolution)

## Init

``` python
def __init__(self, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeInputSplineResolution', node_label=node_label, node_color=node_color)
```
