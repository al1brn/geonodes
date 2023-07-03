# Node *Mean Filter SDF Volume*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/e.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeanFilterSDFVolume.html)
- geonodes name: `MeanFilterSdfVolume`
- bl_idname: `GeometryNodeMeanFilterSDFVolume`

```python
from geonodes import nodes

node = nodes.MeanFilterSdfVolume(volume=None, iterations=None, width=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeanFilterSDFVolume.webp)

### Args:

#### Input socket arguments:

- **volume**: [Volume](Volume.md)
- **iterations**: [Integer](Integer.md)
- **width**: [Integer](Integer.md)

### Output sockets:

- **volume** : [Volume](Volume.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Volume](Volume.md)** |
| [mean_filter_sdf_volume](Volume.md#mean_filter_sdf_volume) | `def mean_filter_sdf_volume(self, iterations=None, width=None):` |

<sub>Go to [top](#node-Mean-Filter-SDF-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

