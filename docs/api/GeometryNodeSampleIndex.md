# Node *Sample Index*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_index.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)
- geonodes name: `SampleIndex`
- bl_idname: `GeometryNodeSampleIndex`

```python
from geonodes import nodes

node = nodes.SampleIndex(geometry=None, value=None, index=None, clamp=False, data_type='FLOAT', domain='POINT')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleIndex.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **value**: **data_type** dependant
- **index**: [Integer](Integer.md)

#### Node parameter arguments:

- **clamp** (bool): default = False
- **data_type** (str): default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- **domain** (str): default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

### Output sockets:

- **value** : ``data_type`` dependant

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets  : ['value']
- Output sockets : ['value']
## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Domain](Domain.md)** |
| [sample_index](Domain.md#sample_index) | `def sample_index(self, value=None, index=None, clamp=False):` |
| **[Geometry](Geometry.md)** |
| [sample_index](Geometry.md#sample_index) | `def sample_index(self, value=None, index=None, clamp=False, domain='POINT'):` |

<sub>Go to [top](#node-Sample-Index) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

