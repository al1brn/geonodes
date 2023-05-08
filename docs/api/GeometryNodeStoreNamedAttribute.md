# Node *Store Named Attribute*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)
- geonodes name: `StoreNamedAttribute`
- bl_idname: `GeometryNodeStoreNamedAttribute`

```python
from geonodes import nodes

node = nodes.StoreNamedAttribute(geometry=None, selection=None, name=None, value=None, data_type='FLOAT', domain='POINT')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeStoreNamedAttribute.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **name**: [String](String.md)
- **value**: **data_type** dependant

#### Node parameter arguments:

- **data_type** (str): default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN', 'FLOAT2')
- **domain** (str): default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN', 'FLOAT2')
- Input sockets  : ['value']
- Output sockets : []
## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Domain](Domain.md)** |
| [store_named_attribute](Domain.md#store_named_attribute) | `def store_named_attribute(self, name=None, value=None):` |
| [store_named_float](Domain.md#store_named_float) | `def store_named_float(self, name=None, value=None):` |
| [store_named_integer](Domain.md#store_named_integer) | `def store_named_integer(self, name=None, value=None):` |
| [store_named_vector](Domain.md#store_named_vector) | `def store_named_vector(self, name=None, value=None):` |
| [store_named_color](Domain.md#store_named_color) | `def store_named_color(self, name=None, value=None):` |
| [store_named_byte_color](Domain.md#store_named_byte_color) | `def store_named_byte_color(self, name=None, value=None):` |
| [store_named_boolean](Domain.md#store_named_boolean) | `def store_named_boolean(self, name=None, value=None):` |
| [store_named_2D_vector](Domain.md#store_named_2D_vector) | `def store_named_2D_vector(self, name=None, value=None):` |
| **[Geometry](Geometry.md)** |
| [store_named_attribute](Geometry.md#store_named_attribute) | `def store_named_attribute(self, selection=None, name=None, value=None, domain='POINT'):` |
| [store_named_boolean](Geometry.md#store_named_boolean) | `def store_named_boolean(self, selection=None, name=None, value=None, domain='POINT'):` |
| [store_named_integer](Geometry.md#store_named_integer) | `def store_named_integer(self, selection=None, name=None, value=None, domain='POINT'):` |
| [store_named_float](Geometry.md#store_named_float) | `def store_named_float(self, selection=None, name=None, value=None, domain='POINT'):` |
| [store_named_vector](Geometry.md#store_named_vector) | `def store_named_vector(self, selection=None, name=None, value=None, domain='POINT'):` |
| [store_named_color](Geometry.md#store_named_color) | `def store_named_color(self, selection=None, name=None, value=None, domain='POINT'):` |

<sub>Go to [top](#node-Store-Named-Attribute) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

