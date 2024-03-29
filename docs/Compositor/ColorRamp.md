# Node ColorRamp

- Node name : 'Color Ramp'
- bl_idname : [CompositorNodeValToRGB](https://docs.blender.org/api/current/bpy.types.CompositorNodeValToRGB.html)


``` python
ColorRamp(fac=None, color_ramp=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- fac : None
- color_ramp : None
- tag_need_exec : None

## Implementation

- [VALUE](/docs/Compositor/socket_VALUE.md) : [color_ramp](/docs/Compositor/socket_VALUE.md#color_ramp)

## Init

``` python
def __init__(self, fac=None, color_ramp=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeValToRGB', node_label=node_label, node_color=node_color, **kwargs)

    self.color_ramp      = color_ramp
    self.tag_need_exec   = tag_need_exec
    self.fac             = fac
```
