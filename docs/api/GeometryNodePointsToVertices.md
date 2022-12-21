# Node Points to Vertices

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html)
- geonodes name: `PointsToVertices`
- bl_idname: `GeometryNodePointsToVertices`

```python
from geonodes import nodes

node = nodes.PointsToVertices(points=None, selection=None)
```

### Args:

#### Input socket arguments:

- **points**: [Points](Points.md)
- **selection**: [Boolean](Boolean.md)

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x1683b2c80>>](Points.md#to_vertices)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomMethod object at 0x1683b0610>>](CloudPoint.md#to_vertices)
