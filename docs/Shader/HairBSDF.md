# Node HairBSDF

- Node name : 'Hair BSDF'
- bl_idname : [ShaderNodeBsdfHair](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfHair.html)


``` python
HairBSDF(color=None, offset=None, roughnessu=None, roughnessv=None, tangent=None, component='Reflection', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- color : None
- offset : None
- roughnessu : None
- roughnessv : None
- tangent : None
- component : Reflection

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, offset=None, roughnessu=None, roughnessv=None, tangent=None, component='Reflection', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeBsdfHair', node_label=node_label, node_color=node_color, **kwargs)

    self.component       = component
    self.color           = color
    self.offset          = offset
    self.roughnessu      = roughnessu
    self.roughnessv      = roughnessv
    self.tangent         = tangent
```
