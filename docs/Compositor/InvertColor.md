# Node InvertColor

- Node name : 'Invert Color'
- bl_idname : [CompositorNodeInvert](https://docs.blender.org/api/current/bpy.types.CompositorNodeInvert.html)


``` python
InvertColor(fac=None, color=None, invert_alpha=False, invert_rgb=True, tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- fac : None
- color : None
- invert_alpha : False
- invert_rgb : True
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, fac=None, color=None, invert_alpha=False, invert_rgb=True, tag_need_exec=None, node_label=None, node_color=None):

    Node.__init__(self, 'CompositorNodeInvert', node_label=node_label, node_color=node_color)

    self.invert_alpha    = invert_alpha
    self.invert_rgb      = invert_rgb
    self.tag_need_exec   = tag_need_exec
    self.fac             = fac
    self.color           = color
```
