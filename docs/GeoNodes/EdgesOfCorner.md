# Node EdgesOfCorner

- Node name : 'Edges of Corner'
- bl_idname : [GeometryNodeEdgesOfCorner](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfCorner.html)


``` python
EdgesOfCorner(corner_index=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- corner_index : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [edges_of_corner](/docs/GeoNodes/socket_GEOMETRY.md#edges_of_corner)

## Init

``` python
def __init__(self, corner_index=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeEdgesOfCorner', node_label=node_label, node_color=node_color, **kwargs)

    self.corner_index    = corner_index
```
