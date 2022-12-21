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

 - [named_attribute](Domain.md#named_attribute)
  ```python
  def named_attribute(self, name=None, data_type='FLOAT')
  ```

 - [get_named_float](Domain.md#get_named_float)
  ```python
  def get_named_float(self, name=None)
  ```

 - [get_named_integer](Domain.md#get_named_integer)
  ```python
  def get_named_integer(self, name=None)
  ```

 - [get_named_vector](Domain.md#get_named_vector)
  ```python
  def get_named_vector(self, name=None)
  ```

 - [get_named_color](Domain.md#get_named_color)
  ```python
  def get_named_color(self, name=None)
  ```

 - [get_named_boolean](Domain.md#get_named_boolean)
  ```python
  def get_named_boolean(self, name=None)
  ```

#### [Geometry](Geometry.md)

 - [named_attribute](Geometry.md#named_attribute)
  ```python
  def named_attribute(self, name=None, data_type='FLOAT')
  ```

 - [get_named_float](Geometry.md#get_named_float)
  ```python
  def get_named_float(self, name=None)
  ```

 - [get_named_integer](Geometry.md#get_named_integer)
  ```python
  def get_named_integer(self, name=None)
  ```

 - [get_named_vector](Geometry.md#get_named_vector)
  ```python
  def get_named_vector(self, name=None)
  ```

 - [get_named_color](Geometry.md#get_named_color)
  ```python
  def get_named_color(self, name=None)
  ```

 - [get_named_boolean](Geometry.md#get_named_boolean)
  ```python
  def get_named_boolean(self, name=None)
  ```

