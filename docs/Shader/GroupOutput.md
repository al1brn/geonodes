# Node GroupOutput

- Node name : 'Group Output'
- bl_idname : [NodeGroupOutput](https://docs.blender.org/api/current/bpy.types.NodeGroupOutput.html)


``` python
GroupOutput(is_active_output=True, node_label=None, node_color=None)
```
##### Arguments

- is_active_output : True

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, is_active_output=True, node_label=None, node_color=None):

    Node.__init__(self, 'NodeGroupOutput', node_label=node_label, node_color=node_color)

    self.is_active_output = is_active_output
```
