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

 - [b_and](A.md#b_and) ```python nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='AND'````
 - [b_or](A.md#b_or) ```python nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='OR'````
 - [b_not](A.md#b_not) ```python nodes.BooleanMath(boolean0=boolean0, boolean1=None, operation='NOT'````
 - [nand](A.md#nand) ```python nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='NAND'````
 - [nor](A.md#nor) ```python nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='NOR'````
 - [xnor](A.md#xnor) ```python nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='XNOR'````
 - [xor](A.md#xor) ```python nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='XOR'````
 - [imply](A.md#imply) ```python nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='IMPLY'````
 - [nimply](A.md#nimply) ```python nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='NIMPLY'````
#### [Boolean](Boolean.md)

 - [b_and](Boolean.md#b_and) ```python nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='AND'````
 - [b_or](Boolean.md#b_or) ```python nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='OR'````
 - [b_not](Boolean.md#b_not) ```python nodes.BooleanMath(boolean0=self, boolean1=None, operation='NOT'````
 - [nand](Boolean.md#nand) ```python nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NAND'````
 - [nor](Boolean.md#nor) ```python nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NOR'````
 - [xnor](Boolean.md#xnor) ```python nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XNOR'````
 - [xor](Boolean.md#xor) ```python nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XOR'````
 - [imply](Boolean.md#imply) ```python nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='IMPLY'````
 - [nimply](Boolean.md#nimply) ```python nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NIMPLY'````
