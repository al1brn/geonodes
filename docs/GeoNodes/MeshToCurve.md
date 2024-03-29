# Node MeshToCurve

- Node name : 'Mesh to Curve'
- bl_idname : [GeometryNodeMeshToCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html)


``` python
MeshToCurve(mesh=None, selection=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- mesh : None
- selection : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [mesh_to_curve](/docs/GeoNodes/socket_GEOMETRY.md#mesh_to_curve)

## Init

``` python
def __init__(self, mesh=None, selection=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeMeshToCurve', node_label=node_label, node_color=node_color, **kwargs)

    self.mesh            = mesh
    self.selection       = selection
```
