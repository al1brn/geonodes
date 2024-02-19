# class SubsurfaceScattering (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : SubsurfaceScattering
 - bl_idname : ShaderNodeSubsurfaceScattering

Node parameters
 - falloff : 'RANDOM_WALK'

Input sockets
 - color : Col
 - scale : Float
 - radius : Vect
 - ior : Float
 - anisotropy : Float
 - normal : Vect
 - weight : Float

Output sockets
 - bssrdf : Shader

### Header

``` python
def SubsurfaceScattering(self, color=None, scale=None, radius=None, ior=None, anisotropy=None, normal=None, falloff='RANDOM_WALK', node_label=None, node_color=None):
```

## Implementations

o functions : [subsurface_scattering](/docs/Shader_classes/GLOBAL.md#subsurface_scattering)


