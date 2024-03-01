# Node Grid

- Node name : 'Grid'
- bl_idname : GeometryNodeMeshGrid


``` python
Grid(size_x=None, size_y=None, vertices_x=None, vertices_y=None, node_label=None, node_color=None)
```
##### Arguments

- size_x : None
- size_y : None
- vertices_x : None
- vertices_y : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, size_x=None, size_y=None, vertices_x=None, vertices_y=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeMeshGrid', node_label=node_label, node_color=node_color)

    self.size_x          = size_x
    self.size_y          = size_y
    self.vertices_x      = vertices_x
    self.vertices_y      = vertices_y
```
