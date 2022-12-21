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
 - [b_or](A.md#b_or)
 - [b_not](A.md#b_not)
 - [nand](A.md#nand)
 - [nor](A.md#nor)
 - [xnor](A.md#xnor)
 - [xor](A.md#xor)
 - [imply](A.md#imply)
 - [nimply](A.md#nimply)
#### class [Boolean](Boolean.md)

 - [b_and](Boolean.md#b_and)
 - [b_or](Boolean.md#b_or)
 - [b_not](Boolean.md#b_not)
 - [nand](Boolean.md#nand)
 - [nor](Boolean.md#nor)
 - [xnor](Boolean.md#xnor)
 - [xor](Boolean.md#xor)
 - [imply](Boolean.md#imply)
 - [nimply](Boolean.md#nimply)
