# Node Reroute

- Node name : 'Reroute'
- bl_idname : [NodeReroute](https://docs.blender.org/api/current/bpy.types.NodeReroute.html)


``` python
Reroute(input=None, node_label=None, node_color=None)
```
##### Arguments

- input : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, input=None, node_label=None, node_color=None):

    Node.__init__(self, 'NodeReroute', node_label=node_label, node_color=node_color)

    self.input           = input
```
