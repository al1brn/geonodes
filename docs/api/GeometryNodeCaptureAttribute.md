# Node *Capture Attribute*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
- geonodes name: `CaptureAttribute`
- bl_idname: `GeometryNodeCaptureAttribute`

```python
from geonodes import nodes

node = nodes.CaptureAttribute(geometry=None, value=None, data_type='FLOAT', domain='POINT')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **value**: **data_type** dependant

#### Node parameter arguments:

- **data_type** (str): default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- **domain** (str): default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

### Output sockets:

- **geometry** : [Geometry](Geometry.md)
- **attribute** : ``data_type`` dependant

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets  : ['value']
- Output sockets : ['attribute']
## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Domain](Domain.md)** |
| [capture_attribute](Domain.md#capture_attribute) | `def capture_attribute(self, value=None):` |
| **[Geometry](Geometry.md)** |
| [capture_attribute](Geometry.md#capture_attribute) | `def capture_attribute(self, value=None, domain='POINT'):` |
| [capture_attribute_node](Geometry.md#capture_attribute_node) | `@staticmethod`<br> `def capture_attribute_node(geometry=None, value=None, data_type='FLOAT', domain='POINT'):` |

<sub>Go to [top](#node-Capture-Attribute) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

