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

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **sample_position**: [Vector](Vector.md)

#### Node parameter arguments:

- **domain** (str): default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER')

### Output sockets:

- **index** : [Integer](Integer.md)

## Implementation

#### [Domain](Domain.md)

 - [sample_nearest](Domain.md#sample_nearest)
  ```python
  nodes.SampleNearest(geometry=self.data_socket, sample_position=sample_position, domain=self.domain  ```

#### [Geometry](Geometry.md)

 - [sample_nearest](Geometry.md#sample_nearest)
  ```python
  nodes.SampleNearest(geometry=self, sample_position=sample_position, domain=domain  ```

