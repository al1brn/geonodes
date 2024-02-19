# class RefractionBSDF (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : RefractionBSDF
 - bl_idname : ShaderNodeBsdfRefraction

Node parameters
 - distribution : 'BECKMANN'

Input sockets
 - color : Col
 - roughness : Float
 - ior : Float
 - normal : Vect
 - weight : Float

Output sockets
 - bsdf : Shader

### Header

``` python
def RefractionBSDF(self, color=None, roughness=None, ior=None, normal=None, distribution='BECKMANN', node_label=None, node_color=None):
```

## Implementations

o functions : [refraction_bsdf](/docs/Shader_classes/GLOBAL.md#refraction_bsdf)


