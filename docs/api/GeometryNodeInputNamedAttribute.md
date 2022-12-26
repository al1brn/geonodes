# Node *Named Attribute*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)
- geonodes name: `NamedAttribute`
- bl_idname: `GeometryNodeInputNamedAttribute`

```python
from geonodes import nodes

node = nodes.NamedAttribute(name=None, data_type='FLOAT')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputNamedAttribute.webp)

### Args:

#### Input socket arguments:

- **name**: [String](String.md)

#### Node parameter arguments:

- **data_type** (str): default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')

### Output sockets:

- **attribute** : ``data_type`` dependant

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets  : []
- Output sockets : ['attribute']
## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Domain](Domain.md)** |
| [named_attribute](Domain.md#named_attribute) | `def named_attribute(self, name=None, data_type='FLOAT'):` |
| [named_float](Domain.md#named_float) | `def named_float(self, name=None):` |
| [named_integer](Domain.md#named_integer) | `def named_integer(self, name=None):` |
| [named_vector](Domain.md#named_vector) | `def named_vector(self, name=None):` |
| [named_color](Domain.md#named_color) | `def named_color(self, name=None):` |
| [named_boolean](Domain.md#named_boolean) | `def named_boolean(self, name=None):` |
| **[Geometry](Geometry.md)** |
| [named_attribute](Geometry.md#named_attribute) | `def named_attribute(self, name=None, data_type='FLOAT'):` |
| [named_float](Geometry.md#named_float) | `def named_float(self, name=None):` |
| [named_integer](Geometry.md#named_integer) | `def named_integer(self, name=None):` |
| [named_vector](Geometry.md#named_vector) | `def named_vector(self, name=None):` |
| [named_color](Geometry.md#named_color) | `def named_color(self, name=None):` |
| [named_boolean](Geometry.md#named_boolean) | `def named_boolean(self, name=None):` |

<sub>Go to [top](#node-Named-Attribute) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

