# Node Boolean Math

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
- geonodes name: `WNode`
- bl_idname: `FunctionNodeBooleanMath`

```python
from geonodes import nodes

node = nodes.BooleanMath(boolean0=None, boolean1=None, operation='AND')
```

#### Input socket arguments:

- boolean0: Boolean
- boolean1: Boolean

#### Node parameter arguments:

- operation (str): Node parameter, default = 'AND' in ('AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY')

#### Output sockets:

- **boolean** : Boolean

