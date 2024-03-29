# Node CameraData

- Node name : 'Camera Data'
- bl_idname : [ShaderNodeCameraData](https://docs.blender.org/api/current/bpy.types.ShaderNodeCameraData.html)


``` python
CameraData(node_label=None, node_color=None, **kwargs)
```
## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeCameraData', node_label=node_label, node_color=node_color, **kwargs)
```
