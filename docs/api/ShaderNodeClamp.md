# Node 'Clamp'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)
- geonodes name: `Clamp`
- bl_idname: `ShaderNodeClamp`

```python
from geonodes import nodes

node = nodes.Clamp(value=None, min=None, max=None, clamp_type='MINMAX')
```

[Blender Image](self.node_image_ref)

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

### Global functions

| Name | Definition |
|------|------------|
 | [clamp](A.md#clamp) | `def clamp(value=None, min=None, max=None, clamp_type='MINMAX'):` |
 | [clamp_min_max](A.md#clamp_min_max) | `def clamp_min_max(value=None, min=None, max=None):` |
 | [clamp_range](A.md#clamp_range) | `def clamp_range(value=None, min=None, max=None):` |

### [Float](Float.md)

| Name | Definition |
|------|------------|
 | [clamp](Float.md#clamp) | `def clamp(self, min=None, max=None, clamp_type='MINMAX'):` |
 | [clamp_min_max](Float.md#clamp_min_max) | `def clamp_min_max(self, min=None, max=None):` |
 | [clamp_range](Float.md#clamp_range) | `def clamp_range(self, min=None, max=None):` |

<sub>Go to [top](#node-Clamp) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

