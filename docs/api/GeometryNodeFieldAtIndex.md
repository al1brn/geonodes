# Node *Evaluate at Index*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/v.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
- geonodes name: `EvaluateAtIndex`
- bl_idname: `GeometryNodeFieldAtIndex`

```python
from geonodes import nodes

node = nodes.EvaluateAtIndex(index=None, value=None, data_type='FLOAT', domain='POINT')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

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

| Class or method name | Definition |
|----------------------|------------|
| **[Domain](Domain.md)** |
| [evaluate_at_index](Domain.md#evaluate_at_index) | `def evaluate_at_index(self, index=None, value=None):` |
| **[Geometry](Geometry.md)** |
| [evaluate_at_index](Geometry.md#evaluate_at_index) | `def evaluate_at_index(self, index=None, value=None, domain='POINT'):` |

<sub>Go to [top](#node-Evaluate-at-Index) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

