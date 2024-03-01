# Node Math

- Node name : 'Math'
- bl_idname : [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)


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
- Functions : [abs](/docs/Shader/ShaderTree.md#abs) [add](/docs/Shader/ShaderTree.md#add) [arccos](/docs/Shader/ShaderTree.md#arccos) [arcsin](/docs/Shader/ShaderTree.md#arcsin) [arctan](/docs/Shader/ShaderTree.md#arctan) [arctan2](/docs/Shader/ShaderTree.md#arctan2) [ceil](/docs/Shader/ShaderTree.md#ceil) [compare](/docs/Shader/ShaderTree.md#compare) [cos](/docs/Shader/ShaderTree.md#cos) [cosh](/docs/Shader/ShaderTree.md#cosh) [degrees](/docs/Shader/ShaderTree.md#degrees) [divide](/docs/Shader/ShaderTree.md#divide) [exp](/docs/Shader/ShaderTree.md#exp) [floor](/docs/Shader/ShaderTree.md#floor) [floored_modulo](/docs/Shader/ShaderTree.md#floored_modulo) [fract](/docs/Shader/ShaderTree.md#fract) [greater_than](/docs/Shader/ShaderTree.md#greater_than) [inverse_sqrt](/docs/Shader/ShaderTree.md#inverse_sqrt) [less_than](/docs/Shader/ShaderTree.md#less_than) [log](/docs/Shader/ShaderTree.md#log) [max](/docs/Shader/ShaderTree.md#max) [min](/docs/Shader/ShaderTree.md#min) [mod](/docs/Shader/ShaderTree.md#mod) [multiply](/docs/Shader/ShaderTree.md#multiply) [multiply_add](/docs/Shader/ShaderTree.md#multiply_add) [pingpong](/docs/Shader/ShaderTree.md#pingpong) [power](/docs/Shader/ShaderTree.md#power) [radians](/docs/Shader/ShaderTree.md#radians) [round](/docs/Shader/ShaderTree.md#round) [sign](/docs/Shader/ShaderTree.md#sign) [sin](/docs/Shader/ShaderTree.md#sin) [sinh](/docs/Shader/ShaderTree.md#sinh) [smooth_max](/docs/Shader/ShaderTree.md#smooth_max) [smooth_min](/docs/Shader/ShaderTree.md#smooth_min) [snap](/docs/Shader/ShaderTree.md#snap) [sqrt](/docs/Shader/ShaderTree.md#sqrt) [subtract](/docs/Shader/ShaderTree.md#subtract) [tan](/docs/Shader/ShaderTree.md#tan) [tanh](/docs/Shader/ShaderTree.md#tanh) [trunc](/docs/Shader/ShaderTree.md#trunc) [wrap](/docs/Shader/ShaderTree.md#wrap)

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
