# Node Bevel

- Node name : 'Bevel'
- bl_idname : [ShaderNodeBevel](https://docs.blender.org/api/current/bpy.types.ShaderNodeBevel.html)


``` python
Bevel(radius=None, normal=None, samples=4, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- radius : None
- normal : None
- samples : 4

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, radius=None, normal=None, samples=4, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeBevel', node_label=node_label, node_color=node_color, **kwargs)

    self.samples         = samples
    self.radius          = radius
    self.normal          = normal
```
