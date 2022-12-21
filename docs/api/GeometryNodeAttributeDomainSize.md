# Node Domain Size

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)
- geonodes name: `DomainSize`
- bl_idname: `GeometryNodeAttributeDomainSize`

```python
from geonodes import nodes

node = nodes.DomainSize(geometry=None, component='MESH')
```

#### Input socket arguments:

- geometry: [Geometry](Geometry.md)

#### Node parameter arguments:

- component (str): Node parameter, default = 'MESH' in ('MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES')

#### Output sockets:

- **point_count** : [Integer](Integer)
- **edge_count** : [Integer](Integer)
- **face_count** : [Integer](Integer)
- **face_corner_count** : [Integer](Integer)
- **spline_count** : [Integer](Integer)
- **instance_count** : [Integer](Integer)

