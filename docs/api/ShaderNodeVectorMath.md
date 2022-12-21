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

### Args:

#### Input socket arguments:

- **vector0**: [Vector](Vector.md)
- **vector1**: [Vector](Vector.md)
- **vector2**: [Vector](Vector.md)
- **scale**: [Float](Float.md)

#### Node parameter arguments:

- **operation** (str): default = 'ADD' in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT')

### Output sockets:

- **vector** : [Vector](Vector.md)
- **value** : [Float](Float.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee55300>>](Vector.md#add)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee552d0>>](Vector.md#subtract)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee552a0>>](Vector.md#sub)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee55270>>](Vector.md#multiply)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee55240>>](Vector.md#mul)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee55210>>](Vector.md#divide)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee551e0>>](Vector.md#div)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee551b0>>](Vector.md#multiply_add)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee55180>>](Vector.md#mul_add)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee55150>>](Vector.md#cross_product)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee55120>>](Vector.md#cross)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee550f0>>](Vector.md#project)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee550c0>>](Vector.md#reflect)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee55090>>](Vector.md#refract)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee55060>>](Vector.md#face_forward)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee55030>>](Vector.md#dot_product)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee55000>>](Vector.md#dot)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54fd0>>](Vector.md#distance)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16ee54fa0>>](Vector.md#length-property)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54f70>>](Vector.md#scale)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54f40>>](Vector.md#normalize)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54f10>>](Vector.md#absolute)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54ee0>>](Vector.md#abs)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54eb0>>](Vector.md#minimum)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54e80>>](Vector.md#min)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54e50>>](Vector.md#maximum)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54e20>>](Vector.md#max)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54df0>>](Vector.md#floor)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54dc0>>](Vector.md#ceil)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54d90>>](Vector.md#fraction)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54d60>>](Vector.md#fract)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54d30>>](Vector.md#modulo)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54d00>>](Vector.md#wrap)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54cd0>>](Vector.md#snap)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54ca0>>](Vector.md#sine)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54c70>>](Vector.md#sin)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54c40>>](Vector.md#cosine)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54c10>>](Vector.md#cos)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54be0>>](Vector.md#tangent)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54bb0>>](Vector.md#tan)
