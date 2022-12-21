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

#### class [Mesh](Mesh.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4f8b20>>](Mesh.md#instance_on_points)
#### class [Curve](Curve.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4f8b20>>](Curve.md#instance_on_points)
#### class [Points](Points.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4f8b20>>](Points.md#instance_on_points)
#### class [Instances](Instances.md)

 - [<bound method Generator.fname of <generator.code_gen.Constructor object at 0x16d4f8b80>>](Instances.md#InstanceOnPoints-classmethod)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4f8b50>>](Instances.md#on_points)
#### class [Vertex](Vertex.md)

 - [<bound method Generator.fname of <generator.code_gen.DomMethod object at 0x16d4f8af0>>](Vertex.md#instance_on_points)
#### class [ControlPoint](ControlPoint.md)

 - [<bound method Generator.fname of <generator.code_gen.DomMethod object at 0x16d4f8ac0>>](ControlPoint.md#instance_on_points)
#### class [CloudPoint](CloudPoint.md)

 - [<bound method Generator.fname of <generator.code_gen.DomMethod object at 0x16d4f8a90>>](CloudPoint.md#instance_on_points)
