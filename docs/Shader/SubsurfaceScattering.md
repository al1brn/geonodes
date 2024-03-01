# Node SubsurfaceScattering

- Node name : 'Subsurface Scattering'
- bl_idname : [Subsurface Scattering](https://docs.blender.org/api/current/bpy.types.Subsurface Scattering.html)


``` python
SubsurfaceScattering(color=None, scale=None, radius=None, ior=None, anisotropy=None, normal=None, falloff='RANDOM_WALK', node_label=None, node_color=None)
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
def __init__(self, color=None, scale=None, radius=None, ior=None, anisotropy=None, normal=None, falloff='RANDOM_WALK', node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeSubsurfaceScattering', node_label=node_label, node_color=node_color)

    self.falloff         = falloff
    self.color           = color
    self.scale           = scale
    self.radius          = radius
    self.ior             = ior
    self.anisotropy      = anisotropy
    self.normal          = normal
```
