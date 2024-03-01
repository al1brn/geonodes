# Node Wireframe

- Node name : 'Wireframe'
- bl_idname : ShaderNodeWireframe


``` python
Wireframe(size=None, use_pixel_size=False, node_label=None, node_color=None)
```
##### Arguments

- size : None
- use_pixel_size : False

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, size=None, use_pixel_size=False, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeWireframe', node_label=node_label, node_color=node_color)

    self.use_pixel_size  = use_pixel_size
    self.size            = size
```
