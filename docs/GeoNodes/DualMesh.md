# Node DualMesh

- Node name : 'Dual Mesh'
- bl_idname : [GeometryNodeDualMesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeDualMesh.html)


``` python
DualMesh(mesh=None, keep_boundaries=None, node_label=None, node_color=None)
```
##### Arguments

- mesh : None
- keep_boundaries : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [dual_mesh](/docs/GeoNodes/socket_GEOMETRY.md#dual_mesh) [dual_mesh](/docs/GeoNodes/socket_GEOMETRY.md#dual_mesh)

## Init

``` python
def __init__(self, mesh=None, keep_boundaries=None, node_label=None, node_color=None):

    Node.__init__(self, 'GeometryNodeDualMesh', node_label=node_label, node_color=node_color)

    self.mesh            = mesh
    self.keep_boundaries = keep_boundaries
```
