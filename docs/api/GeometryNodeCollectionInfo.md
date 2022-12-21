# Node Collection Info

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/collection_info.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCollectionInfo.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeCollectionInfo`

```python
from geonodes import nodes

node = nodes.CollectionInfo(collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL')
```

#### Input socket arguments:

- collection: Collection
- separate_children: Boolean
- reset_children: Boolean

#### Node parameter arguments:

- transform_space (str): Node parameter, default = 'ORIGINAL' in ('ORIGINAL', 'RELATIVE')

#### Output sockets:

- **geometry** : Geometry

