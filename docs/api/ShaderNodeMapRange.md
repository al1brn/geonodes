# Node Map Range

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)
- geonodes name: `MapRange`
- bl_idname: `ShaderNodeMapRange`

```python
from geonodes import nodes

node = nodes.MapRange(value=None, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, vector=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR')
```

### Args:#### Input socket arguments:

- **value**: [Float](Float.md)
- **from_min**: **data_type** dependant
- **from_max**: **data_type** dependant
- **to_min**: **data_type** dependant
- **to_max**: **data_type** dependant
- **steps**: **data_type** dependant
- **vector**: [Vector](Vector.md)

#### Node parameter arguments:

- **clamp** (bool): default = True
- **data_type** (str): default = 'FLOAT' in ('FLOAT', 'FLOAT_VECTOR')
- **interpolation_type** (str): default = 'LINEAR' in ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP')

### Output sockets:

- **result** : [Float](Float.md)
- **vector** : [Vector](Vector.md)

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'FLOAT_VECTOR')
- Input sockets  : ['from_min', 'from_max', 'to_min', 'to_max', 'steps']
- Output sockets : []
