# Node RepeatInput

- Node name : 'Repeat Input'
- bl_idname : GeometryNodeRepeatInput


``` python
RepeatInput(iterations=None, pair_with_output=None, paired_output=None, node_label=None, node_color=None)
```
##### Arguments

- iterations : None
- pair_with_output : None
- paired_output : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, iterations=None, pair_with_output=None, paired_output=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeRepeatInput', node_label=node_label, node_color=node_color)

    self.pair_with_output = pair_with_output
    self.paired_output   = paired_output
    self.iterations      = iterations
```
