# Node AntiAliasing

- Node name : 'Anti-Aliasing'
- bl_idname : [CompositorNodeAntiAliasing](https://docs.blender.org/api/current/bpy.types.CompositorNodeAntiAliasing.html)


``` python
AntiAliasing(image=None, contrast_limit=0.20000000298023224, corner_rounding=0.25, tag_need_exec=None, threshold=1.0, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- contrast_limit : 0.20000000298023224
- corner_rounding : 0.25
- tag_need_exec : None
- threshold : 1.0

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, contrast_limit=0.20000000298023224, corner_rounding=0.25, tag_need_exec=None, threshold=1.0, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeAntiAliasing', node_label=node_label, node_color=node_color, **kwargs)

    self.contrast_limit  = contrast_limit
    self.corner_rounding = corner_rounding
    self.tag_need_exec   = tag_need_exec
    self.threshold       = threshold
    self.image           = image
```
