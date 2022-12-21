# Node Field at Index

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
- geonodes name: `FieldAtIndex`
- bl_idname: `GeometryNodeFieldAtIndex`

```python
from geonodes import nodes

node = nodes.FieldAtIndex(index=None, value=None, data_type='FLOAT', domain='POINT')
```

### Args:

#### Input socket arguments:

- **index**: [Integer](Integer.md)
- **value**: **data_type** dependant

#### Node parameter arguments:

- **data_type** (str): default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- **domain** (str): default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

### Output sockets:

- **value** : ``data_type`` dependant

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets  : ['value']
- Output sockets : ['value']
## Implementation

#### class [Geometry](Geometry.md)

 - [field_at_index](Geometry.md#field_at_index)
#### class [Domain](Domain.md)

 - [field_at_index](Domain.md#field_at_index)