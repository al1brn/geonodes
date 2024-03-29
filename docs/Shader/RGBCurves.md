# Node RGBCurves

- Node name : 'RGB Curves'
- bl_idname : [ShaderNodeRGBCurve](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBCurve.html)


``` python
RGBCurves(fac=None, color=None, mapping=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- fac : None
- color : None
- mapping : None

## Implementation

- [RGBA](/docs/Shader/socket_RGBA.md) : [rgb_curves](/docs/Shader/socket_RGBA.md#rgb_curves)

## Init

``` python
def __init__(self, fac=None, color=None, mapping=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeRGBCurve', node_label=node_label, node_color=node_color, **kwargs)

    self.mapping         = mapping
    self.fac             = fac
    self.color           = color
```
