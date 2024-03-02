# Node RGBCurves

- Node name : 'RGB Curves'
- bl_idname : [CompositorNodeCurveRGB](https://docs.blender.org/api/current/bpy.types.CompositorNodeCurveRGB.html)


``` python
RGBCurves(fac=None, image=None, black_level=None, white_level=None, mapping=None, tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- fac : None
- image : None
- black_level : None
- white_level : None
- mapping : None
- tag_need_exec : None

## Implementation

- [RGBA](/docs/Compositor/RGBA.md) : [rgb_curves](/docs/Compositor/RGBA.md#rgb_curves)

## Init

``` python
def __init__(self, fac=None, image=None, black_level=None, white_level=None, mapping=None, tag_need_exec=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeCurveRGB', node_label=node_label, node_color=node_color)

    self.mapping         = mapping
    self.tag_need_exec   = tag_need_exec
    self.fac             = fac
    self.image           = image
    self.black_level     = black_level
    self.white_level     = white_level
```
