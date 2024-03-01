# Node PrincipledHairBSDF

- Node name : 'Principled Hair BSDF'
- bl_idname : ShaderNodeBsdfHairPrincipled


``` python
PrincipledHairBSDF(color=None, roughness=None, radial_roughness=None, coat=None, ior=None, offset=None, random_roughness=None, random=None, aspect_ratio=None, reflection=None, transmission=None, secondary_reflection=None, absorption_coefficient=None, melanin=None, melanin_redness=None, tint=None, random_color=None, model='CHIANG', parametrization='COLOR', node_label=None, node_color=None)
```
##### Arguments

- color : None
- roughness : None
- radial_roughness : None
- coat : None
- ior : None
- offset : None
- random_roughness : None
- random : None
- aspect_ratio : None
- reflection : None
- transmission : None
- secondary_reflection : None
- absorption_coefficient : None
- melanin : None
- melanin_redness : None
- tint : None
- random_color : None
- model : 'CHIANG'
- parametrization : 'COLOR'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, roughness=None, radial_roughness=None, coat=None, ior=None, offset=None, random_roughness=None, random=None, aspect_ratio=None, reflection=None, transmission=None, secondary_reflection=None, absorption_coefficient=None, melanin=None, melanin_redness=None, tint=None, random_color=None, model='CHIANG', parametrization='COLOR', node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeBsdfHairPrincipled', node_label=node_label, node_color=node_color)

    self.model           = model
    self.parametrization = parametrization
    self.color           = color
    self.roughness       = roughness
    self.radial_roughness = radial_roughness
    self.coat            = coat
    self.ior             = ior
    self.offset          = offset
    self.random_roughness = random_roughness
    self.random          = random
    self.aspect_ratio    = aspect_ratio
    self.reflection      = reflection
    self.transmission    = transmission
    self.secondary_reflection = secondary_reflection
    self.absorption_coefficient = absorption_coefficient
    self.melanin         = melanin
    self.melanin_redness = melanin_redness
    self.tint            = tint
    self.random_color    = random_color
```
