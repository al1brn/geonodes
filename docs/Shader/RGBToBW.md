# Node RGBToBW

- Node name : 'RGB to BW'
- bl_idname : ShaderNodeRGBToBW


``` python
RGBToBW(color=None, node_label=None, node_color=None)
```
##### Arguments

- color : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeRGBToBW', node_label=node_label, node_color=node_color)

    self.color           = color
```
