# Node Frame

- Node name : 'Frame'
- bl_idname : NodeFrame


``` python
Frame(label_size=20, shrink=True, text=None, node_label=None, node_color=None)
```
##### Arguments

- label_size : 20
- shrink : True
- text : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, label_size=20, shrink=True, text=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'NodeFrame', node_label=node_label, node_color=node_color)

    self.label_size      = label_size
    self.shrink          = shrink
    self.text            = text
```
