# Node *Bounding Box*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)
- geonodes name: `BoundingBox`
- bl_idname: `GeometryNodeBoundBox`

```python
from geonodes import nodes

node = nodes.BoundingBox(geometry=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeBoundBox.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)

### Output sockets:

- **bounding_box** : [Geometry](Geometry.md)
- **min** : [Vector](Vector.md)
- **max** : [Vector](Vector.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Geometry](Geometry.md)** |
| [bounding_box](Geometry.md#bounding_box) | `@property`<br> `def bounding_box(self):` |
| [bounding_box_min](Geometry.md#bounding_box_min) | `@property`<br> `def bounding_box_min(self):` |
| [bounding_box_min](Geometry.md#bounding_box_min) | `@property`<br> `def bounding_box_min(self):` |

<sub>Go to [top](#node-Bounding-Box) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

