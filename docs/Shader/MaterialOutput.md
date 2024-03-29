# Node MaterialOutput

- Node name : 'Material Output'
- bl_idname : [ShaderNodeOutputMaterial](https://docs.blender.org/api/current/bpy.types.ShaderNodeOutputMaterial.html)


``` python
MaterialOutput(surface=None, volume=None, displacement=None, is_active_output=True, target='ALL', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- surface : None
- volume : None
- displacement : None
- is_active_output : True
- target : 'ALL'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, surface=None, volume=None, displacement=None, is_active_output=True, target='ALL', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeOutputMaterial', node_label=node_label, node_color=node_color, **kwargs)

    self.is_active_output = is_active_output
    self.target          = target
    self.surface         = surface
    self.volume          = volume
    self.displacement    = displacement
```
