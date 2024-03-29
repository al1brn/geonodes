# Node LightOutput

- Node name : 'Light Output'
- bl_idname : [ShaderNodeOutputLight](https://docs.blender.org/api/current/bpy.types.ShaderNodeOutputLight.html)


``` python
LightOutput(surface=None, is_active_output=True, target='ALL', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- surface : None
- is_active_output : True
- target : 'ALL'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, surface=None, is_active_output=True, target='ALL', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeOutputLight', node_label=node_label, node_color=node_color, **kwargs)

    self.is_active_output = is_active_output
    self.target          = target
    self.surface         = surface
```
