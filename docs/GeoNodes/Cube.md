# Node Cube

- Node name : 'Cube'
- bl_idname : [GeometryNodeMeshCube](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCube.html)


``` python
Cube(size=None, vertices_x=None, vertices_y=None, vertices_z=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- size : None
- vertices_x : None
- vertices_y : None
- vertices_z : None

## Implementation

- Functions : [cube](/docs/GeoNodes/GeoNodesTree.md#cube)

## Init

``` python
def __init__(self, size=None, vertices_x=None, vertices_y=None, vertices_z=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeMeshCube', node_label=node_label, node_color=node_color, **kwargs)

    self.size            = size
    self.vertices_x      = vertices_x
    self.vertices_y      = vertices_y
    self.vertices_z      = vertices_z
```
