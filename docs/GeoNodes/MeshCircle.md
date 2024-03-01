# Node MeshCircle

- Node name : 'Mesh Circle'
- bl_idname : [Mesh Circle](https://docs.blender.org/api/current/bpy.types.Mesh Circle.html)


``` python
MeshCircle(vertices=None, radius=None, fill_type='NONE', node_label=None, node_color=None)
```
##### Arguments

- vertices : None
- radius : None
- fill_type : 'NONE'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, vertices=None, radius=None, fill_type='NONE', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeMeshCircle', node_label=node_label, node_color=node_color)

    self.fill_type       = fill_type
    self.vertices        = vertices
    self.radius          = radius
```
