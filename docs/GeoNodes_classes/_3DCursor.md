# Node Math

- Node name : 'Math'
- bl_idname : ShaderNodeMath


``` python
Math(value=None, value_1=None, value_2=None, operation='ADD', use_clamp=False, node_label=None, node_color=None)
```
##### Arguments

- value : None
- value_1 : None
- value_2 : None
- operation : ADD
- use_clamp : False

## Implementation

- [Float](/docs/Float.md) : [abs](/docs/abs.md#abs) [add](/docs/add.md#add) [arccos](/docs/arccos.md#arccos) [arcsin](/docs/arcsin.md#arcsin) [arctan](/docs/arctan.md#arctan) [arctan2](/docs/arctan2.md#arctan2) [ceil](/docs/ceil.md#ceil) [compare](/docs/compare.md#compare) [cos](/docs/cos.md#cos) [cosh](/docs/cosh.md#cosh) [degrees](/docs/degrees.md#degrees) [divide](/docs/divide.md#divide) [exp](/docs/exp.md#exp) [floored_modulo](/docs/floored_modulo.md#floored_modulo) [fract](/docs/fract.md#fract) [inverse_sqrt](/docs/inverse_sqrt.md#inverse_sqrt) [log](/docs/log.md#log) [math_floor](/docs/math_floor.md#math_floor) [math_greater_than](/docs/math_greater_than.md#math_greater_than) [math_less_than](/docs/math_less_than.md#math_less_than) [math_round](/docs/math_round.md#math_round) [max](/docs/max.md#max) [min](/docs/min.md#min) [mod](/docs/mod.md#mod) [multiply](/docs/multiply.md#multiply) [multiply_add](/docs/multiply_add.md#multiply_add) [pingpong](/docs/pingpong.md#pingpong) [power](/docs/power.md#power) [radians](/docs/radians.md#radians) [sign](/docs/sign.md#sign) [sin](/docs/sin.md#sin) [sinh](/docs/sinh.md#sinh) [smooth_max](/docs/smooth_max.md#smooth_max) [smooth_min](/docs/smooth_min.md#smooth_min) [snap](/docs/snap.md#snap) [sqrt](/docs/sqrt.md#sqrt) [subtract](/docs/subtract.md#subtract) [tan](/docs/tan.md#tan) [tanh](/docs/tanh.md#tanh) [trunc](/docs/trunc.md#trunc) [wrap](/docs/wrap.md#wrap)
- [Int](/docs/Int.md) : [abs](/docs/abs.md#abs) [add](/docs/add.md#add) [arccos](/docs/arccos.md#arccos) [arcsin](/docs/arcsin.md#arcsin) [arctan](/docs/arctan.md#arctan) [arctan2](/docs/arctan2.md#arctan2) [ceil](/docs/ceil.md#ceil) [compare](/docs/compare.md#compare) [cos](/docs/cos.md#cos) [cosh](/docs/cosh.md#cosh) [degrees](/docs/degrees.md#degrees) [divide](/docs/divide.md#divide) [exp](/docs/exp.md#exp) [floored_modulo](/docs/floored_modulo.md#floored_modulo) [fract](/docs/fract.md#fract) [inverse_sqrt](/docs/inverse_sqrt.md#inverse_sqrt) [log](/docs/log.md#log) [math_floor](/docs/math_floor.md#math_floor) [math_greater_than](/docs/math_greater_than.md#math_greater_than) [math_less_than](/docs/math_less_than.md#math_less_than) [math_round](/docs/math_round.md#math_round) [max](/docs/max.md#max) [min](/docs/min.md#min) [mod](/docs/mod.md#mod) [multiply](/docs/multiply.md#multiply) [multiply_add](/docs/multiply_add.md#multiply_add) [pingpong](/docs/pingpong.md#pingpong) [power](/docs/power.md#power) [radians](/docs/radians.md#radians) [sign](/docs/sign.md#sign) [sin](/docs/sin.md#sin) [sinh](/docs/sinh.md#sinh) [smooth_max](/docs/smooth_max.md#smooth_max) [smooth_min](/docs/smooth_min.md#smooth_min) [snap](/docs/snap.md#snap) [sqrt](/docs/sqrt.md#sqrt) [subtract](/docs/subtract.md#subtract) [tan](/docs/tan.md#tan) [tanh](/docs/tanh.md#tanh) [trunc](/docs/trunc.md#trunc) [wrap](/docs/wrap.md#wrap)
- Functions : [abs](/docs/abs.md#abs) [add](/docs/add.md#add) [arccos](/docs/arccos.md#arccos) [arcsin](/docs/arcsin.md#arcsin) [arctan](/docs/arctan.md#arctan) [arctan2](/docs/arctan2.md#arctan2) [ceil](/docs/ceil.md#ceil) [compare](/docs/compare.md#compare) [cos](/docs/cos.md#cos) [cosh](/docs/cosh.md#cosh) [degrees](/docs/degrees.md#degrees) [divide](/docs/divide.md#divide) [exp](/docs/exp.md#exp) [floored_modulo](/docs/floored_modulo.md#floored_modulo) [fract](/docs/fract.md#fract) [inverse_sqrt](/docs/inverse_sqrt.md#inverse_sqrt) [log](/docs/log.md#log) [math_floor](/docs/math_floor.md#math_floor) [math_greater_than](/docs/math_greater_than.md#math_greater_than) [math_less_than](/docs/math_less_than.md#math_less_than) [math_round](/docs/math_round.md#math_round) [max](/docs/max.md#max) [min](/docs/min.md#min) [mod](/docs/mod.md#mod) [multiply](/docs/multiply.md#multiply) [multiply_add](/docs/multiply_add.md#multiply_add) [pingpong](/docs/pingpong.md#pingpong) [power](/docs/power.md#power) [radians](/docs/radians.md#radians) [sign](/docs/sign.md#sign) [sin](/docs/sin.md#sin) [sinh](/docs/sinh.md#sinh) [smooth_max](/docs/smooth_max.md#smooth_max) [smooth_min](/docs/smooth_min.md#smooth_min) [snap](/docs/snap.md#snap) [sqrt](/docs/sqrt.md#sqrt) [subtract](/docs/subtract.md#subtract) [tan](/docs/tan.md#tan) [tanh](/docs/tanh.md#tanh) [trunc](/docs/trunc.md#trunc) [wrap](/docs/wrap.md#wrap)

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
