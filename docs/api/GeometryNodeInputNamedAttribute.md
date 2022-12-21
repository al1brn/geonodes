# Node Named Attribute

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)
- geonodes name: `NamedAttribute`
- bl_idname: `GeometryNodeInputNamedAttribute`

```python
from geonodes import nodes

node = nodes.NamedAttribute(name=None, data_type='FLOAT')
```

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

#### [Domain](Domain.md)

 - [named_attribute](Domain.md#named_attribute) ```python nodes.NamedAttribute(name=name, data_type=data_type````
 - [get_named_float](Domain.md#get_named_float) ```python nodes.NamedAttribute(name=name, data_type='FLOAT'````
 - [get_named_integer](Domain.md#get_named_integer) ```python nodes.NamedAttribute(name=name, data_type='INT'````
 - [get_named_vector](Domain.md#get_named_vector) ```python nodes.NamedAttribute(name=name, data_type='FLOAT_VECTOR'````
 - [get_named_color](Domain.md#get_named_color) ```python nodes.NamedAttribute(name=name, data_type='FLOAT_COLOR'````
 - [get_named_boolean](Domain.md#get_named_boolean) ```python nodes.NamedAttribute(name=name, data_type='BOOLEAN'````
#### [Geometry](Geometry.md)

 - [named_attribute](Geometry.md#named_attribute) ```python nodes.NamedAttribute(name=name, data_type=data_type````
 - [get_named_float](Geometry.md#get_named_float) ```python nodes.NamedAttribute(name=name, data_type='FLOAT'````
 - [get_named_integer](Geometry.md#get_named_integer) ```python nodes.NamedAttribute(name=name, data_type='INT'````
 - [get_named_vector](Geometry.md#get_named_vector) ```python nodes.NamedAttribute(name=name, data_type='FLOAT_VECTOR'````
 - [get_named_color](Geometry.md#get_named_color) ```python nodes.NamedAttribute(name=name, data_type='FLOAT_COLOR'````
 - [get_named_boolean](Geometry.md#get_named_boolean) ```python nodes.NamedAttribute(name=name, data_type='BOOLEAN'````
