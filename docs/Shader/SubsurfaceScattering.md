# Node SubsurfaceScattering

- Node name : 'Subsurface Scattering'
- bl_idname : [ShaderNodeSubsurfaceScattering](https://docs.blender.org/api/current/bpy.types.ShaderNodeSubsurfaceScattering.html)


``` python
SubsurfaceScattering(color=None, scale=None, radius=None, ior=None, anisotropy=None, normal=None, falloff='RANDOM_WALK', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- color : None
- scale : None
- radius : None
- ior : None
- anisotropy : None
- normal : None
- falloff : 'RANDOM_WALK'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, scale=None, radius=None, ior=None, anisotropy=None, normal=None, falloff='RANDOM_WALK', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeSubsurfaceScattering', node_label=node_label, node_color=node_color, **kwargs)

    self.falloff         = falloff
    self.color           = color
    self.scale           = scale
    self.radius          = radius
    self.ior             = ior
    self.anisotropy      = anisotropy
    self.normal          = normal
```
