# Node ColorSpill

- Node name : 'Color Spill'
- bl_idname : [CompositorNodeColorSpill](https://docs.blender.org/api/current/bpy.types.CompositorNodeColorSpill.html)


``` python
ColorSpill(image=None, fac=None, channel='G', limit_channel='R', limit_method='SIMPLE', ratio=1.0, tag_need_exec=None, unspill_blue=0.0, unspill_green=0.0, unspill_red=0.0, use_unspill=False, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- fac : None
- channel : 'G'
- limit_channel : 'R'
- limit_method : 'SIMPLE'
- ratio : 1.0
- tag_need_exec : None
- unspill_blue : 0.0
- unspill_green : 0.0
- unspill_red : 0.0
- use_unspill : False

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, fac=None, channel='G', limit_channel='R', limit_method='SIMPLE', ratio=1.0, tag_need_exec=None, unspill_blue=0.0, unspill_green=0.0, unspill_red=0.0, use_unspill=False, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeColorSpill', node_label=node_label, node_color=node_color, **kwargs)

    self.channel         = channel
    self.limit_channel   = limit_channel
    self.limit_method    = limit_method
    self.ratio           = ratio
    self.tag_need_exec   = tag_need_exec
    self.unspill_blue    = unspill_blue
    self.unspill_green   = unspill_green
    self.unspill_red     = unspill_red
    self.use_unspill     = use_unspill
    self.image           = image
    self.fac             = fac
```
