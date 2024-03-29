# Node Holdout

- Node name : 'Holdout'
- bl_idname : [ShaderNodeHoldout](https://docs.blender.org/api/current/bpy.types.ShaderNodeHoldout.html)


``` python
Holdout(node_label=None, node_color=None, **kwargs)
```
## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeHoldout', node_label=node_label, node_color=node_color, **kwargs)
```
