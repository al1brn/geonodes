# Node Mix

- Node name : 'Mix'
- bl_idname : [CompositorNodeMixRGB](https://docs.blender.org/api/current/bpy.types.CompositorNodeMixRGB.html)


``` python
Mix(fac=None, image=None, image_1=None, blend_type='MIX', tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- fac : None
- image : None
- image_1 : None
- blend_type : 'MIX'
- tag_need_exec : None
- use_alpha : False
- use_clamp : False

## Implementation

- [RGBA](/docs/Compositor/socket_RGBA.md) : [mix](/docs/Compositor/socket_RGBA.md#mix) [mix_add](/docs/Compositor/socket_RGBA.md#mix_add) [mix_burn](/docs/Compositor/socket_RGBA.md#mix_burn) [mix_color](/docs/Compositor/socket_RGBA.md#mix_color) [mix_darken](/docs/Compositor/socket_RGBA.md#mix_darken) [mix_difference](/docs/Compositor/socket_RGBA.md#mix_difference) [mix_divide](/docs/Compositor/socket_RGBA.md#mix_divide) [mix_dodge](/docs/Compositor/socket_RGBA.md#mix_dodge) [mix_exclusion](/docs/Compositor/socket_RGBA.md#mix_exclusion) [mix_hue](/docs/Compositor/socket_RGBA.md#mix_hue) [mix_lighten](/docs/Compositor/socket_RGBA.md#mix_lighten) [mix_linear_light](/docs/Compositor/socket_RGBA.md#mix_linear_light) [mix_mix](/docs/Compositor/socket_RGBA.md#mix_mix) [mix_multiply](/docs/Compositor/socket_RGBA.md#mix_multiply) [mix_overlay](/docs/Compositor/socket_RGBA.md#mix_overlay) [mix_saturation](/docs/Compositor/socket_RGBA.md#mix_saturation) [mix_screen](/docs/Compositor/socket_RGBA.md#mix_screen) [mix_soft_light](/docs/Compositor/socket_RGBA.md#mix_soft_light) [mix_subtract](/docs/Compositor/socket_RGBA.md#mix_subtract) [mix_value](/docs/Compositor/socket_RGBA.md#mix_value)
- [VALUE](/docs/Compositor/socket_VALUE.md) : [mix](/docs/Compositor/socket_VALUE.md#mix)
- [VECTOR](/docs/Compositor/socket_VECTOR.md) : [mix](/docs/Compositor/socket_VECTOR.md#mix)

## Init

``` python
def __init__(self, fac=None, image=None, image_1=None, blend_type='MIX', tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeMixRGB', node_label=node_label, node_color=node_color, **kwargs)

    self.blend_type      = blend_type
    self.tag_need_exec   = tag_need_exec
    self.use_alpha       = use_alpha
    self.use_clamp       = use_clamp
    self.fac             = fac
    self.image           = image
    self.image_1         = image_1
```
