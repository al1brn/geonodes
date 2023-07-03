# Node *Sample Volume*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/a.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleVolume.html)
- geonodes name: `SampleVolume`
- bl_idname: `GeometryNodeSampleVolume`

```python
from geonodes import nodes

node = nodes.SampleVolume(volume=None, grid=None, position=None, grid_type='FLOAT', interpolation_mode='TRILINEAR')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleVolume.webp)

### Args:

#### Input socket arguments:

- **volume**: [Volume](Volume.md)
- **grid**: **interpolation_mode** dependant
- **position**: [Vector](Vector.md)

#### Node parameter arguments:

- **grid_type** (str): default = 'FLOAT' in ('FLOAT', 'FLOAT_VECTOR', 'INT', 'BOOLEAN')
- **interpolation_mode** (str): default = 'TRILINEAR' in ('NEAREST', 'TRILINEAR', 'TRIQUADRATIC')

### Output sockets:

- **value** : ``interpolation_mode`` dependant

#### Shared sockets:

- Driving parameter : ``interpolation_mode`` in ('NEAREST', 'TRILINEAR', 'TRIQUADRATIC')
- Input sockets  : ['grid']
- Output sockets : ['value']
## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Volume](Volume.md)** |
| [sample](Volume.md#sample) | `def sample(self, grid=None, position=None, grid_type='FLOAT', interpolation_mode='TRILINEAR'):` |
| [sample_float](Volume.md#sample_float) | `def sample_float(self, grid=None, position=None, interpolation_mode='TRILINEAR'):` |
| [sample_vector](Volume.md#sample_vector) | `def sample_vector(self, grid=None, position=None, interpolation_mode='TRILINEAR'):` |
| [sample_integer](Volume.md#sample_integer) | `def sample_integer(self, grid=None, position=None, interpolation_mode='TRILINEAR'):` |
| [sample_boolean](Volume.md#sample_boolean) | `def sample_boolean(self, grid=None, position=None, interpolation_mode='TRILINEAR'):` |

<sub>Go to [top](#node-Sample-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

