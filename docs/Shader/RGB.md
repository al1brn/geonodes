# Node RGB

- Node name : 'RGB'
- bl_idname : [ShaderNodeRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGB.html)


``` python
RGB(node_label=None, node_color=None, **kwargs)
```
## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeRGB', node_label=node_label, node_color=node_color, **kwargs)
```
