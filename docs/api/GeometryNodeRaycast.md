# Node Raycast

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)
- geonodes name: `Raycast`
- bl_idname: `GeometryNodeRaycast`

```python
from geonodes import nodes

node = nodes.Raycast(target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED')
```

#### Input socket arguments:

- target_geometry: [Geometry](Geometry.md)
- attribute: `data_type` dependant
- source_position: [Vector](Vector.md)
- ray_direction: [Vector](Vector.md)
- ray_length: [Float](Float.md)

#### Node parameter arguments:

- data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- mapping (str): Node parameter, default = 'INTERPOLATED' in ('INTERPOLATED', 'NEAREST')

#### Output sockets:

- **is_hit** : Boolean
- **hit_position** : Vector
- **hit_normal** : Vector
- **hit_distance** : Float
- **attribute** : ``data_type`` dependant

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets  : ['attribute']
- Output sockets : ['attribute']
