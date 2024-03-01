# Node Math

- Node name : 'Math'
- bl_idname : [Math](https://docs.blender.org/api/current/bpy.types.Math.html)


``` python
Math(value=None, value_1=None, value_2=None, operation='ADD', use_clamp=False, node_label=None, node_color=None)
```
##### Arguments

- value : None
- value_1 : None
- value_2 : None
- operation : 'ADD'
- use_clamp : False

## Implementation

- [Float](/docs/Shader/Float.md) : [abs](/docs/Shader/Float.md#abs) [add](/docs/Shader/Float.md#add) [arccos](/docs/Shader/Float.md#arccos) [arcsin](/docs/Shader/Float.md#arcsin) [arctan](/docs/Shader/Float.md#arctan) [arctan2](/docs/Shader/Float.md#arctan2) [ceil](/docs/Shader/Float.md#ceil) [compare](/docs/Shader/Float.md#compare) [cos](/docs/Shader/Float.md#cos) [cosh](/docs/Shader/Float.md#cosh) [degrees](/docs/Shader/Float.md#degrees) [divide](/docs/Shader/Float.md#divide) [exp](/docs/Shader/Float.md#exp) [floor](/docs/Shader/Float.md#floor) [floored_modulo](/docs/Shader/Float.md#floored_modulo) [fract](/docs/Shader/Float.md#fract) [greater_than](/docs/Shader/Float.md#greater_than) [inverse_sqrt](/docs/Shader/Float.md#inverse_sqrt) [less_than](/docs/Shader/Float.md#less_than) [log](/docs/Shader/Float.md#log) [max](/docs/Shader/Float.md#max) [min](/docs/Shader/Float.md#min) [mod](/docs/Shader/Float.md#mod) [multiply](/docs/Shader/Float.md#multiply) [multiply_add](/docs/Shader/Float.md#multiply_add) [pingpong](/docs/Shader/Float.md#pingpong) [power](/docs/Shader/Float.md#power) [radians](/docs/Shader/Float.md#radians) [round](/docs/Shader/Float.md#round) [sign](/docs/Shader/Float.md#sign) [sin](/docs/Shader/Float.md#sin) [sinh](/docs/Shader/Float.md#sinh) [smooth_max](/docs/Shader/Float.md#smooth_max) [smooth_min](/docs/Shader/Float.md#smooth_min) [snap](/docs/Shader/Float.md#snap) [sqrt](/docs/Shader/Float.md#sqrt) [subtract](/docs/Shader/Float.md#subtract) [tan](/docs/Shader/Float.md#tan) [tanh](/docs/Shader/Float.md#tanh) [trunc](/docs/Shader/Float.md#trunc) [wrap](/docs/Shader/Float.md#wrap)
- Functions : [abs](/docs/Shader/Shader.md#abs) [add](/docs/Shader/Shader.md#add) [arccos](/docs/Shader/Shader.md#arccos) [arcsin](/docs/Shader/Shader.md#arcsin) [arctan](/docs/Shader/Shader.md#arctan) [arctan2](/docs/Shader/Shader.md#arctan2) [ceil](/docs/Shader/Shader.md#ceil) [compare](/docs/Shader/Shader.md#compare) [cos](/docs/Shader/Shader.md#cos) [cosh](/docs/Shader/Shader.md#cosh) [degrees](/docs/Shader/Shader.md#degrees) [divide](/docs/Shader/Shader.md#divide) [exp](/docs/Shader/Shader.md#exp) [floor](/docs/Shader/Shader.md#floor) [floored_modulo](/docs/Shader/Shader.md#floored_modulo) [fract](/docs/Shader/Shader.md#fract) [greater_than](/docs/Shader/Shader.md#greater_than) [inverse_sqrt](/docs/Shader/Shader.md#inverse_sqrt) [less_than](/docs/Shader/Shader.md#less_than) [log](/docs/Shader/Shader.md#log) [max](/docs/Shader/Shader.md#max) [min](/docs/Shader/Shader.md#min) [mod](/docs/Shader/Shader.md#mod) [multiply](/docs/Shader/Shader.md#multiply) [multiply_add](/docs/Shader/Shader.md#multiply_add) [pingpong](/docs/Shader/Shader.md#pingpong) [power](/docs/Shader/Shader.md#power) [radians](/docs/Shader/Shader.md#radians) [round](/docs/Shader/Shader.md#round) [sign](/docs/Shader/Shader.md#sign) [sin](/docs/Shader/Shader.md#sin) [sinh](/docs/Shader/Shader.md#sinh) [smooth_max](/docs/Shader/Shader.md#smooth_max) [smooth_min](/docs/Shader/Shader.md#smooth_min) [snap](/docs/Shader/Shader.md#snap) [sqrt](/docs/Shader/Shader.md#sqrt) [subtract](/docs/Shader/Shader.md#subtract) [tan](/docs/Shader/Shader.md#tan) [tanh](/docs/Shader/Shader.md#tanh) [trunc](/docs/Shader/Shader.md#trunc) [wrap](/docs/Shader/Shader.md#wrap)

## Init

``` python
def __init__(self, value=None, value_1=None, value_2=None, operation='ADD', use_clamp=False, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeMath', node_label=node_label, node_color=node_color)

    self.operation       = operation
    self.use_clamp       = use_clamp
    self.value           = value
    self.value_1         = value_1
    self.value_2         = value_2
```
