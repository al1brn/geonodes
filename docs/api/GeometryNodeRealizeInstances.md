# Node Realize Instances

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/realize_instances.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRealizeInstances.html)
- geonodes name: `RealizeInstances`
- bl_idname: `GeometryNodeRealizeInstances`

```python
from geonodes import nodes

node = nodes.RealizeInstances(geometry=None, legacy_behavior=False)
```

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)

#### Node parameter arguments:

- **legacy_behavior** (bool): default = False

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

#### class [Instances](Instances.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16d4f8a00>>](Instances.md#realize)
