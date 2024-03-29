# Node Bump

- Node name : 'Bump'
- bl_idname : [ShaderNodeBump](https://docs.blender.org/api/current/bpy.types.ShaderNodeBump.html)


``` python
Bump(strength=None, distance=None, height=None, normal=None, invert=False, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- strength : None
- distance : None
- height : None
- normal : None
- invert : False

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, strength=None, distance=None, height=None, normal=None, invert=False, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeBump', node_label=node_label, node_color=node_color, **kwargs)

    self.invert          = invert
    self.strength        = strength
    self.distance        = distance
    self.height          = height
    self.normal          = normal
```
