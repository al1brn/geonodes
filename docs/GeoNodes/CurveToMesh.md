# Node CurveToMesh

- Node name : 'Curve to Mesh'
- bl_idname : [GeometryNodeCurveToMesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToMesh.html)


``` python
CurveToMesh(curve=None, profile_curve=None, fill_caps=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- curve : None
- profile_curve : None
- fill_caps : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [curve_to_mesh](/docs/GeoNodes/socket_GEOMETRY.md#curve_to_mesh)

## Init

``` python
def __init__(self, curve=None, profile_curve=None, fill_caps=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeCurveToMesh', node_label=node_label, node_color=node_color, **kwargs)

    self.curve           = curve
    self.profile_curve   = profile_curve
    self.fill_caps       = fill_caps
```
