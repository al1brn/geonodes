# Node Compare

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
- geonodes name: `Compare`
- bl_idname: `FunctionNodeCompare`

```python
from geonodes import nodes

node = nodes.Compare(a=None, b=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN')
```

### Args:

#### Input socket arguments:

- **a**: **data_type** dependant
- **b**: **data_type** dependant
- **c**: [Float](Float.md)
- **angle**: [Float](Float.md)
- **epsilon**: [Float](Float.md)

#### Node parameter arguments:

- **data_type** (str): default = 'FLOAT' in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')
- **mode** (str): default = 'ELEMENT' in ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION')
- **operation** (str): default = 'GREATER_THAN' in ('LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL')

### Output sockets:

- **result** : [Boolean](Boolean.md)

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')
- Input sockets  : ['a', 'b']
- Output sockets : []
