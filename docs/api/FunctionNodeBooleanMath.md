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

#### class [Boolean](Boolean.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e378760>>](Boolean.md#b_and)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e37b0d0>>](Boolean.md#b_or)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e37a2f0>>](Boolean.md#b_not)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e37a410>>](Boolean.md#nand)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e37af80>>](Boolean.md#nor)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e379ed0>>](Boolean.md#xnor)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e37b610>>](Boolean.md#xor)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e37b640>>](Boolean.md#imply)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e37a440>>](Boolean.md#nimply)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e37a230>>](function.md#b_and)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e3787f0>>](function.md#b_or)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e37a590>>](function.md#b_not)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e378b20>>](function.md#nand)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e37a170>>](function.md#nor)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e3786a0>>](function.md#xnor)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e37b760>>](function.md#xor)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e3788b0>>](function.md#imply)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e378820>>](function.md#nimply)
