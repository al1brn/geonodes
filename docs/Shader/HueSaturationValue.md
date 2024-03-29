# Node HueSaturationValue

- Node name : 'Hue/Saturation/Value'
- bl_idname : [ShaderNodeHueSaturation](https://docs.blender.org/api/current/bpy.types.ShaderNodeHueSaturation.html)


``` python
HueSaturationValue(hue=None, saturation=None, value=None, fac=None, color=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- hue : None
- saturation : None
- value : None
- fac : None
- color : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, hue=None, saturation=None, value=None, fac=None, color=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeHueSaturation', node_label=node_label, node_color=node_color, **kwargs)

    self.hue             = hue
    self.saturation      = saturation
    self.value           = value
    self.fac             = fac
    self.color           = color
```
