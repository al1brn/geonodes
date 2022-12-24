# Node *Separate Components*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)
- geonodes name: `SeparateComponents`
- bl_idname: `GeometryNodeSeparateComponents`

```python
from geonodes import nodes

node = nodes.SeparateComponents(geometry=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateComponents.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)

### Output sockets:

- **mesh** : [Mesh](Mesh.md)
- **point_cloud** : [Geometry](Geometry.md)
- **curve** : [Curve](Curve.md)
- **volume** : [Volume](Volume.md)
- **instances** : [Instances](Instances.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Geometry](Geometry.md)** |
| [separate_components](Geometry.md#separate_components) | `@property`<br> `def separate_components(self):` |
| [mesh_component](Geometry.md#mesh_component) | `@property`<br> `def mesh_component(self):` |
| [curve_component](Geometry.md#curve_component) | `@property`<br> `def curve_component(self):` |
| [points_component](Geometry.md#points_component) | `@property`<br> `def points_component(self):` |
| [volume_component](Geometry.md#volume_component) | `@property`<br> `def volume_component(self):` |
| [instances_component](Geometry.md#instances_component) | `@property`<br> `def instances_component(self):` |

<sub>Go to [top](#node-Separate-Components) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

