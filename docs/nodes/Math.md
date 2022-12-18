
# Node Math

> Geometry node name: [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)<br>
  Blender type: [Math](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Math(value0=None, value1=None, value2=None, operation='ADD', use_clamp=False, label=None, node_color=None)
```



## Arguments


### Input sockets

- value0 : Float
- value1 : Float
- value2 : Float

### Parameters

- operation : str (default = 'ADD') in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES')
- use_clamp : bool (default = False)

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- value : Float
