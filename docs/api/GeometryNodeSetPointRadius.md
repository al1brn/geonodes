# Node Set Point Radius

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html)
- geonodes name: `SetPointRadius`
- bl_idname: `GeometryNodeSetPointRadius`

```python
from geonodes import nodes

node = nodes.SetPointRadius(points=None, selection=None, radius=None)
```

### Args:

#### Input socket arguments:

- **points**: [Points](Points.md)
- **selection**: [Boolean](Boolean.md)
- **radius**: [Float](Float.md)

### Output sockets:

- **points** : [Points](Points.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x1683b14b0>>](Points.md#set_point_radius)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomSetter object at 0x1683b0a90>>](CloudPoint.md#radius)
