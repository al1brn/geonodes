# Node *Distribute Points in Volume*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_in_volume.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsInVolume.html)
- geonodes name: `DistributePointsInVolume`
- bl_idname: `GeometryNodeDistributePointsInVolume`

```python
from geonodes import nodes

node = nodes.DistributePointsInVolume(volume=None, density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDistributePointsInVolume.webp)

### Args:

#### Input socket arguments:

- **volume**: [Volume](Volume.md)
- **density**: [Float](Float.md)
- **seed**: [Integer](Integer.md)
- **spacing**: [Vector](Vector.md)
- **threshold**: [Float](Float.md)

#### Node parameter arguments:

- **mode** (str): default = 'DENSITY_RANDOM' in ('DENSITY_RANDOM', 'DENSITY_GRID')

### Output sockets:

- **points** : [Points](Points.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Volume](Volume.md)** |
| [distribute_points](Volume.md#distribute_points) | `def distribute_points(self, density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM'):` |
| [distribute_points_random](Volume.md#distribute_points_random) | `def distribute_points_random(self, density=None, seed=None):` |
| [distribute_points_grid](Volume.md#distribute_points_grid) | `def distribute_points_grid(self, spacing=None, threshold=None):` |

<sub>Go to [top](#node-Distribute-Points-in-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

