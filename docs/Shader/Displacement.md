# Node Displacement

- Node name : 'Displacement'
- bl_idname : [ShaderNodeDisplacement](https://docs.blender.org/api/current/bpy.types.ShaderNodeDisplacement.html)


``` python
Displacement(height=None, midlevel=None, scale=None, normal=None, space='OBJECT', node_label=None, node_color=None, **kwargs)
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
def __init__(self, height=None, midlevel=None, scale=None, normal=None, space='OBJECT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeDisplacement', node_label=node_label, node_color=node_color, **kwargs)

    self.space           = space
    self.height          = height
    self.midlevel        = midlevel
    self.scale           = scale
    self.normal          = normal
```
