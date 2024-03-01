# Node CurveOfPoint

- Node name : 'Curve of Point'
- bl_idname : [Curve of Point](https://docs.blender.org/api/current/bpy.types.Curve of Point.html)


``` python
CurveOfPoint(point_index=None, node_label=None, node_color=None)
```
##### Arguments

- point_index : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [curve_of_point](/docs/GeoNodes/Geometry.md#curve_of_point)

## Init

``` python
def __init__(self, point_index=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeCurveOfPoint', node_label=node_label, node_color=node_color)

    self.point_index     = point_index
```
