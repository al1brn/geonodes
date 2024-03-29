# Node VolumeScatter

- Node name : 'Volume Scatter'
- bl_idname : [ShaderNodeVolumeScatter](https://docs.blender.org/api/current/bpy.types.ShaderNodeVolumeScatter.html)


``` python
VolumeScatter(color=None, density=None, anisotropy=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- color : None
- density : None
- anisotropy : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, density=None, anisotropy=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeVolumeScatter', node_label=node_label, node_color=node_color, **kwargs)

    self.color           = color
    self.density         = density
    self.anisotropy      = anisotropy
```
