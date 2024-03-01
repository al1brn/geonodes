# Node Holdout

- Node name : 'Holdout'
- bl_idname : [Holdout](https://docs.blender.org/api/current/bpy.types.Holdout.html)


``` python
Holdout(node_label=None, node_color=None)
```
## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeHoldout', node_label=node_label, node_color=node_color)
```
