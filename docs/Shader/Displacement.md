# Node Displacement

- Node name : 'Displacement'
- bl_idname : ShaderNodeDisplacement


``` python
Displacement(height=None, midlevel=None, scale=None, normal=None, space='OBJECT', node_label=None, node_color=None)
```
##### Arguments

- height : None
- midlevel : None
- scale : None
- normal : None
- space : 'OBJECT'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, height=None, midlevel=None, scale=None, normal=None, space='OBJECT', node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeDisplacement', node_label=node_label, node_color=node_color)

    self.space           = space
    self.height          = height
    self.midlevel        = midlevel
    self.scale           = scale
    self.normal          = normal
```
