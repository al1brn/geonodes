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

#### Global functions

 - [clamp](A.md#clamp)
 - [clamp_min_max](A.md#clamp_min_max)
 - [clamp_range](A.md#clamp_range)
#### class [Float](Float.md)

 - [clamp](Float.md#clamp)
 - [clamp_min_max](Float.md#clamp_min_max)
 - [clamp_range](Float.md#clamp_range)
