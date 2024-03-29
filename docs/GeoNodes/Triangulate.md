# Node Triangulate

- Node name : 'Triangulate'
- bl_idname : [GeometryNodeTriangulate](https://docs.blender.org/api/current/bpy.types.GeometryNodeTriangulate.html)


``` python
Triangulate(mesh=None, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- mesh : None
- selection : None
- minimum_vertices : None
- ngon_method : 'BEAUTY'
- quad_method : 'SHORTEST_DIAGONAL'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [triangulate](/docs/GeoNodes/socket_GEOMETRY.md#triangulate)

## Init

``` python
def __init__(self, mesh=None, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeTriangulate', node_label=node_label, node_color=node_color, **kwargs)

    self.ngon_method     = ngon_method
    self.quad_method     = quad_method
    self.mesh            = mesh
    self.selection       = selection
    self.minimum_vertices = minimum_vertices
```
