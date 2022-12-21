# Node 'Random Value'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)
- geonodes name: `RandomValue`
- bl_idname: `FunctionNodeRandomValue`

```python
from geonodes import nodes

node = nodes.RandomValue(min=None, max=None, probability=None, ID=None, seed=None, data_type='FLOAT')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeRandomValue.webp)

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

### Global functions

| Name | Definition |
|------|------------|
 | [random_float](A.md#random_float) | `def random_float(min=None, max=None, ID=None, seed=None):` |
 | [random_integer](A.md#random_integer) | `def random_integer(min=None, max=None, ID=None, seed=None):` |
 | [random_vector](A.md#random_vector) | `def random_vector(min=None, max=None, ID=None, seed=None):` |
 | [random_boolean](A.md#random_boolean) | `def random_boolean(probability=None, ID=None, seed=None):` |

### [Domain](Domain.md)

| Name | Definition |
|------|------------|
 | [random_float](Domain.md#random_float) | `def random_float(self, min=None, max=None, ID=None, seed=None):` |
 | [random_integer](Domain.md#random_integer) | `def random_integer(self, min=None, max=None, ID=None, seed=None):` |
 | [random_vector](Domain.md#random_vector) | `def random_vector(self, min=None, max=None, ID=None, seed=None):` |
 | [random_boolean](Domain.md#random_boolean) | `def random_boolean(self, probability=None, ID=None, seed=None):` |

### [Geometry](Geometry.md)

| Name | Definition |
|------|------------|
 | [random_float](Geometry.md#random_float) | `def random_float(self, min=None, max=None, ID=None, seed=None):` |
 | [random_integer](Geometry.md#random_integer) | `def random_integer(self, min=None, max=None, ID=None, seed=None):` |
 | [random_vector](Geometry.md#random_vector) | `def random_vector(self, min=None, max=None, ID=None, seed=None):` |
 | [random_boolean](Geometry.md#random_boolean) | `def random_boolean(self, probability=None, ID=None, seed=None):` |

<sub>Go to [top](#node-Random-Value) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

