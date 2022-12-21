# Node Random Value

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)
- geonodes name: `RandomValue`
- bl_idname: `FunctionNodeRandomValue`

```python
from geonodes import nodes

node = nodes.RandomValue(min=None, max=None, probability=None, ID=None, seed=None, data_type='FLOAT')
```

### Args:

#### Input socket arguments:

- **min**: **data_type** dependant
- **max**: **data_type** dependant
- **probability**: [Float](Float.md)
- **ID**: [Integer](Integer.md)
- **seed**: [Integer](Integer.md)

#### Node parameter arguments:

- **data_type** (str): default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')

### Output sockets:

- **value** : ``data_type`` dependant

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')
- Input sockets  : ['min', 'max']
- Output sockets : ['value']
## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x16ee55ba0>>](Geometry.md#random_float)
 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x16ee55b70>>](Geometry.md#random_integer)
 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x16ee55b40>>](Geometry.md#random_vector)
 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x16ee55b10>>](Geometry.md#random_boolean)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomAttribute object at 0x16ee55ae0>>](Domain.md#random_float)
 - [<bound method Generator.fname of <generator.code_gen.DomAttribute object at 0x16ee55ab0>>](Domain.md#random_integer)
 - [<bound method Generator.fname of <generator.code_gen.DomAttribute object at 0x16ee55a80>>](Domain.md#random_vector)
 - [<bound method Generator.fname of <generator.code_gen.DomAttribute object at 0x16ee55a50>>](Domain.md#random_boolean)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16ee55c60>>](function.md#random_float)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16ee55c30>>](function.md#random_integer)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16ee55c00>>](function.md#random_vector)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16ee55bd0>>](function.md#random_boolean)
