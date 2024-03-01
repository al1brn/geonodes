# Node CurveTangent

- Node name : 'Curve Tangent'
- bl_idname : [Curve Tangent](https://docs.blender.org/api/current/bpy.types.Curve Tangent.html)


``` python
CurveTangent(node_label=None, node_color=None)
```
## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [curve_tangent](/docs/GeoNodes/Geometry.md#curve_tangent)

## Init

``` python
def __init__(self, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeInputTangent', node_label=node_label, node_color=node_color)
```
