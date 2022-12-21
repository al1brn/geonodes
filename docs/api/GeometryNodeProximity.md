# Node Geometry Proximity

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)
- geonodes name: `GeometryProximity`
- bl_idname: `GeometryNodeProximity`

```python
from geonodes import nodes

node = nodes.GeometryProximity(target=None, source_position=None, target_element='FACES')
```

#### Input socket arguments:

- target: Geometry
- source_position: Vector

#### Node parameter arguments:

- target_element (str): Node parameter, default = 'FACES' in ('POINTS', 'EDGES', 'FACES')

#### Output sockets:

- **position** : Vector
- **distance** : Float

