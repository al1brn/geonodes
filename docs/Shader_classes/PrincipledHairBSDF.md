# class PrincipledHairBSDF (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : PrincipledHairBSDF
 - bl_idname : ShaderNodeBsdfHairPrincipled

Node parameters
 - model : 'CHIANG'
 - parametrization : 'COLOR'

Input sockets
 - color : Col
 - melanin : Float
 - melanin_redness : Float
 - tint : Col
 - absorption_coefficient : Vect
 - aspect_ratio : Float
 - roughness : Float
 - radial_roughness : Float
 - coat : Float
 - ior : Float
 - offset : Float
 - random_color : Float
 - random_roughness : Float
 - random : Float
 - weight : Float
 - reflection : Float
 - transmission : Float
 - secondary_reflection : Float

Output sockets
 - bsdf : Shader

### Header

``` python
def PrincipledHairBSDF(self, color=None, roughness=None, radial_roughness=None, coat=None, ior=None, offset=None, random_roughness=None, random=None, aspect_ratio=None, reflection=None, transmission=None, secondary_reflection=None,
absorption_coefficient=None, melanin=None, melanin_redness=None, tint=None, random_color=None, model='CHIANG', parametrization='COLOR', node_label=None, node_color=None):
```

## Implementations

o functions : [principled_hair_bsdf](/docs/Shader_classes/GLOBAL.md#principled_hair_bsdf)


