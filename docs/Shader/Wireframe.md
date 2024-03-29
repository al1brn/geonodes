# Node Wireframe

- Node name : 'Wireframe'
- bl_idname : [ShaderNodeWireframe](https://docs.blender.org/api/current/bpy.types.ShaderNodeWireframe.html)


``` python
Wireframe(size=None, use_pixel_size=False, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- size : None
- use_pixel_size : False

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, size=None, use_pixel_size=False, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeWireframe', node_label=node_label, node_color=node_color, **kwargs)

    self.use_pixel_size  = use_pixel_size
    self.size            = size
```
