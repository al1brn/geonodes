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

#### class [Geometry](Geometry.md)

 - [random_float](Geometry.md#random_float)
 - [random_integer](Geometry.md#random_integer)
 - [random_vector](Geometry.md#random_vector)
 - [random_boolean](Geometry.md#random_boolean)
#### class [Domain](Domain.md)

 - [random_float](Domain.md#random_float)
 - [random_integer](Domain.md#random_integer)
 - [random_vector](Domain.md#random_vector)
 - [random_boolean](Domain.md#random_boolean)
#### Global functions

 - [random_float](function.md#random_float)
 - [random_integer](function.md#random_integer)
 - [random_vector](function.md#random_vector)
 - [random_boolean](function.md#random_boolean)