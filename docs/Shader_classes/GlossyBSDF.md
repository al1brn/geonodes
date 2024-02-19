# class GlossyBSDF (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : GlossyBSDF
 - bl_idname : ShaderNodeBsdfAnisotropic

Node parameters
 - distribution : 'MULTI_GGX'

Input sockets
 - color : Col
 - roughness : Float
 - anisotropy : Float
 - rotation : Float
 - normal : Vect
 - tangent : Vect
 - weight : Float

Output sockets
 - bsdf : Shader

### Header

``` python
def GlossyBSDF(self, color=None, roughness=None, anisotropy=None, rotation=None, normal=None, tangent=None, distribution='MULTI_GGX', node_label=None, node_color=None):
```

## Implementations

o functions : [glossy_bsdf](/docs/Shader_classes/GLOBAL.md#glossy_bsdf)

