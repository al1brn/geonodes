# Node CurveTangent

- Node name : 'Curve Tangent'
- bl_idname : [GeometryNodeInputTangent](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputTangent.html)


``` python
CurveTangent(node_label=None, node_color=None, **kwargs)
```
## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [curve_tangent](/docs/GeoNodes/socket_GEOMETRY.md#curve_tangent)

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputTangent', node_label=node_label, node_color=node_color, **kwargs)
```
