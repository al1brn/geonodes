# Node Sample Nearest

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_nearest.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html)
- geonodes name: `SampleNearest`
- bl_idname: `GeometryNodeSampleNearest`

```python
from geonodes import nodes

node = nodes.SampleNearest(geometry=None, sample_position=None, domain='POINT')
```

#### Input socket arguments:

- geometry: Geometry
- sample_position: Vector

#### Node parameter arguments:

- domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER')

#### Output sockets:

- **index** : Integer

