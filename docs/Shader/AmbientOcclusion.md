# Node AmbientOcclusion

- Node name : 'Ambient Occlusion'
- bl_idname : ShaderNodeAmbientOcclusion


``` python
AmbientOcclusion(color=None, distance=None, normal=None, inside=False, only_local=False, samples=16, node_label=None, node_color=None)
```
##### Arguments

- color : None
- distance : None
- normal : None
- inside : False
- only_local : False
- samples : 16

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, distance=None, normal=None, inside=False, only_local=False, samples=16, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeAmbientOcclusion', node_label=node_label, node_color=node_color)

    self.inside          = inside
    self.only_local      = only_local
    self.samples         = samples
    self.color           = color
    self.distance        = distance
    self.normal          = normal
```
