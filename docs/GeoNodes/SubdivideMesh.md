# Node SubdivideMesh

- Node name : 'Subdivide Mesh'
- bl_idname : [GeometryNodeSubdivideMesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideMesh.html)


``` python
SubdivideMesh(mesh=None, level=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- mesh : None
- level : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [subdivide_mesh](/docs/GeoNodes/socket_GEOMETRY.md#subdivide_mesh)

## Init

``` python
def __init__(self, mesh=None, level=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeSubdivideMesh', node_label=node_label, node_color=node_color, **kwargs)

    self.mesh            = mesh
    self.level           = level
```
