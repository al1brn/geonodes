# Node Geometry to Instance

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html)
- geonodes name: `GeometryToInstance`
- bl_idname: `GeometryNodeGeometryToInstance`

```python
from geonodes import nodes

node = nodes.GeometryToInstance(*geometry)
```

### Args:

#### Input socket arguments:

- **geometry**: *[Geometry](Geometry.md)

### Output sockets:

- **instances** : [Instances](Instances.md)

## Implementation

#### class [Geometry](Geometry.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4f9930>>](Geometry.md#to_instance)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4f9960>>](function.md#geometry_to_instance)
