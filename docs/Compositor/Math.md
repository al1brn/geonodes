# Node Math

- Node name : 'Math'
- bl_idname : [CompositorNodeMath](https://docs.blender.org/api/current/bpy.types.CompositorNodeMath.html)


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

- [VALUE](/docs/Compositor/VALUE.md) : [abs](/docs/Compositor/VALUE.md#abs) [add](/docs/Compositor/VALUE.md#add) [arccos](/docs/Compositor/VALUE.md#arccos) [arcsin](/docs/Compositor/VALUE.md#arcsin) [arctan](/docs/Compositor/VALUE.md#arctan) [arctan2](/docs/Compositor/VALUE.md#arctan2) [ceil](/docs/Compositor/VALUE.md#ceil) [compare](/docs/Compositor/VALUE.md#compare) [cos](/docs/Compositor/VALUE.md#cos) [cosh](/docs/Compositor/VALUE.md#cosh) [degrees](/docs/Compositor/VALUE.md#degrees) [divide](/docs/Compositor/VALUE.md#divide) [exp](/docs/Compositor/VALUE.md#exp) [floor](/docs/Compositor/VALUE.md#floor) [floored_modulo](/docs/Compositor/VALUE.md#floored_modulo) [fract](/docs/Compositor/VALUE.md#fract) [greater_than](/docs/Compositor/VALUE.md#greater_than) [inverse_sqrt](/docs/Compositor/VALUE.md#inverse_sqrt) [less_than](/docs/Compositor/VALUE.md#less_than) [log](/docs/Compositor/VALUE.md#log) [max](/docs/Compositor/VALUE.md#max) [min](/docs/Compositor/VALUE.md#min) [mod](/docs/Compositor/VALUE.md#mod) [multiply](/docs/Compositor/VALUE.md#multiply) [multiply_add](/docs/Compositor/VALUE.md#multiply_add) [pingpong](/docs/Compositor/VALUE.md#pingpong) [power](/docs/Compositor/VALUE.md#power) [radians](/docs/Compositor/VALUE.md#radians) [round](/docs/Compositor/VALUE.md#round) [sign](/docs/Compositor/VALUE.md#sign) [sin](/docs/Compositor/VALUE.md#sin) [sinh](/docs/Compositor/VALUE.md#sinh) [smooth_max](/docs/Compositor/VALUE.md#smooth_max) [smooth_min](/docs/Compositor/VALUE.md#smooth_min) [snap](/docs/Compositor/VALUE.md#snap) [sqrt](/docs/Compositor/VALUE.md#sqrt) [subtract](/docs/Compositor/VALUE.md#subtract) [tan](/docs/Compositor/VALUE.md#tan) [tanh](/docs/Compositor/VALUE.md#tanh) [trunc](/docs/Compositor/VALUE.md#trunc) [wrap](/docs/Compositor/VALUE.md#wrap)
- Functions : [abs](/docs/Compositor/CompositorTree.md#abs) [add](/docs/Compositor/CompositorTree.md#add) [arccos](/docs/Compositor/CompositorTree.md#arccos) [arcsin](/docs/Compositor/CompositorTree.md#arcsin) [arctan](/docs/Compositor/CompositorTree.md#arctan) [arctan2](/docs/Compositor/CompositorTree.md#arctan2) [ceil](/docs/Compositor/CompositorTree.md#ceil) [compare](/docs/Compositor/CompositorTree.md#compare) [cos](/docs/Compositor/CompositorTree.md#cos) [cosh](/docs/Compositor/CompositorTree.md#cosh) [degrees](/docs/Compositor/CompositorTree.md#degrees) [divide](/docs/Compositor/CompositorTree.md#divide) [exp](/docs/Compositor/CompositorTree.md#exp) [floor](/docs/Compositor/CompositorTree.md#floor) [floored_modulo](/docs/Compositor/CompositorTree.md#floored_modulo) [fract](/docs/Compositor/CompositorTree.md#fract) [greater_than](/docs/Compositor/CompositorTree.md#greater_than) [inverse_sqrt](/docs/Compositor/CompositorTree.md#inverse_sqrt) [less_than](/docs/Compositor/CompositorTree.md#less_than) [log](/docs/Compositor/CompositorTree.md#log) [max](/docs/Compositor/CompositorTree.md#max) [min](/docs/Compositor/CompositorTree.md#min) [mod](/docs/Compositor/CompositorTree.md#mod) [multiply](/docs/Compositor/CompositorTree.md#multiply) [multiply_add](/docs/Compositor/CompositorTree.md#multiply_add) [pingpong](/docs/Compositor/CompositorTree.md#pingpong) [power](/docs/Compositor/CompositorTree.md#power) [radians](/docs/Compositor/CompositorTree.md#radians) [round](/docs/Compositor/CompositorTree.md#round) [sign](/docs/Compositor/CompositorTree.md#sign) [sin](/docs/Compositor/CompositorTree.md#sin) [sinh](/docs/Compositor/CompositorTree.md#sinh) [smooth_max](/docs/Compositor/CompositorTree.md#smooth_max) [smooth_min](/docs/Compositor/CompositorTree.md#smooth_min) [snap](/docs/Compositor/CompositorTree.md#snap) [sqrt](/docs/Compositor/CompositorTree.md#sqrt) [subtract](/docs/Compositor/CompositorTree.md#subtract) [tan](/docs/Compositor/CompositorTree.md#tan) [tanh](/docs/Compositor/CompositorTree.md#tanh) [trunc](/docs/Compositor/CompositorTree.md#trunc) [wrap](/docs/Compositor/CompositorTree.md#wrap)

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
