# Node Mix

- Node name : 'Mix'
- bl_idname : [Mix](https://docs.blender.org/api/current/bpy.types.Mix.html)


``` python
Mix(fac=None, image=None, image_1=None, blend_type='MIX', tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None)
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

- [Col](/docs/Compositor/Col.md) : [mix](/docs/Compositor/Col.md#mix) [mix_add](/docs/Compositor/Col.md#mix_add) [mix_burn](/docs/Compositor/Col.md#mix_burn) [mix_color](/docs/Compositor/Col.md#mix_color) [mix_darken](/docs/Compositor/Col.md#mix_darken) [mix_difference](/docs/Compositor/Col.md#mix_difference) [mix_divide](/docs/Compositor/Col.md#mix_divide) [mix_dodge](/docs/Compositor/Col.md#mix_dodge) [mix_exclusion](/docs/Compositor/Col.md#mix_exclusion) [mix_hue](/docs/Compositor/Col.md#mix_hue) [mix_lighten](/docs/Compositor/Col.md#mix_lighten) [mix_linear_light](/docs/Compositor/Col.md#mix_linear_light) [mix_mix](/docs/Compositor/Col.md#mix_mix) [mix_multiply](/docs/Compositor/Col.md#mix_multiply) [mix_overlay](/docs/Compositor/Col.md#mix_overlay) [mix_saturation](/docs/Compositor/Col.md#mix_saturation) [mix_screen](/docs/Compositor/Col.md#mix_screen) [mix_soft_light](/docs/Compositor/Col.md#mix_soft_light) [mix_subtract](/docs/Compositor/Col.md#mix_subtract) [mix_value](/docs/Compositor/Col.md#mix_value)
- [Float](/docs/Compositor/Float.md) : [mix](/docs/Compositor/Float.md#mix)
- [Vect](/docs/Compositor/Vect.md) : [mix](/docs/Compositor/Vect.md#mix)

## Init

``` python
def __init__(self, fac=None, image=None, image_1=None, blend_type='MIX', tag_need_exec=None, use_alpha=False, use_clamp=False, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeMixRGB', node_label=node_label, node_color=node_color)

    self.blend_type      = blend_type
    self.tag_need_exec   = tag_need_exec
    self.use_alpha       = use_alpha
    self.use_clamp       = use_clamp
    self.fac             = fac
    self.image           = image
    self.image_1         = image_1
```
