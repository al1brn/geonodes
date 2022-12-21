# Node Separate Geometry

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)
- geonodes name: `SeparateGeometry`
- bl_idname: `GeometryNodeSeparateGeometry`

```python
from geonodes import nodes

node = nodes.SeparateGeometry(geometry=None, selection=None, domain='POINT')
```

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)

#### Node parameter arguments:

- **domain** (str): default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

### Output sockets:

- **selection** : [Geometry](Geometry.md)
- **inverted** : [Geometry](Geometry.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x1683b2080>>](Geometry.md#separate)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomMethod object at 0x1683b1120>>](Domain.md#separate)
