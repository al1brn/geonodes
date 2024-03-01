# Node UVSphere

- Node name : 'UV Sphere'
- bl_idname : [GeometryNodeMeshUVSphere](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshUVSphere.html)


``` python
UVSphere(segments=None, rings=None, radius=None, node_label=None, node_color=None)
```
##### Arguments

- segments : None
- rings : None
- radius : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, segments=None, rings=None, radius=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeMeshUVSphere', node_label=node_label, node_color=node_color)

    self.segments        = segments
    self.rings           = rings
    self.radius          = radius
```
