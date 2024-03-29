# Node ObjectInfo

- Node name : 'Object Info'
- bl_idname : [ShaderNodeObjectInfo](https://docs.blender.org/api/current/bpy.types.ShaderNodeObjectInfo.html)


``` python
ObjectInfo(node_label=None, node_color=None, **kwargs)
```
## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeObjectInfo', node_label=node_label, node_color=node_color, **kwargs)
```
