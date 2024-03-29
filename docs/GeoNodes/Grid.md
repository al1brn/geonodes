# Node Grid

- Node name : 'Grid'
- bl_idname : [GeometryNodeMeshGrid](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshGrid.html)


``` python
Grid(size_x=None, size_y=None, vertices_x=None, vertices_y=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- size_x : None
- size_y : None
- vertices_x : None
- vertices_y : None

## Implementation

- Functions : [grid](/docs/GeoNodes/GeoNodesTree.md#grid)

## Init

``` python
def __init__(self, size_x=None, size_y=None, vertices_x=None, vertices_y=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeMeshGrid', node_label=node_label, node_color=node_color, **kwargs)

    self.size_x          = size_x
    self.size_y          = size_y
    self.vertices_x      = vertices_x
    self.vertices_y      = vertices_y
```
