# Node Delete Geometry

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)
- geonodes name: `DeleteGeometry`
- bl_idname: `GeometryNodeDeleteGeometry`

```python
from geonodes import nodes

node = nodes.DeleteGeometry(geometry=None, selection=None, domain='POINT', mode='ALL')
```

#### Input socket arguments:

- geometry: [Geometry](Geometry.md)
- selection: [Boolean](Boolean.md)

#### Node parameter arguments:

- domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')
- mode (str): Node parameter, default = 'ALL' in ('ALL', 'EDGE_FACE', 'ONLY_FACE')

#### Output sockets:

- **geometry** : Geometry

