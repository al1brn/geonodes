# Node BrightnessContrast

- Node name : 'Brightness/Contrast'
- bl_idname : [Brightness/Contrast](https://docs.blender.org/api/current/bpy.types.Brightness/Contrast.html)


``` python
BrightnessContrast(color=None, bright=None, contrast=None, node_label=None, node_color=None)
```
##### Arguments

- color : None
- bright : None
- contrast : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, bright=None, contrast=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeBrightContrast', node_label=node_label, node_color=node_color)

    self.color           = color
    self.bright          = bright
    self.contrast        = contrast
```
