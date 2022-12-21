# Node Collection Info

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/collection_info.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCollectionInfo.html)
- geonodes name: `CollectionInfo`
- bl_idname: `GeometryNodeCollectionInfo`

```python
from geonodes import nodes

node = nodes.CollectionInfo(collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL')
```

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

#### [Geometry](Geometry.md)

 - [Collection](Geometry.md#Collection-classmethod) ```python nodes.CollectionInfo(collection=collection, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space````
