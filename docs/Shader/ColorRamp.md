# Node ColorRamp

- Node name : 'Color Ramp'
- bl_idname : [Color Ramp](https://docs.blender.org/api/current/bpy.types.Color Ramp.html)


``` python
ColorRamp(fac=None, color_ramp=None, node_label=None, node_color=None)
```
##### Arguments

- fac : None
- color_ramp : None

## Implementation

- [Float](/docs/Shader/Float.md) : [color_ramp](/docs/Shader/Float.md#color_ramp)

## Init

``` python
def __init__(self, fac=None, color_ramp=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeValToRGB', node_label=node_label, node_color=node_color)

    self.color_ramp      = color_ramp
    self.fac             = fac
```
