# Node GroupInput

- Node name : 'Group Input'
- bl_idname : [NodeGroupInput](https://docs.blender.org/api/current/bpy.types.NodeGroupInput.html)


``` python
GroupInput(node_label=None, node_color=None, **kwargs)
```
## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'NodeGroupInput', node_label=node_label, node_color=node_color, **kwargs)
```
