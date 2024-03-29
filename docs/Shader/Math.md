# Node Math

- Node name : 'Math'
- bl_idname : [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)


``` python
Math(value=None, value_1=None, value_2=None, operation='ADD', use_clamp=False, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- value : None
- value_1 : None
- value_2 : None
- operation : 'ADD'
- use_clamp : False

## Implementation

- [VALUE](/docs/Shader/socket_VALUE.md) : [abs](/docs/Shader/socket_VALUE.md#abs) [add](/docs/Shader/socket_VALUE.md#add) [arccos](/docs/Shader/socket_VALUE.md#arccos) [arcsin](/docs/Shader/socket_VALUE.md#arcsin) [arctan](/docs/Shader/socket_VALUE.md#arctan) [arctan2](/docs/Shader/socket_VALUE.md#arctan2) [ceil](/docs/Shader/socket_VALUE.md#ceil) [compare](/docs/Shader/socket_VALUE.md#compare) [cos](/docs/Shader/socket_VALUE.md#cos) [cosh](/docs/Shader/socket_VALUE.md#cosh) [degrees](/docs/Shader/socket_VALUE.md#degrees) [divide](/docs/Shader/socket_VALUE.md#divide) [exp](/docs/Shader/socket_VALUE.md#exp) [floor](/docs/Shader/socket_VALUE.md#floor) [floored_modulo](/docs/Shader/socket_VALUE.md#floored_modulo) [fract](/docs/Shader/socket_VALUE.md#fract) [greater_than](/docs/Shader/socket_VALUE.md#greater_than) [inverse_sqrt](/docs/Shader/socket_VALUE.md#inverse_sqrt) [less_than](/docs/Shader/socket_VALUE.md#less_than) [log](/docs/Shader/socket_VALUE.md#log) [max](/docs/Shader/socket_VALUE.md#max) [min](/docs/Shader/socket_VALUE.md#min) [mod](/docs/Shader/socket_VALUE.md#mod) [multiply](/docs/Shader/socket_VALUE.md#multiply) [multiply_add](/docs/Shader/socket_VALUE.md#multiply_add) [pingpong](/docs/Shader/socket_VALUE.md#pingpong) [power](/docs/Shader/socket_VALUE.md#power) [radians](/docs/Shader/socket_VALUE.md#radians) [round](/docs/Shader/socket_VALUE.md#round) [sign](/docs/Shader/socket_VALUE.md#sign) [sin](/docs/Shader/socket_VALUE.md#sin) [sinh](/docs/Shader/socket_VALUE.md#sinh) [smooth_max](/docs/Shader/socket_VALUE.md#smooth_max) [smooth_min](/docs/Shader/socket_VALUE.md#smooth_min) [snap](/docs/Shader/socket_VALUE.md#snap) [sqrt](/docs/Shader/socket_VALUE.md#sqrt) [subtract](/docs/Shader/socket_VALUE.md#subtract) [tan](/docs/Shader/socket_VALUE.md#tan) [tanh](/docs/Shader/socket_VALUE.md#tanh) [trunc](/docs/Shader/socket_VALUE.md#trunc) [wrap](/docs/Shader/socket_VALUE.md#wrap)
- Functions : [abs](/docs/Shader/ShaderTree.md#abs) [add](/docs/Shader/ShaderTree.md#add) [arccos](/docs/Shader/ShaderTree.md#arccos) [arcsin](/docs/Shader/ShaderTree.md#arcsin) [arctan](/docs/Shader/ShaderTree.md#arctan) [arctan2](/docs/Shader/ShaderTree.md#arctan2) [ceil](/docs/Shader/ShaderTree.md#ceil) [compare](/docs/Shader/ShaderTree.md#compare) [cos](/docs/Shader/ShaderTree.md#cos) [cosh](/docs/Shader/ShaderTree.md#cosh) [degrees](/docs/Shader/ShaderTree.md#degrees) [divide](/docs/Shader/ShaderTree.md#divide) [exp](/docs/Shader/ShaderTree.md#exp) [floor](/docs/Shader/ShaderTree.md#floor) [floored_modulo](/docs/Shader/ShaderTree.md#floored_modulo) [fract](/docs/Shader/ShaderTree.md#fract) [greater_than](/docs/Shader/ShaderTree.md#greater_than) [inverse_sqrt](/docs/Shader/ShaderTree.md#inverse_sqrt) [less_than](/docs/Shader/ShaderTree.md#less_than) [log](/docs/Shader/ShaderTree.md#log) [max](/docs/Shader/ShaderTree.md#max) [min](/docs/Shader/ShaderTree.md#min) [mod](/docs/Shader/ShaderTree.md#mod) [multiply](/docs/Shader/ShaderTree.md#multiply) [multiply_add](/docs/Shader/ShaderTree.md#multiply_add) [pingpong](/docs/Shader/ShaderTree.md#pingpong) [power](/docs/Shader/ShaderTree.md#power) [radians](/docs/Shader/ShaderTree.md#radians) [round](/docs/Shader/ShaderTree.md#round) [sign](/docs/Shader/ShaderTree.md#sign) [sin](/docs/Shader/ShaderTree.md#sin) [sinh](/docs/Shader/ShaderTree.md#sinh) [smooth_max](/docs/Shader/ShaderTree.md#smooth_max) [smooth_min](/docs/Shader/ShaderTree.md#smooth_min) [snap](/docs/Shader/ShaderTree.md#snap) [sqrt](/docs/Shader/ShaderTree.md#sqrt) [subtract](/docs/Shader/ShaderTree.md#subtract) [tan](/docs/Shader/ShaderTree.md#tan) [tanh](/docs/Shader/ShaderTree.md#tanh) [trunc](/docs/Shader/ShaderTree.md#trunc) [wrap](/docs/Shader/ShaderTree.md#wrap)

## Init

``` python
def __init__(self, value=None, value_1=None, value_2=None, operation='ADD', use_clamp=False, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeMath', node_label=node_label, node_color=node_color, **kwargs)

    self.operation       = operation
    self.use_clamp       = use_clamp
    self.value           = value
    self.value_1         = value_1
    self.value_2         = value_2
```
