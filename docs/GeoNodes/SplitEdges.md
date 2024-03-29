# Node SplitEdges

- Node name : 'Split Edges'
- bl_idname : [GeometryNodeSplitEdges](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitEdges.html)


``` python
SplitEdges(mesh=None, selection=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- mesh : None
- selection : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [split_edges](/docs/GeoNodes/socket_GEOMETRY.md#split_edges)

## Init

``` python
def __init__(self, mesh=None, selection=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeSplitEdges', node_label=node_label, node_color=node_color, **kwargs)

    self.mesh            = mesh
    self.selection       = selection
```
