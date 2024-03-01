# Node LightPath

- Node name : 'Light Path'
- bl_idname : [Light Path](https://docs.blender.org/api/current/bpy.types.Light Path.html)


``` python
LightPath(node_label=None, node_color=None)
```
## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeLightPath', node_label=node_label, node_color=node_color)
```
