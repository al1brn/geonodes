# Node HueSaturationValue

- Node name : 'Hue/Saturation/Value'
- bl_idname : [CompositorNodeHueSat](https://docs.blender.org/api/current/bpy.types.CompositorNodeHueSat.html)


``` python
HueSaturationValue(image=None, hue=None, saturation=None, value=None, fac=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- hue : None
- saturation : None
- value : None
- fac : None
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, hue=None, saturation=None, value=None, fac=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeHueSat', node_label=node_label, node_color=node_color, **kwargs)

    self.tag_need_exec   = tag_need_exec
    self.image           = image
    self.hue             = hue
    self.saturation      = saturation
    self.value           = value
    self.fac             = fac
```
