# Node HueCorrect

- Node name : 'Hue Correct'
- bl_idname : [Hue Correct](https://docs.blender.org/api/current/bpy.types.Hue Correct.html)


``` python
HueCorrect(fac=None, image=None, mapping=None, tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- fac : None
- image : None
- mapping : None
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, fac=None, image=None, mapping=None, tag_need_exec=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeHueCorrect', node_label=node_label, node_color=node_color)

    self.mapping         = mapping
    self.tag_need_exec   = tag_need_exec
    self.fac             = fac
    self.image           = image
```
