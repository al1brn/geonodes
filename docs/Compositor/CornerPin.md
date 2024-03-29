# Node CornerPin

- Node name : 'Corner Pin'
- bl_idname : [CompositorNodeCornerPin](https://docs.blender.org/api/current/bpy.types.CompositorNodeCornerPin.html)


``` python
CornerPin(image=None, upper_left=None, upper_right=None, lower_left=None, lower_right=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- upper_left : None
- upper_right : None
- lower_left : None
- lower_right : None
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, upper_left=None, upper_right=None, lower_left=None, lower_right=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeCornerPin', node_label=node_label, node_color=node_color, **kwargs)

    self.tag_need_exec   = tag_need_exec
    self.image           = image
    self.upper_left      = upper_left
    self.upper_right     = upper_right
    self.lower_left      = lower_left
    self.lower_right     = lower_right
```
