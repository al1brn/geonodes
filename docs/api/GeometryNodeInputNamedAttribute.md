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

#### class [Geometry](Geometry.md)

 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x16d4f9000>>](Geometry.md#named_attribute)
 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x16d4f8fd0>>](Geometry.md#get_named_float)
 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x16d4f8fa0>>](Geometry.md#get_named_integer)
 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x16d4f8f70>>](Geometry.md#get_named_vector)
 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x16d4f8f40>>](Geometry.md#get_named_color)
 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x16d4f8f10>>](Geometry.md#get_named_boolean)
#### class [Domain](Domain.md)

 - [<bound method Generator.fname of <generator.code_gen.DomAttribute object at 0x16d4f8eb0>>](Domain.md#named_attribute)
 - [<bound method Generator.fname of <generator.code_gen.DomAttribute object at 0x16d4f8e80>>](Domain.md#get_named_float)
 - [<bound method Generator.fname of <generator.code_gen.DomAttribute object at 0x16d4f8e50>>](Domain.md#get_named_integer)
 - [<bound method Generator.fname of <generator.code_gen.DomAttribute object at 0x16d4f8e20>>](Domain.md#get_named_vector)
 - [<bound method Generator.fname of <generator.code_gen.DomAttribute object at 0x16d4f8df0>>](Domain.md#get_named_color)
 - [<bound method Generator.fname of <generator.code_gen.DomAttribute object at 0x16d4f8dc0>>](Domain.md#get_named_boolean)
