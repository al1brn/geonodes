# Node Group

- Node name : 'Group'
- bl_idname : GeometryNodeGroup


``` python
Group(node_tree=None, node_label=None, node_color=None)
```
##### Arguments

- node_tree : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, node_tree=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeGroup', node_label=node_label, node_color=node_color)

    self.node_tree       = node_tree
```
