# Node SubdivisionSurface

- Node name : 'Subdivision Surface'
- bl_idname : GeometryNodeSubdivisionSurface


``` python
SubdivisionSurface(mesh=None, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES', node_label=None, node_color=None)
```
##### Arguments

- mesh : None
- level : None
- edge_crease : None
- vertex_crease : None
- boundary_smooth : 'ALL'
- uv_smooth : 'PRESERVE_BOUNDARIES'

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [subdivision_surface](/docs/GeoNodes/Geometry.md#subdivision_surface)

## Init

``` python
def __init__(self, mesh=None, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeSubdivisionSurface', node_label=node_label, node_color=node_color)

    self.boundary_smooth = boundary_smooth
    self.uv_smooth       = uv_smooth
    self.mesh            = mesh
    self.level           = level
    self.edge_crease     = edge_crease
    self.vertex_crease   = vertex_crease
```
