# Node CurveHandlePositions

- Node name : 'Curve Handle Positions'
- bl_idname : [GeometryNodeInputCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)


``` python
CurveHandlePositions(relative=None, node_label=None, node_color=None)
```
##### Arguments

- relative : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [curve_handle_positions](/docs/GeoNodes/Geometry.md#curve_handle_positions)

## Init

``` python
def __init__(self, relative=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeInputCurveHandlePositions', node_label=node_label, node_color=node_color)

    self.relative        = relative
```
