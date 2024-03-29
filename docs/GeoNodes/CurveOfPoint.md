# Node CurveOfPoint

- Node name : 'Curve of Point'
- bl_idname : [GeometryNodeCurveOfPoint](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveOfPoint.html)


``` python
CurveOfPoint(point_index=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- point_index : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [curve_of_point](/docs/GeoNodes/socket_GEOMETRY.md#curve_of_point)

## Init

``` python
def __init__(self, point_index=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeCurveOfPoint', node_label=node_label, node_color=node_color, **kwargs)

    self.point_index     = point_index
```
