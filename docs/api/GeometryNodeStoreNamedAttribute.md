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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x1639dc640>>](Geometry.md#store_named_attribute)
 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x1639dd930>>](Geometry.md#set_named_boolean)
 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x1639dc550>>](Geometry.md#set_named_integer)
 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x1639dc490>>](Geometry.md#set_named_float)
 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x1639ddf90>>](Geometry.md#set_named_vector)
 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x1639ddab0>>](Geometry.md#set_named_color)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1639dd9c0>>](Domain.md#store_named_attribute)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1639dc880>>](Domain.md#set_named_boolean)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1639ddf00>>](Domain.md#set_named_integer)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1639ddb40>>](Domain.md#set_named_float)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1639ddb10>>](Domain.md#set_named_vector)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1639dc580>>](Domain.md#set_named_color)
