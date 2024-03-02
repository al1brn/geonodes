# Node CurveOfPoint

- Node name : 'Curve of Point'
- bl_idname : [GeometryNodeCurveOfPoint](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveOfPoint.html)


``` python
CurveOfPoint(point_index=None, node_label=None, node_color=None)
```
##### Arguments

- point_index : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/GEOMETRY.md) : [curve_of_point](/docs/GeoNodes/socket_GEOMETRY.md#curve_of_point) [curve_of_point](/docs/GeoNodes/socket_GEOMETRY.md#curve_of_point)

## Init

``` python
def __init__(self, point_index=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeCurveOfPoint', node_label=node_label, node_color=node_color)

    self.point_index     = point_index
```
