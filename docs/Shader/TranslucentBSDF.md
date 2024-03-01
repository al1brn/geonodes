# Node TranslucentBSDF

- Node name : 'Translucent BSDF'
- bl_idname : ShaderNodeBsdfTranslucent


``` python
TranslucentBSDF(color=None, normal=None, node_label=None, node_color=None)
```
##### Arguments

- color : None
- normal : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, normal=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeBsdfTranslucent', node_label=node_label, node_color=node_color)

    self.color           = color
    self.normal          = normal
```
