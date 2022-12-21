# Node 'Separate Geometry'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)
- geonodes name: `SeparateGeometry`
- bl_idname: `GeometryNodeSeparateGeometry`

```python
from geonodes import nodes

node = nodes.SeparateGeometry(geometry=None, selection=None, domain='POINT')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)

#### Node parameter arguments:

- **domain** (str): default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

### Output sockets:

- **selection** : [Geometry](Geometry.md)
- **inverted** : [Geometry](Geometry.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Domain](Domain.md)** |
| [separate](Domain.md#separate) | `def separate(self, geometry=None):` |
| **[Geometry](Geometry.md)** |
| [separate](Geometry.md#separate) | `def separate(self, geometry=None, selection=None, domain='POINT'):` |

<sub>Go to [top](#node-Separate-Geometry) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

