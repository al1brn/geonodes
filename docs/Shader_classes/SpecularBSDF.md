# class SpecularBSDF (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : SpecularBSDF
 - bl_idname : ShaderNodeEeveeSpecular

Node parameters

Input sockets
 - base_color : Col
 - specular : Col
 - roughness : Float
 - emissive_color : Col
 - transparency : Float
 - normal : Vect
 - clear_coat : Float
 - clear_coat_roughness : Float
 - clear_coat_normal : Vect
 - ambient_occlusion : Float
 - weight : Float

Output sockets
 - bsdf : Shader

### Header

``` python
def SpecularBSDF(self, base_color=None, specular=None, roughness=None, emissive_color=None, transparency=None, normal=None, clear_coat=None, clear_coat_roughness=None, clear_coat_normal=None, ambient_occlusion=None, node_label=None, node_color=None):
```

## Implementations

o functions : [specular_bsdf](/docs/Shader_classes/specular_bsdf.md)

