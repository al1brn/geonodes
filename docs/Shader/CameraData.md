# Node CameraData

- Node name : 'Camera Data'
- bl_idname : [Camera Data](https://docs.blender.org/api/current/bpy.types.Camera Data.html)


``` python
CameraData(node_label=None, node_color=None)
```
## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeCameraData', node_label=node_label, node_color=node_color)
```
