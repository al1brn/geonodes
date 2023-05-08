# Node *Transform Geometry*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/r.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTransform.html)
- geonodes name: `TransformGeometry`
- bl_idname: `GeometryNodeTransform`

```python
from geonodes import nodes

node = nodes.TransformGeometry(geometry=None, translation=None, rotation=None, scale=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeTransform.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **translation**: [Vector](Vector.md)
- **rotation**: [Vector](Vector.md)
- **scale**: [Vector](Vector.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Geometry](Geometry.md)** |
| [transform_geometry](Geometry.md#transform_geometry) | `def transform_geometry(self, translation=None, rotation=None, scale=None):` |
| [transform](Geometry.md#transform) | `def transform(self, translation=None, rotation=None, scale=None):` |

<sub>Go to [top](#node-Transform-Geometry) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

