# Node UVAlongStroke

- Node name : 'UV Along Stroke'
- bl_idname : ShaderNodeUVAlongStroke


``` python
UVAlongStroke(use_tips=False, node_label=None, node_color=None)
```
##### Arguments

- use_tips : False

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, use_tips=False, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeUVAlongStroke', node_label=node_label, node_color=node_color)

    self.use_tips        = use_tips
```
