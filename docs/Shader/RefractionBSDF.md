# Node RefractionBSDF

- Node name : 'Refraction BSDF'
- bl_idname : ShaderNodeBsdfRefraction


``` python
RefractionBSDF(color=None, roughness=None, ior=None, normal=None, distribution='BECKMANN', node_label=None, node_color=None)
```
##### Arguments

- color : None
- roughness : None
- ior : None
- normal : None
- distribution : 'BECKMANN'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, roughness=None, ior=None, normal=None, distribution='BECKMANN', node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeBsdfRefraction', node_label=node_label, node_color=node_color)

    self.distribution    = distribution
    self.color           = color
    self.roughness       = roughness
    self.ior             = ior
    self.normal          = normal
```
