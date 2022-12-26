# Node *Boolean Math*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
- geonodes name: `BooleanMath`
- bl_idname: `FunctionNodeBooleanMath`

```python
from geonodes import nodes

node = nodes.BooleanMath(boolean0=None, boolean1=None, operation='AND')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeBooleanMath.webp)

### Args:

#### Input socket arguments:

- **boolean0**: [Boolean](Boolean.md)
- **boolean1**: [Boolean](Boolean.md)

#### Node parameter arguments:

- **operation** (str): default = 'AND' in ('AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY')

### Output sockets:

- **boolean** : [Boolean](Boolean.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Boolean](Boolean.md)** |
| [b_and](Boolean.md#b_and) | `def b_and(self, boolean1=None):` |
| [b_or](Boolean.md#b_or) | `def b_or(self, boolean1=None):` |
| [b_not](Boolean.md#b_not) | `def b_not(self):` |
| [nand](Boolean.md#nand) | `def nand(self, boolean1=None):` |
| [nor](Boolean.md#nor) | `def nor(self, boolean1=None):` |
| [xnor](Boolean.md#xnor) | `def xnor(self, boolean1=None):` |
| [xor](Boolean.md#xor) | `def xor(self, boolean1=None):` |
| [imply](Boolean.md#imply) | `def imply(self, boolean1=None):` |
| [nimply](Boolean.md#nimply) | `def nimply(self, boolean1=None):` |
| Global functions |
| [b_and](functions.md#b_and) | `def b_and(boolean0=None, boolean1=None):` |
| [b_or](functions.md#b_or) | `def b_or(boolean0=None, boolean1=None):` |
| [b_not](functions.md#b_not) | `def b_not(boolean0=None):` |
| [nand](functions.md#nand) | `def nand(boolean0=None, boolean1=None):` |
| [nor](functions.md#nor) | `def nor(boolean0=None, boolean1=None):` |
| [xnor](functions.md#xnor) | `def xnor(boolean0=None, boolean1=None):` |
| [xor](functions.md#xor) | `def xor(boolean0=None, boolean1=None):` |
| [imply](functions.md#imply) | `def imply(boolean0=None, boolean1=None):` |
| [nimply](functions.md#nimply) | `def nimply(boolean0=None, boolean1=None):` |

<sub>Go to [top](#node-Boolean-Math) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

