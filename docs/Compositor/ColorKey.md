# Node ColorKey

- Node name : 'Color Key'
- bl_idname : CompositorNodeColorMatte


``` python
ColorKey(image=None, key_color=None, color_hue=0.009999999776482582, color_saturation=0.10000000149011612, color_value=0.10000000149011612, tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- image : None
- key_color : None
- color_hue : 0.009999999776482582
- color_saturation : 0.10000000149011612
- color_value : 0.10000000149011612
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, key_color=None, color_hue=0.009999999776482582, color_saturation=0.10000000149011612, color_value=0.10000000149011612, tag_need_exec=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeColorMatte', node_label=node_label, node_color=node_color)

    self.color_hue       = color_hue
    self.color_saturation = color_saturation
    self.color_value     = color_value
    self.tag_need_exec   = tag_need_exec
    self.image           = image
    self.key_color       = key_color
```
