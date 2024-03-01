# Node String

- Node name : 'String'
- bl_idname : FunctionNodeInputString


``` python
String(string='', node_label=None, node_color=None)
```
##### Arguments

- string : 

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, string='', node_label=None, node_color=None):

    StackedNode.__init__(self, 'FunctionNodeInputString', node_label=node_label, node_color=node_color)

    self.string          = string
```
