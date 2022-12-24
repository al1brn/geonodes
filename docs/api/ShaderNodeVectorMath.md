# Node *Vector Math*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
- geonodes name: `VectorMath`
- bl_idname: `ShaderNodeVectorMath`

```python
from geonodes import nodes

node = nodes.VectorMath(vector0=None, vector1=None, vector2=None, scale=None, operation='ADD')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeVectorMath.webp)

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

| Class or method name | Definition |
|----------------------|------------|
| **[Vector](Vector.md)** |
| [add](Vector.md#add) | `def add(self, vector=None):` |
| [subtract](Vector.md#subtract) | `def subtract(self, vector=None):` |
| [sub](Vector.md#sub) | `def sub(self, vector=None):` |
| [multiply](Vector.md#multiply) | `def multiply(self, vector=None):` |
| [mul](Vector.md#mul) | `def mul(self, vector=None):` |
| [divide](Vector.md#divide) | `def divide(self, vector=None):` |
| [div](Vector.md#div) | `def div(self, vector=None):` |
| [multiply_add](Vector.md#multiply_add) | `def multiply_add(self, multiplier=None, addend=None):` |
| [mul_add](Vector.md#mul_add) | `def mul_add(self, multiplier=None, addend=None):` |
| [cross_product](Vector.md#cross_product) | `def cross_product(self, vector=None):` |
| [cross](Vector.md#cross) | `def cross(self, vector=None):` |
| [project](Vector.md#project) | `def project(self, vector=None):` |
| [reflect](Vector.md#reflect) | `def reflect(self, vector=None):` |
| [refract](Vector.md#refract) | `def refract(self, vector=None, ior=None):` |
| [face_forward](Vector.md#face_forward) | `def face_forward(self, incident=None, reference=None):` |
| [dot_product](Vector.md#dot_product) | `def dot_product(self, vector=None):` |
| [dot](Vector.md#dot) | `def dot(self, vector=None):` |
| [distance](Vector.md#distance) | `def distance(self, vector=None):` |
| [length](Vector.md#length) | `@property`<br> `def length(self):` |
| [scale](Vector.md#scale) | `def scale(self, scale=None):` |
| [normalize](Vector.md#normalize) | `def normalize(self):` |
| [absolute](Vector.md#absolute) | `def absolute(self):` |
| [abs](Vector.md#abs) | `def abs(self):` |
| [minimum](Vector.md#minimum) | `def minimum(self, vector=None):` |
| [min](Vector.md#min) | `def min(self, vector=None):` |
| [maximum](Vector.md#maximum) | `def maximum(self, vector=None):` |
| [max](Vector.md#max) | `def max(self, vector=None):` |
| [floor](Vector.md#floor) | `def floor(self):` |
| [ceil](Vector.md#ceil) | `def ceil(self):` |
| [fraction](Vector.md#fraction) | `def fraction(self):` |
| [fract](Vector.md#fract) | `def fract(self):` |
| [modulo](Vector.md#modulo) | `def modulo(self, vector=None):` |
| [wrap](Vector.md#wrap) | `def wrap(self, max=None, min=None):` |
| [snap](Vector.md#snap) | `def snap(self, increment=None):` |
| [sine](Vector.md#sine) | `def sine(self):` |
| [sin](Vector.md#sin) | `def sin(self):` |
| [cosine](Vector.md#cosine) | `def cosine(self):` |
| [cos](Vector.md#cos) | `def cos(self):` |
| [tangent](Vector.md#tangent) | `def tangent(self):` |
| [tan](Vector.md#tan) | `def tan(self):` |

<sub>Go to [top](#node-Vector-Math) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

