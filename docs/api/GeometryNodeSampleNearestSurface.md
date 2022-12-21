# Node Sample Nearest Surface

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample_nearest_surface.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearestSurface.html)
- geonodes name: `SampleNearestSurface`
- bl_idname: `GeometryNodeSampleNearestSurface`

```python
from geonodes import nodes

node = nodes.SampleNearestSurface(mesh=None, value=None, sample_position=None, data_type='FLOAT')
```

#### Input socket arguments:

- `mesh`: [Mesh](Mesh.md)
- `value`: `data_type` dependant
- `sample_position`: [Vector](Vector.md)

#### Node parameter arguments:

- data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')

#### Output sockets:

- **value** : ``data_type`` dependant

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets  : ['value']
- Output sockets : ['value']
