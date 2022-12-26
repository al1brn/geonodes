# Node *Random Value*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

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

| Class or method name | Definition |
|----------------------|------------|
| **[Boolean](Boolean.md)** |
| [Random](Boolean.md#Random) | `@classmethod`<br> `def Random(cls, probability=None, ID=None, seed=None):` |
| **[Domain](Domain.md)** |
| [random_float](Domain.md#random_float) | `@staticmethod`<br> `def random_float(min=None, max=None, ID=None, seed=None):` |
| [random_integer](Domain.md#random_integer) | `@staticmethod`<br> `def random_integer(min=None, max=None, ID=None, seed=None):` |
| [random_vector](Domain.md#random_vector) | `@staticmethod`<br> `def random_vector(min=None, max=None, ID=None, seed=None):` |
| [random_boolean](Domain.md#random_boolean) | `@staticmethod`<br> `def random_boolean(probability=None, ID=None, seed=None):` |
| **[Float](Float.md)** |
| [Random](Float.md#Random) | `@classmethod`<br> `def Random(cls, min=None, max=None, ID=None, seed=None):` |
| **[Geometry](Geometry.md)** |
| [random_float](Geometry.md#random_float) | `@staticmethod`<br> `def random_float(min=None, max=None, ID=None, seed=None):` |
| [random_integer](Geometry.md#random_integer) | `@staticmethod`<br> `def random_integer(min=None, max=None, ID=None, seed=None):` |
| [random_vector](Geometry.md#random_vector) | `@staticmethod`<br> `def random_vector(min=None, max=None, ID=None, seed=None):` |
| [random_boolean](Geometry.md#random_boolean) | `@staticmethod`<br> `def random_boolean(probability=None, ID=None, seed=None):` |
| **[Integer](Integer.md)** |
| [Random](Integer.md#Random) | `@classmethod`<br> `def Random(cls, min=None, max=None, ID=None, seed=None):` |
| **[Vector](Vector.md)** |
| [Random](Vector.md#Random) | `@classmethod`<br> `def Random(cls, min=None, max=None, ID=None, seed=None):` |
| Global functions |
| [random_float](functions.md#random_float) | `def random_float(min=None, max=None, ID=None, seed=None):` |
| [random_integer](functions.md#random_integer) | `def random_integer(min=None, max=None, ID=None, seed=None):` |
| [random_vector](functions.md#random_vector) | `def random_vector(min=None, max=None, ID=None, seed=None):` |
| [random_boolean](functions.md#random_boolean) | `def random_boolean(probability=None, ID=None, seed=None):` |

<sub>Go to [top](#node-Random-Value) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

