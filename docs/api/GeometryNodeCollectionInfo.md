# Node *Collection Info*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/collection_info.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCollectionInfo.html)
- geonodes name: `CollectionInfo`
- bl_idname: `GeometryNodeCollectionInfo`

```python
from geonodes import nodes

node = nodes.CollectionInfo(collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCollectionInfo.webp)

### Args:

#### Input socket arguments:

- **collection**: [Collection](Collection.md)
- **separate_children**: [Boolean](Boolean.md)
- **reset_children**: [Boolean](Boolean.md)

#### Node parameter arguments:

- **transform_space** (str): default = 'ORIGINAL' in ('ORIGINAL', 'RELATIVE')

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Geometry](Geometry.md)** |
| [Collection](Geometry.md#Collection) | `@classmethod`<br> `def Collection(cls, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL'):` |

<sub>Go to [top](#node-Collection-Info) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

