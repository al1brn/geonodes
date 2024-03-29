# Node SplineParameter

- Node name : 'Spline Parameter'
- bl_idname : [GeometryNodeSplineParameter](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)


``` python
SplineParameter(node_label=None, node_color=None, **kwargs)
```
## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [spline_parameter](/docs/GeoNodes/socket_GEOMETRY.md#spline_parameter)

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeSplineParameter', node_label=node_label, node_color=node_color, **kwargs)
```
