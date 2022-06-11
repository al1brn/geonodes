
# Node Math

> Geometry node name: [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html)<br>
  Blender type: [Math](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Math(value0=None, value1=None, value2=None, operation='ADD', label=None)
```



## Arguments


### Input sockets

value0 : Float
- value1 : Float
- value2 : Float

### Parameters

operation : str (default = 'ADD') in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

value : Float

## Data sockets

> Data socket classes implementing this node.
  
[class_name](/docs/sockets/Float.md) [abs](/docs/sockets/Float.md#abs) : Method
- [class_name](/docs/sockets/Float.md) [add](/docs/sockets/Float.md#add) : Method
- [class_name](/docs/sockets/Float.md) [arccos](/docs/sockets/Float.md#arccos) : Method
- [class_name](/docs/sockets/Float.md) [arcsin](/docs/sockets/Float.md#arcsin) : Method
- [class_name](/docs/sockets/Float.md) [arctan](/docs/sockets/Float.md#arctan) : Method
- [class_name](/docs/sockets/Float.md) [arctan2](/docs/sockets/Float.md#arctan2) : Method
- [class_name](/docs/sockets/Float.md) [ceil](/docs/sockets/Float.md#ceil) : Method
- [class_name](/docs/sockets/Float.md) [compare](/docs/sockets/Float.md#compare) : Method
- [class_name](/docs/sockets/Float.md) [cos](/docs/sockets/Float.md#cos) : Method
- [class_name](/docs/sockets/Float.md) [cosh](/docs/sockets/Float.md#cosh) : Method
- [class_name](/docs/sockets/Float.md) [degrees](/docs/sockets/Float.md#degrees) : Method
- [class_name](/docs/sockets/Float.md) [divide](/docs/sockets/Float.md#divide) : Method
- [class_name](/docs/sockets/Float.md) [exp](/docs/sockets/Float.md#exp) : Method
- [class_name](/docs/sockets/Float.md) [floor](/docs/sockets/Float.md#floor) : Method
- [class_name](/docs/sockets/Float.md) [fract](/docs/sockets/Float.md#fract) : Method
- [class_name](/docs/sockets/Float.md) [greater_than](/docs/sockets/Float.md#greater_than) : Method
- [class_name](/docs/sockets/Float.md) [inverse_sqrt](/docs/sockets/Float.md#inverse_sqrt) : Method
- [class_name](/docs/sockets/Float.md) [less_than](/docs/sockets/Float.md#less_than) : Method
- [class_name](/docs/sockets/Float.md) [log](/docs/sockets/Float.md#log) : Method
- [class_name](/docs/sockets/Float.md) [max](/docs/sockets/Float.md#max) : Method
- [class_name](/docs/sockets/Float.md) [min](/docs/sockets/Float.md#min) : Method
- [class_name](/docs/sockets/Float.md) [modulo](/docs/sockets/Float.md#modulo) : Method
- [class_name](/docs/sockets/Float.md) [multiply](/docs/sockets/Float.md#multiply) : Method
- [class_name](/docs/sockets/Float.md) [multiply_add](/docs/sockets/Float.md#multiply_add) : Method
- [class_name](/docs/sockets/Float.md) [pingpong](/docs/sockets/Float.md#pingpong) : Method
- [class_name](/docs/sockets/Float.md) [pow](/docs/sockets/Float.md#pow) : Method
- [class_name](/docs/sockets/Float.md) [radians](/docs/sockets/Float.md#radians) : Method
- [class_name](/docs/sockets/Float.md) [round](/docs/sockets/Float.md#round) : Method
- [class_name](/docs/sockets/Float.md) [sign](/docs/sockets/Float.md#sign) : Method
- [class_name](/docs/sockets/Float.md) [sin](/docs/sockets/Float.md#sin) : Method
- [class_name](/docs/sockets/Float.md) [sinh](/docs/sockets/Float.md#sinh) : Method
- [class_name](/docs/sockets/Float.md) [smooth_max](/docs/sockets/Float.md#smooth_max) : Method
- [class_name](/docs/sockets/Float.md) [smooth_min](/docs/sockets/Float.md#smooth_min) : Method
- [class_name](/docs/sockets/Float.md) [snap](/docs/sockets/Float.md#snap) : Method
- [class_name](/docs/sockets/Float.md) [sqrt](/docs/sockets/Float.md#sqrt) : Method
- [class_name](/docs/sockets/Float.md) [subtract](/docs/sockets/Float.md#subtract) : Method
- [class_name](/docs/sockets/Float.md) [tan](/docs/sockets/Float.md#tan) : Method
- [class_name](/docs/sockets/Float.md) [tanh](/docs/sockets/Float.md#tanh) : Method
- [class_name](/docs/sockets/Float.md) [trunc](/docs/sockets/Float.md#trunc) : Method
- [class_name](/docs/sockets/Float.md) [wrap](/docs/sockets/Float.md#wrap) : Method
- [class_name](/docs/sockets/Integer.md) [abs](/docs/sockets/Integer.md#abs) : Method
- [class_name](/docs/sockets/Integer.md) [add](/docs/sockets/Integer.md#add) : Method
- [class_name](/docs/sockets/Integer.md) [arccos](/docs/sockets/Integer.md#arccos) : Method
- [class_name](/docs/sockets/Integer.md) [arcsin](/docs/sockets/Integer.md#arcsin) : Method
- [class_name](/docs/sockets/Integer.md) [arctan](/docs/sockets/Integer.md#arctan) : Method
- [class_name](/docs/sockets/Integer.md) [arctan2](/docs/sockets/Integer.md#arctan2) : Method
- [class_name](/docs/sockets/Integer.md) [ceil](/docs/sockets/Integer.md#ceil) : Method
- [class_name](/docs/sockets/Integer.md) [compare](/docs/sockets/Integer.md#compare) : Method
- [class_name](/docs/sockets/Integer.md) [cos](/docs/sockets/Integer.md#cos) : Method
- [class_name](/docs/sockets/Integer.md) [cosh](/docs/sockets/Integer.md#cosh) : Method
- [class_name](/docs/sockets/Integer.md) [degrees](/docs/sockets/Integer.md#degrees) : Method
- [class_name](/docs/sockets/Integer.md) [divide](/docs/sockets/Integer.md#divide) : Method
- [class_name](/docs/sockets/Integer.md) [exp](/docs/sockets/Integer.md#exp) : Method
- [class_name](/docs/sockets/Integer.md) [floor](/docs/sockets/Integer.md#floor) : Method
- [class_name](/docs/sockets/Integer.md) [fract](/docs/sockets/Integer.md#fract) : Method
- [class_name](/docs/sockets/Integer.md) [greater_than](/docs/sockets/Integer.md#greater_than) : Method
- [class_name](/docs/sockets/Integer.md) [inverse_sqrt](/docs/sockets/Integer.md#inverse_sqrt) : Method
- [class_name](/docs/sockets/Integer.md) [less_than](/docs/sockets/Integer.md#less_than) : Method
- [class_name](/docs/sockets/Integer.md) [log](/docs/sockets/Integer.md#log) : Method
- [class_name](/docs/sockets/Integer.md) [max](/docs/sockets/Integer.md#max) : Method
- [class_name](/docs/sockets/Integer.md) [min](/docs/sockets/Integer.md#min) : Method
- [class_name](/docs/sockets/Integer.md) [modulo](/docs/sockets/Integer.md#modulo) : Method
- [class_name](/docs/sockets/Integer.md) [multiply](/docs/sockets/Integer.md#multiply) : Method
- [class_name](/docs/sockets/Integer.md) [multiply_add](/docs/sockets/Integer.md#multiply_add) : Method
- [class_name](/docs/sockets/Integer.md) [pingpong](/docs/sockets/Integer.md#pingpong) : Method
- [class_name](/docs/sockets/Integer.md) [pow](/docs/sockets/Integer.md#pow) : Method
- [class_name](/docs/sockets/Integer.md) [radians](/docs/sockets/Integer.md#radians) : Method
- [class_name](/docs/sockets/Integer.md) [round](/docs/sockets/Integer.md#round) : Method
- [class_name](/docs/sockets/Integer.md) [sign](/docs/sockets/Integer.md#sign) : Method
- [class_name](/docs/sockets/Integer.md) [sin](/docs/sockets/Integer.md#sin) : Method
- [class_name](/docs/sockets/Integer.md) [sinh](/docs/sockets/Integer.md#sinh) : Method
- [class_name](/docs/sockets/Integer.md) [smooth_max](/docs/sockets/Integer.md#smooth_max) : Method
- [class_name](/docs/sockets/Integer.md) [smooth_min](/docs/sockets/Integer.md#smooth_min) : Method
- [class_name](/docs/sockets/Integer.md) [snap](/docs/sockets/Integer.md#snap) : Method
- [class_name](/docs/sockets/Integer.md) [sqrt](/docs/sockets/Integer.md#sqrt) : Method
- [class_name](/docs/sockets/Integer.md) [subtract](/docs/sockets/Integer.md#subtract) : Method
- [class_name](/docs/sockets/Integer.md) [tan](/docs/sockets/Integer.md#tan) : Method
- [class_name](/docs/sockets/Integer.md) [tanh](/docs/sockets/Integer.md#tanh) : Method
- [class_name](/docs/sockets/Integer.md) [trunc](/docs/sockets/Integer.md#trunc) : Method
- [class_name](/docs/sockets/Integer.md) [wrap](/docs/sockets/Integer.md#wrap) : Method
- [class_name](/docs/sockets/functions.md) [abs](/docs/sockets/functions.md#abs) : Function
- [class_name](/docs/sockets/functions.md) [add](/docs/sockets/functions.md#add) : Function
- [class_name](/docs/sockets/functions.md) [arccos](/docs/sockets/functions.md#arccos) : Function
- [class_name](/docs/sockets/functions.md) [arcsin](/docs/sockets/functions.md#arcsin) : Function
- [class_name](/docs/sockets/functions.md) [arctan](/docs/sockets/functions.md#arctan) : Function
- [class_name](/docs/sockets/functions.md) [arctan2](/docs/sockets/functions.md#arctan2) : Function
- [class_name](/docs/sockets/functions.md) [ceil](/docs/sockets/functions.md#ceil) : Function
- [class_name](/docs/sockets/functions.md) [compare](/docs/sockets/functions.md#compare) : Function
- [class_name](/docs/sockets/functions.md) [cos](/docs/sockets/functions.md#cos) : Function
- [class_name](/docs/sockets/functions.md) [cosh](/docs/sockets/functions.md#cosh) : Function
- [class_name](/docs/sockets/functions.md) [degrees](/docs/sockets/functions.md#degrees) : Function
- [class_name](/docs/sockets/functions.md) [divide](/docs/sockets/functions.md#divide) : Function
- [class_name](/docs/sockets/functions.md) [exp](/docs/sockets/functions.md#exp) : Function
- [class_name](/docs/sockets/functions.md) [floor](/docs/sockets/functions.md#floor) : Function
- [class_name](/docs/sockets/functions.md) [fract](/docs/sockets/functions.md#fract) : Function
- [class_name](/docs/sockets/functions.md) [greater_than](/docs/sockets/functions.md#greater_than) : Function
- [class_name](/docs/sockets/functions.md) [inverse_sqrt](/docs/sockets/functions.md#inverse_sqrt) : Function
- [class_name](/docs/sockets/functions.md) [less_than](/docs/sockets/functions.md#less_than) : Function
- [class_name](/docs/sockets/functions.md) [log](/docs/sockets/functions.md#log) : Function
- [class_name](/docs/sockets/functions.md) [max](/docs/sockets/functions.md#max) : Function
- [class_name](/docs/sockets/functions.md) [min](/docs/sockets/functions.md#min) : Function
- [class_name](/docs/sockets/functions.md) [modulo](/docs/sockets/functions.md#modulo) : Function
- [class_name](/docs/sockets/functions.md) [multiply](/docs/sockets/functions.md#multiply) : Function
- [class_name](/docs/sockets/functions.md) [multiply_add](/docs/sockets/functions.md#multiply_add) : Function
- [class_name](/docs/sockets/functions.md) [pingpong](/docs/sockets/functions.md#pingpong) : Function
- [class_name](/docs/sockets/functions.md) [pow](/docs/sockets/functions.md#pow) : Function
- [class_name](/docs/sockets/functions.md) [radians](/docs/sockets/functions.md#radians) : Function
- [class_name](/docs/sockets/functions.md) [round](/docs/sockets/functions.md#round) : Function
- [class_name](/docs/sockets/functions.md) [sign](/docs/sockets/functions.md#sign) : Function
- [class_name](/docs/sockets/functions.md) [sin](/docs/sockets/functions.md#sin) : Function
- [class_name](/docs/sockets/functions.md) [sinh](/docs/sockets/functions.md#sinh) : Function
- [class_name](/docs/sockets/functions.md) [smooth_max](/docs/sockets/functions.md#smooth_max) : Function
- [class_name](/docs/sockets/functions.md) [smooth_min](/docs/sockets/functions.md#smooth_min) : Function
- [class_name](/docs/sockets/functions.md) [snap](/docs/sockets/functions.md#snap) : Function
- [class_name](/docs/sockets/functions.md) [sqrt](/docs/sockets/functions.md#sqrt) : Function
- [class_name](/docs/sockets/functions.md) [subtract](/docs/sockets/functions.md#subtract) : Function
- [class_name](/docs/sockets/functions.md) [tan](/docs/sockets/functions.md#tan) : Function
- [class_name](/docs/sockets/functions.md) [tanh](/docs/sockets/functions.md#tanh) : Function
- [class_name](/docs/sockets/functions.md) [trunc](/docs/sockets/functions.md#trunc) : Function
- [class_name](/docs/sockets/functions.md) [wrap](/docs/sockets/functions.md#wrap) : Function
  
