# Node Distribute Points in Volume

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_in_volume.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsInVolume.html)
- geonodes name: `DistributePointsInVolume`
- bl_idname: `GeometryNodeDistributePointsInVolume`

```python
from geonodes import nodes

node = nodes.DistributePointsInVolume(volume=None, density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM')
```

#### Input socket arguments:

- volume: [Volume](Volume.md)
- density: [Float](Float.md)
- seed: [Integer](Integer.md)
- spacing: [Vector](Vector.md)
- threshold: [Float](Float.md)

#### Node parameter arguments:

- mode (str): Node parameter, default = 'DENSITY_RANDOM' in ('DENSITY_RANDOM', 'DENSITY_GRID')

#### Output sockets:

- **points** : Points

