# Node LightFalloff

- Node name : 'Light Falloff'
- bl_idname : [ShaderNodeLightFalloff](https://docs.blender.org/api/current/bpy.types.ShaderNodeLightFalloff.html)


``` python
LightFalloff(strength=None, smooth=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- strength : None
- smooth : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, strength=None, smooth=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeLightFalloff', node_label=node_label, node_color=node_color, **kwargs)

    self.strength        = strength
    self.smooth          = smooth
```
