# Node Math

- Node name : 'Math'
- bl_idname : [Math](https://docs.blender.org/api/current/bpy.types.Math.html)


``` python
Math(value=None, value_1=None, value_2=None, operation='ADD', tag_need_exec=None, use_clamp=False, node_label=None, node_color=None)
```
##### Arguments

- value : None
- value_1 : None
- value_2 : None
- operation : 'ADD'
- tag_need_exec : None
- use_clamp : False

## Implementation

- [Float](/docs/Compositor/Float.md) : [abs](/docs/Compositor/Float.md#abs) [add](/docs/Compositor/Float.md#add) [arccos](/docs/Compositor/Float.md#arccos) [arcsin](/docs/Compositor/Float.md#arcsin) [arctan](/docs/Compositor/Float.md#arctan) [arctan2](/docs/Compositor/Float.md#arctan2) [ceil](/docs/Compositor/Float.md#ceil) [compare](/docs/Compositor/Float.md#compare) [cos](/docs/Compositor/Float.md#cos) [cosh](/docs/Compositor/Float.md#cosh) [degrees](/docs/Compositor/Float.md#degrees) [divide](/docs/Compositor/Float.md#divide) [exp](/docs/Compositor/Float.md#exp) [floor](/docs/Compositor/Float.md#floor) [floored_modulo](/docs/Compositor/Float.md#floored_modulo) [fract](/docs/Compositor/Float.md#fract) [greater_than](/docs/Compositor/Float.md#greater_than) [inverse_sqrt](/docs/Compositor/Float.md#inverse_sqrt) [less_than](/docs/Compositor/Float.md#less_than) [log](/docs/Compositor/Float.md#log) [max](/docs/Compositor/Float.md#max) [min](/docs/Compositor/Float.md#min) [mod](/docs/Compositor/Float.md#mod) [multiply](/docs/Compositor/Float.md#multiply) [multiply_add](/docs/Compositor/Float.md#multiply_add) [pingpong](/docs/Compositor/Float.md#pingpong) [power](/docs/Compositor/Float.md#power) [radians](/docs/Compositor/Float.md#radians) [round](/docs/Compositor/Float.md#round) [sign](/docs/Compositor/Float.md#sign) [sin](/docs/Compositor/Float.md#sin) [sinh](/docs/Compositor/Float.md#sinh) [smooth_max](/docs/Compositor/Float.md#smooth_max) [smooth_min](/docs/Compositor/Float.md#smooth_min) [snap](/docs/Compositor/Float.md#snap) [sqrt](/docs/Compositor/Float.md#sqrt) [subtract](/docs/Compositor/Float.md#subtract) [tan](/docs/Compositor/Float.md#tan) [tanh](/docs/Compositor/Float.md#tanh) [trunc](/docs/Compositor/Float.md#trunc) [wrap](/docs/Compositor/Float.md#wrap)
- Functions : [abs](/docs/Compositor/Compositor.md#abs) [add](/docs/Compositor/Compositor.md#add) [arccos](/docs/Compositor/Compositor.md#arccos) [arcsin](/docs/Compositor/Compositor.md#arcsin) [arctan](/docs/Compositor/Compositor.md#arctan) [arctan2](/docs/Compositor/Compositor.md#arctan2) [ceil](/docs/Compositor/Compositor.md#ceil) [compare](/docs/Compositor/Compositor.md#compare) [cos](/docs/Compositor/Compositor.md#cos) [cosh](/docs/Compositor/Compositor.md#cosh) [degrees](/docs/Compositor/Compositor.md#degrees) [divide](/docs/Compositor/Compositor.md#divide) [exp](/docs/Compositor/Compositor.md#exp) [floor](/docs/Compositor/Compositor.md#floor) [floored_modulo](/docs/Compositor/Compositor.md#floored_modulo) [fract](/docs/Compositor/Compositor.md#fract) [greater_than](/docs/Compositor/Compositor.md#greater_than) [inverse_sqrt](/docs/Compositor/Compositor.md#inverse_sqrt) [less_than](/docs/Compositor/Compositor.md#less_than) [log](/docs/Compositor/Compositor.md#log) [max](/docs/Compositor/Compositor.md#max) [min](/docs/Compositor/Compositor.md#min) [mod](/docs/Compositor/Compositor.md#mod) [multiply](/docs/Compositor/Compositor.md#multiply) [multiply_add](/docs/Compositor/Compositor.md#multiply_add) [pingpong](/docs/Compositor/Compositor.md#pingpong) [power](/docs/Compositor/Compositor.md#power) [radians](/docs/Compositor/Compositor.md#radians) [round](/docs/Compositor/Compositor.md#round) [sign](/docs/Compositor/Compositor.md#sign) [sin](/docs/Compositor/Compositor.md#sin) [sinh](/docs/Compositor/Compositor.md#sinh) [smooth_max](/docs/Compositor/Compositor.md#smooth_max) [smooth_min](/docs/Compositor/Compositor.md#smooth_min) [snap](/docs/Compositor/Compositor.md#snap) [sqrt](/docs/Compositor/Compositor.md#sqrt) [subtract](/docs/Compositor/Compositor.md#subtract) [tan](/docs/Compositor/Compositor.md#tan) [tanh](/docs/Compositor/Compositor.md#tanh) [trunc](/docs/Compositor/Compositor.md#trunc) [wrap](/docs/Compositor/Compositor.md#wrap)

## Init

``` python
def __init__(self, value=None, value_1=None, value_2=None, operation='ADD', tag_need_exec=None, use_clamp=False, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeMath', node_label=node_label, node_color=node_color)

    self.operation       = operation
    self.tag_need_exec   = tag_need_exec
    self.use_clamp       = use_clamp
    self.value           = value
    self.value_1         = value_1
    self.value_2         = value_2
```
