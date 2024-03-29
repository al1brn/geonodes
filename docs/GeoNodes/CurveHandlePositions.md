# Node CurveHandlePositions

- Node name : 'Curve Handle Positions'
- bl_idname : [GeometryNodeInputCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)


``` python
CurveHandlePositions(relative=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- relative : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [curve_handle_positions](/docs/GeoNodes/socket_GEOMETRY.md#curve_handle_positions)

## Init

``` python
def __init__(self, relative=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputCurveHandlePositions', node_label=node_label, node_color=node_color, **kwargs)

    self.relative        = relative
```
