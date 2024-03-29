# Node ChannelKey

- Node name : 'Channel Key'
- bl_idname : [CompositorNodeChannelMatte](https://docs.blender.org/api/current/bpy.types.CompositorNodeChannelMatte.html)


``` python
ChannelKey(image=None, color_space='RGB', limit_channel='R', limit_max=1.0, limit_method='MAX', limit_min=0.0, matte_channel='G', tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- color_space : 'RGB'
- limit_channel : 'R'
- limit_max : 1.0
- limit_method : 'MAX'
- limit_min : 0.0
- matte_channel : 'G'
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, color_space='RGB', limit_channel='R', limit_max=1.0, limit_method='MAX', limit_min=0.0, matte_channel='G', tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeChannelMatte', node_label=node_label, node_color=node_color, **kwargs)

    self.color_space     = color_space
    self.limit_channel   = limit_channel
    self.limit_max       = limit_max
    self.limit_method    = limit_method
    self.limit_min       = limit_min
    self.matte_channel   = matte_channel
    self.tag_need_exec   = tag_need_exec
    self.image           = image
```
