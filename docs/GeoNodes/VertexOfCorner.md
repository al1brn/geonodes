# Node VertexOfCorner

- Node name : 'Vertex of Corner'
- bl_idname : [GeometryNodeVertexOfCorner](https://docs.blender.org/api/current/bpy.types.GeometryNodeVertexOfCorner.html)


``` python
VertexOfCorner(corner_index=None, node_label=None, node_color=None)
```
##### Arguments

- corner_index : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [vertex_of_corner](/docs/GeoNodes/socket_GEOMETRY.md#vertex_of_corner) [vertex_of_corner](/docs/GeoNodes/socket_GEOMETRY.md#vertex_of_corner)

## Init

``` python
def __init__(self, corner_index=None, node_label=None, node_color=None):

    Node.__init__(self, 'GeometryNodeVertexOfCorner', node_label=node_label, node_color=node_color)

    self.corner_index    = corner_index
```
