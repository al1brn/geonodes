# Node *Raycast*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)
- geonodes name: `Raycast`
- bl_idname: `GeometryNodeRaycast`

```python
from geonodes import nodes

node = nodes.Raycast(target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRaycast.webp)

### Args:

#### Input socket arguments:

- **target_geometry**: [Geometry](Geometry.md)
- **attribute**: **data_type** dependant
- **source_position**: [Vector](Vector.md)
- **ray_direction**: [Vector](Vector.md)
- **ray_length**: [Float](Float.md)

#### Node parameter arguments:

- **data_type** (str): default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- **mapping** (str): default = 'INTERPOLATED' in ('INTERPOLATED', 'NEAREST')

### Output sockets:

- **is_hit** : [Boolean](Boolean.md)
- **hit_position** : [Vector](Vector.md)
- **hit_normal** : [Vector](Vector.md)
- **hit_distance** : [Float](Float.md)
- **attribute** : ``data_type`` dependant

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets  : ['attribute']
- Output sockets : ['attribute']
## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Geometry](Geometry.md)** |
| [raycast](Geometry.md#raycast) | `def raycast(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):` |
| [raycast_interpolated](Geometry.md#raycast_interpolated) | `def raycast_interpolated(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None):` |
| [raycast_nearest](Geometry.md#raycast_nearest) | `def raycast_nearest(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None):` |

<sub>Go to [top](#node-Raycast) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

