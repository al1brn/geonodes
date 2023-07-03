# Node *Index of Nearest*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/n.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeIndexOfNearest.html)
- geonodes name: `IndexOfNearest`
- bl_idname: `GeometryNodeIndexOfNearest`

```python
from geonodes import nodes

node = nodes.IndexOfNearest(position=None, group_id=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeIndexOfNearest.webp)

### Args:

#### Input socket arguments:

- **position**: [Vector](Vector.md)
- **group_id**: [Integer](Integer.md)

### Output sockets:

- **index** : [Integer](Integer.md)
- **has_neighbor** : [Boolean](Boolean.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Domain](Domain.md)** |
| [index_of_nearest](Domain.md#index_of_nearest) | `@property`<br> `def index_of_nearest(self, position=None, group_id=None):` |
| **[Geometry](Geometry.md)** |
| [index_of_nearest](Geometry.md#index_of_nearest) | `@property`<br> `def index_of_nearest(self, position=None, group_id=None):` |

<sub>Go to [top](#node-Index-of-Nearest) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

