# Node SplineLength

- Node name : 'Spline Length'
- bl_idname : [GeometryNodeSplineLength](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineLength.html)


``` python
SplineLength(node_label=None, node_color=None)
```
## Implementation

- [GEOMETRY](/docs/GeoNodes/GEOMETRY.md) : [spline_length](/docs/GeoNodes/GEOMETRY.md#spline_length) [spline_length](/docs/GeoNodes/GEOMETRY.md#spline_length)

## Init

``` python
def __init__(self, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeSplineLength', node_label=node_label, node_color=node_color)
```
