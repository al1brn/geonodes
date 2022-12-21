# Node 'Merge by Distance'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/merge_by_distance.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)
- geonodes name: `MergeByDistance`
- bl_idname: `GeometryNodeMergeByDistance`

```python
from geonodes import nodes

node = nodes.MergeByDistance(geometry=None, selection=None, distance=None, mode='ALL')
```

[Blender Image](self.node_image_ref)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **distance**: [Float](Float.md)

#### Node parameter arguments:

- **mode** (str): default = 'ALL' in ('ALL', 'CONNECTED')

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

### [Geometry](Geometry.md)

| Name | Definition |
|------|------------|
 | [merge_by_distance](Geometry.md#merge_by_distance) | `def merge_by_distance(self, selection=None, distance=None, mode='ALL'):` |

### [Vertex](Vertex.md)

| Name | Definition |
|------|------------|
 | [merge_by_distance](Vertex.md#merge_by_distance) | `def merge_by_distance(self, distance=None, mode='ALL'):` |

<sub>Go to [top](#node-Merge-by-Distance) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

