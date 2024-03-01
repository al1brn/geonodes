# Node SplitEdges

- Node name : 'Split Edges'
- bl_idname : GeometryNodeSplitEdges


``` python
SplitEdges(mesh=None, selection=None, node_label=None, node_color=None)
```
##### Arguments

- mesh : None
- selection : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [split_edges](/docs/GeoNodes/Geometry.md#split_edges)

## Init

``` python
def __init__(self, mesh=None, selection=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeSplitEdges', node_label=node_label, node_color=node_color)

    self.mesh            = mesh
    self.selection       = selection
```
