# Node Clamp

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)
- geonodes name: `Clamp`
- bl_idname: `ShaderNodeClamp`

```python
from geonodes import nodes

node = nodes.Clamp(value=None, min=None, max=None, clamp_type='MINMAX')
```

### Args:

#### Input socket arguments:

- **value**: [Float](Float.md)
- **min**: [Float](Float.md)
- **max**: [Float](Float.md)

#### Node parameter arguments:

- **clamp_type** (str): default = 'MINMAX' in ('MINMAX', 'RANGE')

### Output sockets:

- **result** : [Float](Float.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44d6c0>>](Float.md#clamp)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44ec20>>](Float.md#clamp_min_max)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44ef50>>](Float.md#clamp_range)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e44d630>>](function.md#clamp)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e44d690>>](function.md#clamp_min_max)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e44d720>>](function.md#clamp_range)
