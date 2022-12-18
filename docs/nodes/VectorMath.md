
# Node VectorMath

> Geometry node name: [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)<br>
  Blender type: [Vector Math](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.VectorMath(vector0=None, vector1=None, vector2=None, scale=None, operation='ADD', label=None, node_color=None)
```



## Arguments


### Input sockets

- vector0 : Vector
- vector1 : Vector
- vector2 : Vector
- scale : Float

### Parameters

- operation : str (default = 'ADD') in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- vector : Vector
- value : Float
