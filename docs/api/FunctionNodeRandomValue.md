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

#### Global functions

 - [random_float](A.md#random_float)
  ```python
  nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='FLOAT'  ```

 - [random_integer](A.md#random_integer)
  ```python
  nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='INT'  ```

 - [random_vector](A.md#random_vector)
  ```python
  nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='FLOAT_VECTOR'  ```

 - [random_boolean](A.md#random_boolean)
  ```python
  nodes.RandomValue(min=None, max=None, probability=probability, ID=ID, seed=seed, data_type='BOOLEAN'  ```

#### [Domain](Domain.md)

 - [random_float](Domain.md#random_float)
  ```python
  nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='FLOAT'  ```

 - [random_integer](Domain.md#random_integer)
  ```python
  nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='INT'  ```

 - [random_vector](Domain.md#random_vector)
  ```python
  nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='FLOAT_VECTOR'  ```

 - [random_boolean](Domain.md#random_boolean)
  ```python
  nodes.RandomValue(min=None, max=None, probability=probability, ID=ID, seed=seed, data_type='BOOLEAN'  ```

#### [Geometry](Geometry.md)

 - [random_float](Geometry.md#random_float)
  ```python
  nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='FLOAT'  ```

 - [random_integer](Geometry.md#random_integer)
  ```python
  nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='INT'  ```

 - [random_vector](Geometry.md#random_vector)
  ```python
  nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='FLOAT_VECTOR'  ```

 - [random_boolean](Geometry.md#random_boolean)
  ```python
  nodes.RandomValue(min=None, max=None, probability=probability, ID=ID, seed=seed, data_type='BOOLEAN'  ```

