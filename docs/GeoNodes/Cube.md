# Node Cube

- Node name : 'Cube'
- bl_idname : [GeometryNodeMeshCube](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
Cube(size=None, vertices_x=None, vertices_y=None, vertices_z=None, node_label=None, node_color=None)
```
##### Arguments

- size : None
- vertices_x : None
- vertices_y : None
- vertices_z : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, size=None, vertices_x=None, vertices_y=None, vertices_z=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeMeshCube', node_label=node_label, node_color=node_color)

    self.size            = size
    self.vertices_x      = vertices_x
    self.vertices_y      = vertices_y
    self.vertices_z      = vertices_z
```
