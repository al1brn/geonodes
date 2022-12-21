# Node Interpolate Domain

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/interpolate_domain.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
- geonodes name: `InterpolateDomain`
- bl_idname: `GeometryNodeFieldOnDomain`

```python
from geonodes import nodes

node = nodes.InterpolateDomain(value=None, data_type='FLOAT', domain='POINT')
```

#### Input socket arguments:

- value: `data_type` dependant

#### Node parameter arguments:

- data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

#### Output sockets:

- **value** : ``data_type`` dependant

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets  : ['value']
- Output sockets : ['value']
