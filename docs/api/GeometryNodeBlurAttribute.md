# Node *Blur Attribute*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/l.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)
- geonodes name: `BlurAttribute`
- bl_idname: `GeometryNodeBlurAttribute`

```python
from geonodes import nodes

node = nodes.BlurAttribute(value=None, iterations=None, weight=None, data_type='FLOAT')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeBlurAttribute.webp)

### Args:

#### Input socket arguments:

- **value**: **data_type** dependant
- **iterations**: [Integer](Integer.md)
- **weight**: [Float](Float.md)

#### Node parameter arguments:

- **data_type** (str): default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR')

### Output sockets:

- **value** : ``data_type`` dependant

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR')
- Input sockets  : ['value']
- Output sockets : ['value']
## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Domain](Domain.md)** |
| [blur_attribute](Domain.md#blur_attribute) | `def blur_attribute(self, value=None, iterations=None, weight=None):` |
| [blur_float](Domain.md#blur_float) | `def blur_float(self, value=None, iterations=None, weight=None):` |
| [blur_integer](Domain.md#blur_integer) | `def blur_integer(self, value=None, iterations=None, weight=None):` |
| [blur_vector](Domain.md#blur_vector) | `def blur_vector(self, value=None, iterations=None, weight=None):` |
| [blur_color](Domain.md#blur_color) | `def blur_color(self, value=None, iterations=None, weight=None):` |

<sub>Go to [top](#node-Blur-Attribute) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

