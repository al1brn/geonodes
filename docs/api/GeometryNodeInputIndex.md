# Node *Index*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)
- geonodes name: `Index`
- bl_idname: `GeometryNodeInputIndex`

```python
from geonodes import nodes

node = nodes.Index()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputIndex.webp)

### Output sockets:

- **index** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Domain](Domain.md)** |
| [index](Domain.md#index) | `@property`<br> `def index(self):` |
| [domain_index](Domain.md#domain_index) | `@property`<br> `def domain_index(self):` |
| **[Geometry](Geometry.md)** |
| [index](Geometry.md#index) | `@property`<br> `def index(self):` |

<sub>Go to [top](#node-Index) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

