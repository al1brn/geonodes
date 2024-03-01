# Node LightOutput

- Node name : 'Light Output'
- bl_idname : [Light Output](https://docs.blender.org/api/current/bpy.types.Light Output.html)


``` python
LightOutput(surface=None, is_active_output=True, target='ALL', node_label=None, node_color=None)
```
##### Arguments

- surface : None
- is_active_output : True
- target : 'ALL'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, surface=None, is_active_output=True, target='ALL', node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeOutputLight', node_label=node_label, node_color=node_color)

    self.is_active_output = is_active_output
    self.target          = target
    self.surface         = surface
```
