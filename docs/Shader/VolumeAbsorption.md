# Node VolumeAbsorption

- Node name : 'Volume Absorption'
- bl_idname : [ShaderNodeVolumeAbsorption](https://docs.blender.org/api/current/bpy.types.ShaderNodeVolumeAbsorption.html)


``` python
VolumeAbsorption(color=None, density=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- color : None
- density : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, density=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeVolumeAbsorption', node_label=node_label, node_color=node_color, **kwargs)

    self.color           = color
    self.density         = density
```
