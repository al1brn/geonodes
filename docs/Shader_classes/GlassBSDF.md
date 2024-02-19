# class GlassBSDF (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : GlassBSDF
 - bl_idname : ShaderNodeBsdfGlass

Node parameters
 - distribution : 'MULTI_GGX'

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
def GlassBSDF(self, color=None, roughness=None, ior=None, normal=None, distribution='MULTI_GGX', node_label=None, node_color=None):
```

## Implementations

o functions : [glass_bsdf](/docs/Shader_classes/GLOBAL.md#glass_bsdf)


