# Node SubdivisionSurface

- Node name : 'Subdivision Surface'
- bl_idname : [GeometryNodeSubdivisionSurface](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivisionSurface.html)


``` python
SubdivisionSurface(mesh=None, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- mesh : None
- level : None
- edge_crease : None
- vertex_crease : None
- boundary_smooth : 'ALL'
- uv_smooth : 'PRESERVE_BOUNDARIES'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [subdivision_surface](/docs/GeoNodes/socket_GEOMETRY.md#subdivision_surface)

## Init

``` python
def __init__(self, mesh=None, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeSubdivisionSurface', node_label=node_label, node_color=node_color, **kwargs)

    self.boundary_smooth = boundary_smooth
    self.uv_smooth       = uv_smooth
    self.mesh            = mesh
    self.level           = level
    self.edge_crease     = edge_crease
    self.vertex_crease   = vertex_crease
```
