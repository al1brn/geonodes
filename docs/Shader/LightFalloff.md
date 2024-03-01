# Node LightFalloff

- Node name : 'Light Falloff'
- bl_idname : [ShaderNodeLightFalloff](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
LightFalloff(strength=None, smooth=None, node_label=None, node_color=None)
```
##### Arguments

- strength : None
- smooth : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, strength=None, smooth=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeLightFalloff', node_label=node_label, node_color=node_color)

    self.strength        = strength
    self.smooth          = smooth
```
