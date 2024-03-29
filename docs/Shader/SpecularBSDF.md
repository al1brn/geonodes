# Node SpecularBSDF

- Node name : 'Specular BSDF'
- bl_idname : [ShaderNodeEeveeSpecular](https://docs.blender.org/api/current/bpy.types.ShaderNodeEeveeSpecular.html)


``` python
SpecularBSDF(base_color=None, specular=None, roughness=None, emissive_color=None, transparency=None, normal=None, clear_coat=None, clear_coat_roughness=None, clear_coat_normal=None, ambient_occlusion=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- base_color : None
- specular : None
- roughness : None
- emissive_color : None
- transparency : None
- normal : None
- clear_coat : None
- clear_coat_roughness : None
- clear_coat_normal : None
- ambient_occlusion : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, base_color=None, specular=None, roughness=None, emissive_color=None, transparency=None, normal=None, clear_coat=None, clear_coat_roughness=None, clear_coat_normal=None, ambient_occlusion=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeEeveeSpecular', node_label=node_label, node_color=node_color, **kwargs)

    self.base_color      = base_color
    self.specular        = specular
    self.roughness       = roughness
    self.emissive_color  = emissive_color
    self.transparency    = transparency
    self.normal          = normal
    self.clear_coat      = clear_coat
    self.clear_coat_roughness = clear_coat_roughness
    self.clear_coat_normal = clear_coat_normal
    self.ambient_occlusion = ambient_occlusion
```
