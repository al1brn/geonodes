# Node Boolean Math

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
- geonodes name: `BooleanMath`
- bl_idname: `FunctionNodeBooleanMath`

```python
from geonodes import nodes

node = nodes.BooleanMath(boolean0=None, boolean1=None, operation='AND')
```

### Args:

#### Input socket arguments:

- **boolean0**: [Boolean](Boolean.md)
- **boolean1**: [Boolean](Boolean.md)

#### Node parameter arguments:

- **operation** (str): default = 'AND' in ('AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY')

### Output sockets:

- **boolean** : [Boolean](Boolean.md)

## Implementation

#### Global functions

 - [b_and](A.md#b_and)
  ```python
  def b_and(boolean0=None, boolean1=None)
  ```

 - [b_or](A.md#b_or)
  ```python
  def b_or(boolean0=None, boolean1=None)
  ```

 - [b_not](A.md#b_not)
  ```python
  def b_not(boolean0=None)
  ```

 - [nand](A.md#nand)
  ```python
  def nand(boolean0=None, boolean1=None)
  ```

 - [nor](A.md#nor)
  ```python
  def nor(boolean0=None, boolean1=None)
  ```

 - [xnor](A.md#xnor)
  ```python
  def xnor(boolean0=None, boolean1=None)
  ```

 - [xor](A.md#xor)
  ```python
  def xor(boolean0=None, boolean1=None)
  ```

 - [imply](A.md#imply)
  ```python
  def imply(boolean0=None, boolean1=None)
  ```

 - [nimply](A.md#nimply)
  ```python
  def nimply(boolean0=None, boolean1=None)
  ```

#### [Boolean](Boolean.md)

 - [b_and](Boolean.md#b_and)
  ```python
  def b_and(self, boolean1=None)
  ```

 - [b_or](Boolean.md#b_or)
  ```python
  def b_or(self, boolean1=None)
  ```

 - [b_not](Boolean.md#b_not)
  ```python
  def b_not(self)
  ```

 - [nand](Boolean.md#nand)
  ```python
  def nand(self, boolean1=None)
  ```

 - [nor](Boolean.md#nor)
  ```python
  def nor(self, boolean1=None)
  ```

 - [xnor](Boolean.md#xnor)
  ```python
  def xnor(self, boolean1=None)
  ```

 - [xor](Boolean.md#xor)
  ```python
  def xor(self, boolean1=None)
  ```

 - [imply](Boolean.md#imply)
  ```python
  def imply(self, boolean1=None)
  ```

 - [nimply](Boolean.md#nimply)
  ```python
  def nimply(self, boolean1=None)
  ```

