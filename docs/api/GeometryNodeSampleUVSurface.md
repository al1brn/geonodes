# Node 'Sample UV Surface'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample_uv_surface.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleUVSurface.html)
- geonodes name: `SampleUvSurface`
- bl_idname: `GeometryNodeSampleUVSurface`

```python
from geonodes import nodes

node = nodes.SampleUvSurface(mesh=None, value=None, source_uv_map=None, sample_uv=None, data_type='FLOAT')
```

### Args:

#### Input socket arguments:

- **mesh**: [Mesh](Mesh.md)
- **value**: **data_type** dependant
- **source_uv_map**: [Vector](Vector.md)
- **sample_uv**: [Vector](Vector.md)

#### Node parameter arguments:

- **data_type** (str): default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')

### Output sockets:

- **value** : ``data_type`` dependant
- **is_valid** : [Boolean](Boolean.md)

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets  : ['value']
- Output sockets : ['value']
## Implementation

### [Mesh](Mesh.md)

| Name | Definition |
|------|------------|
 | [sample_uv_surface](Mesh.md#sample_uv_surface) | `def sample_uv_surface(self, value=None, source_uv_map=None, sample_uv=None):` |

<sub>Go to [top](#node-{wnode.bnode.name}) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

