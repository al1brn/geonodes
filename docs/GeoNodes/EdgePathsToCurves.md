# Node EdgePathsToCurves

- Node name : 'Edge Paths to Curves'
- bl_idname : [GeometryNodeEdgePathsToCurves](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToCurves.html)


``` python
EdgePathsToCurves(mesh=None, start_vertices=None, next_vertex_index=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- mesh : None
- start_vertices : None
- next_vertex_index : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [edge_paths_to_curves](/docs/GeoNodes/socket_GEOMETRY.md#edge_paths_to_curves)

## Init

``` python
def __init__(self, mesh=None, start_vertices=None, next_vertex_index=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeEdgePathsToCurves', node_label=node_label, node_color=node_color, **kwargs)

    self.mesh            = mesh
    self.start_vertices  = start_vertices
    self.next_vertex_index = next_vertex_index
```
