# Node Field at Index

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeFieldAtIndex`

```python
from geonodes import nodes

node = nodes.FieldAtIndex(index=None, value=None, data_type='FLOAT', domain='POINT')
```

#### Input socket arguments:

- index: Integer
- value: `data_type` dependant

#### Node parameter arguments:

- data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

#### Output sockets:

- **value** : ``data_type`` dependant

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')- Input sockets  : ['value']- Output sockets : ['value']