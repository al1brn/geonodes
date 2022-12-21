# Node Instance on Points

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)
- geonodes name: `InstanceOnPoints`
- bl_idname: `GeometryNodeInstanceOnPoints`

```python
from geonodes import nodes

node = nodes.InstanceOnPoints(points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None)
```

### Args:

#### Input socket arguments:

- **points**: [Points](Points.md)
- **selection**: [Boolean](Boolean.md)
- **instance**: [Geometry](Geometry.md)
- **pick_instance**: [Boolean](Boolean.md)
- **instance_index**: [Integer](Integer.md)
- **rotation**: [Vector](Vector.md)
- **scale**: [Vector](Vector.md)

### Output sockets:

- **instances** : [Instances](Instances.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x1683b2020>>](Mesh.md#instance_on_points)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x1683b2020>>](Curve.md#instance_on_points)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x1683b2020>>](Points.md#instance_on_points)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Constructor object at 0x1683b3c70>>](Instances.md#InstanceOnPoints-classmethod)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x1683b30a0>>](Instances.md#on_points)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomMethod object at 0x1683b20b0>>](Vertex.md#instance_on_points)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomMethod object at 0x1683b1f00>>](ControlPoint.md#instance_on_points)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomMethod object at 0x1683b3130>>](CloudPoint.md#instance_on_points)
