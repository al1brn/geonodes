# Node LineStyleOutput

- Node name : 'Line Style Output'
- bl_idname : [Line Style Output](https://docs.blender.org/api/current/bpy.types.Line Style Output.html)


``` python
LineStyleOutput(color=None, color_fac=None, alpha=None, alpha_fac=None, blend_type='MIX', is_active_output=True, target='ALL', use_alpha=False, use_clamp=False, node_label=None, node_color=None)
```
##### Arguments

- color : None
- color_fac : None
- alpha : None
- alpha_fac : None
- blend_type : 'MIX'
- is_active_output : True
- target : 'ALL'
- use_alpha : False
- use_clamp : False

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, color_fac=None, alpha=None, alpha_fac=None, blend_type='MIX', is_active_output=True, target='ALL', use_alpha=False, use_clamp=False, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeOutputLineStyle', node_label=node_label, node_color=node_color)

    self.blend_type      = blend_type
    self.is_active_output = is_active_output
    self.target          = target
    self.use_alpha       = use_alpha
    self.use_clamp       = use_clamp
    self.color           = color
    self.color_fac       = color_fac
    self.alpha           = alpha
    self.alpha_fac       = alpha_fac
```
