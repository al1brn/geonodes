# Node PrincipledVolume

- Node name : 'Principled Volume'
- bl_idname : [ShaderNodeVolumePrincipled](https://docs.blender.org/api/current/bpy.types.ShaderNodeVolumePrincipled.html)


``` python
PrincipledVolume(color=None, color_attribute=None, density=None, density_attribute=None, anisotropy=None, absorption_color=None, emission_strength=None, emission_color=None, blackbody_intensity=None, blackbody_tint=None, temperature=None, temperature_attribute=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- color : None
- color_attribute : None
- density : None
- density_attribute : None
- anisotropy : None
- absorption_color : None
- emission_strength : None
- emission_color : None
- blackbody_intensity : None
- blackbody_tint : None
- temperature : None
- temperature_attribute : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, color_attribute=None, density=None, density_attribute=None, anisotropy=None, absorption_color=None, emission_strength=None, emission_color=None, blackbody_intensity=None, blackbody_tint=None, temperature=None, temperature_attribute=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeVolumePrincipled', node_label=node_label, node_color=node_color, **kwargs)

    self.color           = color
    self.color_attribute = color_attribute
    self.density         = density
    self.density_attribute = density_attribute
    self.anisotropy      = anisotropy
    self.absorption_color = absorption_color
    self.emission_strength = emission_strength
    self.emission_color  = emission_color
    self.blackbody_intensity = blackbody_intensity
    self.blackbody_tint  = blackbody_tint
    self.temperature     = temperature
    self.temperature_attribute = temperature_attribute
```
