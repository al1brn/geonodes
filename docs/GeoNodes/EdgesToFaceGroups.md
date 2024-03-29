# Node EdgesToFaceGroups

- Node name : 'Edges to Face Groups'
- bl_idname : [GeometryNodeEdgesToFaceGroups](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesToFaceGroups.html)


``` python
EdgesToFaceGroups(boundary_edges=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- boundary_edges : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [edges_to_face_groups](/docs/GeoNodes/socket_GEOMETRY.md#edges_to_face_groups)

## Init

``` python
def __init__(self, boundary_edges=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeEdgesToFaceGroups', node_label=node_label, node_color=node_color, **kwargs)

    self.boundary_edges  = boundary_edges
```
