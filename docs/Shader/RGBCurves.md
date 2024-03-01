# Node RGBCurves

- Node name : 'RGB Curves'
- bl_idname : [RGB Curves](https://docs.blender.org/api/current/bpy.types.RGB Curves.html)


``` python
RGBCurves(fac=None, color=None, mapping=None, node_label=None, node_color=None)
```
##### Arguments

- fac : None
- color : None
- mapping : None

## Implementation

- [Col](/docs/Shader/Col.md) : [rgb_curves](/docs/Shader/Col.md#rgb_curves)

## Init

``` python
def __init__(self, fac=None, color=None, mapping=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeRGBCurve', node_label=node_label, node_color=node_color)

    self.mapping         = mapping
    self.fac             = fac
    self.color           = color
```
