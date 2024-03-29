# Node MeshCircle

- Node name : 'Mesh Circle'
- bl_idname : [GeometryNodeMeshCircle](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCircle.html)


``` python
MeshCircle(vertices=None, radius=None, fill_type='NONE', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vertices : None
- radius : None
- fill_type : 'NONE'

## Implementation

- Functions : [mesh_circle](/docs/GeoNodes/GeoNodesTree.md#mesh_circle)

## Init

``` python
def __init__(self, vertices=None, radius=None, fill_type='NONE', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeMeshCircle', node_label=node_label, node_color=node_color, **kwargs)

    self.fill_type       = fill_type
    self.vertices        = vertices
    self.radius          = radius
```
