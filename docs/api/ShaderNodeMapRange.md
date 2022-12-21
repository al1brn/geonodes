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

#### [Float](Float.md)

 - [map_range](Float.md#map_range) ```python nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=steps, vector=None, clamp=clamp, data_type='FLOAT', interpolation_type=interpolation_type````
 - [map_range_linear](Float.md#map_range_linear) ```python nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=None, vector=None, clamp=clamp, data_type='FLOAT', interpolation_type='LINEAR'````
 - [map_range_stepped](Float.md#map_range_stepped) ```python nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=steps, vector=None, clamp=clamp, data_type='FLOAT', interpolation_type='STEPPED'````
 - [map_range_smooth](Float.md#map_range_smooth) ```python nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=None, vector=None, clamp=clamp, data_type='FLOAT', interpolation_type='SMOOTHSTEP'````
 - [map_range_smoother](Float.md#map_range_smoother) ```python nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=None, vector=None, clamp=clamp, data_type='FLOAT', interpolation_type='SMOOTHERSTEP'````
#### [Vector](Vector.md)

 - [map_range](Vector.md#map_range) ```python nodes.MapRange(value=None, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=steps, vector=self, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type=interpolation_type````
 - [map_range_linear](Vector.md#map_range_linear) ```python nodes.MapRange(value=None, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=None, vector=self, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type='LINEAR'````
 - [map_range_stepped](Vector.md#map_range_stepped) ```python nodes.MapRange(value=None, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=steps, vector=self, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type='STEPPED'````
 - [map_range_smooth](Vector.md#map_range_smooth) ```python nodes.MapRange(value=None, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=None, vector=self, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type='SMOOTHSTEP'````
 - [map_range_smoother](Vector.md#map_range_smoother) ```python nodes.MapRange(value=None, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=None, vector=self, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type='SMOOTHERSTEP'````
