# Node Store Named Attribute

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)
- geonodes name: `StoreNamedAttribute`
- bl_idname: `GeometryNodeStoreNamedAttribute`

```python
from geonodes import nodes

node = nodes.StoreNamedAttribute(geometry=None, name=None, value=None, data_type='FLOAT', domain='POINT')
```

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **name**: [String](String.md)
- **value**: **data_type** dependant

#### Node parameter arguments:

- **data_type** (str): default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN')
- **domain** (str): default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN')
- Input sockets  : ['value']
- Output sockets : []
## Implementation

#### class [Geometry](Geometry.md)

 - [store_named_attribute](Geometry.md#store_named_attribute)
 - [set_named_boolean](Geometry.md#set_named_boolean)
 - [set_named_integer](Geometry.md#set_named_integer)
 - [set_named_float](Geometry.md#set_named_float)
 - [set_named_vector](Geometry.md#set_named_vector)
 - [set_named_color](Geometry.md#set_named_color)
#### class [Domain](Domain.md)

 - [store_named_attribute](Domain.md#store_named_attribute)
 - [set_named_boolean](Domain.md#set_named_boolean)
 - [set_named_integer](Domain.md#set_named_integer)
 - [set_named_float](Domain.md#set_named_float)
 - [set_named_vector](Domain.md#set_named_vector)
 - [set_named_color](Domain.md#set_named_color)