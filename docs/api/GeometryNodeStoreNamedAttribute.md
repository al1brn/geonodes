# Node Store Named Attribute

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)
- geonodes name: `StoreNamedAttribute`
- bl_idname: `GeometryNodeStoreNamedAttribute`

```python
from geonodes import nodes

node = nodes.StoreNamedAttribute(geometry=None, name=None, value=None, data_type='FLOAT', domain='POINT')
```

#### Input socket arguments:

- geometry: Geometry
- name: String
- value: `data_type` dependant

#### Node parameter arguments:

- data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN')
- domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

#### Output sockets:

- **geometry** : Geometry

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN')
- Input sockets  : ['value']
- Output sockets : []
