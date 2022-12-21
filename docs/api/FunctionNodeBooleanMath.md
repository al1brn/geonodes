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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44fdf0>>](Boolean.md#b_and)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44e140>>](Boolean.md#b_or)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44e950>>](Boolean.md#b_not)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44ffd0>>](Boolean.md#nand)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44f430>>](Boolean.md#nor)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44f2b0>>](Boolean.md#xnor)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44f370>>](Boolean.md#xor)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44ead0>>](Boolean.md#imply)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44e0b0>>](Boolean.md#nimply)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x1683b2b60>>](function.md#b_and)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x1683b0490>>](function.md#b_or)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x1683b15a0>>](function.md#b_not)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x1683b2fe0>>](function.md#nand)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x1683b3f70>>](function.md#nor)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x1683b3fd0>>](function.md#xnor)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x1683b1630>>](function.md#xor)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e44e6b0>>](function.md#imply)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e44c0d0>>](function.md#nimply)
