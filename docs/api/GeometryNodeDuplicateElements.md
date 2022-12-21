# Node Duplicate Elements

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)
- geonodes name: `DuplicateElements`
- bl_idname: `GeometryNodeDuplicateElements`

```python
from geonodes import nodes

node = nodes.DuplicateElements(geometry=None, selection=None, amount=None, domain='POINT')
```

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **amount**: [Integer](Integer.md)

#### Node parameter arguments:

- **domain** (str): default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'SPLINE', 'INSTANCE')

### Output sockets:

- **geometry** : [Geometry](Geometry.md)
- **duplicate_index** : [Integer](Integer.md)

## Implementation

### [Domain](Domain.md)

| Name | Definition |
|------|------------|
 | [duplicate](Domain.md#duplicate) | `def duplicate(self, amount=None):` |

### [Geometry](Geometry.md)

| Name | Definition |
|------|------------|
 | [duplicate](Geometry.md#duplicate) | `def duplicate(self, selection=None, amount=None, domain='POINT'):` |

