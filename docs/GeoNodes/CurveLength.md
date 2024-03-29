# Node CurveLength

- Node name : 'Curve Length'
- bl_idname : [GeometryNodeCurveLength](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveLength.html)


``` python
CurveLength(curve=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- curve : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [curve_length](/docs/GeoNodes/socket_GEOMETRY.md#curve_length)

## Init

``` python
def __init__(self, curve=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeCurveLength', node_label=node_label, node_color=node_color, **kwargs)

    self.curve           = curve
```
