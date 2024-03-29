# Node ColorRamp

- Node name : 'Color Ramp'
- bl_idname : [ShaderNodeValToRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html)


``` python
ColorRamp(fac=None, color_ramp=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- fac : None
- color_ramp : None

## Implementation

- [VALUE](/docs/Shader/socket_VALUE.md) : [color_ramp](/docs/Shader/socket_VALUE.md#color_ramp)

## Init

``` python
def __init__(self, fac=None, color_ramp=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeValToRGB', node_label=node_label, node_color=node_color, **kwargs)

    self.color_ramp      = color_ramp
    self.fac             = fac
```
