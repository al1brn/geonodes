# Node SplineResolution

- Node name : 'Spline Resolution'
- bl_idname : [GeometryNodeInputSplineResolution](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineResolution.html)


``` python
SplineResolution(node_label=None, node_color=None, **kwargs)
```
## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [spline_resolution](/docs/GeoNodes/socket_GEOMETRY.md#spline_resolution)

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputSplineResolution', node_label=node_label, node_color=node_color, **kwargs)
```
