# Node *Clamp*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)
- geonodes name: `Clamp`
- bl_idname: `ShaderNodeClamp`

```python
from geonodes import nodes

node = nodes.Clamp(value=None, min=None, max=None, clamp_type='MINMAX')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeClamp.webp)

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

| Class or method name | Definition |
|----------------------|------------|
| **[Float](Float.md)** |
| [clamp](Float.md#clamp) | `def clamp(self, min=None, max=None, clamp_type='MINMAX'):` |
| [clamp_min_max](Float.md#clamp_min_max) | `def clamp_min_max(self, min=None, max=None):` |
| [clamp_range](Float.md#clamp_range) | `def clamp_range(self, min=None, max=None):` |
| Global functions |
| [clamp](functions.md#clamp) | `def clamp(value=None, min=None, max=None, clamp_type='MINMAX'):` |
| [clamp_min_max](functions.md#clamp_min_max) | `def clamp_min_max(value=None, min=None, max=None):` |
| [clamp_range](functions.md#clamp_range) | `def clamp_range(value=None, min=None, max=None):` |

<sub>Go to [top](#node-Clamp) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

