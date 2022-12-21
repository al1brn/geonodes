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

#### [Domain](Domain.md)

 - [store_named_attribute](Domain.md#store_named_attribute) ```python nodes.StoreNamedAttribute(geometry=self.data_socket, name=name, value=value, data_type=data_type_, domain=self.domain````
 - [set_named_boolean](Domain.md#set_named_boolean) ```python nodes.StoreNamedAttribute(geometry=self.data_socket, name=name, value=value, data_type='BOOLEAN', domain=self.domain````
 - [set_named_integer](Domain.md#set_named_integer) ```python nodes.StoreNamedAttribute(geometry=self.data_socket, name=name, value=value, data_type='INT', domain=self.domain````
 - [set_named_float](Domain.md#set_named_float) ```python nodes.StoreNamedAttribute(geometry=self.data_socket, name=name, value=value, data_type='FLOAT', domain=self.domain````
 - [set_named_vector](Domain.md#set_named_vector) ```python nodes.StoreNamedAttribute(geometry=self.data_socket, name=name, value=value, data_type='FLOAT_VECTOR', domain=self.domain````
 - [set_named_color](Domain.md#set_named_color) ```python nodes.StoreNamedAttribute(geometry=self.data_socket, name=name, value=value, data_type='FLOAT_COLOR', domain=self.domain````
#### [Geometry](Geometry.md)

 - [store_named_attribute](Geometry.md#store_named_attribute) ```python nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type=data_type_, domain=domain````
 - [set_named_boolean](Geometry.md#set_named_boolean) ```python nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='BOOLEAN', domain=domain````
 - [set_named_integer](Geometry.md#set_named_integer) ```python nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='INT', domain=domain````
 - [set_named_float](Geometry.md#set_named_float) ```python nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='FLOAT', domain=domain````
 - [set_named_vector](Geometry.md#set_named_vector) ```python nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='FLOAT_VECTOR', domain=domain````
 - [set_named_color](Geometry.md#set_named_color) ```python nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='FLOAT_COLOR', domain=domain````
