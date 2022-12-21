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

#### class [Vector](Vector.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3ddae0>>](Vector.md#add)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dd5a0>>](Vector.md#subtract)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dd930>>](Vector.md#sub)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dd8a0>>](Vector.md#multiply)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dfd00>>](Vector.md#mul)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dd9c0>>](Vector.md#divide)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dd780>>](Vector.md#div)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dd4e0>>](Vector.md#multiply_add)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3ddc00>>](Vector.md#mul_add)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3df790>>](Vector.md#cross_product)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3df730>>](Vector.md#cross)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3de530>>](Vector.md#project)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3de560>>](Vector.md#reflect)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3deaa0>>](Vector.md#refract)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dfe50>>](Vector.md#face_forward)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dfdf0>>](Vector.md#dot_product)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dfe80>>](Vector.md#dot)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dfee0>>](Vector.md#distance)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16e3dd240>>](Vector.md#length-property)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dff10>>](Vector.md#scale)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3df580>>](Vector.md#normalize)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3df3d0>>](Vector.md#absolute)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3df760>>](Vector.md#abs)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3df460>>](Vector.md#minimum)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dffa0>>](Vector.md#min)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dee60>>](Vector.md#maximum)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3df4c0>>](Vector.md#max)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3df7f0>>](Vector.md#floor)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3de2f0>>](Vector.md#ceil)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3de4d0>>](Vector.md#fraction)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3de410>>](Vector.md#fract)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dff70>>](Vector.md#modulo)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3df3a0>>](Vector.md#wrap)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dd1e0>>](Vector.md#snap)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dcaf0>>](Vector.md#sine)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3def50>>](Vector.md#sin)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3decb0>>](Vector.md#cosine)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dc910>>](Vector.md#cos)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dc7f0>>](Vector.md#tangent)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dca30>>](Vector.md#tan)
