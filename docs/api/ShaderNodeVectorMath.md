# Node Vector Math

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
- geonodes name: `VectorMath`
- bl_idname: `ShaderNodeVectorMath`

```python
from geonodes import nodes

node = nodes.VectorMath(vector0=None, vector1=None, vector2=None, scale=None, operation='ADD')
```

#### Input socket arguments:

- vector0: [Vector](Vector.md)
- vector1: [Vector](Vector.md)
- vector2: [Vector](Vector.md)
- scale: [Float](Float.md)

#### Node parameter arguments:

- operation (str): Node parameter, default = 'ADD' in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT')

#### Output sockets:

- **vector** : [Vector](Vector)
- **value** : [Float](Float)

