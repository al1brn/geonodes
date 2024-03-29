# Node ActiveCamera

- Node name : 'Active Camera'
- bl_idname : [GeometryNodeInputActiveCamera](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputActiveCamera.html)


``` python
ActiveCamera(node_label=None, node_color=None, **kwargs)
```
## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputActiveCamera', node_label=node_label, node_color=node_color, **kwargs)
```
