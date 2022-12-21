# Node Accumulate Field

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/accumulate_field.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
- geonodes name: `AccumulateField`
- bl_idname: `GeometryNodeAccumulateField`

```python
from geonodes import nodes

node = nodes.AccumulateField(value=None, group_index=None, data_type='FLOAT', domain='POINT')
```

### Args:#### Input socket arguments:

- **value**: **data_type** dependant
- **group_index**: [Integer](Integer.md)

#### Node parameter arguments:

- **data_type** (str): default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR')
- **domain** (str): default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

### Output sockets:

- **leading** : ``data_type`` dependant
- **trailing** : ``data_type`` dependant
- **total** : ``data_type`` dependant

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR')
- Input sockets  : ['value']
- Output sockets : ['leading', 'trailing', 'total']
