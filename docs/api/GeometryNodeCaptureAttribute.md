# Node Capture Attribute

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
- geonodes name: `CaptureAttribute`
- bl_idname: `GeometryNodeCaptureAttribute`

```python
from geonodes import nodes

node = nodes.CaptureAttribute(geometry=None, value=None, data_type='FLOAT', domain='POINT')
```

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

#### class [Geometry](Geometry.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x16e1a3f70>>](Geometry.md#capture_attribute)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e1a3d60>>](Geometry.md#capture_attribute_node)
#### class [Domain](Domain.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16e1a3f40>>](Domain.md#capture_attribute)
