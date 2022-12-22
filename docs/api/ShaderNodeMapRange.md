# Node *Map Range*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)
- geonodes name: `MapRange`
- bl_idname: `ShaderNodeMapRange`

```python
from geonodes import nodes

node = nodes.MapRange(value=None, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, vector=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeMapRange.webp)

### Args:

#### Input socket arguments:

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
## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Float](Float.md)** |
| [map_range](Float.md#map_range) | `def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True, interpolation_type='LINEAR'):` |
| [map_range_linear](Float.md#map_range_linear) | `def map_range_linear(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):` |
| [map_range_stepped](Float.md#map_range_stepped) | `def map_range_stepped(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True):` |
| [map_range_smooth](Float.md#map_range_smooth) | `def map_range_smooth(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):` |
| [map_range_smoother](Float.md#map_range_smoother) | `def map_range_smoother(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):` |
| **[Vector](Vector.md)** |
| [map_range](Vector.md#map_range) | `def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True, interpolation_type='LINEAR'):` |
| [map_range_linear](Vector.md#map_range_linear) | `def map_range_linear(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):` |
| [map_range_stepped](Vector.md#map_range_stepped) | `def map_range_stepped(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True):` |
| [map_range_smooth](Vector.md#map_range_smooth) | `def map_range_smooth(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):` |
| [map_range_smoother](Vector.md#map_range_smoother) | `def map_range_smoother(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):` |

<sub>Go to [top](#node-Map-Range) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

