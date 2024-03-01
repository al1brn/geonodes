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

- [Float](/docs/Compositor/Float.md) : [abs](/docs/Compositor/Float.md#abs) [add](/docs/Compositor/Float.md#add) [arccos](/docs/Compositor/Float.md#arccos) [arcsin](/docs/Compositor/Float.md#arcsin) [arctan](/docs/Compositor/Float.md#arctan) [arctan2](/docs/Compositor/Float.md#arctan2) [ceil](/docs/Compositor/Float.md#ceil) [compare](/docs/Compositor/Float.md#compare) [cos](/docs/Compositor/Float.md#cos) [cosh](/docs/Compositor/Float.md#cosh) [degrees](/docs/Compositor/Float.md#degrees) [divide](/docs/Compositor/Float.md#divide) [exp](/docs/Compositor/Float.md#exp) [floor](/docs/Compositor/Float.md#floor) [floored_modulo](/docs/Compositor/Float.md#floored_modulo) [fract](/docs/Compositor/Float.md#fract) [greater_than](/docs/Compositor/Float.md#greater_than) [inverse_sqrt](/docs/Compositor/Float.md#inverse_sqrt) [less_than](/docs/Compositor/Float.md#less_than) [log](/docs/Compositor/Float.md#log) [max](/docs/Compositor/Float.md#max) [min](/docs/Compositor/Float.md#min) [mod](/docs/Compositor/Float.md#mod) [multiply](/docs/Compositor/Float.md#multiply) [multiply_add](/docs/Compositor/Float.md#multiply_add) [pingpong](/docs/Compositor/Float.md#pingpong) [power](/docs/Compositor/Float.md#power) [radians](/docs/Compositor/Float.md#radians) [round](/docs/Compositor/Float.md#round) [sign](/docs/Compositor/Float.md#sign) [sin](/docs/Compositor/Float.md#sin) [sinh](/docs/Compositor/Float.md#sinh) [smooth_max](/docs/Compositor/Float.md#smooth_max) [smooth_min](/docs/Compositor/Float.md#smooth_min) [snap](/docs/Compositor/Float.md#snap) [sqrt](/docs/Compositor/Float.md#sqrt) [subtract](/docs/Compositor/Float.md#subtract) [tan](/docs/Compositor/Float.md#tan) [tanh](/docs/Compositor/Float.md#tanh) [trunc](/docs/Compositor/Float.md#trunc) [wrap](/docs/Compositor/Float.md#wrap)
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
